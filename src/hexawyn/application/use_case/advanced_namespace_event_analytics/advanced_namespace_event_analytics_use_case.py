from __future__ import annotations

from hexawyn.application.ports.driving.advanced_namespace_event_analytics.advanced_namespace_event_analytics_command import (
    AdvancedNamespaceEventAnalyticsCommand,
)
from hexawyn.application.ports.driving.advanced_namespace_event_analytics.advanced_namespace_event_analytics_response import (
    AdvancedNamespaceEventAnalyticsResponse,
)
from hexawyn.application.ports.driving.advanced_namespace_event_analytics.advanced_namespace_event_analytics_service_port import (
    AdvancedNamespaceEventAnalyticsServicePort,
)


class AdvancedNamespaceEventAnalyticsUseCase:
    def __init__(self, service: AdvancedNamespaceEventAnalyticsServicePort) -> None:
        self._svc = service

    def execute(
        self, command: AdvancedNamespaceEventAnalyticsCommand
    ) -> AdvancedNamespaceEventAnalyticsResponse:
        return self._svc.analyze(command)
