from __future__ import annotations

from hexawyn.application.ports.driving.compare_cluster_health.compare_cluster_health_command import (  # noqa: E501
    CompareClusterHealthCommand,
)
from hexawyn.application.ports.driving.compare_cluster_health.compare_cluster_health_response import (  # noqa: E501
    CompareClusterHealthResponse,
)
from hexawyn.application.ports.driving.compare_cluster_health.compare_cluster_health_service_port import (  # noqa: E501
    CompareClusterHealthServicePort,
)


class CompareClusterHealthUseCase:
    def __init__(self, service: CompareClusterHealthServicePort) -> None:
        self._service = service

    def execute(self, command: CompareClusterHealthCommand) -> CompareClusterHealthResponse:
        return self._service.compare(command)
