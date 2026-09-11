# Plan de datos

## 1. Vivienda — capa pública

### BCRPData
Series prioritarias:
- PD37940PQ — índice de precios hedónicos de inmuebles.
- PD37944PQ — precio/m² US$ 12 distritos.
- PD37945PQ — precio/m² S/ constantes 2009.
- PD37946PQ — precio/m² S/ corrientes.
- PD41940PQ–PD41952PQ — PER venta/alquiler por distrito y promedio.
- PD37957PQ, PD17459PQ–PD17468PQ, PD37958PQ — precio/m² por distrito.
- PN07848NM — tasa hipotecaria bancaria en soles.
- PN00542MM — saldo crédito hipotecario MN.
- PN00538MM — crecimiento anual crédito hipotecario total.
- PD04722MM — tasa de referencia.

### INEI
- IPC.
- índice de precios de materiales de construcción.
- índices unificados de precios de construcción.
- precios de maquinaria/equipo.
- demografía/empleo/ingreso cuando el diseño lo requiera.

### Datos abiertos municipales
Ejemplo localizado: licencias de edificación de San Isidro. Buscar y versionar datasets equivalentes de otros distritos.

## 2. Vivienda — capa privada/propia

Granularidad objetivo: **unidad × fecha**.

Campos mínimos:
- proyecto;
- unidad;
- distrito/geografía;
- tipología;
- piso;
- área;
- precio de lista;
- precio final;
- descuento;
- estado comercial;
- fecha de cambio de estado;
- fecha de separación/venta;
- fecha de entrada a stock;
- etapa del proyecto;
- stock competidor/proyecto, si existe;
- canal/lead signals solo cuando tenga justificación económica.

No subir datos corporativos sensibles al repositorio público. Guardar únicamente:
- diccionario;
- esquema;
- transformaciones;
- estadísticas agregadas anonimizadas;
- código que espere rutas locales/secretos fuera de Git.

## 3. Combustibles

Fuentes:
- Osinergmin: precios minoristas/referencia, estructura sectorial, ventas;
- geolocalización de estaciones, cuando esté disponible;
- precios internacionales / referencia;
- BCRP: FX, inflación, actividad;
- INDECOPI: resoluciones/sanciones como ground truth histórico para validación de screenings.

Unidad ideal:
**estación × combustible × día/semana**.

## 4. Retail online

Construcción propia:
**retailer × SKU × fecha × precio_regular × precio_promocional × disponibilidad**.

Enriquecimiento:
- marca;
- categoría;
- origen/importación si puede aproximarse;
- TC;
- IPC/IPM;
- eventos comerciales.

Debe respetarse robots.txt, términos de uso y límites operativos.

## 5. Cacao

Posibles fuentes:
- MIDAGRI/SIEA: producción, rendimiento, superficie, precio en chacra por región;
- BCRP: exportaciones agro/cacao;
- SUNAT/MINCETUR si se requiere comercio más granular;
- precios internacionales;
- clima: precipitación/temperatura/ENSO si se construye una identificación basada en shocks.

Unidad ideal:
**región × mes**.

## Reglas de provenance

Todo dataset incorporado debe registrar:
- source_url;
- retrieved_at;
- frecuencia;
- unidad;
- periodo;
- licencia/restricciones;
- hash o versión;
- transformaciones;
- responsable del script.

Nunca mezclar raw y transformed sin una capa explícita.
