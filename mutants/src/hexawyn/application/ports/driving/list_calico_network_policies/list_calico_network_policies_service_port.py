from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.calico.list_calico_network_policies.command import (
    ListCalicoNetworkPoliciesCommand,
)
from hexawyn.application.use_case.calico.list_calico_network_policies.response import (
    ListCalicoNetworkPoliciesResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class ListCalicoNetworkPoliciesServicePort(ABC):
    """Inbound port for listing Calico network policies."""

    @abstractmethod
    def list_policies(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse: ...
