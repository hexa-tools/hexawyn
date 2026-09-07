from abc import ABC, abstractmethod

from hexawyn.application.ports.driven.k8s_port import ClusterMetrics


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class MetricsPort(ABC):
    """Port for metrics — Prometheus, CloudWatch, Azure Monitor, Datadog."""

    @abstractmethod
    def get_cluster_metrics(self) -> ClusterMetrics:
        """Get cluster-level resource utilization metrics."""
