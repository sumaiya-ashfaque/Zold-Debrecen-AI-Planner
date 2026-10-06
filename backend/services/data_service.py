from pathlib import Path
import json
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data" / "demo"

def load_json(name: str):
    return json.loads((DATA_DIR / name).read_text(encoding="utf-8"))

def load_csv(name: str) -> pd.DataFrame:
    return pd.read_csv(DATA_DIR / name)

def planting_candidates():
    return load_json("planting_candidates.geojson")["features"]

def tree_groups():
    return load_json("tree_groups.geojson")["features"]

def resources():
    return load_json("resources.json")

def weather():
    return load_json("weather.json")

def environmental():
    return load_csv("green_sentinel_sample.csv")
