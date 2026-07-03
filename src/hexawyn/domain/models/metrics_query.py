from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

QueryType = Literal["instant", "range"]
UnitHint = Literal["cores", "bytes", "percent", "raw"]


@dataclass(frozen=True)
class PrometheusMetricResult:
    """One time series result — either an instant `value` or a `values` series."""

    labels: dict[str, str]
    value: float | None = None
    values: list[tuple[str, float]] = field(default_factory=list)
    formatted_value: str = ""


@dataclass(frozen=True)
class PrometheusQueryRequest:
    promql: str
    query_type: QueryType = "instant"
    start: str | None = None
    end: str | None = None
    step: str = "15s"
    unit_hint: UnitHint = "raw"


@dataclass(frozen=True)
class PrometheusQueryResult:
    """Structured, parsed Prometheus query result — timestamps/units already applied."""

    query: str
    query_type: QueryType
    results: list[PrometheusMetricResult] = field(default_factory=list)
    result_count: int = 0
    truncated: bool = False
    no_data: bool = False
    summary: str = ""
