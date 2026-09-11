# Runbook T1 — del histórico de precios al primer dataset econométrico

Fecha: 2026-09-11

## Objetivo

Ejecutar el camino mínimo para demostrar que T1 es empíricamente viable antes de estimar causalidad.

Orden obligatorio:
1. perfilar `raw_mercado.unidades_historial`;
2. perfilar cotizaciones en `raw_cygnus.proforma_unidad` + `raw_cygnus.proformas`;
3. construir eventos de repricing;
4. alinear repricing con stock/lifecycle/venta;
5. medir overlap y cobertura;
6. recién después estimar modelos.

## Gate 1 — historial de lista

Debe responder:
- filas, unidades, proyectos, snapshots, rango temporal;
- unidades con 2+/5+ snapshots;
- unidades con 2+ precios distintos;
- número de price cuts / increases;
- magnitud y frecuencia de cambios.

Si no hay variación suficiente, no usar `precio_lista` como tratamiento causal.

## Gate 2 — historia de cotización / negociación

Usar `proforma_unidad` como grain unidad × proforma y `proformas` para `precio_base` vs `precio_venta`.

Medir:
- unidades con múltiples proformas;
- unidades con múltiples precios cotizados;
- descuento_pct = 1 - precio_venta/precio_base;
- tiempo entre cotizaciones;
- cotización final antes de separación/venta.

Advertencia: precio cotizado != cambio general de lista.

## Gate 3 — evento de repricing

Construir CTE reproducible con `lag(precio_lista)` por unidad y fecha.

Output mínimo:
- codigo_proyecto;
- codigo_unidad;
- fecha_snapshot;
- precio_anterior;
- precio_lista;
- cambio_abs;
- cambio_pct;
- direction = CUT/INCREASE;
- days_since_previous_snapshot.

## Gate 4 — research panel

Grain objetivo:
`codigo_unidad × observed_date`

Campos:
- proyecto/unidad anonimizados;
- atributos de producto;
- precio_lista vigente;
- precio cotizado si existe;
- descuento;
- estado comercial as-of;
- stock/proyecto as-of;
- absorción 30d as-of;
- separación/venta futura;
- days_to_sale;
- market controls del longitudinal engine.

## Gate 5 — leakage & overlap

Antes de modelar:
- toda feature debe existir en `observed_date`;
- sale_date y outcomes futuros solo como labels;
- treatment debe variar dentro de proyecto/unidad o cohortes comparables;
- comparar treated vs untreated;
- documentar proyectos sin soporte común.

## Gate 6 — model ladder

1. descriptivo;
2. Kaplan–Meier / survival descriptivo;
3. FE / discrete-time hazard;
4. event study si hay timing escalonado;
5. DiD solo si hay policy event defendible;
6. ML para heterogeneidad/challenger, no para causalidad primaria.

## Criterio GO

T1 sigue como tesis principal si:
- hay historia temporal suficiente;
- hay repricing observable;
- existe overlap;
- outcomes pueden alinearse point-in-time;
- la semántica de list/quoted/transaction price queda separada.

Si falla repricing unit-level, bajar treatment a proyecto × tipología × fecha antes de abandonar T1.