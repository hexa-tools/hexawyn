from __future__ import annotations

from dataclasses import dataclass


@dataclass
class SpanBottleneckAnalysisResponse:
    bottleneck: str = "neither"
    confidence: str = "low"
    bottleneck_pct_of_total: float = 0.0
    db_avg_ms: float = 0.0
    redis_avg_ms: float = 0.0
    db_slowest: str | None = None
    redis_slowest: str | None = None
    reasons: list[str] | None = None
    error: str | None = None
