from langchain_chroma import Chroma
from langchain_core.documents import Document

from ai.embeddings import MeridianDeterministicEmbeddings
from core.config import CHROMA_DIR
from services.property_service import load_properties


class MeridianVectorStore:
    def __init__(self) -> None:
        self.embeddings = MeridianDeterministicEmbeddings()
        self.collection_name = "meridian-properties"
        self.store = self._build_store()

    def _build_store(self) -> Chroma:
        properties = load_properties()
        docs = []
        for prop in properties:
            page = (
                f"{prop.title}. {prop.description}. Located in {prop.location}. "
                f"Price ${prop.price:,.0f}. Investment score {prop.investment_score}. "
                f"Rental yield {prop.rental_yield}. Amenities: {', '.join(prop.amenities)}"
            )
            docs.append(Document(page_content=page, metadata={"id": prop.id}))

        return Chroma.from_documents(
            documents=docs,
            embedding=self.embeddings,
            collection_name=self.collection_name,
            persist_directory=str(CHROMA_DIR),
        )

    def similarity_search(self, query: str, k: int = 5) -> list[str]:
        matches = self.store.similarity_search(query, k=k)
        return [item.metadata["id"] for item in matches]
