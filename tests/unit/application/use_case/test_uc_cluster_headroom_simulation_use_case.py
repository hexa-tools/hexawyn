"""Unit tests for ClusterHeadroomSimulationUseCase."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.cluster_headroom_simulation.cluster_headroom_simulation_service_port import (
    ClusterHeadroomSimulationServicePort,
)
from hexawyn.application.use_case.cluster_headroom_simulation.cluster_headroom_simulation_use_case import (
    ClusterHeadroomSimulationUseCase,
)


class TestClusterHeadroomSimulationUseCase:
    def test_execute_delegates_to_service(self) -> None:
        mock_service = MagicMock(spec=ClusterHeadroomSimulationServicePort)
        use_case = ClusterHeadroomSimulationUseCase(service=mock_service)

        use_case.execute(MagicMock())

        mock_service.simulate.assert_called_once()

    def test_service_error_propagates(self) -> None:
        mock_service = MagicMock(spec=ClusterHeadroomSimulationServicePort)
        mock_service.simulate.side_effect = RuntimeError("test error")
        use_case = ClusterHeadroomSimulationUseCase(service=mock_service)

        with pytest.raises(RuntimeError, match="test error"):
            use_case.execute(MagicMock())
