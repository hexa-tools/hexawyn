from abc import ABC, abstractmethod
from typing import TypedDict


class NodeInfoRaw(TypedDict):
    name: str
    allocatable_cpu_cores: float
    allocatable_memory_gb: float
    cordoned: bool


class PodUsageRaw(TypedDict):
    pod_name: str
    namespace: str
    node_name: str
    cpu_usage_cores: float
    memory_usage_gb: float
    is_daemonset: bool


class HotNodeAnalysisPort(ABC):
    """Driven port: node allocatable/cordon status and cluster-wide pod
    usage joined to node assignment + DaemonSet ownership. Per-node
    utilization history comes from the existing MetricsQueryPort (ECA-31),
    not this port."""

    @abstractmethod
    def list_nodes(self) -> list[NodeInfoRaw]:
        """Fetches every node's allocatable capacity and cordoned status.

        Raises InsufficientPermissionsError when RBAC denies access.
        Raises ClusterUnreachableError on other cluster/API failures.
        """

    @abstractmethod
    def list_pod_usage(self) -> list[PodUsageRaw]:
        """Fetches every pod's actual CPU/memory usage, the node it's
        scheduled on, and whether it's owned by a DaemonSet.

        Raises InsufficientPermissionsError when RBAC denies access.
        Raises ClusterUnreachableError on other cluster/API failures.
        """
