from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.calico.get_calico_host_endpoints.command import (
    GetCalicoHostEndpointsCommand,
)
from hexawyn.application.use_case.calico.get_calico_host_endpoints.response import (
    GetCalicoHostEndpointsResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class GetCalicoHostEndpointsServicePort(ABC):
    """Inbound port for listing Calico HostEndpoints."""

    @abstractmethod
    def get_endpoints(
        self, command: GetCalicoHostEndpointsCommand
    ) -> GetCalicoHostEndpointsResponse: ...
