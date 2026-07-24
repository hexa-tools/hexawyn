from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.use_case.get_namespace_events.command import GetNamespaceEventsCommand
from hexawyn.application.use_case.get_namespace_events.response import GetNamespaceEventsResponse


class GetNamespaceEventsUseCase:
    def __init__(self, port: K8sPort) -> None:
        self._port = port

    def execute(self, command: GetNamespaceEventsCommand) -> GetNamespaceEventsResponse:
        return GetNamespaceEventsResponse()
