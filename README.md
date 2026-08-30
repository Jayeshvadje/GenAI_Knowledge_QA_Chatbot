GenAI Knowledge QA Chatbot

A simple, production-oriented GenAI question-answering application built
with Python, FastAPI, and Google’s Gemini API.

The application accepts a user’s question through a REST API, validates
the request, sends the question to Gemini through a dedicated LLM
service, and returns a structured answer.

Architecture

                             USER
                               |
                               | Question
                               v
                        +--------------+
                        |    FastAPI   |
                        |   /ask API   |
                        +--------------+
                               |
                               | Validate request
                               v
                        +--------------+
                        | LLM Service  |
                        +--------------+
                               |
                               | Generate answer
                               v
                        +----------------+
                        | Google Gemini  |
                        |      API       |
                        +----------------+
                               |
                               | Answer
                               v
                        +--------------+
                        |    FastAPI   |
                        +--------------+
                               |
                               v
                             USER

Key Features

-   FastAPI REST API
-   Google Gemini LLM integration
-   Environment-based configuration
-   Pydantic request validation
-   Structured API response models
-   Graceful error handling
-   Application logging
-   Automated API tests with pytest
-   Gemini calls mocked during automated tests
-   GitHub Actions CI pipeline
-   Clean separation between API, configuration, and LLM service layers

Example Questions

The application can answer general questions such as:

-   Who is the Prime Minister of India?
-   Who is the captain of the Indian cricket team?
-   Explain artificial intelligence in simple words.
-   What is machine learning?
-   What is the difference between AI and ML?

Tech Stack

-   Python
-   FastAPI
-   Uvicorn
-   Google Gemini API
-   google-genai
-   Pydantic
-   Pydantic Settings
-   Pytest
-   HTTPX
-   GitHub Actions

Project Structure

    GenAI_Knowledge_QA_Chatbot/
    |
    +-- .github/
    |   +-- workflows/
    |       +-- tests.yml
    |
    +-- app/
    |   +-- api/
    |   |   +-- __init__.py
    |   |   +-- main.py
    |   |
    |   +-- core/
    |   |   +-- __init__.py
    |   |   +-- config.py
    |   |   +-- logging_config.py
    |   |
    |   +-- services/
    |       +-- __init__.py
    |       +-- llm_service.py
    |
    +-- tests/
    |   +-- test_api.py
    |
    +-- .env.example
    +-- .gitignore
    +-- pytest.ini
    +-- README.md
    +-- requirements.txt

How the Application Works

1.  The user sends a question to the /ask endpoint.
2.  FastAPI receives the request.
3.  Pydantic validates the question.
4.  The LLM service sends the question to Google Gemini.
5.  Gemini generates an answer.
6.  FastAPI returns the question and generated answer as a structured
    JSON response.
7.  Errors are handled gracefully and logged.

API Endpoints

Health Check

    GET /health

Example response:

    {
      "status": "ok"
    }

Ask a Question

    POST /ask

Request:

    {
      "question": "Who is the Prime Minister of India?"
    }

Response:

    {
      "question": "Who is the Prime Minister of India?",
      "answer": "..."
    }

Local Setup

1. Clone the repository

    git clone <your-github-repository-url>
    cd GenAI_Knowledge_QA_Chatbot

2. Create a virtual environment

Windows PowerShell:

    python -m venv .venv

Activate it:

    .venv\Scripts\Activate.ps1

3. Install dependencies

    pip install -r requirements.txt

4. Configure environment variables

Create a local .env file in the project root.

Add:

    GEMINI_API_KEY=your_actual_gemini_api_key
    GEMINI_MODEL=gemini-3.7-flash

Never commit the .env file or expose the API key publicly.

.env.example is provided as a safe configuration template.

5. Run the application

    uvicorn app.api.main:app --reload

The application will be available at:

    http://127.0.0.1:8000

6. Open API documentation

FastAPI automatically provides interactive Swagger documentation:

    http://127.0.0.1:8000/docs

Use the Swagger UI to test /health and /ask.

Running Tests

Run all automated tests with:

    pytest -v

The test suite covers:

-   Health endpoint
-   Empty question validation
-   Maximum question length validation
-   Successful /ask response
-   LLM failure handling

The Gemini API is mocked in the /ask tests, so the test suite does not
require a real Gemini API call.

CI/CD

GitHub Actions automatically runs the test suite when changes are pushed
to the configured branches or when a pull request targets main or
develop.

The CI workflow:

    Code Push / Pull Request
              |
              v
       Checkout Repository
              |
              v
        Setup Python 3.12
              |
              v
      Install Dependencies
              |
              v
           Run Pytest
              |
           +--+--+
           |     |
           v     v
        Passed  Failed

Configuration and Security

The application uses Pydantic Settings for configuration.

Sensitive values such as the Gemini API key are loaded from .env.

The .env file is excluded from Git through .gitignore.

The repository should contain only:

    .env.example

with placeholder values.

Never commit:

    GEMINI_API_KEY=real-api-key

to GitHub.

Git Workflow

The project follows a feature-branch workflow:

    main
      |
      v
    develop
      |
      +--> feature branch
              |
              v
           Develop
              |
              v
            Commit
              |
              v
          Pull Request
              |
              v
           develop

Examples of feature branches used during development:

    feature/project-setup
    feature/project-structure
    feature/configuration
    feature/fastapi-app
    feature/gemini-integration
    feature/api-validation
    feature/error-handling
    feature/logging
    feature/production-ready

Design Decisions

Why Gemini?

Google Gemini provides the LLM capability required for this application
and can be accessed through Google’s official Python SDK.

Why a separate LLM service?

The Gemini integration is isolated in llm_service.py so that the API
layer is responsible for HTTP requests while the service layer is
responsible for communicating with the LLM.

This separation makes the application easier to maintain and test.

Why not RAG?

This project is intentionally designed as a simple general
question-answering application. It does not answer questions from a
private document collection or knowledge base.

Therefore, RAG, document ingestion, embeddings, and vector databases are
outside the scope of this application.

Why mock Gemini in tests?

Automated tests should not depend on an external LLM API.

Mocking the LLM call makes tests:

-   Faster
-   More reliable
-   Independent of network availability
-   Free from Gemini API usage during tests
-   Suitable for CI environments

Current Scope

Included:

-   General user question answering
-   Gemini LLM integration
-   REST API
-   Validation
-   Error handling
-   Logging
-   Automated tests
-   GitHub Actions CI

Intentionally excluded:

-   RAG
-   Document ingestion
-   Embeddings
-   Vector databases
-   Knowledge-base retrieval
-   Docker

Future Improvements

Possible future improvements, if required:

-   Authentication and authorization
-   Rate limiting
-   Better prompt management
-   Conversation history
-   Streaming responses
-   Frontend interface
-   Production deployment
-   Monitoring and observability improvements

These are intentionally not part of the current minimal application.

Project Status

Completed and working.

The application has been tested locally and through GitHub Actions CI.

Author

Add your name here.

License

Add the appropriate license for your project.
