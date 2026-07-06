from __future__ import annotations

from hexawyn.application.ports.driving.compare_service_cost.compare_service_cost_command import (
    CompareServiceCostCommand,
)
from hexawyn.application.ports.driving.compare_service_cost.compare_service_cost_response import (
    CompareServiceCostResponse,
)
from hexawyn.application.ports.driving.compare_service_cost.compare_service_cost_service_port import (
    CompareServiceCostServicePort,
)


class CompareServiceCostUseCase:
    def __init__(self, service: CompareServiceCostServicePort) -> None:
        self._service = service

    def execute(self, command: CompareServiceCostCommand) -> CompareServiceCostResponse:
        return self._service.compare(command)
