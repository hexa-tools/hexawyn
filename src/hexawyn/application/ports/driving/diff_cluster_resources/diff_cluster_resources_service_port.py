from abc import ABC, abstractmethod

from hexawyn.application.use_case.cluster.diff_cluster_resources.command import (  # noqa: E501
    DiffClusterResourcesCommand,
)
from hexawyn.application.use_case.cluster.diff_cluster_resources.response import (  # noqa: E501
    DiffClusterResourcesResponse,
)


class DiffClusterResourcesServicePort(ABC):
    @abstractmethod
    def diff(self, command: DiffClusterResourcesCommand) -> DiffClusterResourcesResponse: ...
