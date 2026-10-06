from __future__ import annotations

def allocate_actions(actions: list[dict], crews: int, trucks: int):
    if crews <= 0:
        return []

    crew_slots = [{"crew_id": f"Crew {i+1}", "load": 0} for i in range(crews)]
    truck_slots = [{"truck_id": f"Truck {i+1}", "load": 0} for i in range(max(0, trucks))]
    allocations = []

    for action in actions:
        crew = min(crew_slots, key=lambda x: x["load"])
        crew["load"] += action["duration_minutes"]

        truck_id = None
        if action["water_liters"] > 0 and truck_slots:
            truck = min(truck_slots, key=lambda x: x["load"])
            truck["load"] += action["water_liters"]
            truck_id = truck["truck_id"]

        allocations.append({
            **action,
            "crew_id": crew["crew_id"],
            "truck_id": truck_id,
        })

    return allocations
