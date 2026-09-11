"""Perfil SELECT-only de Medallio para T1.

Uso:
    set MEDALLIO_DSN=postgresql://...
    python analytics/medallio_readiness.py

No importa código de bd_replica_crm ni modifica medallio_dw.
Los CSV de detalle se guardan bajo data/private/ y quedan fuera de Git.
"""

from __future__ import annotations

import os
from pathlib import Path

import pandas as pd
import psycopg2

ROOT = Path(__file__).resolve().parents[1]
PRIVATE = ROOT / "data" / "private"
FINDINGS = ROOT / "analytics" / "findings"
PRIVATE.mkdir(parents=True, exist_ok=True)
FINDINGS.mkdir(parents=True, exist_ok=True)

dsn = os.getenv("MEDALLIO_DSN")
if not dsn:
    raise SystemExit("Falta MEDALLIO_DSN. No guardes credenciales en Git.")

relations_sql = """
SELECT table_schema, table_name, table_type
FROM information_schema.tables
WHERE table_schema IN ('core','analytics','raw_cygnus','raw_mercado')
  AND (
    table_name ILIKE '%unidad%' OR table_name ILIKE '%stock%'
    OR table_name ILIKE '%venta%' OR table_name ILIKE '%absor%'
    OR table_name ILIKE '%precio%' OR table_name ILIKE '%proforma%'
  )
ORDER BY table_schema, table_name
"""

pricing_sql = """
SELECT table_schema, table_name, ordinal_position, column_name, data_type
FROM information_schema.columns
WHERE table_schema IN ('core','analytics','raw_cygnus','raw_mercado')
  AND (
    column_name ILIKE '%precio%' OR column_name ILIKE '%price%'
    OR column_name ILIKE '%descuento%' OR column_name ILIKE '%discount%'
    OR column_name ILIKE '%monto%' OR column_name ILIKE '%lista%'
  )
ORDER BY table_schema, table_name, ordinal_position
"""

temporal_sql = """
SELECT table_schema, table_name, ordinal_position, column_name, data_type
FROM information_schema.columns
WHERE table_schema IN ('core','analytics','raw_cygnus','raw_mercado')
  AND (
    column_name ILIKE '%fecha%' OR column_name ILIKE '%date%'
    OR column_name ILIKE '%created%' OR column_name ILIKE '%updated%'
    OR column_name ILIKE '%vigencia%' OR column_name ILIKE '%snapshot%'
    OR column_name ILIKE '%observed%'
  )
ORDER BY table_schema, table_name, ordinal_position
"""

with psycopg2.connect(dsn) as conn:
    conn.set_session(readonly=True)
    relations = pd.read_sql_query(relations_sql, conn)
    pricing = pd.read_sql_query(pricing_sql, conn)
    temporal = pd.read_sql_query(temporal_sql, conn)
    conn.rollback()

relations.to_csv(PRIVATE / "medallio_readiness_relations.csv", index=False)
pricing.to_csv(PRIVATE / "medallio_pricing_columns.csv", index=False)
temporal.to_csv(PRIVATE / "medallio_temporal_columns.csv", index=False)

pricing_tables = (
    pricing.groupby(["table_schema","table_name"])
    .size().reset_index(name="pricing_like_columns")
    .sort_values("pricing_like_columns", ascending=False)
)
temporal_tables = (
    temporal.groupby(["table_schema","table_name"])
    .size().reset_index(name="temporal_like_columns")
    .sort_values("temporal_like_columns", ascending=False)
)

summary = [
    "# Medallio readiness local",
    "",
    "Generado por analytics/medallio_readiness.py.",
    "",
    "## Resumen",
    f"- Relaciones candidatas: {len(relations)}",
    f"- Relaciones con señales de pricing: {pricing[['table_schema','table_name']].drop_duplicates().shape[0]}",
    f"- Relaciones con señales temporales: {temporal[['table_schema','table_name']].drop_duplicates().shape[0]}",
    "",
    "## Top pricing",
    pricing_tables.head(20).to_markdown(index=False),
    "",
    "## Top temporal",
    temporal_tables.head(20).to_markdown(index=False),
    "",
    "## Gate siguiente",
    "",
    "Demostrar una relación con múltiples observaciones históricas por unidad",
    "que contenga simultáneamente precio/descuento y fecha de vigencia/observación.",
    "",
    "No interpretar fecha_precio_actualizado como historia longitudinal sin esa prueba.",
]
(FINDINGS / "medallio_readiness_local.md").write_text("\n".join(summary), encoding="utf-8")

print("\n".join(summary[:8]))
print(f"Detalle privado: {PRIVATE}")
