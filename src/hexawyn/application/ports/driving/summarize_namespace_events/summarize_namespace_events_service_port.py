from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.summarize_namespace_events.summarize_namespace_events_command import (
    SummarizeNamespaceEventsCommand,
)
from hexawyn.application.ports.driving.summarize_namespace_events.summarize_namespace_events_response import (
    SummarizeNamespaceEventsResponse,
)


class SummarizeNamespaceEventsServicePort(ABC):
    @abstractmethod
    def summarize(
        self, command: SummarizeNamespaceEventsCommand
    ) -> SummarizeNamespaceEventsResponse: ...
