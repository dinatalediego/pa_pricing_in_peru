# Revisión de literatura — síntesis

Fecha de corte inicial: 2026-09-10.

## 1. Qué está maduro en Perú

### Hedonic pricing
La literatura peruana ya tiene:
- índices hedónicos;
- determinantes estructurales/locacionales;
- valoración de vivienda;
- aplicaciones por distrito;
- comparación reciente con ML.

Por tanto, un nuevo hedónico solo sería competitivo si introduce identificación espacial/temporal nueva o se integra a una pregunta diferente.

### Predicción
En 2025 ya existe una tesis ESAN con más de 40,000 observaciones 2014–2024 comparando regresión, árbol y XGBoost para precios de departamentos en Lima. También existe trabajo de ML para alquileres y VARMA para velocidad de venta.

Conclusión: **accuracy sola no es gap.**

## 2. El espacio que queda abierto

La literatura revisada raramente observa simultáneamente:
- precio de lista;
- cambios de precio;
- descuento;
- precio transaccional;
- tiempo en stock;
- stock contemporáneo;
- momento de venta.

La literatura internacional muestra que estas variables deben analizarse conjuntamente porque list price y time-on-market reflejan decisiones del vendedor y poder de negociación.

Esto crea un puente natural hacia microdatos de inmobiliarias peruanas.

## 3. Macro y pass-through

El BCRP tiene una agenda muy desarrollada de pass-through del tipo de cambio. En 2026 publicó evidencia con VAR bayesianos, parámetros cambiantes y no linealidades. El gap no sería repetir ERPT sobre IPC, sino estudiar:

**shock macro → costo/proyecto → precio lista/descuento → absorción**

Ese “último kilómetro” microeconómico es particularmente interesante.

## 4. Mercado de combustibles

Existe evidencia histórica sobre determinantes de precios minoristas en Lima y un caso reciente de screening de colusión en Chimbote. Osinergmin ofrece una infraestructura de datos mucho más rica hoy.

La oportunidad es construir panel espacial nacional y estimar competencia/pass-through con alta frecuencia.

## 5. Cacao

Muchas tesis explican exportaciones con precio, producción y tipo de cambio. Repetir esa especificación aporta poco.

Una pregunta más fuerte sería cuánto, cuándo y dónde se transmite el precio internacional al productor, y si cooperativas/intermediación/clima alteran ese pass-through.

## 6. Regla de lectura para el RAG

Cuando se agregue una fuente, capturar:
- pregunta;
- unidad de observación;
- periodo;
- dataset;
- identificación;
- modelo;
- finding;
- limitación;
- gap que deja abierto;
- tema del repositorio al que alimenta.
