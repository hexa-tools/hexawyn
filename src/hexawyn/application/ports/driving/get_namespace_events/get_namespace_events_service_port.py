from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.troubleshooting.get_namespace_events.command import (
    GetNamespaceEventsCommand,
)
from hexawyn.application.use_case.troubleshooting.get_namespace_events.response import (
    GetNamespaceEventsResponse,
)


class GetNamespaceEventsServicePort(ABC):
    @abstractmethod
    def get_events(self, command: GetNamespaceEventsCommand) -> GetNamespaceEventsResponse: ...
