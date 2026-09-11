---
type: decision
market: housing
country: Peru
date_added: 2026-09-10
confidence: high
thesis_topics: [T1]
---

# Ejecución del planteamiento T1 — estado real

## Decisión

Se ejecuta la arquitectura de investigación a dos escalas:

1. **MICRO privado:** Cygnus mediante Medallio / `bd_replica_crm`.
2. **MERCADO longitudinal:** Peruvian Real Estate Longitudinal Data Engine dentro de `decidecasa-platform`.
3. **RESEARCH:** `pa_pricing_in_peru` como dueño de literatura, contratos, econometría, resultados y RAG.

Los repositorios fuente permanecen separados.

## Hallazgo A — Medallio ya cubre gran parte de los outcomes

Revisión de solo lectura del código de `dinatalediego/bd_replica_crm` confirma que su arquitectura ya modela o documenta lifecycle, reconciliación de ventas, movimientos de stock, venta detalle, stock diario y absorción.

### Gap Medallio para T1

El gap crítico sigue siendo demostrar **historia point-in-time de pricing**.

Se localizaron señales útiles:
- `raw_cygnus.unidades` expone `precio_lista`, `precio_base_proforma`, `descuento_venta`, `precio_venta`, `precio_m2` y `fecha_precio_actualizado`;
- existe una fuente `unidades_precios_desde`;
- `raw_mercado.unidades` también contiene precios;
- el loader de `raw_mercado` crea snapshots físicos antes de reemplazar el estado corriente.

Pero tener una fecha de precio no demuestra historia por unidad. La prueba final debe ejecutarse contra el PostgreSQL local.

## Hallazgo B — el Peruvian Real Estate Longitudinal Data Engine ya tiene historia real

Repositorio fuente identificado: `dinatalediego/decidecasa-platform`.

Subproyecto: `decidecasa-platform/data_inmobiliaria_ml_training/real_analytics_full_project/real_analytics_full_project`.

Supabase fuente validado en modo read-only.

### Estado observado

- `gold.fact_project_snapshot`: 11,400 filas; 681 proyectos; cobertura 2026-05-17 → 2026-09-11; 0 `content_hash` nulos.
- `gold.fact_tipologia_snapshot`: 126,779 filas; 681 proyectos; cobertura 2026-05-17 → 2026-09-11; 0 `content_hash` nulos.
- `gold.fact_project_event`: 7,426 eventos; 499 proyectos; cobertura 2026-05-18 → 2026-09-11.

### Profundidad longitudinal

Entre los 681 proyectos:
- 531 tienen ≥2 snapshots;
- 521 tienen ≥5;
- 415 tienen ≥10;
- mediana: 25 snapshots/fechas por proyecto.

### Eventos observados

- 4,075 cambios de `available_units` en 488 proyectos;
- 1,354 cambios de `price_m2_avg` en 478 proyectos;
- 1,344 cambios de `price_avg` en 477 proyectos;
- 653 cambios de `price_min` en 353 proyectos.

Promedio de magnitud absoluta observado:
- `price_m2_avg`: ~1.96%;
- `price_avg`: ~3.28%;
- `price_min`: ~8.65%.

Estos valores son descriptivos. Un cambio agregado de precio de proyecto puede deberse a repricing real, cambio del mix de unidades visibles, entrada/salida de tipologías o variaciones de disponibilidad.

## Consecuencia para la tesis

Ya existe una arquitectura empírica real:

```text
MERCADO: snapshots + eventos
        +
MICRO: lifecycle + stock + venta + absorción
        ↓
pa_pricing_in_peru
        ↓
pricing → sale hazard / time-to-sale
```

## Gate inmediato

### MICRO
Ejecutar el profiler local de Medallio y demostrar número de observaciones históricas de pricing por unidad, unidades repriced, secuencia temporal, descuento vigente y relación con venta.

### MERCADO
Usar el panel existente para construir `relative_market_price`, `local_supply`, `market_price_change`, `local_available_units` y benchmarks de precio/m².

## Decisión de arquitectura

**GO.**

El motor longitudinal cumple el mínimo para aportar validez externa y contexto. La condición pendiente para un T1 causal fuerte es la profundidad histórica de pricing dentro de Medallio.