from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.troubleshooting.advanced_namespace_event_analytics.command import (  # noqa: E501
    AdvancedNamespaceEventAnalyticsCommand,
)
from hexawyn.application.use_case.troubleshooting.advanced_namespace_event_analytics.response import (  # noqa: E501
    AdvancedNamespaceEventAnalyticsResponse,
)


class AdvancedNamespaceEventAnalyticsServicePort(ABC):
    @abstractmethod
    def analyze(
        self, command: AdvancedNamespaceEventAnalyticsCommand
    ) -> AdvancedNamespaceEventAnalyticsResponse: ...
