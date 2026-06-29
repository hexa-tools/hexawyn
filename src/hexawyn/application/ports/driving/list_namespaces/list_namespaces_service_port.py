from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.list_namespaces.list_namespaces_command import (
    ListNamespacesCommand,
)
from hexawyn.application.ports.driving.list_namespaces.list_namespaces_response import (
    ListNamespacesResponse,
)


class ListNamespacesServicePort(ABC):
    @abstractmethod
    def list_namespaces(self, command: ListNamespacesCommand) -> ListNamespacesResponse: ...
