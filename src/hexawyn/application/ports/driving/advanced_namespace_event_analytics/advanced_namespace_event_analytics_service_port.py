from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.advanced_namespace_event_analytics.advanced_namespace_event_analytics_command import (
    AdvancedNamespaceEventAnalyticsCommand,
)
from hexawyn.application.ports.driving.advanced_namespace_event_analytics.advanced_namespace_event_analytics_response import (
    AdvancedNamespaceEventAnalyticsResponse,
)


class AdvancedNamespaceEventAnalyticsServicePort(ABC):
    @abstractmethod
    def analyze(
        self, command: AdvancedNamespaceEventAnalyticsCommand
    ) -> AdvancedNamespaceEventAnalyticsResponse: ...
