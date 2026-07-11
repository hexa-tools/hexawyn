from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class BudgetAlertRecommendation:
    action: str
    description: str


@dataclass
class BudgetIntelligenceReport:
    period_label: str
    current_spend_eur: float = 0.0
    projected_spend_eur: float = 0.0
    budget_monthly_eur: float = 0.0
    overshoot_pct: float = 0.0
    budget_exceeded: bool = False
    recommendations: list[BudgetAlertRecommendation] = field(default_factory=list)
    config_available: bool = False
    explanation: str = ""
