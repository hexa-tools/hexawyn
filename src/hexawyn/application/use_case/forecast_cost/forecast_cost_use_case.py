from __future__ import annotations

from hexawyn.application.ports.driving.forecast_cost.forecast_cost_command import (
    ForecastCostCommand,
)
from hexawyn.application.ports.driving.forecast_cost.forecast_cost_response import (
    ForecastCostResponse,
)
from hexawyn.application.ports.driving.forecast_cost.forecast_cost_service_port import (
    ForecastCostServicePort,
)


class ForecastCostUseCase:
    def __init__(self, service: ForecastCostServicePort) -> None:
        self._service = service

    def execute(self, command: ForecastCostCommand) -> ForecastCostResponse:
        return self._service.forecast_cost(command)
