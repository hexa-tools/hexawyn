from abc import ABC, abstractmethod
from typing import TypedDict


class ResourceInventoryRaw(TypedDict):
    kind: str
    name: str
    namespace: str
    image_tag: str
    replicas: int
    is_secret: bool


class ClusterInventoryData(TypedDict):
    cluster_name: str
    resources: list[ResourceInventoryRaw]


class ClusterDiffPort(ABC):
    """Driven port — returns the full resource inventory for a cluster context.

    Resources include Deployments, Services, ConfigMaps, and Secrets.
    """

    @abstractmethod
    def get_resource_inventory(self, cluster_context: str) -> ClusterInventoryData: ...
