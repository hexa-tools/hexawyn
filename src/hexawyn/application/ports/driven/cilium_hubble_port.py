from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.domain.models.cilium import CiliumFlowQuery, CiliumFlowsResult


class CiliumHubblePort(ABC):
    """Outbound port to query Cilium flow logs (Hubble Relay)."""

    @abstractmethod
    def get_flows(self, query: CiliumFlowQuery) -> CiliumFlowsResult: ...
