# Convenciones RAG

Este repositorio funciona como knowledge base.

## Qué debe indexarse

Prioridad alta:
- `research/*.md`
- `literature/*.csv`
- `analytics/**/findings.md`
- diccionarios de datos
- ADRs/metodología
- resultados agregados

Prioridad baja:
- código boilerplate;
- archivos binarios;
- datasets raw grandes.

## Estructura recomendada para nuevos hallazgos

Usar encabezado:

```
---
type: literature|dataset|finding|gap|method|decision
market: housing|fuel|retail|cacao|macro
country: Peru
date_added: YYYY-MM-DD
source_date: YYYY-MM-DD
confidence: high|medium|low
thesis_topics: [T1, T2]
---
```

Luego:

1. **Claim**
2. **Evidence**
3. **Method**
4. **Limitations**
5. **Why it matters**
6. **Source**
7. **Next test**

## Regla de atomicidad

Una nota debe poder responder una pregunta concreta sin depender de contexto oculto.

Malo:
> “Esto demuestra que conviene subir.”

Bueno:
> “En el paper X, un mayor markup se asocia con mayor precio de venta y mayor time-on-market; para T1 esto implica modelar conjuntamente precio y duración y tratar el pricing como endógeno.”

## Provenance

Nunca convertir:
- correlación → causalidad;
- feature importance → efecto causal;
- screening → prueba de colusión;
- forecast → recomendación óptima

sin evidencia adicional.

## Vocabulario estable

Usar consistentemente:
- `list_price`
- `effective_price`
- `discount_pct`
- `time_on_market`
- `absorption_rate`
- `inventory`
- `sale_hazard`
- `pass_through`

Esto mejora retrieval semántico y reduce sinónimos ambiguos.
