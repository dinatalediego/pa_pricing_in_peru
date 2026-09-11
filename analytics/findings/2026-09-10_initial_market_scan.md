---
type: finding
market: housing
country: Peru
date_added: 2026-09-10
source_date: 2026-09-04
confidence: high
thesis_topics: [T1, T2, T3]
---

# Initial market scan — vivienda y condiciones financieras

## Claim 1 — El índice hedónico muestra aceleración reciente

La serie BCRP PD37940PQ pasa de **109.5 en Q1-2024** a **110.3 en Q1-2025** y **119.0 en Q1-2026**.

Cálculos reproducibles sobre la serie:
- Q2-2025 YoY: +2.19%
- Q3-2025 YoY: +4.02%
- Q4-2025 YoY: +6.11%
- Q1-2026 YoY: +7.89%
- Q1-2026 QoQ: +2.23%

### Interpretación
Descriptivamente, el ritmo de crecimiento del índice se acelera durante 2025 y al inicio de 2026. Esto **no identifica causalidad** y no implica por sí solo boom, burbuja ni aumento equivalente en cada distrito/proyecto.

### Por qué importa
T1/T3 deberían modelar heterogeneidad por distrito/proyecto y separar:
- nivel de precio;
- velocidad de venta;
- inventario;
- descuento;
- condiciones de financiamiento.

Fuente:
https://estadisticas.bcrp.gob.pe/estadisticas/series/quarterly/results/PD37940PQ/

---

## Claim 2 — El crédito hipotecario también gana dinamismo

La tasa de crecimiento anual del crédito hipotecario total (BCRP PN00538MM):
- Jul-2025: **6.3%**
- Dic-2025: **7.3%**
- Jul-2026: **7.6%**

La tasa hipotecaria bancaria promedio en moneda nacional (PN07848NM) se mantiene alrededor de **7.5%** desde fines de 2025 hasta Ago-2026.

### Interpretación
Existe un entorno útil para estudiar demanda: el crédito hipotecario crece algo más rápido mientras la tasa promedio observada permanece relativamente estable. No atribuir a esto el crecimiento de precios sin identificación adicional.

Fuentes:
https://estadisticas.bcrp.gob.pe/estadisticas/series/mensuales/resultados/PN00538MM
https://estadisticas.bcrp.gob.pe/estadisticas/series/mensuales/resultados/PN07848NM

---

## Claim 3 — El tipo de cambio aporta una variación macro útil para T2

El tipo de cambio bancario promedio BCRP:
- Ago-2025: **3.5432 S/ por US$**
- Ago-2026: **3.36385 S/ por US$**

Variación interanual aproximada: **-5.06%**.

### Interpretación
La apreciación observada aporta variación temporal para investigar pass-through hacia costos/precios inmobiliarios, pero un diseño causal debe distinguir:
- tipo de cambio;
- materiales de construcción;
- financiamiento;
- demanda;
- etapa del proyecto;
- inventario.

Fuente:
https://estadisticas.bcrp.gob.pe/estadisticas/series/api/PN01210PM/json/

---

# Decisión que genera este scan

La evidencia descriptiva actual refuerza dos líneas:

1. **T1:** estimar cómo cambios internos de pricing alteran absorción/time-on-market dentro de un mercado que está cambiando.
2. **T2:** estudiar cuánto de shocks macro/costos llega a precio lista, descuento y precio efectivo.

La siguiente evidencia crítica no es otra serie agregada: es reconstruir el panel **unidad × fecha** y medir si existen suficientes cambios históricos de precio/descuento para identificación.

# Next test

Crear un diagnóstico de microdatos con:
- número de unidades;
- proyectos;
- meses;
- cambios de precio por unidad;
- distribución de magnitud de cambios;
- cambios de descuento;
- ventas posteriores;
- time-on-market;
- calendario de reglas/hitos de pricing.

Gate:
si casi no hay variación de pricing dentro de unidad/proyecto, T1 debe reformularse hacia proyecto-tipología o T2/T3.
