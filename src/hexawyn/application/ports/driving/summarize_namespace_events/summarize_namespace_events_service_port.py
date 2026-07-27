from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.troubleshooting.summarize_namespace_events.command import (  # noqa: E501
    SummarizeNamespaceEventsCommand,
)
from hexawyn.application.use_case.troubleshooting.summarize_namespace_events.response import (  # noqa: E501
    SummarizeNamespaceEventsResponse,
)


class SummarizeNamespaceEventsServicePort(ABC):
    @abstractmethod
    def summarize(
        self, command: SummarizeNamespaceEventsCommand
    ) -> SummarizeNamespaceEventsResponse: ...
