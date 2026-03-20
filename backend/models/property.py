from dataclasses import dataclass


@dataclass
class Property:
    id: str
    title: str
    description: str
    location: str
    price: float
    bedrooms: int
    bathrooms: int
    amenities: list[str]
    investment_score: int
    rental_yield: float
    image_url: str
