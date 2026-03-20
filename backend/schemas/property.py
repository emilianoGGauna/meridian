from pydantic import BaseModel, Field


class PropertyResponse(BaseModel):
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


class SearchRequest(BaseModel):
    query: str = Field(..., min_length=2)
    max_price: float | None = None
    min_bedrooms: int | None = None
    location: str | None = None


class SearchResponse(BaseModel):
    query: str
    results: list[PropertyResponse]


class AIChatRequest(BaseModel):
    message: str
    session_id: str = "default"


class AIChatResponse(BaseModel):
    message: str
    properties: list[PropertyResponse]
    suggestions: list[str]
