-- ============================================================
-- pa_pricing_in_peru
-- Medallio Research Readiness Discovery
-- READ ONLY: no crea, modifica ni borra objetos.
-- Objetivo: descubrir si existe suficiente historia temporal
-- de pricing/descuentos para T1.
-- ============================================================

-- 1. Objetos relevantes ya disponibles
SELECT
    table_schema,
    table_name,
    table_type
FROM information_schema.tables
WHERE table_schema IN ('core', 'analytics', 'raw_cygnus', 'raw_mercado')
  AND (
      table_name ILIKE '%unidad%'
      OR table_name ILIKE '%stock%'
      OR table_name ILIKE '%venta%'
      OR table_name ILIKE '%absor%'
      OR table_name ILIKE '%precio%'
      OR table_name ILIKE '%proforma%'
  )
ORDER BY table_schema, table_name;

-- 2. Buscar TODAS las columnas candidatas de pricing/discount.
-- Esto evita asumir de antemano dónde vive la información.
SELECT
    table_schema,
    table_name,
    ordinal_position,
    column_name,
    data_type
FROM information_schema.columns
WHERE table_schema IN ('core', 'analytics', 'raw_cygnus', 'raw_mercado')
  AND (
      column_name ILIKE '%precio%'
      OR column_name ILIKE '%price%'
      OR column_name ILIKE '%descuento%'
      OR column_name ILIKE '%discount%'
      OR column_name ILIKE '%monto%'
      OR column_name ILIKE '%lista%'
  )
ORDER BY table_schema, table_name, ordinal_position;

-- 3. Buscar fechas que puedan definir vigencia point-in-time.
SELECT
    table_schema,
    table_name,
    ordinal_position,
    column_name,
    data_type
FROM information_schema.columns
WHERE table_schema IN ('core', 'analytics', 'raw_cygnus', 'raw_mercado')
  AND (
      column_name ILIKE '%fecha%'
      OR column_name ILIKE '%date%'
      OR column_name ILIKE '%created%'
      OR column_name ILIKE '%updated%'
      OR column_name ILIKE '%vigencia%'
      OR column_name ILIKE '%snapshot%'
      OR column_name ILIKE '%observed%'
  )
ORDER BY table_schema, table_name, ordinal_position;

-- 4. Verificar presencia de relaciones que T1 espera consumir.
WITH expected(schema_name, relation_name) AS (
    VALUES
      ('core', 'dim_proyecto'),
      ('core', 'dim_unidad'),
      ('core', 'fact_ciclo_comercial_unidad'),
      ('analytics', 'v_ciclo_comercial_reconciliado'),
      ('analytics', 'fact_movimientos_stock'),
      ('analytics', 'fact_ventas_detalle'),
      ('analytics', 'agg_ventas_mensual'),
      ('analytics', 'fact_stock_ofertado_diario'),
      ('analytics', 'fact_absorcion_proyecto_diario')
)
SELECT
    e.schema_name,
    e.relation_name,
    CASE WHEN t.table_name IS NOT NULL THEN true ELSE false END AS exists_as_table_or_view
FROM expected e
LEFT JOIN information_schema.tables t
  ON t.table_schema = e.schema_name
 AND t.table_name = e.relation_name
ORDER BY 1,2;

-- 5. Pregunta que debe responder el analista después:
-- ¿Existe una relación con múltiples observaciones temporales del mismo
-- codigo_unidad y precio/descuento vigente en cada fecha?
--
-- Si NO existe, no crearla aquí. El ownership del histórico operacional
-- corresponde a Medallio. Esta consulta solo produce evidencia para
-- definir el siguiente data contract.
