from __future__ import annotations

from hexawyn.application.ports.driving.compute_budget_intelligence.compute_budget_intelligence_command import (  # noqa: E501
    ComputeBudgetIntelligenceCommand,
)
from hexawyn.application.ports.driving.compute_budget_intelligence.compute_budget_intelligence_response import (  # noqa: E501
    ComputeBudgetIntelligenceResponse,
)
from hexawyn.application.ports.driving.compute_budget_intelligence.compute_budget_intelligence_service_port import (  # noqa: E501
    ComputeBudgetIntelligenceServicePort,
)


class ComputeBudgetIntelligenceUseCase:
    def __init__(self, service: ComputeBudgetIntelligenceServicePort) -> None:
        self._service = service

    def execute(
        self, command: ComputeBudgetIntelligenceCommand
    ) -> ComputeBudgetIntelligenceResponse:
        return self._service.compute(command)
