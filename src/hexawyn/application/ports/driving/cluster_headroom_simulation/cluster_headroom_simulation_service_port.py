from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.cluster_headroom_simulation.cluster_headroom_simulation_command import (
    ClusterHeadroomSimulationCommand,
)
from hexawyn.application.ports.driving.cluster_headroom_simulation.cluster_headroom_simulation_response import (
    ClusterHeadroomSimulationResponse,
)


class ClusterHeadroomSimulationServicePort(ABC):
    @abstractmethod
    def simulate(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse: ...
