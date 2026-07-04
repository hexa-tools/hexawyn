from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driving.cluster_capacity_ceiling_forecast.cluster_capacity_ceiling_forecast_command import (
    ClusterCapacityCeilingForecastCommand,
)
from hexawyn.application.ports.driving.cluster_capacity_ceiling_forecast.cluster_capacity_ceiling_forecast_response import (
    ClusterCapacityCeilingForecastResponse,
)
from hexawyn.application.ports.driving.cluster_capacity_ceiling_forecast.cluster_capacity_ceiling_forecast_service_port import (
    ClusterCapacityCeilingForecastServicePort,
)
from hexawyn.application.use_case.cluster_capacity_ceiling_forecast.cluster_capacity_ceiling_forecast_use_case import (
    ClusterCapacityCeilingForecastUseCase,
)


class TestClusterCapacityCeilingForecastUseCase:
    def test_execute_delegates_to_service(self) -> None:
        service = MagicMock(spec=ClusterCapacityCeilingForecastServicePort)
        expected = ClusterCapacityCeilingForecastResponse(critical_resource="CPU")
        service.forecast.return_value = expected
        use_case = ClusterCapacityCeilingForecastUseCase(service=service)
        command = ClusterCapacityCeilingForecastCommand()

        result = use_case.execute(command)

        service.forecast.assert_called_once_with(command)
        assert result is expected
