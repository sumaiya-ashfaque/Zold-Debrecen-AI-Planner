import json
from backend.models.schemas import PlanRequest
from backend.api.routes import _make_plan

if __name__ == "__main__":
    plan = _make_plan(PlanRequest())
    print(json.dumps({
        "scenario": plan["scenario"],
        "kpis": plan["kpis"],
        "routes": [
            {
                "resource_id": r["resource_id"],
                "distance_km": r["distance_km"],
                "tasks": [
                    {
                        "time": t["scheduled_time"],
                        "task": t["label"],
                        "area": t["area"],
                        "water_liters": t["water_liters"],
                    }
                    for t in r["schedule"]
                ],
            }
            for r in plan["routes"]
        ],
    }, indent=2, ensure_ascii=False))
