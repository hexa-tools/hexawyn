from abc import ABC, abstractmethod
from typing import TypedDict


class PodInfo(TypedDict):
    name: str
    namespace: str
    status: str
    restarts: int


class ClusterMetrics(TypedDict):
    cpu_usage_pct: float
    memory_usage_pct: float
    node_count: int
    pod_count: int


class Finding(TypedDict):
    severity: str
    message: str
    remediation: str


class ClusterContext(TypedDict):
    name: str
    cluster: str
    provider: str
    namespace: str


class K8sPort(ABC):
    """Port for Kubernetes cluster operations — read-only."""

    @abstractmethod
    def list_pods(self, namespace: str | None = None) -> list[PodInfo]:
        """List all pods, optionally filtered by namespace."""

    @abstractmethod
    def get_cluster_metrics(self) -> ClusterMetrics:
        """Get cluster-level resource utilization metrics."""

    @abstractmethod
    def get_findings(self) -> list[Finding]:
        """Get list of findings with severity, message, remediation."""

    @abstractmethod
    def get_health_score(self) -> int:
        """Get cluster health score 0-100."""

    @abstractmethod
    def get_health_status(self) -> str:
        """Get cluster health status: healthy | degraded | critical."""

    @abstractmethod
    def get_cluster_context(self) -> ClusterContext:
        """Get current cluster context metadata."""
