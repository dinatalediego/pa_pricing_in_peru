-- ============================================================
-- pa_pricing_in_peru
-- Peruvian Real Estate Longitudinal Data Engine
-- Research extract v1
-- READ ONLY.
-- ============================================================

WITH project_panel AS (
    SELECT
        snapshot_date,
        project_key,
        source,
        project_name,
        district_slug,
        unit_type_key,
        price_min,
        price_avg,
        price_max,
        price_m2_min,
        price_m2_avg,
        price_m2_max,
        available_units,
        typology_count,
        content_hash,
        observed_at,
        lag(price_avg) OVER (
            PARTITION BY project_key
            ORDER BY snapshot_date, observed_at
        ) AS prev_price_avg,
        lag(price_m2_avg) OVER (
            PARTITION BY project_key
            ORDER BY snapshot_date, observed_at
        ) AS prev_price_m2_avg,
        lag(available_units) OVER (
            PARTITION BY project_key
            ORDER BY snapshot_date, observed_at
        ) AS prev_available_units
    FROM gold.fact_project_snapshot
    WHERE parse_ok = true
),
features AS (
    SELECT
        *,
        CASE
            WHEN prev_price_avg IS NULL OR prev_price_avg = 0 THEN NULL
            ELSE price_avg / prev_price_avg - 1
        END AS project_price_change_pct,
        CASE
            WHEN prev_price_m2_avg IS NULL OR prev_price_m2_avg = 0 THEN NULL
            ELSE price_m2_avg / prev_price_m2_avg - 1
        END AS project_price_m2_change_pct,
        available_units - prev_available_units AS available_units_change
    FROM project_panel
)
SELECT
    snapshot_date,
    project_key,
    source,
    project_name,
    district_slug,
    unit_type_key,
    price_min,
    price_avg,
    price_max,
    price_m2_min,
    price_m2_avg,
    price_m2_max,
    available_units,
    typology_count,
    project_price_change_pct,
    project_price_m2_change_pct,
    available_units_change,
    content_hash,
    observed_at
FROM features
ORDER BY project_key, snapshot_date, observed_at;
