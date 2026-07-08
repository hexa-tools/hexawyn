from __future__ import annotations

from hexawyn.application.ports.driven.trace_event_correlation_port import TraceEventCorrelationPort
from hexawyn.domain.models.trace_k8s_events import K8sEvent, TraceEventCorrelationRequest


class KubernetesEventAdapter(TraceEventCorrelationPort):
    def fetch_k8s_events(self, request: TraceEventCorrelationRequest) -> list[K8sEvent]:
        return []

    def fetch_slowest_span(self, request: TraceEventCorrelationRequest) -> str | None:
        return None
