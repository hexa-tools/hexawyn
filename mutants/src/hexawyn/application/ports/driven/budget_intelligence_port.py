from abc import ABC, abstractmethod
from typing import TypedDict


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class BudgetIntelligenceData(TypedDict):
    current_spend_eur: float
    projected_spend_eur: float
    budget_monthly_eur: float | None


class BudgetIntelligencePort(ABC):
    @abstractmethod
    def get_budget_intelligence_data(self, period: str) -> BudgetIntelligenceData: ...
