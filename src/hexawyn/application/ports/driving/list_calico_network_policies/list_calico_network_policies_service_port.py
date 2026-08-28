from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.calico.list_calico_network_policies.command import (
    ListCalicoNetworkPoliciesCommand,
)
from hexawyn.application.use_case.calico.list_calico_network_policies.response import (
    ListCalicoNetworkPoliciesResponse,
)


class ListCalicoNetworkPoliciesServicePort(ABC):
    """Inbound port for listing Calico network policies."""

    @abstractmethod
    def list_policies(
        self, command: ListCalicoNetworkPoliciesCommand
    ) -> ListCalicoNetworkPoliciesResponse: ...
