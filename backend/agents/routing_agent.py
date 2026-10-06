from backend.optimization.resource_allocator import allocate_actions
from backend.optimization.route_optimizer import build_routes

def create_operational_routes(selected_actions: list[dict], crews: int, trucks: int):
    allocations = allocate_actions(selected_actions, crews=crews, trucks=trucks)
    return build_routes(allocations)
