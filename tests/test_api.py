from fastapi.testclient import TestClient
from unittest.mock import patch
from app.api.main import app


client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_empty_question():
    response = client.post(
        "/ask",
        json={"question": ""},
    )

    assert response.status_code == 422


def test_question_too_long():
    response = client.post(
        "/ask",
        json={"question": "a" * 1001},
    )

    assert response.status_code == 422


def test_ask_question():
    with patch(
        "app.api.main.llm_service.generate_answer"
    ) as mock_generate_answer:
        mock_generate_answer.return_value = "The Prime Minister of India is Narendra Modi."

        response = client.post(
            "/ask",
            json={"question": "Who is the Prime Minister of India?"},
        )

    assert response.status_code == 200
    assert response.json() == {
        "question": "Who is the Prime Minister of India?",
        "answer": "The Prime Minister of India is Narendra Modi.",
    }

    mock_generate_answer.assert_called_once_with(
        "Who is the Prime Minister of India?"
    )

def test_ask_question_llm_failure():
    with patch(
        "app.api.main.llm_service.generate_answer"
    ) as mock_generate_answer:
        mock_generate_answer.side_effect = Exception("Gemini API error")

        response = client.post(
            "/ask",
            json={"question": "What is artificial intelligence?"},
        )

    assert response.status_code == 500
    assert response.json() == {
        "detail": "Unable to generate an answer. Please try again later."
    }