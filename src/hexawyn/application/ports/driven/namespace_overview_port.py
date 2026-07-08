from abc import ABC, abstractmethod
from typing import TypedDict


class PodStatusRaw(TypedDict):
    name: str
    status: str


class DeploymentStatusRaw(TypedDict):
    name: str
    ready_replicas: int
    desired_replicas: int


class HpaStatusRaw(TypedDict):
    name: str
    current_replicas: int
    max_replicas: int


class NamespaceOverviewRawData(TypedDict):
    namespace_status: str
    pods: list[PodStatusRaw]
    deployments: list[DeploymentStatusRaw]
    services_count: int
    hpas: list[HpaStatusRaw]


class NamespaceOverviewPort(ABC):
    """Driven port: fetches pods, deployments, service count, and HPAs for
    one namespace in a single bulk call."""

    @abstractmethod
    def get_namespace_overview_data(self, namespace: str) -> NamespaceOverviewRawData:
        """Fetches pods/deployments/services/HPAs for the namespace.

        Raises ResourceNotFoundError when the namespace no longer exists.
        Raises InsufficientPermissionsError when RBAC denies access.
        Raises ClusterUnreachableError on other cluster/API failures.
        """
