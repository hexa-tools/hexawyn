from abc import ABC, abstractmethod
from typing import TypedDict


class BudgetIntelligenceData(TypedDict):
    current_spend_eur: float
    projected_spend_eur: float
    budget_monthly_eur: float | None


class BudgetIntelligencePort(ABC):
    @abstractmethod
    def get_budget_intelligence_data(self, period: str) -> BudgetIntelligenceData: ...
