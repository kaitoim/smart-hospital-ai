from backend.llm import GroqClient
from backend.prompt import (
    SYSTEM_PROMPT,
    REPORT_PROMPT_TEMPLATE
)
from backend.memory import ConversationMemory
from backend.knowledge import KnowledgeBase


class Chatbot:

    REPORT_KEYWORDS = [
        "lapor",
        "mau lapor",
        "ingin lapor",
        "buat laporan",
        "buat tiket",
        "buat ticket",
        "buat aduan",
        "pengaduan",
        "minta diperbaiki",
        "minta teknisi",
        "lapor gangguan",
        "lapor ke it",
        "lapor ke tim it",
        "cara lapor",
        "bagaimana lapor",
        "gimana lapor",
        "cara lapornya"
    ]

    INFO_PATTERNS = [
        "cara membuat laporan",
        "cara buat laporan",
        "nomor helpdesk",
        "kontak helpdesk",
        "kontak admin",
        "hubungi admin",
        "siapa admin",
        "cara menghubungi"
    ]

    BARE_REPORT_PHRASES = [
        "lapor",
        "mau lapor",
        "ingin lapor",
        "buat laporan",
        "buat tiket",
        "cara lapor",
        "bagaimana cara lapor",
        "bagaimana cara lapornya",
        "gimana lapor",
        "cara lapornya"
    ]

    CLARIFICATION_MESSAGE = (
        "Baik, saya dapat membantu menyusun laporan.\n\n"
        "Mohon informasikan:\n"
        "1. Lokasi\n"
        "2. Perangkat\n"
        "3. Keluhan\n"
        "4. Tindakan yang sudah dilakukan"
    )

    def __init__(self):

        self.llm = None

        self.memory = ConversationMemory()

        self.knowledge = KnowledgeBase()

    def is_report_request(self, question):
        """Return True jika pesan mengindikasikan permintaan lapor gangguan."""

        question = question.lower().strip()

        if any(pattern in question for pattern in self.INFO_PATTERNS):
            return False

        return any(
            keyword in question
            for keyword in self.REPORT_KEYWORDS
        )

    def needs_clarification(self, question):
        """Return True jika user minta lapor tapi belum menyertakan detail apa pun."""

        question = question.lower().strip().rstrip("?!.")

        return question in self.BARE_REPORT_PHRASES

    def _get_last_assistant_answer(self):
        for msg in reversed(self.memory.get_messages()):
            if msg["role"] == "assistant":
                return msg["content"]
        return None

    def ask(self, question):

        if self.is_report_request(question):

            self.memory.add_user(question)

            if self.needs_clarification(question):
                answer = self.CLARIFICATION_MESSAGE
                self.memory.add_assistant(answer)
                return answer

            if self.llm is None:
                self.llm = GroqClient()

            history = self.memory.to_text()

            prompt = REPORT_PROMPT_TEMPLATE.format(
                history=history
            )

            answer = self.llm.generate([
                {
                    "role": "system",
                    "content": prompt
                }
            ])

            self.memory.add_assistant(answer)

            self.memory.clear()

            return answer

        kb_result = self.knowledge.search(question)

        if kb_result:

            answer = kb_result["answer"]

            last_answer = self._get_last_assistant_answer()

            if answer != last_answer:

                self.memory.add_user(question)
                self.memory.add_assistant(answer)

                return answer

        if self.llm is None:
            self.llm = GroqClient()

        self.memory.add_user(question)

        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

        messages.extend(
            self.memory.get_messages()
        )

        answer = self.llm.generate(messages)

        self.memory.add_assistant(answer)

        return answer

    def clear(self):

        self.memory.clear()