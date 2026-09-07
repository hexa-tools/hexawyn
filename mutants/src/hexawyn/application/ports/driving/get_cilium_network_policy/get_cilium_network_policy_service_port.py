from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cilium.get_cilium_network_policy.command import (
    GetCiliumNetworkPolicyCommand,
)
from hexawyn.application.use_case.cilium.get_cilium_network_policy.response import (
    GetCiliumNetworkPolicyResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class GetCiliumNetworkPolicyServicePort(ABC):
    @abstractmethod
    def get(self, command: GetCiliumNetworkPolicyCommand) -> GetCiliumNetworkPolicyResponse: ...
