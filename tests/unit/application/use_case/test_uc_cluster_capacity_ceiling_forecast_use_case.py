"""Unit tests for ClusterCapacityCeilingForecastUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.cluster_capacity_ceiling_forecast.cluster_capacity_ceiling_forecast_service_port import (
    ClusterCapacityCeilingForecastServicePort,
)
from hexawyn.application.use_case.cluster_capacity_ceiling_forecast.cluster_capacity_ceiling_forecast_use_case import (
    ClusterCapacityCeilingForecastUseCase,
)


class TestClusterCapacityCeilingForecastUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=ClusterCapacityCeilingForecastServicePort)
        use_case = ClusterCapacityCeilingForecastUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.forecast.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=ClusterCapacityCeilingForecastServicePort)
        mock_service.forecast.side_effect = RuntimeError("test error")
        use_case = ClusterCapacityCeilingForecastUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
