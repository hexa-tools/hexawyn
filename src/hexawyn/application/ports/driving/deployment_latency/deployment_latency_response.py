from __future__ import annotations

from dataclasses import dataclass


@dataclass
class DeploymentLatencyResponse:
    service_name: str = ""
    verdict: str = "inconclusive"
    p50_delta_pct: float = 0.0
    p95_delta_pct: float = 0.0
    p99_delta_pct: float = 0.0
    before_p99_ms: float = 0.0
    after_p99_ms: float = 0.0
    suggestion: str | None = None
    error: str | None = None
