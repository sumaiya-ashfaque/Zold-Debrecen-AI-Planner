# Zöld Debrecen AI Planner

A working prototype for AI-assisted urban greening planning in Debrecen.

The system supports three connected workflows:

- **Plant** — rank candidate locations for new trees.
- **Protect** — prioritize existing tree groups for watering or inspection.
- **Execute** — allocate crews, water, vehicles, and routes under operational constraints.

The repository uses simulated demo assets around real Debrecen locations. It does not represent official municipal decisions.

## Architecture

```text
Green Sentinel-style demo data
Satellite / vegetation indicators
Weather data
Debrecen urban context
          |
          v
Data Quality Agent
          |
          +-------------------+
          |                   |
          v                   v
Planting Opportunity     Tree Care Agent
Agent                    |
          \              /
           v            v
          Action Selection
                 |
                 v
       Resource Allocation
                 |
                 v
        Routing & Scheduling
                 |
                 v
        Dispatch / Replanning
```

## Tech stack

- Frontend: React, TypeScript, Vite, React Leaflet
- Backend: FastAPI, Pydantic, Pandas
- Optimization: OR-Tools with deterministic fallback routing
- Tests: Pytest
- Map: OpenStreetMap

## Repository structure

```text
frontend/             React application
backend/              FastAPI API and multi-agent logic
data/demo/            Seeded prototype datasets
scripts/              Demo and evaluation scripts
tests/                Backend tests
docs/                 Architecture and methodology
```

## Quick start

### Backend

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r backend/requirements.txt
```

Run the API from the repository root:

```bash
uvicorn backend.main:app --reload
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Open:

```text
http://localhost:5173
```

The frontend expects the backend at `http://127.0.0.1:8000`.

## Docker

```bash
docker compose up --build
```

Frontend:

```text
http://localhost:5173
```

Backend:

```text
http://localhost:8000
```

## Main API endpoints

```text
GET  /health
GET  /api/planting/candidates
GET  /api/care/priorities
POST /api/plan/generate
POST /api/plan/replan
POST /api/dispatch/sms
GET  /api/data-quality/report
```

## Demo scenarios

The prototype includes:

- rain forecast change
- one truck unavailable
- 25% budget reduction
- emergency dry-tree group
- priority shift toward schools and public-transport areas

## Data

`data/demo/` contains simulated prototype records for:

- planting candidates
- existing tree groups
- Green Sentinel-style environmental measurements
- weather forecast
- crews and vehicles

Coordinates reference real areas of Debrecen, but scores, asset records, care states, costs, and operational resources are demo values.

## Tests

```bash
pytest -q
```

## License

MIT
