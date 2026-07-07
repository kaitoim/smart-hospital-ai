import os
from groq import Groq
from backend.config import Settings


class GroqClient:

    def __init__(self):

        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError(
                "Environment variable GROQ_API_KEY belum diset."
            )

        self.client = Groq(api_key=api_key)

    def generate(self, messages):

        response = self.client.chat.completions.create(
            model=Settings.MODEL,
            messages=messages,
            temperature=Settings.TEMPERATURE,
            top_p=Settings.TOP_P,
            max_tokens=Settings.MAX_TOKENS,
        )

        return response.choices[0].message.content