from app.config import settings

def generate_answer(question: str, contexts: list[dict]) -> str:
    context = "\n\n".join(
        f"[{c['document']}]\n{c['text']}" for c in contexts
    )
    if not contexts:
        return "I could not find relevant information in the approved knowledge base."

    if settings.use_azure_openai:
        from langchain_openai import AzureChatOpenAI
        llm = AzureChatOpenAI(
            azure_endpoint=settings.azure_openai_endpoint,
            api_key=settings.azure_openai_api_key,
            api_version=settings.azure_openai_api_version,
            azure_deployment=settings.azure_openai_chat_deployment,
            temperature=0,
        )
        prompt = (
            "Answer only from the supplied enterprise context. "
            "If the answer is not supported, say that it is not available. "
            "Cite document names in the answer.\n\n"
            f"Question: {question}\n\nContext:\n{context}"
        )
        return llm.invoke(prompt).content

    # Deterministic demo response so the repository runs without credentials.
    return (
        "Demo grounded response. Relevant knowledge was retrieved from: "
        + ", ".join(c["document"] for c in contexts)
        + ". In Azure mode, Azure OpenAI generates the final answer from these contexts."
    )
