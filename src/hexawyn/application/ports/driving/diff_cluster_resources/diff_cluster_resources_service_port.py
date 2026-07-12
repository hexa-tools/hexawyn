from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.diff_cluster_resources.diff_cluster_resources_command import (  # noqa: E501
    DiffClusterResourcesCommand,
)
from hexawyn.application.ports.driving.diff_cluster_resources.diff_cluster_resources_response import (  # noqa: E501
    DiffClusterResourcesResponse,
)


class DiffClusterResourcesServicePort(ABC):
    @abstractmethod
    def diff(self, command: DiffClusterResourcesCommand) -> DiffClusterResourcesResponse: ...
