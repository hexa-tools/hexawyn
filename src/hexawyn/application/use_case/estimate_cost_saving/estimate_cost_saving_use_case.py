from __future__ import annotations

from hexawyn.application.ports.driving.estimate_cost_saving.estimate_cost_saving_command import (
    EstimateCostSavingCommand,
)
from hexawyn.application.ports.driving.estimate_cost_saving.estimate_cost_saving_response import (
    EstimateCostSavingResponse,
)
from hexawyn.application.ports.driving.estimate_cost_saving.estimate_cost_saving_service_port import (
    EstimateCostSavingServicePort,
)


class EstimateCostSavingUseCase:
    def __init__(self, service: EstimateCostSavingServicePort) -> None:
        self._service = service

    def execute(self, command: EstimateCostSavingCommand) -> EstimateCostSavingResponse:
        return self._service.estimate_cost_saving(command)
