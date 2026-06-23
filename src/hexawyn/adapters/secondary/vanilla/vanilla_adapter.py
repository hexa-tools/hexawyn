from hexawyn.application.ports.driven.k8s_port import (
    ClusterContext,
    ClusterHealthPort,
    ClusterMetrics,
    Finding,
    K8sPort,
    PodInfo,
)


class VanillaAdapter(K8sPort, ClusterHealthPort):
    """Minimal adapter for vanilla Kubernetes — no cloud provider dependencies."""

    def __init__(self, cluster_name: str) -> None:
        self._cluster_name = cluster_name

    def list_pods(self, namespace: str | None = None) -> list[PodInfo]:
        return []

    def get_cluster_metrics(self) -> ClusterMetrics:
        return {
            "cpu_usage_pct": 0.0,
            "memory_usage_pct": 0.0,
            "node_count": 0,
            "pod_count": 0,
        }

    def get_findings(self) -> list[Finding]:
        return []

    def get_health_score(self) -> int:
        return 100

    def get_health_status(self) -> str:
        return "healthy"

    def get_cluster_context(self) -> ClusterContext:
        return {
            "name": self._cluster_name,
            "cluster": self._cluster_name,
            "provider": "vanilla",
            "namespace": "default",
        }
