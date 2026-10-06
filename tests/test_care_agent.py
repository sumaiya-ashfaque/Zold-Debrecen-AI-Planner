from backend.services.data_service import tree_groups, weather
from backend.agents.tree_care_agent import prioritize_tree_groups

def test_rain_reduces_or_delays_some_care():
    base = prioritize_tree_groups(tree_groups(), weather(), scenario="base")
    rain = prioritize_tree_groups(tree_groups(), weather(), scenario="rain")
    base_water = sum(x["properties"]["planned_water_liters"] for x in base)
    rain_water = sum(x["properties"]["planned_water_liters"] for x in rain)
    assert rain_water <= base_water
