# Analytics Roadmap

## Objetivo

No limitar el repositorio a revisión bibliográfica. Cada tema debe producir evidencia computable y versionada.

## Fase A — Public-data EDA

### Vivienda
Outputs:
- índice hedónico y variaciones YoY/QoQ;
- precios/m² por distrito;
- PER venta/alquiler;
- tasa hipotecaria y crédito;
- materiales de construcción;
- régimen macro/inmobiliario.

### Combustibles
Outputs:
- distribución de precios;
- dispersión por mercado local;
- mapas de competencia;
- velocidad y asimetría de pass-through.

### Cacao
Outputs:
- precio internacional vs chacra;
- producción/rendimiento;
- transmisión regional;
- heterogeneidad.

## Fase B — Microdata inmobiliaria

Tablas analíticas recomendadas:

### unit_price_panel
Una fila por unidad-fecha:
- unit_id
- date
- project_id
- typology
- area_m2
- list_price
- final_price
- discount_pct
- commercial_state
- stock_age_days
- project_stock
- project_stage

### unit_sale_event
- unit_id
- first_stock_date
- separation_date
- sale_date
- event
- duration_days

### project_market_panel
- project_id
- month
- inventory
- sales
- absorption
- avg_list_price_m2
- avg_effective_price_m2
- avg_discount
- competitor metrics
- mortgage_rate
- fx
- construction_cost_index

## Model ladder

1. descriptive facts;
2. OLS/panel FE;
3. survival;
4. event study / DiD;
5. IV if credible;
6. heterogeneity;
7. predictive ML challenger;
8. policy simulation.

## Output contract

Cada análisis debe guardar:
- tabla final CSV/parquet;
- figura PNG/SVG;
- notebook/script;
- `findings.md` con 3–10 conclusiones;
- assumptions;
- data_version;
- timestamp.

El RAG debe recuperar **conclusiones con provenance**, no outputs huérfanos.
