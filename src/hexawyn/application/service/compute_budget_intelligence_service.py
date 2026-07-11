from __future__ import annotations

from hexawyn.application.ports.driven.budget_intelligence_port import BudgetIntelligencePort
from hexawyn.application.ports.driving.compute_budget_intelligence.compute_budget_intelligence_command import (  # noqa: E501
    ComputeBudgetIntelligenceCommand,
)
from hexawyn.application.ports.driving.compute_budget_intelligence.compute_budget_intelligence_response import (  # noqa: E501
    ComputeBudgetIntelligenceResponse,
)
from hexawyn.application.ports.driving.compute_budget_intelligence.compute_budget_intelligence_service_port import (  # noqa: E501
    ComputeBudgetIntelligenceServicePort,
)
from hexawyn.domain.services.budget_intelligence.budget_intelligence_service import (
    compute_budget_intelligence,
)


class ComputeBudgetIntelligenceService(ComputeBudgetIntelligenceServicePort):
    def __init__(self, budget_intelligence_port: BudgetIntelligencePort) -> None:
        self._port = budget_intelligence_port

    def compute(
        self, command: ComputeBudgetIntelligenceCommand
    ) -> ComputeBudgetIntelligenceResponse:
        data = self._port.get_budget_intelligence_data(command.period)
        result = compute_budget_intelligence(data, period=command.period)
        return ComputeBudgetIntelligenceResponse(result=result)
