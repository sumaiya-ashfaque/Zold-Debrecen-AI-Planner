from backend.api.routes import _make_plan
from backend.models.schemas import PlanRequest

def test_base_plan_has_routes_and_kpis():
    plan = _make_plan(PlanRequest())
    assert "routes" in plan
    assert "kpis" in plan
    assert plan["kpis"]["urgent_coverage_pct"] >= 0

def test_truck_unavailable_reduces_truck_count():
    plan = _make_plan(PlanRequest(scenario="truck_unavailable"))
    assert plan["resources"]["trucks"] == 1
