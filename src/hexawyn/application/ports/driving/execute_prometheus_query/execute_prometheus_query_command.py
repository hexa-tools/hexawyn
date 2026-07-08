from __future__ import annotations

from dataclasses import dataclass

from hexawyn.domain.models.metrics_query import QueryType, UnitHint


@dataclass(frozen=True)
class ExecutePrometheusQueryCommand:
    promql: str
    query_type: QueryType = "instant"
    start: str | None = None
    end: str | None = None
    step: str = "15s"
    unit_hint: UnitHint = "raw"
    timeout_seconds: float = 15.0
