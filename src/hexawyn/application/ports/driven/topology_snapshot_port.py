from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.domain.services.topology.exporter import DependencyGraphExport


class TopologySnapshotPort(ABC):
    @abstractmethod
    def save_snapshot(self, cluster_name: str, graph_export: DependencyGraphExport) -> None:
        """Persist a topology snapshot for historical comparison.

        Best-effort: implementations must not raise on storage failure — the
        caller treats this as non-blocking persistence.
        """
