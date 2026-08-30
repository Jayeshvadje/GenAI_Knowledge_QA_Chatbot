from google import genai

from app.core.config import settings


class LLMService:
    def __init__(self):
        self.client = genai.Client(
            api_key=settings.gemini_api_key
        )
        self.model = settings.gemini_model

    def generate_answer(self, question: str) -> str:
        response = self.client.models.generate_content(
            model=self.model,
            contents=question,
        )

        return response.text