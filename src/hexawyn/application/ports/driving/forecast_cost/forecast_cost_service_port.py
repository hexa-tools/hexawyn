from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.forecast_cost.forecast_cost_command import (
    ForecastCostCommand,
)
from hexawyn.application.ports.driving.forecast_cost.forecast_cost_response import (
    ForecastCostResponse,
)


class ForecastCostServicePort(ABC):
    @abstractmethod
    def forecast_cost(self, command: ForecastCostCommand) -> ForecastCostResponse: ...
