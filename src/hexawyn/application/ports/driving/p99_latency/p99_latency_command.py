from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class P99LatencyCommand:
    endpoint: str
    time_window_minutes: int = 120
    slo_threshold_ms: float = 500.0
