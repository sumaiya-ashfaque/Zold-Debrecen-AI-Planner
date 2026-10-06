from backend.services.data_service import environmental
from backend.agents.data_quality_agent import clean_environmental_data

def test_invalid_values_are_flagged():
    cleaned, report = clean_environmental_data(environmental())
    assert report["flagged_records"] >= 2
    assert cleaned["temperature_c"].max() <= 55
    assert cleaned["pm25_ug_m3"].min() >= 0
