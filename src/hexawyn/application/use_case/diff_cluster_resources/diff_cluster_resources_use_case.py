from __future__ import annotations

from hexawyn.application.ports.driving.diff_cluster_resources.diff_cluster_resources_command import (  # noqa: E501
    DiffClusterResourcesCommand,
)
from hexawyn.application.ports.driving.diff_cluster_resources.diff_cluster_resources_response import (  # noqa: E501
    DiffClusterResourcesResponse,
)
from hexawyn.application.ports.driving.diff_cluster_resources.diff_cluster_resources_service_port import (  # noqa: E501
    DiffClusterResourcesServicePort,
)


class DiffClusterResourcesUseCase:
    def __init__(self, service: DiffClusterResourcesServicePort) -> None:
        self._service = service

    def execute(self, command: DiffClusterResourcesCommand) -> DiffClusterResourcesResponse:
        return self._service.diff(command)
