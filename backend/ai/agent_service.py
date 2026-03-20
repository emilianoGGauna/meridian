import re
from collections import defaultdict

from ai.vector_store import MeridianVectorStore
from models.property import Property
from services.property_service import load_properties


class MeridianAIAgent:
    def __init__(self) -> None:
        self.vector_store = MeridianVectorStore()
        self.memory: dict[str, dict[str, str | float | int]] = defaultdict(dict)

    def _parse_budget(self, prompt: str) -> float | None:
        match = re.search(r"under\s*\$?([\d.]+)\s*(m|million)?", prompt.lower())
        if not match:
            return None
        value = float(match.group(1))
        if match.group(2):
            value *= 1_000_000
        return value

    def _apply_filters(self, properties: list[Property], prompt: str, session_id: str) -> list[Property]:
        profile = self.memory[session_id]
        budget = self._parse_budget(prompt)
        if budget:
            profile["max_price"] = budget

        max_price = profile.get("max_price")
        if isinstance(max_price, (int, float)):
            properties = [item for item in properties if item.price <= max_price]

        if "high roi" in prompt.lower() or "investment" in prompt.lower():
            properties = sorted(properties, key=lambda item: (item.investment_score, item.rental_yield), reverse=True)

        return properties

    def chat(self, message: str, session_id: str = "default") -> tuple[str, list[Property], list[str]]:
        ids = self.vector_store.similarity_search(message, k=6)
        lookup = {item.id: item for item in load_properties()}
        ranked = [lookup[item_id] for item_id in ids if item_id in lookup]
        filtered = self._apply_filters(ranked, message, session_id)
        top = filtered[:3]

        if not top:
            response = "I couldn’t find a perfect fit yet. I can widen your search by region, budget, or investment profile."
        else:
            response = "I curated properties aligned to your intent, balancing location prestige, ROI potential, and design quality."

        suggestions = [
            "Show similar homes with higher rental yield",
            "Compare this shortlist by 5-year appreciation",
            "Refine for waterfront properties only",
        ]
        return response, top, suggestions
