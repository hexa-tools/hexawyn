from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.calico.calico_connectivity_health.command import (
    CalicoConnectivityHealthCommand,
)
from hexawyn.application.use_case.calico.calico_connectivity_health.response import (
    CalicoConnectivityHealthResponse,
)


class CalicoConnectivityHealthServicePort(ABC):
    """Inbound port for the Calico dataplane connectivity health."""

    @abstractmethod
    def health(
        self, command: CalicoConnectivityHealthCommand
    ) -> CalicoConnectivityHealthResponse: ...
