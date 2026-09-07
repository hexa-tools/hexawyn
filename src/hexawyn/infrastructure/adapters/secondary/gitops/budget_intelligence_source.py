from __future__ import annotations

from hexawyn.application.ports.driven.budget_intelligence_port import (
    BudgetIntelligenceData,
)
from hexawyn.infrastructure.config.config_manager import load_config


class ConfigBudgetIntelligenceSource:
    def fetch_budget_intelligence_data(self, period: str) -> BudgetIntelligenceData:
        config = load_config()
        business = config.get("business")
        budget: float | None = None
        if isinstance(business, dict):
            raw = business.get("cloud_budget_monthly")
            budget = _as_float(raw)
        return BudgetIntelligenceData(
            current_spend_eur=0.0,
            projected_spend_eur=0.0,
            budget_monthly_eur=budget,
        )


def _as_float(value: object) -> float | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int | float):
        return float(value)
    return None
