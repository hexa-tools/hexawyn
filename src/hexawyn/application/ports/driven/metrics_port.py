from abc import ABC, abstractmethod

from hexawyn.application.ports.driven.k8s_port import ClusterMetrics


class MetricsPort(ABC):
    """Port for metrics — Prometheus, CloudWatch, Azure Monitor, Datadog."""

    @abstractmethod
    def get_cluster_metrics(self) -> ClusterMetrics:
        """Get cluster-level resource utilization metrics."""
