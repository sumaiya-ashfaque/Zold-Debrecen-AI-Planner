from __future__ import annotations
from copy import deepcopy

WEIGHTS = {
    "canopy_deficit": 0.28,
    "heat_exposure": 0.25,
    "public_benefit": 0.20,
    "feasibility": 0.17,
    "green_connectivity": 0.10,
}

def score_candidate(feature: dict, public_priority: bool = False):
    item = deepcopy(feature)
    factors = item["properties"]["factors"].copy()
    weights = WEIGHTS.copy()

    if public_priority:
        weights["public_benefit"] = 0.30
        weights["canopy_deficit"] = 0.23
        weights["heat_exposure"] = 0.22
        weights["feasibility"] = 0.15
        weights["green_connectivity"] = 0.10

    score = sum(float(factors[k]) * weights[k] for k in weights)
    item["properties"]["opportunity_score"] = round(score, 3)
    item["properties"]["status"] = (
        "recommended_for_site_inspection"
        if score >= 0.78
        else "potential_candidate"
        if score >= 0.65
        else "low_priority"
    )
    return item

def rank_candidates(features: list[dict], public_priority: bool = False):
    scored = [score_candidate(f, public_priority=public_priority) for f in features]
    return sorted(scored, key=lambda f: f["properties"]["opportunity_score"], reverse=True)
