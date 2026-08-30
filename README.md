# GenAI Knowledge QA Chatbot

A simple GenAI question-answering application that uses an LLM to answer user queries.

## Project Status

🚧 Under development

## How It Works

The application accepts a user's question through a FastAPI API and sends it to an LLM to generate an answer.

```text
User Question
      ↓
   FastAPI
      ↓
  LLM Service
      ↓
   LLM Answer
      ↓
     User