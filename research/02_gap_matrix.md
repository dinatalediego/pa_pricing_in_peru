# Matriz literatura → gap → contribución

## Mercado inmobiliario peruano

| Literatura encontrada | Qué ya responde | Qué NO conviene repetir | Gap defendible |
|---|---|---|---|
| BCRP Mundaca & Sánchez (2018), índice hedónico | valoración de atributos e índice de precios | otro hedónico estándar | respuesta de demanda a cambios de precio |
| Orrego/BCRP (2014), fundamentos macro | equilibrio de precio vivienda vs fundamentos | otra cointegración agregada similar | transmisión macro a decisiones micro de pricing |
| Vílchez/PUCP (2015), dinámica de precios | variables explicativas del boom inmobiliario | “qué explica el precio de Lima” agregado | heterogeneidad por proyecto/tipología/etapa |
| UNI (2017), índice hedónico vivienda nueva | índice ajustado por calidad | nuevo índice sin capa decisional | índice precio+TOM+stock+absorción |
| ULima (2018), valoración por atributos | valoración hedónica + capacidad de pago | estimar solo precio | elasticidad/hazard de venta |
| URP (2019), determinantes estructurales y entorno | atributos y entorno | regresión transversal | panel longitudinal con cambios de precio |
| UNALM (2024), VARMA velocidad de ventas | forecasting de sales velocity | forecast como objetivo final | efecto causal del pricing sobre sales velocity |
| ESAN (2025), ML precio departamentos | XGBoost supera modelos simples | comparar algoritmos por RMSE | causalidad, policy learning y decisión |
| UPEU (2024), ML alquileres | predicción de rentas | otro modelo predictivo | negociación, duración, dinámica |
| Metro Line 1 (2023), hedónico cross-sectional | proximidad y precio | distancia-estación transversal | DiD/event study con hitos y absorción |
| UNMSM (2025), gestión/proyección comercial | integración y control de ventas | dashboard/automatización como tesis | inferencia económica y decisiones de pricing |

## Literatura internacional útil

- Carrillo (2013): combina list price, sale price y time-on-market para medir “heat” y poder negociador.
- Besbes & Maglaras (2012): pricing dinámico bajo inventario, horizonte y milestones financieros.
- Koster & Rouwendal (2024): trade-off entre markup, precio de venta y time-on-market.
- literatura de time-on-market: el precio y la duración están determinados conjuntamente; ignorar endogeneidad sesga conclusiones.

## Mercado de combustibles

Antecedentes:
- Ruiz Díaz (2002): 84 estaciones, 22 distritos de Lima; diferenciación de marca, ubicación y competencia poco intensa.
- Correa Adanaque (2025): screening de colusión en 21 estaciones de Chimbote, episodios 2012/2014.

Gap:
- panel moderno, nacional, high-frequency;
- competencia espacial;
- pass-through dinámico;
- heterogeneidad por marca/mercado local;
- detección de episodios anómalos sin confundir paralelismo competitivo con colusión.

## Retail online

Antecedente fuerte:
- Coronado, Lahura & Vega (2021): 4.5 millones de precios online de una tienda, 2016–2020; menor rigidez que referencias internacionales.

Gap:
- múltiples retailers;
- post-COVID;
- promociones vs precio regular;
- categorías importadas vs domésticas;
- pass-through tipo de cambio/costos;
- sincronización competitiva.

## Cacao

Literatura peruana encontrada:
- Sevilla (2017): producción, precio y TC → exportaciones.
- Castillo & Hilarión (2020): precio nacional/internacional, producción, TC → exportaciones.
- Guardia et al. (2023): producción, precio en chacra, rendimiento/superficie → exportación con ARDL.
- Huanaco (2024): rol de intermediarios/cadena de valor en ingresos del productor, con agenda empírica pendiente.
- estudios 2024–2025 siguen concentrándose en calidad, FOB y exportación.

Gap:
**transmisión del shock internacional hacia el productor regional**, velocidad/asimetría del pass-through y rol de intermediación/clima.

## Conclusión de gap

El patrón transversal es importante:

> En Perú hay abundante trabajo sobre **niveles de precios y predicción**, pero menos evidencia que conecte **cambios de precio → respuesta de demanda → duración/inventario → decisión óptima**, especialmente con microdatos longitudinales.

Ese debe ser el eje central del repositorio.
