from abc import ABC, abstractmethod

from hexawyn.application.use_case.cluster.check_cluster_operator_health.command import (  # noqa: E501
    CheckClusterOperatorHealthCommand,
)
from hexawyn.application.use_case.cluster.check_cluster_operator_health.response import (  # noqa: E501
    CheckClusterOperatorHealthResponse,
)


class CheckClusterOperatorHealthServicePort(ABC):
    @abstractmethod
    def check(
        self, command: CheckClusterOperatorHealthCommand
    ) -> CheckClusterOperatorHealthResponse: ...
