from fastapi import APIRouter, HTTPException

from ai.agent_service import MeridianAIAgent
from schemas.property import (
    AIChatRequest,
    AIChatResponse,
    PropertyResponse,
    SearchRequest,
    SearchResponse,
)
from services.property_service import get_property_by_id, load_properties

router = APIRouter()
agent = MeridianAIAgent()


@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "platform": "MERIDIAN"}


@router.get("/properties", response_model=list[PropertyResponse])
def list_properties() -> list[PropertyResponse]:
    return [PropertyResponse(**item.__dict__) for item in load_properties()]


@router.get("/properties/{property_id}", response_model=PropertyResponse)
def property_detail(property_id: str) -> PropertyResponse:
    item = get_property_by_id(property_id)
    if not item:
        raise HTTPException(status_code=404, detail="Property not found")
    return PropertyResponse(**item.__dict__)


@router.post("/search", response_model=SearchResponse)
def search_properties(payload: SearchRequest) -> SearchResponse:
    results = []
    for item in load_properties():
        if payload.max_price and item.price > payload.max_price:
            continue
        if payload.min_bedrooms and item.bedrooms < payload.min_bedrooms:
            continue
        if payload.location and payload.location.lower() not in item.location.lower():
            continue
        if payload.query.lower() not in f"{item.title} {item.description} {item.location}".lower():
            continue
        results.append(PropertyResponse(**item.__dict__))
    return SearchResponse(query=payload.query, results=results)


@router.post("/ai/chat", response_model=AIChatResponse)
def ai_chat(payload: AIChatRequest) -> AIChatResponse:
    message, properties, suggestions = agent.chat(payload.message, payload.session_id)
    return AIChatResponse(
        message=message,
        properties=[PropertyResponse(**item.__dict__) for item in properties],
        suggestions=suggestions,
    )
