from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.use_case.list_namespaces.command import ListNamespacesCommand
from hexawyn.application.use_case.list_namespaces.response import ListNamespacesResponse


class ListNamespacesUseCase:
    def __init__(self, k8s_port: K8sPort) -> None:
        self._k8s = k8s_port

    def execute(self, command: ListNamespacesCommand) -> ListNamespacesResponse:
        namespaces = self._k8s.list_namespaces()
        return ListNamespacesResponse(namespaces=namespaces)
