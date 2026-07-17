from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driving.cluster_headroom_simulation.cluster_headroom_simulation_command import (
    ClusterHeadroomSimulationCommand,
)
from hexawyn.application.ports.driving.cluster_headroom_simulation.cluster_headroom_simulation_response import (
    ClusterHeadroomSimulationResponse,
)
from hexawyn.application.ports.driving.cluster_headroom_simulation.cluster_headroom_simulation_service_port import (
    ClusterHeadroomSimulationServicePort,
)
from hexawyn.application.use_case.cluster_headroom_simulation.cluster_headroom_simulation_use_case import (
    ClusterHeadroomSimulationUseCase,
)


class TestClusterHeadroomSimulationUseCase:
    def test_execute_delegates_to_service(self) -> None:
        service = MagicMock(spec=ClusterHeadroomSimulationServicePort)
        expected = ClusterHeadroomSimulationResponse(verdict="fits")
        service.simulate.return_value = expected
        use_case = ClusterHeadroomSimulationUseCase(service=service)
        command = ClusterHeadroomSimulationCommand()

        result = use_case.execute(command)

        service.simulate.assert_called_once_with(command)
        assert result is expected
