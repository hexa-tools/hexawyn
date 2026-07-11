from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

CostCategory = Literal["compute", "storage", "network"]
GrowthModel = Literal["linear", "exponential", "decreasing", "flat"]
ProjectionConfidence = Literal["low", "medium", "high"]


@dataclass(frozen=True)
class MonthlyCostPoint:
    month: str
    total_usd: float
    by_category: dict[str, float]


@dataclass(frozen=True)
class ProjectedMonth:
    month_offset: int
    month_label: str
    realistic_usd: float
    optimistic_usd: float
    pessimistic_usd: float
    by_category: dict[str, float]


@dataclass
class BudgetProjectionReport:
    current_monthly_usd: float
    growth_rate_pct: float
    growth_model: str
    projected_months: list[ProjectedMonth] = field(default_factory=list)
    six_month_total_realistic: float = 0.0
    confidence: str = "low"
    budget_threshold_usd: float | None = None
    budget_exceeded: bool = False
    budget_breach_month: str | None = None
    warning: str = ""
