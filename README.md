# Pricing & Market Analytics in Peru — Thesis Research Lab

Repositorio de investigación para desarrollar una tesis sobre **pricing dinámico, demanda y absorción inmobiliaria en Perú**, con énfasis en economía aplicada, econometría, data analytics y decision intelligence.

## Tesis de trabajo principal

> **Pricing dinámico y absorción en vivienda nueva en Lima: efecto de cambios de precio y descuentos sobre la probabilidad y velocidad de venta, con heterogeneidad por etapa, tipología, inventario y condiciones de mercado.**

La contribución no será “predecir el precio”, sino estimar:

**pricing → demanda → duración → inventario → decisión**

## Arquitectura de datos a dos escalas

### MICRO — Medallio / Cygnus
`bd_replica_crm` y `medallio_dw` funcionan como **cliente/fuente externa privada**.

Aportan:
- lifecycle real;
- stock;
- ventas;
- separaciones/anulaciones;
- absorción;
- time-to-sale;
- pricing/descuentos cuando se demuestre historia point-in-time.

Este repositorio **no importa código ni RAW** desde `bd_replica_crm`; consume SELECT/extracts mediante contrato versionado y sin PII.

### MERCADO — Peruvian Real Estate Longitudinal Data Engine
Aporta:
- asking prices longitudinales;
- competencia;
- oferta;
- listing age;
- cambios de precio;
- geografía;
- benchmarks de mercado.

### RESEARCH — pa_pricing_in_peru
Es dueño de:
- literatura;
- hypotheses;
- data contracts;
- identificación;
- econometría;
- ML complementario;
- robustness;
- resultados;
- RAG.

Ver: `research/06_dual_scale_research_architecture.md`.

## Estructura

- `research/00_profile_and_interests.md`: intereses y ventajas comparativas.
- `research/01_thesis_shortlist.md`: ranking de temas.
- `research/02_gap_matrix.md`: literatura → gap → contribución.
- `research/03_data_plan.md`: datasets y granularidad.
- `research/04_methodology_playbook.md`: diseños econométricos.
- `research/05_broader_market_scan.md`: alternativas de mercado.
- `research/06_dual_scale_research_architecture.md`: micro privado + mercado longitudinal.
- `research/07_microdata_gap_matrix.md`: readiness de Medallio para T1.
- `contracts/medallio_research_client_v1.md`: frontera SELECT-only con Medallio.
- `contracts/market_longitudinal_engine_v1.md`: contrato del panel de mercado.
- `literature/literature_matrix.csv`: matriz de papers/tesis.
- `data/catalog_sources.csv`: fuentes.
- `analytics/`: análisis reproducibles y findings.
- `rag/README.md`: convenciones de recuperación.

## Gate actual

Medallio ya tiene una base fuerte para **outcomes**: lifecycle, venta, movimientos de stock, stock diario y absorción.

El principal gap que debe demostrarse antes de escoger estimador es:

> **¿Existe suficiente historia point-in-time de precio de lista, precio efectivo y descuento para identificar eventos de repricing?**

Ejecutar en modo solo lectura:

`analytics/sql/00_medallio_readiness_discovery.sql`

Después medir:
- unidades con ≥1 / ≥2 repricings;
- días entre cambios;
- magnitud del cambio;
- price cuts vs increases;
- cambios de descuento;
- venta posterior 7/30/60/90 días;
- overlap treated/control.

La estructura real del tratamiento decidirá el diseño econométrico.

## Regla de investigación

**literatura → gap → datos → identificación → estimación → decisión → evidencia**

No declarar causalidad con:
- correlaciones;
- feature importance;
- forecast;
- SHAP;
- desaparición de listings como venta confirmada.

## Privacidad

No se versionan datos privados de cliente, PII, credenciales ni dumps. `.gitignore` protege rutas de extractos privados por defecto.

## Estado

Arquitectura inicial y primera revisión de literatura: **2026-09-10**.
