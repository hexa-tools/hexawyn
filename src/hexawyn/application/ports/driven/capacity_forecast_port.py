from abc import ABC, abstractmethod
from typing import TypedDict


class ClusterCapacityInfoRaw(TypedDict):
    total_allocatable_cpu_cores: float
    total_allocatable_memory_gb: float
    autoscaler_enabled: bool


class CapacityForecastPort(ABC):
    """Driven port: node-allocatable capacity totals and cluster-autoscaler
    presence. Deliberately narrow — cluster CPU/memory usage history is
    fetched via the existing MetricsQueryPort (ECA-31), not duplicated here."""

    @abstractmethod
    def get_cluster_capacity_info(self) -> ClusterCapacityInfoRaw:
        """Fetches total allocatable CPU/memory across all nodes and whether
        a cluster-autoscaler is present.

        Raises InsufficientPermissionsError when RBAC denies access.
        Raises ClusterUnreachableError on other cluster/API failures.
        """
