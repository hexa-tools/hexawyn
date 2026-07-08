from abc import ABC, abstractmethod
from typing import TypedDict


class NamespaceRawData(TypedDict):
    """Raw waste data for one namespace — from K8s (requests) and Prometheus (actual usage)."""

    namespace: str
    cpu_requested_cores: float | None
    memory_requested_gb: float | None
    cpu_actual_avg_cores: float | None
    memory_actual_avg_gb: float | None
    age_hours: float
    has_resource_requests: bool


class NamespaceWasteAnalysisPort(ABC):
    """Driven port: provides raw K8s resource requests and Prometheus actual usage per namespace."""

    @abstractmethod
    def get_all_namespace_waste_data(self, window_days: int) -> list[NamespaceRawData]:
        """Fetch resource requests (K8s) and actual avg usage (Prometheus) for all namespaces.

        Returns an entry per namespace.
        Raises PrometheusUnavailableError when Prometheus is unreachable.
        Raises ClusterUnreachableError when the K8s API cannot be reached.
        """
