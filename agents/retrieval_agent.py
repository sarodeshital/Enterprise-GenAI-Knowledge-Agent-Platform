from app.services.vector_store import VectorStore

store = VectorStore()

def retrieve(question: str):
    return store.search(question, k=3)
