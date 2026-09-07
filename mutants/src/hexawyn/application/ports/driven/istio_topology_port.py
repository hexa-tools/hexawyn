from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driven.kubernetes_topology_port import EdgeRecordData


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class IstioTopologyPort(ABC):
    @abstractmethod
    def get_virtual_service_edges(self, namespace: str | None) -> list[EdgeRecordData] | None:
        """Return edges inferred from Istio VirtualServices.

        Returns None when the mesh is not installed or unreachable, signaling
        callers to fall back to NetworkPolicy-based inference.
        """
