from __future__ import annotations

from hexawyn.adapters.secondary.gitops.kubernetes_event_adapter import (
    KubernetesEventAdapter,
)
from hexawyn.application.ports.driven.trace_event_correlation_port import (
    TraceEventCorrelationPort,
)
from hexawyn.domain.models.trace_k8s_events import TraceEventCorrelationRequest


class TestKubernetesEventAdapter:
    def test_implements_port(self) -> None:
        assert isinstance(KubernetesEventAdapter(), TraceEventCorrelationPort)

    def test_fetch_events_returns_empty(self) -> None:
        r = KubernetesEventAdapter().fetch_k8s_events(TraceEventCorrelationRequest(trace_id="x"))
        assert r == []

    def test_fetch_slowest_span_returns_none(self) -> None:
        r = KubernetesEventAdapter().fetch_slowest_span(TraceEventCorrelationRequest(trace_id="x"))
        assert r is None
