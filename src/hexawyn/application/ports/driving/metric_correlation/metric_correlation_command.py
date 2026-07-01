from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class MetricCorrelationCommand:
    primary_service: str
    correlated_service: str
    time_window_minutes: int = 30
