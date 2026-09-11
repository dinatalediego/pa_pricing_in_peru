"""EDA inicial del mercado inmobiliario peruano con BCRPData.

Ejecutar desde raíz:
    python analytics/01_housing_market_regime.py

Guarda resultados en data/processed y reports/figures.
"""

from pathlib import Path
import sys

import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.bcrp_api import get_series_json

OUT = ROOT / "data" / "processed"
FIG = ROOT / "reports" / "figures"
OUT.mkdir(parents=True, exist_ok=True)
FIG.mkdir(parents=True, exist_ok=True)

SERIES = {
    "PD37940PQ": "housing_hedonic_index",
    "PD37944PQ": "price_m2_usd_12_districts",
    "PD37941PQ": "price_m2_usd_high_segment",
    "PD38028PQ": "price_m2_usd_middle_segment",
}


def bcrp_json_to_long(payload: dict) -> pd.DataFrame:
    periods = payload["periods"]
    rows = []
    for p in periods:
        row = {"period": p["name"]}
        for item in p.get("values", []):
            row[item["series"]] = item.get("value")
        rows.append(row)
    df = pd.DataFrame(rows)
    for c in df.columns:
        if c != "period":
            df[c] = pd.to_numeric(df[c], errors="coerce")
    return df


payload = get_series_json(list(SERIES), start="2013-1", end="2026-1")
df = bcrp_json_to_long(payload).rename(columns=SERIES)

for c in SERIES.values():
    if c in df:
        df[f"{c}_yoy_pct"] = df[c].pct_change(4) * 100

df.to_csv(OUT / "bcrp_housing_quarterly.csv", index=False)

if "housing_hedonic_index" in df:
    ax = df.plot(x="period", y="housing_hedonic_index", figsize=(11, 5), legend=False)
    ax.set_title("Perú/Lima: índice hedónico de precios de inmuebles")
    ax.set_xlabel("Trimestre")
    ax.set_ylabel("Índice")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig(FIG / "housing_hedonic_index.png", dpi=160)
    plt.close()

latest = df.tail(8)
latest.to_csv(OUT / "bcrp_housing_latest_8q.csv", index=False)

print(latest.to_string(index=False))
print(f"\nSaved: {OUT}")
