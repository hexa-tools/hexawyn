from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ServiceCostBreakdown:
    pod_name: str
    namespace: str
    cpu_cost: float
    memory_cost: float
    total_cost: float


@dataclass(frozen=True)
class MonthCost:
    month: str
    total_cost: float
    cpu_cost: float
    memory_cost: float
    pod_breakdown: list[ServiceCostBreakdown]


@dataclass
class ServiceCostComparison:
    service_name: str = ""
    current_month: MonthCost | None = None
    previous_month: MonthCost | None = None
    cost_delta: float = 0.0
    cost_delta_pct: float = 0.0
    trend: str = "stable"
    recommendation: str = ""
