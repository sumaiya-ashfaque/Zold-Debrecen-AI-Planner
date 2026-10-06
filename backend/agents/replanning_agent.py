from copy import deepcopy

def apply_resource_scenario(resources: dict, scenario: str):
    updated = deepcopy(resources)
    if scenario == "truck_unavailable":
        updated["trucks"] = max(1, updated["trucks"] - 1)
    elif scenario == "budget_cut":
        updated["budget_huf"] = int(updated["budget_huf"] * 0.75)
    return updated
