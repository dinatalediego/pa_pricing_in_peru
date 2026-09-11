# Peruvian Real Estate Longitudinal Data Engine — Research Contract v1

Estado: DESIGN
Fecha: 2026-09-10

## Misión

Crear evidencia longitudinal del mercado inmobiliario que complemente, no replique, el microdato privado.

## Grain base

`market_listing_id × snapshot_date`

## Entidades

- listing;
- property/unit;
- project;
- developer/broker cuando sea observable públicamente;
- district/geography;
- snapshot;
- source.

## Variables críticas

### Precio
- asking_price
- currency
- asking_price_pen
- price_m2
- observed_discount/promotion
- previous_asking_price
- asking_price_change_pct

### Producto
- area_m2
- bedrooms
- bathrooms
- parking
- floor
- typology
- delivery_stage / delivery_date proxy

### Temporal
- first_seen_at
- last_seen_at
- snapshot_date
- listing_age_days
- relisted_flag

### Mercado
- active_supply_local
- new_listings_30d
- disappeared_listings_30d
- median_price_m2_local
- price_dispersion_local

### Geografía
- district
- lat/lon when legally/publicly available
- geohash or spatial cell for research
- distance to relevant amenities when derived

## Outcomes proxy

El motor de mercado normalmente no observa venta real.

Debe distinguir explícitamente:

- `listing_disappeared`
- `likely_sold_proxy`
- `sold_confirmed`

Nunca tratar desaparición del portal como venta confirmada sin evidencia.

## Lo que cubre frente a Medallio

| Concepto | Medallio | Market engine |
|---|---|---|
| Venta real | Sí | generalmente no |
| Separación/anulación | Sí | no |
| Precio efectivo transado | potencialmente sí | no |
| Asking price | sí/depende | sí |
| Histórico de competidores | no completo | sí |
| Stock mercado | parcial | sí/proxy |
| Time-on-market | real interno | listing proxy |
| Geografía externa | parcial | fuerte |
| Validez externa | limitada a empresa | amplia |

## Bridge keys

No unir a nivel de cliente.

Joins permitidos:
- date/week/month;
- district;
- spatial cell;
- typology;
- bedroom bucket;
- area bucket;
- price segment;
- project when publicly identifiable and research-appropriate.

## Derived market controls

Para cada unidad/fecha del micro:

- competitor_stock_1km/3km;
- competitor_median_price_m2;
- relative_price_index;
- local_new_supply_30d;
- local_listing_age_median;
- local_price_change_rate;
- local_discount_share.

Esto permite estimar si una respuesta a precio depende de la presión competitiva.

## Calidad

- deduplicación cross-snapshot;
- entity resolution documentado;
- source provenance;
- no confundir listing con unit;
- no imputar sale sin flag de incertidumbre;
- snapshots append-only;
- raw immutable fuera del research mart;
- tests de continuidad de series.

## Valor académico

Este motor convierte la tesis de una evaluación de una firma en:

> un estudio microeconómico de pricing con contexto competitivo longitudinal del mercado peruano.
