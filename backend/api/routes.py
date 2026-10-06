from fastapi import APIRouter, HTTPException
from backend.models.schemas import PlanRequest, ReplanRequest, DispatchRequest
from backend.services.data_service import planting_candidates, tree_groups, weather, environmental
from backend.agents.data_quality_agent import clean_environmental_data
from backend.agents.planting_opportunity_agent import rank_candidates
from backend.agents.tree_care_agent import prioritize_tree_groups
from backend.agents.action_selection_agent import select_actions
from backend.agents.routing_agent import create_operational_routes
from backend.agents.replanning_agent import apply_resource_scenario
from backend.services.sms_service import send_mock_sms

router = APIRouter(prefix="/api")

def _make_plan(request: PlanRequest):
    public_priority = request.scenario == "public_priority"
    plant = rank_candidates(planting_candidates(), public_priority=public_priority)
    care = prioritize_tree_groups(tree_groups(), weather(), scenario=request.scenario)

    resources = request.resources.model_dump()
    resources = apply_resource_scenario(resources, request.scenario)

    selection = select_actions(
        plant,
        care,
        budget_huf=resources["budget_huf"],
        water_liters=resources["water_liters"],
        scenario=request.scenario,
    )

    routes = create_operational_routes(
        selection["selected_actions"],
        crews=resources["crews"],
        trucks=resources["trucks"],
    )

    urgent = [x for x in care if x["properties"]["urgency"] == "urgent"]
    selected_ids = {x["task_id"].replace("CARE-", "") for x in selection["selected_actions"]}
    urgent_covered = sum(1 for x in urgent if x["properties"]["id"] in selected_ids)

    return {
        "scenario": request.scenario,
        "resources": resources,
        "planting_candidates": plant,
        "care_priorities": care,
        "selection": selection,
        "routes": routes,
        "kpis": {
            "new_trees_selected": sum(
                x["properties"]["recommended_trees"]
                for x in plant
                if f"PLANT-{x['properties']['id']}" in {a["task_id"] for a in selection["selected_actions"]}
            ),
            "urgent_zones_total": len(urgent),
            "urgent_zones_covered": urgent_covered,
            "urgent_coverage_pct": round(100 * urgent_covered / len(urgent), 1) if urgent else 100.0,
            "water_used_liters": selection["water_used_liters"],
            "distance_km": round(sum(r["distance_km"] for r in routes), 2),
        },
    }

@router.get("/planting/candidates")
def get_planting_candidates():
    return rank_candidates(planting_candidates())

@router.get("/care/priorities")
def get_care_priorities():
    return prioritize_tree_groups(tree_groups(), weather())

@router.get("/data-quality/report")
def get_data_quality_report():
    _, report = clean_environmental_data(environmental())
    return report

@router.post("/plan/generate")
def generate_plan(request: PlanRequest):
    return _make_plan(request)

@router.post("/plan/replan")
def replan(request: ReplanRequest):
    return _make_plan(PlanRequest(scenario=request.scenario))

@router.post("/dispatch/sms")
def dispatch_sms(request: DispatchRequest):
    plan = _make_plan(PlanRequest())
    all_tasks = [t for r in plan["routes"] for t in r["schedule"]]
    task = next((t for t in all_tasks if t["task_id"] == request.task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return send_mock_sms(task, request.destination)
