from backend.models.schemas import PlanRequest
from backend.api.routes import _make_plan

SCENARIOS = ["base", "rain", "truck_unavailable", "budget_cut", "emergency_dry", "public_priority"]

if __name__ == "__main__":
    print("scenario,new_trees,urgent_coverage_pct,water_liters,distance_km")
    for scenario in SCENARIOS:
        plan = _make_plan(PlanRequest(scenario=scenario))
        k = plan["kpis"]
        print(f"{scenario},{k['new_trees_selected']},{k['urgent_coverage_pct']},{k['water_used_liters']},{k['distance_km']}")
