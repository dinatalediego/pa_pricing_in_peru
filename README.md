# Pricing & Market Analytics in Peru — Thesis Research Lab

Repositorio de investigación para identificar, comparar y desarrollar temas de tesis sobre **pricing, demanda, competencia y mercados peruanos**, con énfasis en economía aplicada, econometría, data analytics y decision intelligence.

## Objetivo

Convertir evidencia pública y privada en una línea de investigación reproducible:

**literatura → gap → datos → identificación → estimación → decisión → evidencia**

El repositorio está diseñado también como base documental para un **RAG**. Por ello, los hallazgos importantes se guardan en Markdown/CSV con títulos explícitos, fechas, fuente, método, variables y relevancia para la tesis.

## Hipótesis de trabajo principal

La línea con mejor combinación de ajuste al perfil, originalidad y ventaja de datos es:

> **Pricing dinámico y absorción en vivienda nueva en Lima: efecto de cambios de precio y descuentos sobre la probabilidad y velocidad de venta, con heterogeneidad por etapa, tipología y condiciones de mercado.**

La contribución no sería “predecir el precio” sino estimar **cómo responde la demanda/absorción ante decisiones de pricing** y cómo esa respuesta cambia según inventario, etapa del proyecto y entorno macroeconómico.

## Estructura

- `research/00_profile_and_interests.md`: intereses y ventajas comparativas del investigador.
- `research/01_thesis_shortlist.md`: ranking de temas candidatos.
- `research/02_gap_matrix.md`: comparación literatura → gap → contribución.
- `research/03_data_plan.md`: datasets públicos/privados y granularidad.
- `research/04_methodology_playbook.md`: diseños econométricos y analytics sugeridos.
- `literature/literature_matrix.csv`: matriz estructurada de tesis/papers/publicaciones.
- `literature/README.md`: lectura narrativa de la literatura.
- `data/catalog_sources.csv`: catálogo inicial de fuentes.
- `analytics/README.md`: outputs analíticos esperados.
- `src/bcrp_api.py`: cliente mínimo para BCRPData.
- `analytics/01_housing_market_regime.py`: EDA reproducible del mercado inmobiliario.
- `rag/README.md`: convenciones para recuperación RAG.

## Regla de selección de tesis

Una idea solo pasa a “candidata fuerte” si cumple simultáneamente:

1. existe una pregunta económica clara;
2. hay un gap demostrable frente a literatura peruana;
3. existe o puede construirse data suficiente;
4. puede plantearse una estrategia de identificación creíble;
5. el resultado tiene interpretación de negocio/política, no solo precisión predictiva.

## Estado

Primera revisión de literatura y arquitectura de investigación: **2026-09-10**.

La matriz debe actualizarse cada vez que se encuentre una tesis, paper, dataset o hecho estilizado que cambie la evaluación de un tema.
