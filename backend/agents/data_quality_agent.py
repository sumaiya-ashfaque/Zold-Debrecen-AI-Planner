from __future__ import annotations
import pandas as pd
import numpy as np

VALID_RANGES = {
    "temperature_c": (-35.0, 55.0),
    "humidity_pct": (0.0, 100.0),
    "pm25_ug_m3": (0.0, 1000.0),
    "soil_moisture_pct": (0.0, 100.0),
}

def clean_environmental_data(df: pd.DataFrame):
    cleaned = df.copy()
    flags = []

    for idx, row in cleaned.iterrows():
        row_flags = []
        for col, (low, high) in VALID_RANGES.items():
            value = row.get(col)
            if pd.isna(value):
                row_flags.append(f"{col}:missing")
                continue
            if value < low or value > high:
                row_flags.append(f"{col}:invalid")
                cleaned.loc[idx, col] = np.nan
        flags.append(row_flags)

    numeric_cols = list(VALID_RANGES)
    cleaned[numeric_cols] = cleaned[numeric_cols].interpolate(limit_direction="both")
    cleaned["quality_flags"] = flags
    cleaned["quality_score"] = cleaned["quality_flags"].apply(
        lambda x: max(0.0, round(1.0 - 0.18 * len(x), 2))
    )

    report = {
        "records": int(len(cleaned)),
        "flagged_records": int(sum(bool(x) for x in flags)),
        "valid_records": int(sum(not x for x in flags)),
        "mean_quality_score": round(float(cleaned["quality_score"].mean()), 3) if len(cleaned) else 0.0,
    }
    return cleaned, report
