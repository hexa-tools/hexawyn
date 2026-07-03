from __future__ import annotations

from hexawyn.application.ports.driving.analyze_critical_namespace_events.analyze_critical_namespace_events_command import (
    AnalyzeCriticalNamespaceEventsCommand,
)
from hexawyn.application.ports.driving.analyze_critical_namespace_events.analyze_critical_namespace_events_response import (
    AnalyzeCriticalNamespaceEventsResponse,
)
from hexawyn.application.ports.driving.analyze_critical_namespace_events.analyze_critical_namespace_events_service_port import (
    AnalyzeCriticalNamespaceEventsServicePort,
)


class AnalyzeCriticalNamespaceEventsUseCase:
    def __init__(self, service: AnalyzeCriticalNamespaceEventsServicePort) -> None:
        self._svc = service

    def execute(
        self, command: AnalyzeCriticalNamespaceEventsCommand
    ) -> AnalyzeCriticalNamespaceEventsResponse:
        return self._svc.analyze(command)
