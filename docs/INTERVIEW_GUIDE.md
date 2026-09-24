# Interview Deep-Dive Guide

## 1. 60-second project explanation

"I built an enterprise GenAI knowledge and agent platform using Python, FastAPI,
LangGraph, RAG and Azure OpenAI. A user sends a question to the API. LangGraph
orchestrates the workflow: it classifies the request, retrieves relevant enterprise
documents from a vector index, sends only the retrieved context to the LLM, and
returns a grounded response with source metadata. I designed it so the local
development version uses FAISS, while a production Azure implementation can use
Azure AI Search, managed identity, Key Vault and Application Insights."

## 2. End-to-end request flow

1. Client sends POST /query.
2. FastAPI validates the request with Pydantic.
3. LangGraph creates workflow state.
4. Classifier selects the knowledge-retrieval route.
5. Retriever performs semantic similarity search.
6. Top-K context is passed to the generation layer.
7. Azure OpenAI generates the answer in Azure mode.
8. The response includes answer, source documents, route and grounded flag.

## 3. Why RAG instead of fine-tuning?

RAG is suitable when enterprise knowledge changes and answers must be grounded in
retrievable source material. Fine-tuning changes model behavior/knowledge patterns,
but does not by itself provide a current document retrieval mechanism.

## 4. Why LangGraph?

The workflow is stateful and can later include conditional branches, validation,
human approval, retry limits and tool calls. A graph makes those control points explicit.

## 5. Why FAISS?

FAISS is lightweight for local development and demonstrates the vector-search concept.
For an Azure production architecture, Azure AI Search is a natural enterprise-oriented
replacement when hybrid search, metadata filters and managed infrastructure are required.

## 6. Azure OpenAI 429 scenario

Explain:
- identify 429 as a rate/quota-related response;
- inspect request and token rates;
- use bounded exponential backoff for transient failures;
- reduce unnecessary prompt/context size;
- cache repeatable work where appropriate;
- review quota/deployment capacity;
- monitor the result.

## 7. Hallucination scenario

Explain:
- improve retrieval quality;
- enforce a grounded prompt;
- reject/abstain when context is insufficient;
- add citation/source requirements;
- evaluate faithfulness and retrieval quality;
- monitor failures and add regression tests.

## 8. Production architecture

API Gateway / Front Door
-> FastAPI service
-> LangGraph orchestration
-> Azure AI Search
-> Azure OpenAI
-> Key Vault
-> Application Insights / OpenTelemetry
-> CI/CD

For higher scale, add asynchronous processing, caching, rate limiting, autoscaling,
private networking and resilience controls as required by the workload.

## 9. Questions to practice

- Explain your project in 60 seconds.
- Explain the architecture without looking at the diagram.
- Why RAG?
- What are embeddings?
- How does cosine similarity work?
- What is Top-K?
- What is reranking?
- How do you evaluate RAG?
- What is an agent?
- Agent vs workflow?
- Why LangGraph?
- What is graph state?
- What is a conditional edge?
- How would you add human-in-the-loop?
- How do you prevent agent loops?
- Azure OpenAI vs OpenAI API?
- How do you authenticate securely?
- How do you handle 429?
- How do you reduce latency?
- How do you reduce token cost?
- How do you secure enterprise data?
- How do you monitor an LLM application?
- What would you change before production?

## 10. Do not overclaim

Only describe features you actually implement. If you say Azure AI Search,
Entra ID, Key Vault, CI/CD or production deployment was used, be prepared to show
the implementation and explain it.
