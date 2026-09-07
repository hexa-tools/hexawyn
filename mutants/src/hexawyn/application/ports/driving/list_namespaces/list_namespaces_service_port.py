from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cluster.list_namespaces.command import (
    ListNamespacesCommand,
)
from hexawyn.application.use_case.cluster.list_namespaces.response import (
    ListNamespacesResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class ListNamespacesServicePort(ABC):
    @abstractmethod
    def list_namespaces(self, command: ListNamespacesCommand) -> ListNamespacesResponse: ...
