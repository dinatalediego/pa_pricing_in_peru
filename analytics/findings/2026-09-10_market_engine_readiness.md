---
type: finding
market: housing
country: Peru
date_added: 2026-09-10
confidence: high
thesis_topics: [T1, T3]
---

# Peruvian Real Estate Longitudinal Data Engine — readiness para T1

## Claim

La capa longitudinal de mercado ya tiene profundidad suficiente para funcionar como **contexto competitivo y fuente de eventos de pricing**, aunque todavía no debe interpretarse como transacciones reales.

## Evidence

| Dataset | Filas | Proyectos | Inicio | Fin observado |
|---|---:|---:|---|---|
| gold.fact_project_snapshot | 11,400 | 681 | 2026-05-17 | 2026-09-11 |
| gold.fact_tipologia_snapshot | 126,779 | 681 | 2026-05-17 | 2026-09-11 |
| gold.fact_project_event | 7,426 | 499 | 2026-05-18 | 2026-09-11 |

Todos los snapshots observados tenían `content_hash` presente y `parse_ok=true`.

## Longitudinal depth

- 531 proyectos con 2+ snapshots.
- 521 proyectos con 5+.
- 415 proyectos con 10+.
- Mediana = 25 fechas/snapshots por proyecto.

## Events

- 4,075 eventos `available_units`.
- 1,354 eventos `price_m2_avg`.
- 1,344 eventos `price_avg`.
- 653 eventos `price_min`.

## Important limitation

Un cambio agregado de precio de proyecto **no equivale necesariamente a repricing**. Puede ser causado por cambio de mix, salida/entrada de unidades, variación de stock o cambio real de precio.

Por ello, para inferencia se debe preferir `fact_tipologia_snapshot`, usar `content_hash` para distinguir reobservaciones y tratar `fact_project_event` como detector, no como prueba causal.

## Decision

**GO para usar el market engine en T1.**

Pendiente: profundidad point-in-time de pricing privado en Medallio, bridge geográfico/proyecto-tipología y overlap temporal entre fuentes.