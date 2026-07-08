from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ComputeTeamCostCommand:
    cpu_price_per_core_hour: float = 0.03
    memory_price_per_gb_hour: float = 0.01
    storage_price_per_gb_month: float = 0.10
