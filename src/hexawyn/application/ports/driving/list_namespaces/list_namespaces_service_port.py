from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.cluster.list_namespaces.command import (
    ListNamespacesCommand,
)
from hexawyn.application.use_case.cluster.list_namespaces.response import (
    ListNamespacesResponse,
)


class ListNamespacesServicePort(ABC):
    @abstractmethod
    def list_namespaces(self, command: ListNamespacesCommand) -> ListNamespacesResponse: ...
