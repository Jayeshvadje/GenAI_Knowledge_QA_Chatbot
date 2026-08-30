import logging

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from app.core.config import settings
from app.core.logging_config import setup_logging
from app.services.llm_service import LLMService


setup_logging()

logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
)

llm_service = LLMService()


class QuestionRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=1,
        max_length=1000,
        description="Question to ask the AI",
    )


@app.get("/health")
def health_check():
    logger.info("Health check requested")
    return {"status": "ok"}


@app.post("/ask")
def ask_question(request: QuestionRequest):
    logger.info("Question received")

    try:
        answer = llm_service.generate_answer(request.question)

        logger.info("Answer generated successfully")

        return {
            "question": request.question,
            "answer": answer,
        }

    except Exception:
        logger.exception("Failed to generate answer")

        raise HTTPException(
            status_code=500,
            detail="Unable to generate an answer. Please try again later.",
        )