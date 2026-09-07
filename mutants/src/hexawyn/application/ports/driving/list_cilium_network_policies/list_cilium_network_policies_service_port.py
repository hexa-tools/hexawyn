from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cilium.list_cilium_network_policies.command import (
    ListCiliumNetworkPoliciesCommand,
)
from hexawyn.application.use_case.cilium.list_cilium_network_policies.response import (
    ListCiliumNetworkPoliciesResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class ListCiliumNetworkPoliciesServicePort(ABC):
    @abstractmethod
    def list(
        self, command: ListCiliumNetworkPoliciesCommand
    ) -> ListCiliumNetworkPoliciesResponse: ...
