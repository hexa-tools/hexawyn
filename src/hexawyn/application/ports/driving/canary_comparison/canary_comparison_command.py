from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CanaryComparisonCommand:
    service_name: str
    time_window_minutes: int = 30
    traffic_split_pct: float = 5.0
