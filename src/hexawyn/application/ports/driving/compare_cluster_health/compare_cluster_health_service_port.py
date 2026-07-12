from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.compare_cluster_health.compare_cluster_health_command import (  # noqa: E501
    CompareClusterHealthCommand,
)
from hexawyn.application.ports.driving.compare_cluster_health.compare_cluster_health_response import (  # noqa: E501
    CompareClusterHealthResponse,
)


class CompareClusterHealthServicePort(ABC):
    @abstractmethod
    def compare(self, command: CompareClusterHealthCommand) -> CompareClusterHealthResponse: ...
