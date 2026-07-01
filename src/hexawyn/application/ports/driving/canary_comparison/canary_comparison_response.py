from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CanaryComparisonResponse:
    service_name: str = ""
    canary_version: str = ""
    stable_version: str = ""
    verdict: str = "unknown"
    confidence: str = "unknown"
    p99_delta_pct: float = 0.0
    error_rate_delta_pct: float = 0.0
    canary_count: int = 0
    stable_count: int = 0
    traffic_split_pct: float = 0.0
    reasons: list[str] | None = None
    error: str | None = None
