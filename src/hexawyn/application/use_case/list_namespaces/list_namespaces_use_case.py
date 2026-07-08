from __future__ import annotations

from hexawyn.application.ports.driving.list_namespaces.list_namespaces_command import (
    ListNamespacesCommand,
)
from hexawyn.application.ports.driving.list_namespaces.list_namespaces_response import (
    ListNamespacesResponse,
)
from hexawyn.application.ports.driving.list_namespaces.list_namespaces_service_port import (
    ListNamespacesServicePort,
)


class ListNamespacesUseCase:
    """Entry point — depends on the service port abstraction, not the concrete service."""

    def __init__(self, service: ListNamespacesServicePort) -> None:
        self._service = service

    def execute(self, command: ListNamespacesCommand) -> ListNamespacesResponse:
        return self._service.list_namespaces(command)
