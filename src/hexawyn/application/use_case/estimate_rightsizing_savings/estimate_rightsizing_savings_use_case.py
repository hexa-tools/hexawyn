from __future__ import annotations

from hexawyn.application.ports.driving.estimate_rightsizing_savings.estimate_rightsizing_savings_command import (
    EstimateRightsizingSavingsCommand,
)
from hexawyn.application.ports.driving.estimate_rightsizing_savings.estimate_rightsizing_savings_response import (
    EstimateRightsizingSavingsResponse,
)
from hexawyn.application.ports.driving.estimate_rightsizing_savings.estimate_rightsizing_savings_service_port import (
    EstimateRightsizingSavingsServicePort,
)


class EstimateRightsizingSavingsUseCase:
    def __init__(self, service: EstimateRightsizingSavingsServicePort) -> None:
        self._service = service

    def execute(
        self, command: EstimateRightsizingSavingsCommand
    ) -> EstimateRightsizingSavingsResponse:
        return self._service.estimate_rightsizing_savings(command)
