from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cluster_headroom_simulation.command import (
    ClusterHeadroomSimulationCommand,
)
from hexawyn.application.use_case.cluster_headroom_simulation.response import (
    ClusterHeadroomSimulationResponse,
)


class ClusterHeadroomSimulationServicePort(ABC):
    @abstractmethod
    def simulate(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse: ...
