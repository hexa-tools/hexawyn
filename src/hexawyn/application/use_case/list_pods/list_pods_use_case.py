from __future__ import annotations

from hexawyn.application.ports.driving.list_pods.list_pods_command import ListPodsCommand
from hexawyn.application.ports.driving.list_pods.list_pods_response import ListPodsResponse
from hexawyn.application.ports.driving.list_pods.list_pods_service_port import (
    ListPodsServicePort,
)


class ListPodsUseCase:
    """Entry point — depends on the service port abstraction."""

    def __init__(self, service: ListPodsServicePort) -> None:
        self._service = service

    def execute(self, command: ListPodsCommand) -> ListPodsResponse:
        return self._service.list_pods(command)
