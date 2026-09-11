# Peruvian Real Estate Longitudinal Data Engine — Research Contract v1

Estado: **VALIDATED CURRENT CONTRACT**
Fecha: 2026-09-10

## Fuente real

Repositorio:
`dinatalediego/decidecasa-platform`

Subproyecto:
`decidecasa-platform/data_inmobiliaria_ml_training/real_analytics_full_project/real_analytics_full_project`

Supabase:
fuente longitudinal de mercado, consumida por `pa_pricing_in_peru` en modo lectura.

## Grains disponibles hoy

### Proyecto × snapshot
`gold.fact_project_snapshot`

Campos observados:
- snapshot_date
- project_key
- source
- project_name
- district_slug
- unit_type_key
- price_min / price_avg / price_max
- price_m2_min / price_m2_avg / price_m2_max
- available_units
- typology_count
- content_hash
- observed_at

### Tipología × snapshot
`gold.fact_tipologia_snapshot`

Campos observados:
- snapshot_date
- project_key
- fuente
- proyecto
- modelo
- area_m2
- precio_desde
- moneda
- precio_m2
- unidades_disponibles
- piso_min / piso_max
- dormitorios
- banos
- content_hash
- scraped_at

### Proyecto × evento
`gold.fact_project_event`

Campos observados:
- event_date
- project_key
- event_type
- metric_name
- old_value
- new_value
- delta_abs
- delta_pct
- previous_snapshot_id
- current_snapshot_id
- old_content_hash
- new_content_hash
- severity
- is_actionable

## Evidencia validada

Al 2026-09-10:
- 11,400 snapshots de proyecto;
- 126,779 snapshots de tipología;
- 7,426 eventos;
- 681 proyectos en el panel de snapshots;
- cobertura desde 2026-05-17;
- 0 content_hash nulos en snapshots revisados.

## Misión para T1

Complementar el microdato privado con:
- asking-price benchmarks;
- variación de precio observable;
- unidades disponibles;
- mix de tipologías;
- presión competitiva;
- geografía;
- evolución temporal de mercado.

## Regla causal

El market engine **no observa venta confirmada del mercado completo**.

Por tanto:
- una caída de `available_units` no equivale automáticamente a venta;
- un cambio de `price_avg` puede reflejar cambio de mix;
- `fact_project_event` detecta cambio, no demuestra causa;
- para repricing se prefiere `fact_tipologia_snapshot` cuando la identidad del producto sea estable.

## Bridge con Medallio

No unir a nivel de cliente.

Joins permitidos:
- date/week/month;
- project cuando sea públicamente identificable;
- district;
- typology;
- bedroom bucket;
- area bucket;
- price segment;
- spatial cell.

## Derived market controls

Para cada observación micro, cuando el bridge sea posible:
- market_price_m2;
- relative_market_price;
- local_available_units;
- local_price_change_rate;
- local_supply_pressure;
- project_market_position;
- market_regime.

## Roadmap — grain futuro

El grain ideal futuro sigue siendo:

`market_listing_id × snapshot_date`

Esto permitiría:
- listing_age_days;
- first_seen_at / last_seen_at;
- relisted_flag;
- asking-price changes a nivel listing;
- desaparición de listings;
- proxies más finos de time-on-market.

**No asumir que este grain existe hasta validarlo explícitamente.**

## Ownership

El engine es dueño de:
- scraping;
- entity resolution;
- snapshotting;
- event detection;
- provenance;
- data quality.

`pa_pricing_in_peru` es dueño de:
- research extract;
- diseño econométrico;
- identificación;
- hipótesis;
- robustness;
- resultados.

## Valor académico

El motor convierte la tesis de una evaluación de una sola firma en:

> un estudio microeconómico de pricing con contexto competitivo longitudinal del mercado peruano.
