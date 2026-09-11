---
type: finding
market: housing
country: Peru
date_added: 2026-09-11
confidence: high
thesis_topics: [T1]
---

# Medallio pricing evidence — second local discovery

## Claim

Medallio sí contiene una fuente histórica explícita para `raw_mercado`, aunque no mediante tablas cuyo nombre incluya `snapshot`.

## Evidence

Del catálogo local exportado:

- `raw_mercado.unidades_historial` existe.
- Tiene al menos `fecha_snapshot`, `precio_lista`, `precio_venta`, `precio_m2`, `fecha_separacion`, `fecha_venta`.
- También existen `raw_mercado.unidades`, `raw_mercado.v_unidades_actual` y `raw_mercado.cargas` con `fecha_snapshot`.
- `etl_control.raw_mercado_load_runs` no existe en la instancia consultada.

Por eso, la búsqueda anterior por `table_name ILIKE '%snapshot%'` produjo un falso negativo conceptual: el histórico está nombrado `unidades_historial`.

## Proformas como segunda fuente temporal

`raw_cygnus.proforma_unidad` expone:
- `codigo_unidad`;
- `codigo_proforma`;
- `precio_venta`;
- `fecha_creacion`;
- `fecha_actualizacion`;
- estado de la proforma.

`raw_cygnus.proformas` expone:
- `precio_base`;
- `precio_venta`;
- `fecha_creacion`;
- `fecha_actualizacion`.

En la muestra local recibida:
- 20 filas de `proforma_unidad`;
- 17 unidades únicas;
- 2 unidades aparecen en más de una proforma;
- ninguna de esas repeticiones muestra variación de `precio_venta` dentro de la muestra;
- 40 proformas revisadas;
- 7 tienen `precio_venta < precio_base`.

Esta muestra no permite estimar frecuencia histórica de repricing, pero demuestra que puede construirse una historia de cotizaciones y descuentos negociados.

## Semantic warning

No confundir:

1. `raw_mercado.unidades_historial` → snapshots de inventario/precio de la fuente mercado.
2. `proforma_unidad` / `proformas` → precios cotizados/negociados dentro del funnel comercial.
3. policy/list-price history → aún debe demostrarse para `raw_cygnus`.

Una cotización distinta a otra puede reflejar negociación por cliente, bundle de unidades o condiciones comerciales, no necesariamente un cambio general de lista.

## Next test

Perfilar `raw_mercado.unidades_historial` completo:
- filas;
- unidades;
- proyectos;
- rango de `fecha_snapshot`;
- snapshots por unidad;
- unidades con variación de `precio_lista`;
- magnitud y frecuencia de repricing;
- cobertura por proyecto.

Perfilar `proforma_unidad` completo:
- proformas por unidad;
- unidades con múltiples cotizaciones;
- unidades con precio cotizado distinto;
- diferencias temporales;
- relación entre `precio_base` y `precio_venta`;
- alineación posterior con separación/venta.

## Decision

El camino histórico no está bloqueado. El siguiente paso es cuantificar `raw_mercado.unidades_historial` antes de diseñar cualquier nuevo ledger.