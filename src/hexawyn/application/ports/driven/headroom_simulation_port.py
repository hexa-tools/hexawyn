from abc import ABC, abstractmethod
from typing import TypedDict


class HeadroomCapacityInfoRaw(TypedDict):
    total_allocatable_cpu_cores: float
    total_allocatable_memory_gb: float
    node_count: int
    largest_node_cpu_cores: float
    largest_node_memory_gb: float
    autoscaler_enabled: bool


class HeadroomSimulationPort(ABC):
    """Driven port: node-allocatable totals, node count, and the largest
    single node's capacity — narrower than CapacityForecastPort (ECA-74),
    which only exposes summed totals; this feature additionally needs
    per-node granularity for the unschedulable-workload and
    average-node-size checks."""

    @abstractmethod
    def get_node_capacity_info(self) -> HeadroomCapacityInfoRaw:
        """Fetches total allocatable CPU/memory, node count, the largest
        single node's allocatable capacity, and whether a cluster-autoscaler
        is present.

        Raises InsufficientPermissionsError when RBAC denies access.
        Raises ClusterUnreachableError on other cluster/API failures.
        """
