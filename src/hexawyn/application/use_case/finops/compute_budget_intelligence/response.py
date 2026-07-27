from dataclasses import dataclass

from hexawyn.domain.models.budget_intelligence import BudgetIntelligenceReport


@dataclass
class ComputeBudgetIntelligenceResponse:
    result: BudgetIntelligenceReport
