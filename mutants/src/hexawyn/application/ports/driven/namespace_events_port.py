from abc import ABC, abstractmethod

from hexawyn.domain.models.namespace_event import GetNamespaceEventsRequest, NamespaceEvent


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class NamespaceEventsPort(ABC):
    @abstractmethod
    def list_events(self, request: GetNamespaceEventsRequest) -> list[NamespaceEvent]: ...
