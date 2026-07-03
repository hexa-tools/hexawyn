from __future__ import annotations

from hexawyn.application.ports.driving.summarize_namespace_events.summarize_namespace_events_command import (
    SummarizeNamespaceEventsCommand,
)
from hexawyn.application.ports.driving.summarize_namespace_events.summarize_namespace_events_response import (
    SummarizeNamespaceEventsResponse,
)
from hexawyn.application.ports.driving.summarize_namespace_events.summarize_namespace_events_service_port import (
    SummarizeNamespaceEventsServicePort,
)


class SummarizeNamespaceEventsUseCase:
    def __init__(self, service: SummarizeNamespaceEventsServicePort) -> None:
        self._svc = service

    def execute(self, command: SummarizeNamespaceEventsCommand) -> SummarizeNamespaceEventsResponse:
        return self._svc.summarize(command)
