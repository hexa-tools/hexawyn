from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ComputeSLOErrorBudgetCommand:
    service_name: str
    slo_target: float = 0.999
    rolling_window_days: int = 30
