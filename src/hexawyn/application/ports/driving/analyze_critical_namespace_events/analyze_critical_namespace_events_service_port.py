from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.analyze_critical_namespace_events.analyze_critical_namespace_events_command import (
    AnalyzeCriticalNamespaceEventsCommand,
)
from hexawyn.application.ports.driving.analyze_critical_namespace_events.analyze_critical_namespace_events_response import (
    AnalyzeCriticalNamespaceEventsResponse,
)


class AnalyzeCriticalNamespaceEventsServicePort(ABC):
    @abstractmethod
    def analyze(
        self, command: AnalyzeCriticalNamespaceEventsCommand
    ) -> AnalyzeCriticalNamespaceEventsResponse: ...
