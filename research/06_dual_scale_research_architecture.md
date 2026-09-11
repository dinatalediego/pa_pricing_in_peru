# T1 — Arquitectura de investigación a dos escalas

Fecha: 2026-09-10

## Tesis central

> **Pricing dinámico y absorción en vivienda nueva en Lima: efecto de los cambios de precios y descuentos sobre la probabilidad y velocidad de venta.**

La investigación se construirá con **dos escalas complementarias** que no deben confundirse ni mezclarse físicamente.

---

# 1. Escala MICRO — cliente privado / Cygnus vía Medallio

Fuente operativa externa:

`dinatalediego/bd_replica_crm` → PostgreSQL `medallio_dw`

Rol dentro de la tesis:

- observar ciclos comerciales reales;
- reconstruir entrada/salida de stock;
- medir ventas/separaciones/anulaciones;
- obtener time-to-event real;
- observar tratamientos de pricing cuando exista historia;
- estimar efectos con alta granularidad;
- estudiar heterogeneidad por proyecto, tipología, etapa y stock.

**Medallio es un cliente/fuente de datos, no una dependencia de código de este repositorio.**

El repositorio académico:
- no importa módulos desde `bd_replica_crm`;
- no modifica schemas de Medallio;
- no replica RAW;
- no almacena PII;
- no publica datos comerciales privados;
- consume únicamente extractos/consultas SELECT bajo contrato.

---

# 2. Escala MACRO/MERCADO — Peruvian Real Estate Longitudinal Data Engine

Rol:

Construir un panel longitudinal del mercado inmobiliario peruano para observar aquello que una sola empresa no puede representar:

- oferta competidora;
- asking prices;
- cambios de asking price;
- nuevas publicaciones;
- desaparición/reaparición de listings;
- time-on-market proxy;
- stock por zona;
- precio/m²;
- promociones observables;
- atributos del inmueble/proyecto;
- geografía;
- entorno de tasas, TC, inflación y costos;
- shocks de infraestructura/regulación cuando corresponda.

Esta capa puede crecer sin depender de Cygnus.

---

# 3. Escala ACADÉMICA — pa_pricing_in_peru

Este repositorio es dueño de:

- pregunta de investigación;
- literatura;
- hypotheses;
- data contracts;
- metodología;
- notebooks/scripts de investigación;
- tablas anonimizadas/agregadas;
- resultados;
- robustness checks;
- provenance;
- hallazgos RAG;
- paper/tesis.

No es dueño de sistemas productivos de origen.

---

# 4. Arquitectura lógica

```text
                    ┌──────────────────────────────┐
                    │ Peruvian Real Estate        │
                    │ Longitudinal Data Engine    │
                    │ mercado / competencia       │
                    └──────────────┬───────────────┘
                                   │ market contract
                                   ▼
┌───────────────────────┐   ┌──────────────────────────────┐
│ MEDALLIO              │   │ pa_pricing_in_peru           │
│ bd_replica_crm        │──▶│ Research / Econometrics      │
│ cliente privado       │   │ Causal + Predictive + RAG    │
└───────────────────────┘   └──────────────────────────────┘
      research contract
```

No existe:
`pa_pricing_in_peru -> import bd_replica_crm`

Sí existe:
`pa_pricing_in_peru <- versioned data contract <- medallio_dw`

---

# 5. Por qué las dos escalas son mejores que una

## Micro aporta validez interna

Puede observar:
- evento real de separación/venta;
- lifecycle;
- reingreso;
- stock verdadero;
- pricing efectivo;
- descuentos;
- tiempo real hasta venta.

Permite responder:
**¿qué ocurre dentro de una empresa cuando cambia su política de precio?**

## Mercado aporta validez externa

Puede observar:
- competidores;
- mercado fuera del portafolio Cygnus;
- cambios de precio externos;
- tendencias por distrito;
- presión de oferta;
- shocks comunes.

Permite responder:
**¿el mecanismo observado en Cygnus aparece también en el mercado?**

---

# 6. Diseño académico sugerido

## Paper / capítulo 1 — Facts
Caracterizar mercado y empresa:
- distribución price/m²;
- inventory age;
- discount;
- absorption;
- time-on-market;
- frecuencia de repricing.

## Paper / capítulo 2 — Micro causal
Estimación en Cygnus:
- unit/project FE;
- survival;
- event study;
- DiD si existe policy change;
- IV solo si aparece instrumento creíble.

Outcome principal:
**sale hazard / time-to-sale**

Treatment principal:
**effective price / discount / repricing event**

## Paper / capítulo 3 — External validity
Contrastar:
- cambios de asking price en mercado;
- duración de listing;
- oferta;
- competencia;
- respuesta por distrito/tipología.

## Paper / capítulo 4 — Decision layer
Simular:
- precio vs velocidad;
- revenue vs inventory carrying time;
- elasticidad heterogénea;
- política de repricing.

ML entra aquí como challenger/heterogeneity/policy support, no como identificación causal.

---

# 7. Regla de privacidad

En GitHub solo pueden existir:
- schemas;
- diccionarios;
- SQL parametrizado;
- agregados seguros;
- IDs hash no reversibles si fueran indispensables;
- resultados que superen revisión de disclosure.

Nunca:
- nombres;
- teléfonos;
- DNI/documentos;
- emails;
- códigos que permitan reidentificar clientes;
- extractos completos de CRM;
- secretos o credenciales.

---

# 8. Ventaja científica

La combinación crea una tesis poco común:

```text
micro real transaction data
        +
market longitudinal listings
        +
macro financial conditions
        ↓
pricing → demand → duration → inventory → decision
```

La contribución deja de ser un modelo de precios.

Se convierte en una investigación sobre **comportamiento de demanda y decisiones dinámicas de pricing en un mercado emergente**.
