from abc import ABC, abstractmethod
from typing import TypedDict


class PodMetricSnapshot(TypedDict):
    name: str
    namespace: str
    cpu_cores: float
    memory_gb: float


class PodMetricsPort(ABC):
    """Driven port: per-pod CPU/memory usage from the Kubernetes metrics-server."""

    @abstractmethod
    def get_pod_metrics(self, namespace: str | None = None) -> list[PodMetricSnapshot]:
        """Return current CPU/memory usage per pod from metrics-server.

        Raises MetricsUnavailableError when metrics-server is not installed or unreachable.
        """
