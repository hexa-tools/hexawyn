from __future__ import annotations

from hexawyn.application.ports.driving.cluster_headroom_simulation.cluster_headroom_simulation_command import (
    ClusterHeadroomSimulationCommand,
)
from hexawyn.application.ports.driving.cluster_headroom_simulation.cluster_headroom_simulation_response import (
    ClusterHeadroomSimulationResponse,
)
from hexawyn.application.ports.driving.cluster_headroom_simulation.cluster_headroom_simulation_service_port import (
    ClusterHeadroomSimulationServicePort,
)


class ClusterHeadroomSimulationUseCase:
    def __init__(self, service: ClusterHeadroomSimulationServicePort) -> None:
        self._svc = service

    def execute(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        return self._svc.simulate(command)
