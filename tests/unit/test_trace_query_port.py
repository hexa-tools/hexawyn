from hexawyn.application.ports.driven.trace_query_port import (
    LatencyDiagnosticRequest,
    TraceQueryPort,
    TraceSpan,
)


class TestTraceQueryPortContract:
    def test_port_is_abstract(self) -> None:
        import pytest

        with pytest.raises(TypeError):
            TraceQueryPort()  # type: ignore[abstract]

    def test_abstract_methods_are_defined(self) -> None:
        assert set(TraceQueryPort.__abstractmethods__) == {
            "fetch_slow_spans",
            "fetch_total_traces",
        }

    def test_reexports_domain_contract_types(self) -> None:
        request = LatencyDiagnosticRequest(service_name="svc")
        span = TraceSpan(trace_id="t", span_name="s", duration_ms=1.0)

        assert request.service_name == "svc"
        assert span.duration_ms == 1.0
