from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.calico.calico_connectivity_health.command import (
    CalicoConnectivityHealthCommand,
)
from hexawyn.application.use_case.calico.calico_connectivity_health.response import (
    CalicoConnectivityHealthResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class CalicoConnectivityHealthServicePort(ABC):
    """Inbound port for the Calico dataplane connectivity health."""

    @abstractmethod
    def health(
        self, command: CalicoConnectivityHealthCommand
    ) -> CalicoConnectivityHealthResponse: ...
