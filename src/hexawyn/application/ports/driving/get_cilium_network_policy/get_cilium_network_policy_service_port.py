from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cilium.get_cilium_network_policy.command import (
    GetCiliumNetworkPolicyCommand,
)
from hexawyn.application.use_case.cilium.get_cilium_network_policy.response import (
    GetCiliumNetworkPolicyResponse,
)


class GetCiliumNetworkPolicyServicePort(ABC):
    @abstractmethod
    def get(self, command: GetCiliumNetworkPolicyCommand) -> GetCiliumNetworkPolicyResponse: ...
