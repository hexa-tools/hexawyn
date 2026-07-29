from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.trace_event_correlation_port import TraceEventCorrelationPort
from hexawyn.application.use_case.troubleshooting.trace_k8s_events.command import (
    TraceK8sEventsCommand,
)
from hexawyn.application.use_case.troubleshooting.trace_k8s_events.response import (
    TraceK8sEventsResponse,
)
from hexawyn.domain.models.trace_k8s_events import TraceEventCorrelationRequest, TraceEventResult


class TraceK8sEventsUseCase:
    def __init__(self, port: TraceEventCorrelationPort) -> None:
        self._port = port

    def execute(self, command: TraceK8sEventsCommand) -> TraceK8sEventsResponse:
        req = TraceEventCorrelationRequest(trace_id=command.trace_id)
        events = self._port.fetch_k8s_events(req)
        slowest = self._port.fetch_slowest_span(req)
        r = TraceEventResult.compute(request=req, events=events, slowest_span=slowest)
        return TraceK8sEventsResponse(
            trace_id=r.trace_id,
            matching_events=[asdict(e) for e in r.matching_events],
            slowest_span=r.slowest_span,  # type: ignore
            conclusion=r.conclusion,
        )
