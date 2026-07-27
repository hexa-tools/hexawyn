from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cluster.cluster_capacity_ceiling_forecast.command import (
    ClusterCapacityCeilingForecastCommand,
)
from hexawyn.application.use_case.cluster.cluster_capacity_ceiling_forecast.response import (
    ClusterCapacityCeilingForecastResponse,
)


class ClusterCapacityCeilingForecastServicePort(ABC):
    @abstractmethod
    def forecast(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse: ...
