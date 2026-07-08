from abc import ABC, abstractmethod

from hexawyn.domain.models.namespace_event import GetNamespaceEventsRequest, NamespaceEvent


class NamespaceEventsPort(ABC):
    @abstractmethod
    def list_events(self, request: GetNamespaceEventsRequest) -> list[NamespaceEvent]: ...
