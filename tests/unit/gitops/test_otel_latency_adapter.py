# Auto-generated test for otel_latency_adapter

from __future__ import annotations


class TestOtelLatencyAdapterUnit:
    def test_returns_percentiles(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_latency_adapter import (
            OTelPrometheusLatencyAdapter,
        )
        from hexawyn.domain.models.p99_latency import LatencyPercentileRequest

        adapter = OTelPrometheusLatencyAdapter()
        result = adapter.fetch_percentiles(LatencyPercentileRequest(endpoint="/api/test"))
        assert result.p50_ms >= 0.0
