from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.finops.forecast_cost.command import (
    ForecastCostCommand,
)
from hexawyn.application.use_case.finops.forecast_cost.response import (
    ForecastCostResponse,
)


class ForecastCostServicePort(ABC):
    @abstractmethod
    def forecast_cost(self, command: ForecastCostCommand) -> ForecastCostResponse: ...
