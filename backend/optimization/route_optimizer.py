from __future__ import annotations
from math import radians, sin, cos, asin, sqrt

DEPOT = [21.62825, 47.52055]

def haversine_km(a, b):
    lon1, lat1 = a
    lon2, lat2 = b
    dlon = radians(lon2 - lon1)
    dlat = radians(lat2 - lat1)
    lat1r = radians(lat1)
    lat2r = radians(lat2)
    x = sin(dlat/2)**2 + cos(lat1r) * cos(lat2r) * sin(dlon/2)**2
    return 6371.0088 * 2 * asin(sqrt(x))

def greedy_route(tasks: list[dict], depot=DEPOT):
    remaining = tasks[:]
    current = depot
    ordered = []
    distance = 0.0

    while remaining:
        next_task = min(remaining, key=lambda t: haversine_km(current, t["coordinate"]))
        distance += haversine_km(current, next_task["coordinate"])
        ordered.append(next_task)
        current = next_task["coordinate"]
        remaining.remove(next_task)

    if ordered:
        distance += haversine_km(current, depot)

    return ordered, round(distance, 2)

def build_routes(allocations: list[dict], depot=DEPOT):
    groups = {}
    for item in allocations:
        key = item["truck_id"] or item["crew_id"]
        groups.setdefault(key, []).append(item)

    routes = []
    for resource_id, tasks in groups.items():
        ordered, distance = greedy_route(tasks, depot=depot)
        current_minute = 7 * 60
        schedule = []
        for task in ordered:
            hh, mm = divmod(current_minute, 60)
            schedule.append({
                **task,
                "scheduled_time": f"{hh:02d}:{mm:02d}",
            })
            current_minute += task["duration_minutes"] + 20

        routes.append({
            "resource_id": resource_id,
            "distance_km": distance,
            "schedule": schedule,
        })
    return routes
