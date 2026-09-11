"""Cliente mínimo y reproducible para BCRPData.

Docs oficiales:
https://estadisticas.bcrp.gob.pe/estadisticas/series/ayuda/api

No requiere API key para consultas públicas básicas.
"""

from __future__ import annotations

from io import StringIO
from typing import Iterable, Sequence

import pandas as pd
import requests

BASE_URL = "https://estadisticas.bcrp.gob.pe/estadisticas/series/api"


def _join_series(series: str | Iterable[str]) -> str:
    return series if isinstance(series, str) else "-".join(series)


def _build_url(
    series: str | Iterable[str],
    output_format: str,
    start: str | None = None,
    end: str | None = None,
    lang: str = "esp",
) -> str:
    parts = [BASE_URL, _join_series(series), output_format]
    if start is not None:
        parts.append(start)
        if end is not None:
            parts.extend([end, lang])
    return "/".join(parts)


def get_series_csv(
    series: str | Iterable[str],
    start: str | None = None,
    end: str | None = None,
    lang: str = "esp",
    timeout: int = 30,
) -> pd.DataFrame:
    """Descarga hasta 10 series BCRP de una misma frecuencia en CSV."""
    url = _build_url(series, "csv", start, end, lang)
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    return pd.read_csv(StringIO(response.text))


def get_series_json(
    series: str | Iterable[str],
    start: str | None = None,
    end: str | None = None,
    lang: str = "esp",
    timeout: int = 30,
) -> dict:
    """Descarga hasta 10 series BCRP de una misma frecuencia en JSON."""
    url = _build_url(series, "json", start, end, lang)
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    return response.json()


def json_to_frame(payload: dict, series_codes: Sequence[str]) -> pd.DataFrame:
    """Convierte el JSON oficial de BCRPData a DataFrame ancho.

    BCRPData entrega cada periodo como un nombre y un vector values.
    Los valores respetan el mismo orden en que fueron solicitadas las series.
    La función valida cardinalidad para evitar asignaciones silenciosas.
    """
    series_codes = list(series_codes)
    config_series = payload.get("config", {}).get("series", [])

    if config_series and len(config_series) != len(series_codes):
        raise ValueError(
            "BCRPData devolvió un número de series distinto al solicitado: "
            f"{len(config_series)} vs {len(series_codes)}."
        )

    rows = []
    for period in payload.get("periods", []):
        values = period.get("values", [])
        if len(values) != len(series_codes):
            raise ValueError(
                f"Periodo {period.get('name')} tiene {len(values)} valores; "
                f"se esperaban {len(series_codes)}."
            )
        row = {"period": period.get("name")}
        row.update(dict(zip(series_codes, values)))
        rows.append(row)

    df = pd.DataFrame(rows)
    for column in series_codes:
        if column in df:
            df[column] = pd.to_numeric(df[column], errors="coerce")
    return df
