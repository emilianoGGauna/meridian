import json
from functools import lru_cache

from core.config import DATA_FILE
from models.property import Property


@lru_cache
def load_properties() -> list[Property]:
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        payload = json.load(file)
    return [Property(**item) for item in payload]


def get_property_by_id(property_id: str) -> Property | None:
    for property_item in load_properties():
        if property_item.id == property_id:
            return property_item
    return None
