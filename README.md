# MERIDIAN — The Architecture of Wealth

MERIDIAN is a luxury-grade, AI-native real estate intelligence platform designed for high-net-worth buyers and investment offices.

## Product Pillars

- **Brand Identity:** Ultra-minimal black + gold visual system with architectural symmetry.
- **Frontend Experience:** React + Vite application with premium property browsing, curated insights, and a floating AI intelligence panel.
- **Backend Services:** FastAPI service exposing property catalog, detail endpoints, semantic search, and AI conversation orchestration.
- **AI Core:** LangChain-powered retrieval stack using Chroma vector store and deterministic local embeddings for semantic ranking.
- **Data Intelligence:** Investment metrics per listing (score + rental yield) to support wealth-driven recommendations.

---

## Folder Structure

```text
meridian/
├── backend/
│   ├── ai/
│   │   ├── agent_service.py
│   │   ├── embeddings.py
│   │   └── vector_store.py
│   ├── api/
│   │   └── routes.py
│   ├── core/
│   │   └── config.py
│   ├── data/
│   │   └── properties.json
│   ├── models/
│   │   └── property.py
│   ├── schemas/
│   │   └── property.py
│   ├── services/
│   │   └── property_service.py
│   ├── main.py
│   └── requirements.txt
└── frontend/
    ├── public/
    ├── src/
    │   ├── components/
    │   │   ├── AIChatPanel.jsx
    │   │   ├── Footer.jsx
    │   │   ├── Hero.jsx
    │   │   ├── Navbar.jsx
    │   │   └── PropertyCard.jsx
    │   ├── pages/
    │   │   ├── HomePage.jsx
    │   │   ├── InsightsPage.jsx
    │   │   ├── ListingPage.jsx
    │   │   └── PropertyDetailPage.jsx
    │   ├── styles/
    │   │   └── theme.css
    │   ├── App.jsx
    │   └── main.jsx
    ├── index.html
    ├── package.json
    └── vite.config.js
```

---

## Backend API

### Endpoints

- `GET /health` — service health status.
- `GET /properties` — complete property dataset.
- `GET /properties/{id}` — single property detail.
- `POST /search` — structured filter + keyword query.
- `POST /ai/chat` — private intelligence agent response with curated properties + follow-up suggestions.

### AI Retrieval Flow

1. User input received in `POST /ai/chat`.
2. Intent signal parsed (budget / investment language / context memory).
3. Query embedded via deterministic embedding model.
4. Chroma performs semantic similarity retrieval.
5. Filters and ranking applied (price and ROI-aware ordering).
6. Response returned as structured message + property cards + suggestion chips.

---

## Frontend Experience

### Pages

- **Homepage:** Hero, premium featured properties, and Instagram-style brand grid.
- **Property Listing:** Grid exploration of global inventory.
- **Property Detail:** Full specification + investment stats.
- **Investment Insights:** Strategic market summaries.
- **AI Panel:** Floating intelligence command center with typed responses, cards, and suggestion buttons.

### Design System

- **Palette:** Gold `#C19A5B`, Black `#0A0A0A`, Ivory `#E9E4E1`, Dark Gray `#2C2C34`.
- **Typography:** Cinzel for headlines/wordmark, Montserrat for body.
- **Motion:** Lift + glow card hover, smooth panel transitions, subtle luminous accents.

---

## Local Setup

### Backend

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:5173`.

---

## Scalability Notes

- Swap deterministic embeddings for managed embeddings (OpenAI, Voyage, Cohere).
- Extend vector metadata filters for jurisdiction, asset class, and risk profile.
- Add auth, CRM integrations, and portfolio workspaces.
- Add event streaming + analytics for institutional operator dashboards.
