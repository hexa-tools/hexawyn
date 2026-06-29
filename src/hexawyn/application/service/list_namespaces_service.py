from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.ports.driving.list_namespaces.list_namespaces_command import (
    ListNamespacesCommand,
)
from hexawyn.application.ports.driving.list_namespaces.list_namespaces_response import (
    ListNamespacesResponse,
)
from hexawyn.application.ports.driving.list_namespaces.list_namespaces_service_port import (
    ListNamespacesServicePort,
)


class ListNamespacesService(ListNamespacesServicePort):
    """Lists all namespaces and their age from the K8s API."""

    def __init__(self, k8s_port: K8sPort) -> None:
        self._k8s = k8s_port

    def list_namespaces(self, command: ListNamespacesCommand) -> ListNamespacesResponse:
        namespaces = self._k8s.list_namespaces()
        return ListNamespacesResponse(namespaces=namespaces)
