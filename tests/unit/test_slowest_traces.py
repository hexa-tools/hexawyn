from __future__ import annotations

from hexawyn.domain.models.slowest_traces import (
    SlowestTracesRequest,
    SlowestTracesResult,
    SlowTrace,
)


class TestSlowTrace:
    def test_create(self) -> None:
        st = SlowTrace(
            trace_id="tr001",
            duration_ms=4200.0,
            operation="POST /checkout",
            span_count=42,
        )
        assert st.trace_id == "tr001"
        assert st.duration_ms == 4200.0


class TestSlowestTracesResult:
    def test_ranked(self) -> None:
        traces = [
            SlowTrace(trace_id="tr003", duration_ms=2100.0, operation="GET /cart", span_count=15),
            SlowTrace(
                trace_id="tr001", duration_ms=4200.0, operation="POST /checkout", span_count=42
            ),
            SlowTrace(
                trace_id="tr002", duration_ms=3800.0, operation="POST /checkout", span_count=38
            ),
        ]
        result = SlowestTracesResult.compute(
            request=SlowestTracesRequest(pod_name="checkout-7d", top_n=5),
            traces=traces,
        )
        assert len(result.slowest_traces) == 3
        assert result.slowest_traces[0].trace_id == "tr001"
        assert result.slowest_traces[1].trace_id == "tr002"

    def test_top_n_truncation(self) -> None:
        traces = [
            SlowTrace(
                trace_id=f"tr{i}",
                duration_ms=float(1000 - i * 10),
                operation="GET /x",
                span_count=5,
            )
            for i in range(10)
        ]
        result = SlowestTracesResult.compute(
            request=SlowestTracesRequest(pod_name="pod", top_n=3),
            traces=traces,
        )
        assert len(result.slowest_traces) == 3

    def test_empty(self) -> None:
        result = SlowestTracesResult.compute(
            request=SlowestTracesRequest(pod_name="ghost-pod", top_n=5),
            traces=[],
        )
        assert result.slowest_traces == []
