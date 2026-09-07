from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.calico.get_calico_network_policy.command import (
    GetCalicoNetworkPolicyCommand,
)
from hexawyn.application.use_case.calico.get_calico_network_policy.response import (
    GetCalicoNetworkPolicyResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class GetCalicoNetworkPolicyServicePort(ABC):
    """Inbound port for fetching a single Calico network policy."""

    @abstractmethod
    def get_policy(
        self, command: GetCalicoNetworkPolicyCommand
    ) -> GetCalicoNetworkPolicyResponse: ...
