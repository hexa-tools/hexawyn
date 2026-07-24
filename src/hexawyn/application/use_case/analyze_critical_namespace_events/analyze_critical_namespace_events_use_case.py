from hexawyn.application.ports.driven.k8s_port import K8sPort
from hexawyn.application.ports.driven.namespace_events_port import NamespaceEventsPort
from hexawyn.application.use_case.analyze_critical_namespace_events.command import (
    AnalyzeCriticalNamespaceEventsCommand,
)
from hexawyn.application.use_case.analyze_critical_namespace_events.response import (
    AnalyzeCriticalNamespaceEventsResponse,
)


class AnalyzeCriticalNamespaceEventsUseCase:
    def __init__(self, events_port: NamespaceEventsPort, k8s_port: K8sPort) -> None:
        self._events = events_port
        self._k8s = k8s_port

    def execute(
        self, command: AnalyzeCriticalNamespaceEventsCommand
    ) -> AnalyzeCriticalNamespaceEventsResponse:
        return AnalyzeCriticalNamespaceEventsResponse()
