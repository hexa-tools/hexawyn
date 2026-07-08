from __future__ import annotations

from dataclasses import dataclass


@dataclass
class MetricCorrelationResponse:
    primary_service: str = ""
    correlated_service: str = ""
    status: str = "inconclusive"
    coefficient: float = 0.0
    lag_index: int = 0
    hypothesis: str = ""
    data_point_count: int = 0
    error: str | None = None
