from pathlib import Path
import json
import faiss
from .embeddings import embed_many, embed_text

DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "sample_documents"

class VectorStore:
    def __init__(self):
        self.documents = []
        for path in sorted(DATA_DIR.glob("*.txt")):
            self.documents.append({
                "document": path.name,
                "text": path.read_text(encoding="utf-8")
            })
        matrix = embed_many([d["text"] for d in self.documents])
        self.index = faiss.IndexFlatIP(matrix.shape[1])
        self.index.add(matrix)

    def search(self, query: str, k: int = 3):
        q = embed_text(query).reshape(1, -1)
        scores, indices = self.index.search(q, min(k, len(self.documents)))
        results = []
        for score, idx in zip(scores[0], indices[0]):
            if idx >= 0:
                item = self.documents[int(idx)].copy()
                item["score"] = float(score)
                results.append(item)
        return results
