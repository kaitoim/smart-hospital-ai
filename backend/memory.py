class ConversationMemory:

    def __init__(self, max_messages=20):
        self.messages = []
        self.max_messages = max_messages

    def clear(self):
        self.messages.clear()

    def _trim(self):
        # Simpan hanya N pesan terakhir agar memory tidak membengkak
        if len(self.messages) > self.max_messages:
            self.messages = self.messages[-self.max_messages:]

    def add_user(self, message):
        self.messages.append({
            "role": "user",
            "content": message
        })
        self._trim()

    def add_assistant(self, message):
        self.messages.append({
            "role": "assistant",
            "content": message
        })
        self._trim()

    def get_messages(self):
        return self.messages

    def to_text(self):
        return "\n".join(
            f"{msg['role']}: {msg['content']}"
            for msg in self.messages
        )