from abc import ABC, abstractmethod
from typing import TypedDict


class ClusterMetrics(TypedDict):
    cpu_usage_pct: float
    memory_usage_pct: float
    node_count: int
    pod_count: int


class MetricsPort(ABC):
    """Port for metrics — Prometheus, CloudWatch, Azure Monitor, Datadog."""

    @abstractmethod
    def get_cluster_metrics(self) -> ClusterMetrics:
        """Get cluster-level resource utilization metrics."""
