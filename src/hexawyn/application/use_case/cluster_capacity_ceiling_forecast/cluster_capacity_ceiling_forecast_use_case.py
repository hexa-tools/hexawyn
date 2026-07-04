from __future__ import annotations

from hexawyn.application.ports.driving.cluster_capacity_ceiling_forecast.cluster_capacity_ceiling_forecast_command import (
    ClusterCapacityCeilingForecastCommand,
)
from hexawyn.application.ports.driving.cluster_capacity_ceiling_forecast.cluster_capacity_ceiling_forecast_response import (
    ClusterCapacityCeilingForecastResponse,
)
from hexawyn.application.ports.driving.cluster_capacity_ceiling_forecast.cluster_capacity_ceiling_forecast_service_port import (
    ClusterCapacityCeilingForecastServicePort,
)


class ClusterCapacityCeilingForecastUseCase:
    def __init__(self, service: ClusterCapacityCeilingForecastServicePort) -> None:
        self._svc = service

    def execute(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        return self._svc.forecast(command)
