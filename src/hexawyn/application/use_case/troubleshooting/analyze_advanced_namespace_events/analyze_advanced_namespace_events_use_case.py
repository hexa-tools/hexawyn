from __future__ import annotations

from hexawyn.application.ports.driven.namespace_events_port import NamespaceEventsPort
from hexawyn.application.use_case.troubleshooting.analyze_advanced_namespace_events.command import (
    AnalyzeAdvancedNamespaceEventsCommand,
)
from hexawyn.application.use_case.troubleshooting.analyze_advanced_namespace_events.response import (  # noqa: E501
    AdvancedNamespaceEventAnalyticsResponse,
)


class AnalyzeAdvancedNamespaceEventsUseCase:
    def __init__(self, port: NamespaceEventsPort) -> None:
        self._port = port

    def execute(
        self, command: AnalyzeAdvancedNamespaceEventsCommand
    ) -> AdvancedNamespaceEventAnalyticsResponse:
        events = self._port.list_events(  # type: ignore
            namespace=command.namespace,
            time_window_minutes=command.time_window_minutes,
        )
        return AdvancedNamespaceEventAnalyticsResponse(
            namespace=command.namespace,
            total_events=len(events),
        )
