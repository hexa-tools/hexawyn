from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.compute_budget_intelligence.compute_budget_intelligence_command import (  # noqa: E501
    ComputeBudgetIntelligenceCommand,
)
from hexawyn.application.ports.driving.compute_budget_intelligence.compute_budget_intelligence_response import (  # noqa: E501
    ComputeBudgetIntelligenceResponse,
)


class ComputeBudgetIntelligenceServicePort(ABC):
    @abstractmethod
    def compute(
        self, command: ComputeBudgetIntelligenceCommand
    ) -> ComputeBudgetIntelligenceResponse: ...
