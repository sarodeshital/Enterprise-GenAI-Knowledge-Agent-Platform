import hashlib
import numpy as np

DIMENSION = 384

def embed_text(text: str) -> np.ndarray:
    # Deterministic local demo embedding. Replace with Azure OpenAI embeddings
    # when USE_AZURE_OPENAI=true.
    vec = np.zeros(DIMENSION, dtype="float32")
    tokens = text.lower().split()
    for token in tokens:
        digest = hashlib.sha256(token.encode()).digest()
        idx = int.from_bytes(digest[:4], "little") % DIMENSION
        vec[idx] += 1.0
    norm = np.linalg.norm(vec)
    return vec / norm if norm else vec

def embed_many(texts: list[str]) -> np.ndarray:
    return np.vstack([embed_text(t) for t in texts]).astype("float32")
