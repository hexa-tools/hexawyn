from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.domain.models.fleet_health import ClusterRawMetrics


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class FleetHealthPort(ABC):
    @abstractmethod
    def list_contexts(self) -> list[str]:
        """Return all kubeconfig context names."""

    @abstractmethod
    def get_cluster_raw_metrics(self, context_name: str) -> ClusterRawMetrics:
        """
        Collect raw metrics for a single cluster context.
        Raises ClusterUnreachableError if the cluster cannot be reached.
        """
