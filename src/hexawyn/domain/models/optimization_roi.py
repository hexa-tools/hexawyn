from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

OptimizationCategory = Literal[
    "right_sizing",
    "idle_pod_removal",
    "hpa_tuning",
    "node_consolidation",
    "storage_cleanup",
    "other",
]


@dataclass(frozen=True)
class OptimizationItem:
    name: str
    category: str
    monthly_saving_eur: float
    description: str


@dataclass(frozen=True)
class PerformanceImpact:
    metric: str
    before: float
    after: float
    improved: bool
    regressed: bool


@dataclass
class OptimizationRoiReport:
    baseline_monthly_eur: float = 0.0
    current_monthly_eur: float = 0.0
    monthly_saving_eur: float = 0.0
    annual_saving_eur: float = 0.0
    savings_pct: float = 0.0
    optimizations: list[OptimizationItem] = field(default_factory=list)
    top_optimization: OptimizationItem | None = None
    performance_impacts: list[PerformanceImpact] = field(default_factory=list)
    has_regression: bool = False
    traffic_normalized: bool = False
    traffic_growth_pct: float = 0.0
    has_baseline: bool = True
    warning: str = ""
