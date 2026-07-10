from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.check_cluster_operator_health.check_cluster_operator_health_command import (  # noqa: E501
    CheckClusterOperatorHealthCommand,
)
from hexawyn.application.ports.driving.check_cluster_operator_health.check_cluster_operator_health_response import (  # noqa: E501
    CheckClusterOperatorHealthResponse,
)


class CheckClusterOperatorHealthServicePort(ABC):
    @abstractmethod
    def check(
        self, command: CheckClusterOperatorHealthCommand
    ) -> CheckClusterOperatorHealthResponse: ...
