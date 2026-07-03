from __future__ import annotations

from hexawyn.application.ports.driving.get_namespace_events.get_namespace_events_command import (
    GetNamespaceEventsCommand,
)
from hexawyn.application.ports.driving.get_namespace_events.get_namespace_events_response import (
    GetNamespaceEventsResponse,
)
from hexawyn.application.ports.driving.get_namespace_events.get_namespace_events_service_port import (
    GetNamespaceEventsServicePort,
)


class GetNamespaceEventsUseCase:
    def __init__(self, service: GetNamespaceEventsServicePort) -> None:
        self._svc = service

    def execute(self, command: GetNamespaceEventsCommand) -> GetNamespaceEventsResponse:
        return self._svc.get_events(command)
