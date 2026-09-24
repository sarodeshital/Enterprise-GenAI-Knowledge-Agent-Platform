from fastapi import FastAPI
from app.schemas import QueryRequest, QueryResponse
from app.graph import run_agent

app = FastAPI(
    title="Enterprise GenAI RAG Agent Platform",
    version="1.0.0",
    description="Azure OpenAI + RAG + LangGraph portfolio API",
)

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/query", response_model=QueryResponse)
def query(request: QueryRequest):
    return run_agent(request.question)
