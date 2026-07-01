from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.trace_event_correlation_port import (
    TraceEventCorrelationPort,
)
from hexawyn.domain.models.trace_k8s_events import K8sEvent, K8sEventType


class TestTraceK8sEventsTool:
    def test_returns_events(self) -> None:
        from hexawyn.mcp.tools.trace_k8s_events import trace_k8s_events

        with patch("hexawyn.mcp.server.build_trace_event_correlation_adapter") as m:
            a = MagicMock(spec=TraceEventCorrelationPort)
            a.fetch_k8s_events.return_value = [
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
            a.fetch_slowest_span.return_value = "postgres.query (10:30:00.700 - 10:30:01.900)"
            m.return_value = a
            r = trace_k8s_events(trace_id="slow-trace-789")
        assert r["error"] is None
        assert len(r["matching_events"]) == 2
        assert "OOMKilled" in r["conclusion"]

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.trace_k8s_events import trace_k8s_events

        with patch(
            "hexawyn.mcp.server.build_trace_event_correlation_adapter",
            side_effect=RuntimeError("boom"),
        ):
            r = trace_k8s_events(trace_id="x")
        assert r["error"] == "boom"
