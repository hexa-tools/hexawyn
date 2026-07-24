from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.advanced_namespace_event_analytics.command import (
    AdvancedNamespaceEventAnalyticsCommand,
)
from hexawyn.application.use_case.advanced_namespace_event_analytics.response import (
    AdvancedNamespaceEventAnalyticsResponse,
)


class AdvancedNamespaceEventAnalyticsServicePort(ABC):
    @abstractmethod
    def analyze(
        self, command: AdvancedNamespaceEventAnalyticsCommand
    ) -> AdvancedNamespaceEventAnalyticsResponse: ...
