# Ranking de temas de tesis

Fecha: 2026-09-10

Escala 1–5. Score ponderado: ajuste al perfil 25%, gap 25%, acceso a datos 20%, identificación 15%, valor analytics/portfolio 15%.

| Rank | Tema | Score | Lectura |
|---|---|---:|---|
| 1 | Pricing dinámico y absorción inmobiliaria | 4.65 | Mejor combinación de datos propios, economía y gap |
| 1 | Pass-through macro → pricing inmobiliario | 4.65 | Excelente puente macro-micro y muy alineado |
| 3 | Índice de market heat/bargaining para Lima | 4.53 | Producto académico + ejecutivo muy potente |
| 4 | Combustibles: dispersión, competencia y pass-through | 4.35 | Mejor opción con datos predominantemente públicos |
| 5 | Metro/infraestructura → precio y absorción | 4.15 | Muy causal, pero exige historial geoespacial sólido |
| 6 | Retail online: rigidez, dispersión y pass-through | 4.05 | Buen uso de scraping; recolección costosa |
| 7 | Cacao: precio mundial → precio en chacra | 3.98 | Viable y económicamente interesante |
| 8 | Hipotecas → demanda/affordability | 3.88 | Datos sólidos, pero gap menos diferencial |

---

## T1 — Recomendación principal

### Título provisional
**Pricing dinámico y absorción en vivienda nueva en Lima: respuesta de la demanda a cambios de precios y descuentos**

### Pregunta
¿Cuál es el efecto de cambios en el precio efectivo y en el descuento sobre la probabilidad y velocidad de venta de una unidad inmobiliaria, y cómo varía por etapa del proyecto, tipología, inventario y condiciones de mercado?

### Unidad de observación ideal
Unidad × semana o unidad × mes.

### Outcomes
- venta/separación;
- hazard de venta;
- días hasta venta;
- absorción;
- ingreso/margen esperado;
- probabilidad de caída, si existe.

### Tratamientos
- variación de precio de lista;
- variación de precio final;
- descuento;
- hitos estandarizados de pricing.

### Métodos
Panel FE, event study, survival/hazard models, IV cuando sea defendible, causal forests como heterogeneidad complementaria.

### Gap
La evidencia peruana encontrada se concentra en precio hedónico, predicción de precios, factibilidad y forecasting de velocidad de ventas. Falta evidencia micro-longitudinal enfocada en **elasticidad de demanda/absorción causada por decisiones de pricing**.

---

## T2 — Pass-through macro → micro inmobiliario

### Título provisional
**Del tipo de cambio y los costos de construcción al precio final: pass-through y absorción en proyectos residenciales de Lima**

Pregunta: ¿cuánto y con qué rezago trasladan los proyectos shocks de tipo de cambio, materiales, tasa hipotecaria e inflación hacia precios de lista, descuentos y precio efectivo? ¿El traslado cambia con stock, etapa o velocidad de ventas?

Valor diferencial: conectar la extensa literatura macro de pass-through peruano con decisiones de pricing a nivel de unidad/proyecto.

---

## T3 — Market Heat Index para Lima

### Título provisional
**Precio, inventario y tiempo de venta: un índice de poder de negociación y temperatura del mercado inmobiliario de Lima**

Construir un índice que combine:
- list price;
- transaction/final price;
- descuento;
- time-on-market;
- absorción;
- stock;
- tasa hipotecaria.

La literatura internacional permite interpretarlo como poder de negociación del vendedor. Para Lima sería un producto replicable por distrito/proyecto/tipología.

---

## T4 — Combustibles

### Título provisional
**Competencia espacial y transmisión de shocks en los precios minoristas de combustibles en Perú**

Preguntas posibles:
- ¿qué tan rápido trasladan las estaciones los cambios de precios de referencia?
- ¿hay asimetría “rockets and feathers”?
- ¿cómo cambia el pass-through con densidad de competidores y distancia?
- ¿pueden detectarse episodios anómalos de coordinación mediante dispersión y sincronización?

Fortaleza: Osinergmin posee datos sectoriales y precios; existe antecedente Lima 1999–2000 y Chimbote, pero un panel nacional moderno sería otra escala.

---

## T5 — Infraestructura urbana

### Título provisional
**Accesibilidad y capitalización inmobiliaria: impacto causal de hitos de la Línea 2 del Metro sobre precios y absorción**

No repetir una regresión hedónica cross-sectional. El salto debe ser diseño cuasi-experimental:
- treated/control;
- distancia a estaciones;
- múltiples hitos;
- event study / difference-in-differences;
- efectos sobre precio y velocidad de venta.

---

## T6 — Retail online

### Título provisional
**Rigidez, promociones y pass-through en precios online del retail peruano: evidencia multi-retailer con web scraping**

Gap potencial: extender evidencia de una sola tienda (2016–2020) a varios retailers/categorías, separar precio regular/promoción y medir reacción a FX/inflación/import costs.

---

## T7 — Cacao

### Título provisional
**¿Cuánto del boom internacional llega al productor? Transmisión asimétrica del precio del cacao al precio en chacra por región del Perú**

Métodos: panel regional, ARDL/ECM, asymmetric/NARDL, shocks climáticos y heterogeneidad por región/canal.

Evitar: volver a estimar únicamente “precio + producción + TC → exportaciones”, ya cubierto repetidamente.

---

## Decisión recomendada

Priorizar T1 y mantener T4 como **outside option pública**.

T1 usa la ventaja informacional y profesional del investigador. T4 reduce el riesgo de depender de data corporativa y sigue permitiendo microeconometría, geografía, competencia y data engineering.
