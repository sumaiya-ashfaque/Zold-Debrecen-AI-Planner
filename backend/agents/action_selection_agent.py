from __future__ import annotations

def select_actions(planting: list[dict], care: list[dict], budget_huf: int, water_liters: int, scenario: str = "base"):
    actions = []

    available_budget = int(budget_huf * 0.75) if scenario == "budget_cut" else budget_huf

    for item in planting:
        p = item["properties"]
        if p["status"] == "low_priority":
            continue
        total_cost = int(p["estimated_cost_huf"])
        actions.append({
            "task_id": f"PLANT-{p['id']}",
            "type": "plant",
            "priority": round(70 + p["opportunity_score"] * 30, 2),
            "area": p["area"],
            "label": f"Plant {p['recommended_trees']} trees at {p['id']}",
            "cost_huf": total_cost,
            "water_liters": 0,
            "duration_minutes": int(p.get("duration_minutes", 120)),
            "coordinate": item["geometry"]["coordinates"],
            "mandatory": False,
        })

    urgency_bonus = {"urgent": 35, "high": 25, "watch": 12, "routine": 0}
    for item in care:
        p = item["properties"]
        if p["recommended_action"] == "no_action":
            continue
        actions.append({
            "task_id": f"CARE-{p['id']}",
            "type": "care",
            "priority": round(55 + p["care_score"] * 30 + urgency_bonus[p["urgency"]], 2),
            "area": p["area"],
            "label": f"{p['recommended_action'].replace('_', ' ').title()} — {p['id']}",
            "cost_huf": int(p.get("service_cost_huf", 25000)),
            "water_liters": int(p["planned_water_liters"]),
            "duration_minutes": int(p.get("duration_minutes", 45)),
            "coordinate": item["geometry"]["coordinates"],
            "mandatory": p["urgency"] == "urgent",
        })

    actions.sort(key=lambda x: (not x["mandatory"], -x["priority"]))

    selected = []
    used_budget = 0
    used_water = 0
    for action in actions:
        if used_budget + action["cost_huf"] > available_budget:
            continue
        if used_water + action["water_liters"] > water_liters:
            continue
        selected.append(action)
        used_budget += action["cost_huf"]
        used_water += action["water_liters"]

    return {
        "selected_actions": selected,
        "budget_used_huf": used_budget,
        "budget_limit_huf": available_budget,
        "water_used_liters": used_water,
        "water_limit_liters": water_liters,
    }
