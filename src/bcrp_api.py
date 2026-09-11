"""Cliente mínimo y reproducible para BCRPData.

Docs oficiales:
https://estadisticas.bcrp.gob.pe/estadisticas/series/documentos/bcrpdataapi.pdf

No requiere API key para consultas públicas básicas.
"""

from __future__ import annotations

from io import StringIO
from typing import Iterable

import pandas as pd
import requests

BASE_URL = "https://estadisticas.bcrp.gob.pe/estadisticas/series/api"


def get_series_csv(
    series: str | Iterable[str],
    start: str | None = None,
    end: str | None = None,
    lang: str = "esp",
    timeout: int = 30,
) -> pd.DataFrame:
    """Descarga hasta 10 series BCRP de una misma frecuencia en CSV."""
    if not isinstance(series, str):
        series = "-".join(series)

    parts = [BASE_URL, series, "csv"]
    if start is not None:
        parts.append(start)
        if end is not None:
            parts.append(end)
            parts.append(lang)

    url = "/".join(parts)
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
    """Descarga series BCRP en JSON."""
    if not isinstance(series, str):
        series = "-".join(series)

    parts = [BASE_URL, series, "json"]
    if start is not None:
        parts.append(start)
        if end is not None:
            parts.append(end)
            parts.append(lang)

    url = "/".join(parts)
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    return response.json()
