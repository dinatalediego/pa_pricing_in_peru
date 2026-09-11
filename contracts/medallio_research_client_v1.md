# Medallio Research Client Contract v1

Estado: DRAFT
Fecha: 2026-09-10

## Propósito

Definir qué necesita `pa_pricing_in_peru` de Medallio sin acoplar repositorios ni mover RAW/PII al proyecto académico.

## Ownership

### Medallio / bd_replica_crm
Es dueño de:
- replicación;
- semántica operacional;
- reconciliación;
- lifecycle;
- stock;
- absorción;
- data quality;
- point-in-time correctness.

### pa_pricing_in_peru
Es dueño de:
- research design;
- econometría;
- causal inference;
- comparación de modelos;
- resultados de tesis;
- knowledge/RAG.

## Modo de acceso

**SELECT-only.**

Preferencias:
1. vistas `core.*` / `analytics.*` certificadas;
2. export temporal reproducible;
3. nunca reconstruir reglas comerciales desde `raw_cygnus` dentro de la tesis.

## Objetos ya útiles observados en Medallio

La arquitectura actual ya proporciona o documenta:

- `core.dim_proyecto`
- `core.dim_unidad`
- `core.fact_ciclo_comercial_unidad`
- `analytics.v_ciclo_comercial_reconciliado`
- `analytics.fact_movimientos_stock`
- `analytics.fact_ventas_detalle`
- `analytics.agg_ventas_mensual`
- `analytics.dim_periodo_comercial_proyecto`
- `analytics.fact_stock_ofertado_diario`
- `analytics.fact_absorcion_proyecto_diario`

La absorción detallada por producto está planificada después de validación física de atributos.

## Gap crítico para T1

La propia documentación de Medallio distingue entre:
- dimensión de estado actual;
- lifecycle/stock temporal.

Para T1 falta demostrar el componente esencial:

> **historia point-in-time de precio de lista, precio efectivo y descuento por unidad/proyecto.**

Sin este componente podemos estudiar absorción y duración, pero no identificar adecuadamente una elasticidad de repricing.

## Research extract mínimo

Grain preferido:

`unit_research_id × observed_date`

Campos requeridos:

### Identidad anónima
- unit_research_id
- project_research_id

### Producto
- typology
- bedrooms
- floor
- area_m2

### Estado temporal
- observed_date
- commercial_state
- in_offer_stock
- stock_age_days

### Pricing
- list_price
- effective_price
- discount_amount
- discount_pct
- price_change_flag
- price_change_pct
- price_valid_from

### Outcomes
- separation_event
- cancellation_event
- sale_event
- separation_date
- sale_date

### Contexto proyecto
- project_stage
- project_stock
- project_sales_30d
- project_absorption_30d

## No requerido

Para la pregunta T1 inicial:
- nombre de cliente;
- documento;
- teléfono;
- email;
- texto de interacciones;
- asesor individual.

No deben salir de Medallio.

## Data quality gates

Antes de modelar:

1. grain único;
2. no future leakage;
3. pricing válido as-of observed_date;
4. sale_date >= first_stock_date;
5. price_valid_from <= observed_date;
6. cambios de precio auditables;
7. reingresos de stock consistentes;
8. unidades/proyectos no huérfanos;
9. estados reconciliados;
10. cobertura temporal declarada.

## Export manifest

Cada extracción debe registrar:

```yaml
contract_version: medallio_research_client_v1
extract_id:
generated_at:
source_database: medallio_dw
source_relations:
min_observed_date:
max_observed_date:
rows:
units:
projects:
pricing_coverage_pct:
repriced_units_pct:
pii_included: false
query_sha256:
```

## Boundary

Este contrato puede evolucionar.

La solución correcta ante un nuevo requerimiento es:
1. extender contrato;
2. versionarlo;
3. consultar vista certificada;
4. no copiar lógica interna de Medallio a la tesis.
