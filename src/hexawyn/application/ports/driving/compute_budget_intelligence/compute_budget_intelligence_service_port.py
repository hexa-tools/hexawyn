from abc import ABC, abstractmethod

from hexawyn.application.use_case.finops.compute_budget_intelligence.command import (  # noqa: E501
    ComputeBudgetIntelligenceCommand,
)
from hexawyn.application.use_case.finops.compute_budget_intelligence.response import (  # noqa: E501
    ComputeBudgetIntelligenceResponse,
)


class ComputeBudgetIntelligenceServicePort(ABC):
    @abstractmethod
    def compute(
        self, command: ComputeBudgetIntelligenceCommand
    ) -> ComputeBudgetIntelligenceResponse: ...
