from __future__ import annotations

from typing import Protocol

from hexawyn.application.ports.driven.budget_intelligence_port import (
    BudgetIntelligenceData,
    BudgetIntelligencePort,
)


class BudgetIntelligenceSource(Protocol):
    def fetch_budget_intelligence_data(self, period: str) -> BudgetIntelligenceData: ...


class BudgetIntelligenceAdapter(BudgetIntelligencePort):
    def __init__(self, source: BudgetIntelligenceSource) -> None:
        self._source = source

    def get_budget_intelligence_data(self, period: str) -> BudgetIntelligenceData:
        return self._source.fetch_budget_intelligence_data(period)
