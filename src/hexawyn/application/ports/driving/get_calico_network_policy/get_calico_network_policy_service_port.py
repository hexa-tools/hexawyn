from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.calico.get_calico_network_policy.command import (
    GetCalicoNetworkPolicyCommand,
)
from hexawyn.application.use_case.calico.get_calico_network_policy.response import (
    GetCalicoNetworkPolicyResponse,
)


class GetCalicoNetworkPolicyServicePort(ABC):
    """Inbound port for fetching a single Calico network policy."""

    @abstractmethod
    def get_policy(
        self, command: GetCalicoNetworkPolicyCommand
    ) -> GetCalicoNetworkPolicyResponse: ...
