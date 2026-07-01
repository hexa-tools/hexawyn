from __future__ import annotations

from hexawyn.domain.models.trace_k8s_events import (
    K8sEvent,
    K8sEventType,
    TraceEventCorrelationRequest,
    TraceEventResult,
)


class TestK8sEvent:
    def test_oom(self) -> None:
        e = K8sEvent(
            event_type=K8sEventType.OOM_KILLED,
            pod_name="payment-pod-abc",
            timestamp="10:30:00.850",
            namespace="production",
            reason="OOMKilled",
        )
        assert e.event_type == K8sEventType.OOM_KILLED
        assert e.pod_name == "payment-pod-abc"


class TestTraceEventResult:
    def test_overlap_found(self) -> None:
        events = [
            K8sEvent(
                event_type=K8sEventType.OOM_KILLED,
                pod_name="payment-pod-abc",
                timestamp="10:30:00.850",
                namespace="production",
                reason="OOMKilled",
            ),
            K8sEvent(
                event_type=K8sEventType.CONTAINER_RESTART,
                pod_name="payment-pod-def",
                timestamp="10:30:01.200",
                namespace="production",
                reason="BackOff",
            ),
        ]
        slowest_span = "postgres.query (10:30:00.700 - 10:30:01.900)"
        result = TraceEventResult.compute(
            request=TraceEventCorrelationRequest(trace_id="slow-trace-789"),
            events=events,
            slowest_span=slowest_span,
        )
        assert len(result.matching_events) == 2
        assert result.conclusion is not None

    def test_no_events(self) -> None:
        result = TraceEventResult.compute(
            request=TraceEventCorrelationRequest(trace_id="abc"),
            events=[],
            slowest_span=None,
        )
        assert result.matching_events == []
        assert "no system events" in result.conclusion.lower()
