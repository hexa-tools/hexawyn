from hexawyn.application.ports.driven.capacity_forecast_port import CapacityForecastPort
from hexawyn.application.use_case.cluster_capacity_ceiling_forecast.command import (
    ClusterCapacityCeilingForecastCommand,
)
from hexawyn.application.use_case.cluster_capacity_ceiling_forecast.response import (
    ClusterCapacityCeilingForecastResponse,
)


class ClusterCapacityCeilingForecastUseCase:
    def __init__(self, port: CapacityForecastPort) -> None:
        self._port = port

    def execute(
        self, command: ClusterCapacityCeilingForecastCommand
    ) -> ClusterCapacityCeilingForecastResponse:
        return ClusterCapacityCeilingForecastResponse()
