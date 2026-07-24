from hexawyn.application.ports.driven.headroom_simulation_port import HeadroomSimulationPort
from hexawyn.application.use_case.cluster_headroom_simulation.command import (
    ClusterHeadroomSimulationCommand,
)
from hexawyn.application.use_case.cluster_headroom_simulation.response import (
    ClusterHeadroomSimulationResponse,
)


class ClusterHeadroomSimulationUseCase:
    def __init__(self, port: HeadroomSimulationPort) -> None:
        self._port = port

    def execute(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse:
        return ClusterHeadroomSimulationResponse()
