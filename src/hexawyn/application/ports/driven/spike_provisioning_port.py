from abc import ABC, abstractmethod
from typing import TypedDict


class ClusterCapacityRaw(TypedDict):
    node_count: int
    allocatable_cpu_cores: float
    allocatable_memory_gb: float
    used_cpu_cores: float
    used_memory_gb: float
    autoscaler_enabled: bool


class SpikeProvisioningPort(ABC):
    """Driven port — provides current cluster capacity and optional history for
    spike-provisioning planning."""

    @abstractmethod
    def get_cluster_capacity(self) -> ClusterCapacityRaw:
        """Fetch current node count, allocatable/used CPU and memory, and
        whether a cluster-autoscaler is enabled.

        Raises InsufficientPermissionsError when RBAC denies access.
        Raises ClusterUnreachableError on other cluster/API failures.
        """

    @abstractmethod
    def get_historical_spike_multiplier(self) -> float | None:
        """Return last year's observed peak traffic multiplier for this event,
        or None when no historical data is available (caller then falls back to
        a generic multiplier)."""
