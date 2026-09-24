# Enterprise GenAI Knowledge & Agent Platform

A production-oriented Azure OpenAI + RAG + Agentic AI reference project designed to demonstrate enterprise GenAI engineering skills.

## Use case

Employees can ask questions about enterprise policies, technical documentation, and operational knowledge. The system:

1. Accepts a user question.
2. Classifies the request.
3. Retrieves relevant knowledge from a vector index.
4. Uses an LLM to generate a grounded response.
5. Applies a validation/guardrail step.
6. Returns an answer with source references and structured metadata.

## Architecture

User -> FastAPI -> LangGraph Orchestrator
                         |
             +-----------+-----------+
             |                       |
        Retrieval Agent        Guardrail/Validator
             |                       |
      Embedding + Vector DB          |
             +-----------+-----------+
                         |
                    Azure OpenAI
                         |
                  Grounded Response

## Technology stack

- Python
- FastAPI
- LangChain
- LangGraph
- Azure OpenAI
- FAISS (local development vector store)
- Pydantic
- pytest
- Docker
- Optional Azure AI Search replacement for FAISS in production

## Interview talking points

### Why RAG?
Enterprise knowledge changes frequently. RAG lets the application retrieve current approved documents without retraining the LLM.

### Why LangGraph?
The workflow has explicit state, conditional routing and validation. LangGraph makes the orchestration easier to control than a single prompt chain.

### Why Azure OpenAI?
It provides an enterprise-oriented Azure deployment model, identity/security integration and operational controls.

### Production evolution

For a production deployment, replace local FAISS with Azure AI Search, use Microsoft Entra ID where appropriate, store secrets in Azure Key Vault, deploy the API in Azure Container Apps or AKS, add Application Insights/OpenTelemetry, configure CI/CD, rate limits, retries and evaluation.

## Run locally

```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1

pip install -r requirements.txt
copy .env.example .env
uvicorn app.main:app --reload
```

Open:
`http://127.0.0.1:8000/docs`

The included demo mode works without Azure credentials.

## Environment variables

See `.env.example`.

## Project structure

```text
enterprise-genai-rag-agent-platform/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── schemas.py
│   ├── graph.py
│   ├── agents/
│   │   └── retrieval_agent.py
│   └── services/
│       ├── embeddings.py
│       ├── llm.py
│       └── vector_store.py
├── data/
│   └── sample_documents/
├── tests/
├── .env.example
├── .gitignore
├── Dockerfile
├── requirements.txt
└── README.md
```

## Important interview honesty

This repository is a portfolio/reference implementation. Do not claim Azure deployment, production traffic, latency numbers, model names, or enterprise users unless you actually implemented and measured them.
