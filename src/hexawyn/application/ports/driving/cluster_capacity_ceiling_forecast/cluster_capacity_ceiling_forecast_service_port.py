from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.cluster_capacity_ceiling_forecast.cluster_capacity_ceiling_forecast_command import (
    ClusterCapacityCeilingForecastCommand,
)
from hexawyn.application.ports.driving.cluster_capacity_ceiling_forecast.cluster_capacity_ceiling_forecast_response import (
    ClusterCapacityCeilingForecastResponse,
)


class ClusterCapacityCeilingForecastServicePort(ABC):
    @abstractmethod
    def forecast(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse: ...
