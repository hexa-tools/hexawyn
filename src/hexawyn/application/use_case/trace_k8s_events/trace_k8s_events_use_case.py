from dataclasses import asdict

from hexawyn.application.ports.driven.trace_event_correlation_port import TraceEventCorrelationPort
from hexawyn.application.use_case.trace_k8s_events.command import TraceK8sEventsCommand
from hexawyn.application.use_case.trace_k8s_events.response import TraceK8sEventsResponse


class TraceK8sEventsUseCase:
    def __init__(self, port: TraceEventCorrelationPort) -> None:
        self._port = port

    def execute(self, command: TraceK8sEventsCommand) -> TraceK8sEventsResponse:
        events = self._port.get_k8s_events(namespace=command.namespace)
        return TraceK8sEventsResponse(events=[asdict(e) for e in events])
