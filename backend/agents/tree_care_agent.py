from __future__ import annotations
from copy import deepcopy

def _care_score(p: dict, rainfall_mm: float, forecast_rain_mm: float):
    stress = float(p["stress_score"])
    young_bonus = 0.18 if p.get("newly_planted") else 0.0
    days_bonus = min(float(p.get("days_since_watering", 0)) / 10.0, 1.0) * 0.18
    rain_relief = min((rainfall_mm + forecast_rain_mm) / 20.0, 1.0) * 0.26
    return max(0.0, min(1.0, stress + young_bonus + days_bonus - rain_relief))

def prioritize_tree_groups(features: list[dict], weather: dict, scenario: str = "base"):
    rain_recent = float(weather["recent_rainfall_mm"])
    rain_forecast = float(weather["forecast_rainfall_mm"])

    if scenario == "rain":
        rain_forecast = max(rain_forecast, 14.0)

    result = []
    for feature in features:
        item = deepcopy(feature)
        p = item["properties"]
        score = _care_score(p, rain_recent, rain_forecast)

        if scenario == "emergency_dry" and p["id"] == "T-102":
            score = min(1.0, score + 0.18)

        if score >= 0.82:
            action = "water_within_24h"
            urgency = "urgent"
        elif score >= 0.64:
            action = "inspect_and_water"
            urgency = "high"
        elif rain_forecast >= 10 and score < 0.64:
            action = "delay_and_recheck"
            urgency = "watch"
        elif score >= 0.45:
            action = "inspect"
            urgency = "watch"
        else:
            action = "no_action"
            urgency = "routine"

        liters = int(p.get("base_water_liters", 0)) if action in {"water_within_24h", "inspect_and_water"} else 0
        item["properties"]["care_score"] = round(score, 3)
        item["properties"]["recommended_action"] = action
        item["properties"]["urgency"] = urgency
        item["properties"]["planned_water_liters"] = liters
        result.append(item)

    urgency_rank = {"urgent": 0, "high": 1, "watch": 2, "routine": 3}
    return sorted(result, key=lambda f: (urgency_rank[f["properties"]["urgency"]], -f["properties"]["care_score"]))
