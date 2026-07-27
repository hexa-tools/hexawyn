from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.troubleshooting.analyze_critical_namespace_events.command import (
    AnalyzeCriticalNamespaceEventsCommand,
)
from hexawyn.application.use_case.troubleshooting.analyze_critical_namespace_events.response import (  # noqa: E501
    AnalyzeCriticalNamespaceEventsResponse,
)


class AnalyzeCriticalNamespaceEventsServicePort(ABC):
    @abstractmethod
    def analyze(
        self, command: AnalyzeCriticalNamespaceEventsCommand
    ) -> AnalyzeCriticalNamespaceEventsResponse: ...
