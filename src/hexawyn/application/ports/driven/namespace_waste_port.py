from abc import ABC, abstractmethod

from hexawyn.domain.models.namespace_waste import NamespaceRawData

__all__ = ["NamespaceRawData", "NamespaceWasteAnalysisPort"]


class NamespaceWasteAnalysisPort(ABC):
    """Driven port: provides raw K8s resource requests and Prometheus actual usage per namespace."""

    @abstractmethod
    def get_all_namespace_waste_data(self, window_days: int) -> list[NamespaceRawData]:
        """Fetch resource requests (K8s) and actual avg usage (Prometheus) for all namespaces.

        Returns an entry per namespace.
        Raises PrometheusUnavailableError when Prometheus is unreachable.
        Raises ClusterUnreachableError when the K8s API cannot be reached.
        """
