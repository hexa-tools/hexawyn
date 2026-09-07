from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.domain.models.cilium import (
    CiliumDenialsQuery,
    CiliumDenialsResult,
    CiliumFlowQuery,
    CiliumFlowsResult,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class CiliumHubblePort(ABC):
    """Outbound port to query Cilium flow logs (Hubble Relay)."""

    @abstractmethod
    def get_flows(self, query: CiliumFlowQuery) -> CiliumFlowsResult: ...

    @abstractmethod
    def detect_denials(self, query: CiliumDenialsQuery) -> CiliumDenialsResult: ...
