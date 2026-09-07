from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cluster.cluster_headroom_simulation.command import (
    ClusterHeadroomSimulationCommand,
)
from hexawyn.application.use_case.cluster.cluster_headroom_simulation.response import (
    ClusterHeadroomSimulationResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class ClusterHeadroomSimulationServicePort(ABC):
    @abstractmethod
    def simulate(
        self, command: ClusterHeadroomSimulationCommand
    ) -> ClusterHeadroomSimulationResponse: ...
