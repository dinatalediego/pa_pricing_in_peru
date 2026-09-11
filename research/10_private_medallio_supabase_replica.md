# Private Medallio Supabase Replica — Research Bridge

Fecha: 2026-09-11
Estado: TARGET READY / DATA LOAD PENDING

## Objetivo

Permitir que `pa_pricing_in_peru` consulte Medallio remotamente sin mover lógica operativa fuera de `bd_replica_crm`.

## Arquitectura

```text
medallio_dw local
    │
    │ source read-only
    ▼
bd_replica_crm
scripts/sync_medallio_to_supabase.py
    │
    ▼
Supabase private schemas
medallio_raw_cygnus
medallio_raw_mercado
medallio_core
medallio_analytics
...
    │
    ▼
medallio_research
PII-free semantic views
    │
    ▼
pa_pricing_in_peru
econometrics / causal inference / RAG
```

## Seguridad validada

Los schemas `medallio_*` fueron creados en el Supabase conectado.

Se verificó que:
- `anon` no tiene USAGE;
- `authenticated` no tiene USAGE;
- `service_role` no tiene USAGE.

No deben agregarse estos schemas a la lista de Data API exposed schemas.

## Qué se replica

La fase inicial copia únicamente **BASE TABLES** de:

- raw_cygnus
- raw_mercado
- staging
- core
- analytics
- etl_control
- features
- decision_intelligence
- model_control
- experiments
- observability

Los views no se duplican como source of truth. Se reconstruyen como research semantics después.

## Datos sensibles

La réplica privada puede contener PII porque refleja el DW completo.

Regla:
- raw replica: privada;
- medallio_research: sin identificadores directos;
- GitHub: nunca contiene filas privadas;
- outputs académicos: agregados/anonimizados.

## Primeras relaciones prioritarias después de la carga

1. `medallio_raw_mercado.unidades_historial`
2. `medallio_raw_cygnus.proforma_unidad`
3. `medallio_raw_cygnus.proformas`
4. `medallio_raw_cygnus.unidades`
5. `medallio_core.fact_ciclo_comercial_unidad` si es tabla física replicada
6. tablas físicas de stock/ventas/absorción en `medallio_analytics`

## Research layer futuro

Crear en `medallio_research`:

- `v_list_price_history`
- `v_repricing_events`
- `v_quote_history`
- `v_quote_discounts`
- `v_unit_outcomes`
- `v_pricing_outcome_panel`
- `v_pricing_market_bridge`

## Gate de promoción

No usar una relación para econometría hasta verificar:

- grain;
- cardinalidad;
- cobertura temporal;
- leakage;
- nulls;
- duplicados;
- semántica de pricing;
- source/target row parity.
