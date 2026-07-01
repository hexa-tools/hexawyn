from __future__ import annotations

from hexawyn.application.ports.driving.trace_k8s_events.trace_k8s_events_command import (
    TraceK8sEventsCommand,
)
from hexawyn.application.ports.driving.trace_k8s_events.trace_k8s_events_response import (
    TraceK8sEventsResponse,
)
from hexawyn.application.ports.driving.trace_k8s_events.trace_k8s_events_service_port import (
    TraceK8sEventsServicePort,
)


class TraceK8sEventsUseCase:
    def __init__(self, service: TraceK8sEventsServicePort) -> None:
        self._svc = service

    def execute(self, cmd: TraceK8sEventsCommand) -> TraceK8sEventsResponse:
        return self._svc.correlate(cmd)
