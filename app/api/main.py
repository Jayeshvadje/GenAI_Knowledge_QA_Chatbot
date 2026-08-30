from fastapi import FastAPI
from pydantic import BaseModel, Field

from app.core.config import settings
from app.services.llm_service import LLMService


app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
)

llm_service = LLMService()


class QuestionRequest(BaseModel):
        question: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Question to ask the AI",
    )

@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/ask")
def ask_question(request: QuestionRequest):
    answer = llm_service.generate_answer(request.question)

    return {
        "question": request.question,
        "answer": answer,
    }