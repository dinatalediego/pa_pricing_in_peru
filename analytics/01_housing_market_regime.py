"""EDA inicial del mercado inmobiliario peruano con BCRPData.

Ejecutar desde raíz:
    python analytics/01_housing_market_regime.py

Guarda resultados en data/processed y reports/figures.
"""

from pathlib import Path
import sys

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.bcrp_api import get_series_json, json_to_frame

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

series_codes = list(SERIES)
payload = get_series_json(series_codes, start="2013-1", end="2026-1")
df = json_to_frame(payload, series_codes).rename(columns=SERIES)

for column in SERIES.values():
    if column in df:
        df[f"{column}_yoy_pct"] = df[column].pct_change(4) * 100

df.to_csv(OUT / "bcrp_housing_quarterly.csv", index=False)

if "housing_hedonic_index" in df:
    ax = df.plot(
        x="period",
        y="housing_hedonic_index",
        figsize=(11, 5),
        legend=False,
    )
    ax.set_title("Lima: índice hedónico de precios de inmuebles")
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
