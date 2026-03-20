import hashlib
from typing import List

from langchain_core.embeddings import Embeddings


class MeridianDeterministicEmbeddings(Embeddings):
    """Stable local embedding fallback for offline semantic search demos."""

    def _to_vector(self, text: str, dim: int = 64) -> List[float]:
        tokens = text.lower().split()
        vector = [0.0] * dim
        for token in tokens:
            digest = hashlib.sha256(token.encode("utf-8")).digest()
            for idx in range(dim):
                vector[idx] += digest[idx % len(digest)] / 255.0
        norm = sum(value * value for value in vector) ** 0.5 or 1.0
        return [value / norm for value in vector]

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return [self._to_vector(text) for text in texts]

    def embed_query(self, text: str) -> List[float]:
        return self._to_vector(text)
