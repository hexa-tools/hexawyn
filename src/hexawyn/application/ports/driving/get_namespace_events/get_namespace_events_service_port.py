from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.get_namespace_events.get_namespace_events_command import (
    GetNamespaceEventsCommand,
)
from hexawyn.application.ports.driving.get_namespace_events.get_namespace_events_response import (
    GetNamespaceEventsResponse,
)


class GetNamespaceEventsServicePort(ABC):
    @abstractmethod
    def get_events(self, command: GetNamespaceEventsCommand) -> GetNamespaceEventsResponse: ...
