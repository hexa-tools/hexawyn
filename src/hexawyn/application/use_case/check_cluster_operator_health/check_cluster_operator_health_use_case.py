from __future__ import annotations

from hexawyn.application.ports.driving.check_cluster_operator_health.check_cluster_operator_health_command import (  # noqa: E501
    CheckClusterOperatorHealthCommand,
)
from hexawyn.application.ports.driving.check_cluster_operator_health.check_cluster_operator_health_response import (  # noqa: E501
    CheckClusterOperatorHealthResponse,
)
from hexawyn.application.ports.driving.check_cluster_operator_health.check_cluster_operator_health_service_port import (  # noqa: E501
    CheckClusterOperatorHealthServicePort,
)


class CheckClusterOperatorHealthUseCase:
    def __init__(self, service: CheckClusterOperatorHealthServicePort) -> None:
        self._service = service

    def execute(
        self, command: CheckClusterOperatorHealthCommand
    ) -> CheckClusterOperatorHealthResponse:
        return self._service.check(command)
