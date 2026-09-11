# Microdata readiness — qué ya da Medallio y qué falta para T1

Fecha de revisión: 2026-09-10

Revisión de solo lectura sobre la arquitectura documentada de `bd_replica_crm`.

## Estado observado

Medallio ya avanzó mucho más de lo que necesita una tesis típica en la capa de outcomes.

### Ya resuelto o explícitamente modelado

| Necesidad T1 | Estado Medallio | Lectura |
|---|---|---|
| dimensión proyecto | disponible | core.dim_proyecto |
| dimensión unidad | disponible | core.dim_unidad |
| lifecycle comercial | disponible | fact_ciclo_comercial_unidad |
| reconciliación de venta | disponible | v_ciclo_comercial_reconciliado |
| movimientos de stock | disponible | fact_movimientos_stock |
| stock diario | disponible | fact_stock_ofertado_diario |
| venta detalle | disponible | fact_ventas_detalle |
| ventas mensuales | disponible | agg_ventas_mensual |
| absorción proyecto/día | disponible | fact_absorcion_proyecto_diario |
| absorción detallada producto | siguiente versión | requiere validación atributos |

## Hallazgo principal

El cuello de botella de T1 **ya no es reconstruir ventas o stock**.

El cuello de botella es:

> **reconstruir pricing point-in-time.**

Se necesitan observaciones históricas de:
- precio lista;
- precio final/efectivo;
- descuento;
- regla/campaña;
- fecha de vigencia.

por unidad o, cuando la política haya sido agregada, por proyecto-tipología.

## Cuatro escenarios

### A — Excelente
Existe histórico unit-level de cambios de precio/descuento.

→ T1 puede ser micro causal fuerte.

### B — Bueno
Existe histórico solo proyecto-tipología-fecha.

→ treatment a ese nivel; outcomes siguen unit-level.

### C — Parcial
Solo hay listas de precios periódicas externas/archivadas.

→ reconstruir snapshots y hacer entity matching con unidades.

### D — Débil
Solo existe precio actual + precio final de venta.

→ no afirmar elasticidad dinámica.
Reformular hacia:
- bargaining/discount;
- determinants of time-to-sale;
- macro → effective transaction price;
- market longitudinal engine.

## Información que el mercado longitudinal puede aportar

Aunque Medallio llegue a A/B, el market engine sigue siendo necesario para:

- precio relativo frente a competencia;
- densidad de oferta;
- shocks locales;
- nuevos proyectos;
- price cuts de competidores;
- market regime.

## Primer gate empírico

Antes de estimar cualquier modelo, calcular:

- N proyectos;
- N unidades;
- meses de historia;
- N unidades con ≥1 repricing;
- N unidades con ≥2 repricings;
- mediana días entre repricings;
- distribución price_change_pct;
- share de price cuts vs increases;
- share de cambios de descuento;
- repricing → venta en 7/30/60/90 días;
- tratamiento por proyecto-tipología;
- overlap entre treated/control.

### Go
Hay variación suficiente y overlap.

### Redesign
El pricing cambia solo cuando cambia toda la empresa/proyecto o casi nunca.

## Regla

No escoger el estimador antes de ver esta matriz.

La estructura de tratamiento observada decide si usamos:
- FE;
- event study;
- DiD;
- survival time-varying;
- IV;
- synthetic controls;
- o solo análisis descriptivo/predictivo.
