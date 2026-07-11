from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ComputeOptimizationRoiCommand:
    sprint_id: str
    traffic_growth_pct: float = 0.0
