from __future__ import annotations

from dataclasses import dataclass


@dataclass
class P99LatencyResponse:
    endpoint: str = ""
    time_window_minutes: int = 0
    p50_ms: float = 0.0
    p95_ms: float = 0.0
    p99_ms: float = 0.0
    slo_threshold_ms: float = 0.0
    slo_status: str = "unknown"
    slo_delta_ms: float = 0.0
    sample_count: int = 0
    error: str | None = None
