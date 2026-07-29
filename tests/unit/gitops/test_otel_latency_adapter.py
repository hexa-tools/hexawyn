from __future__ import annotations

from unittest.mock import patch


class TestOtelLatencyAdapterUnit:
    def test_returns_percentiles(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_latency_adapter import (
            OTelPrometheusLatencyAdapter,
        )
        from hexawyn.domain.models.p99_latency import LatencyPercentileRequest

        adapter = OTelPrometheusLatencyAdapter()
        result = adapter.fetch_percentiles(LatencyPercentileRequest(endpoint="/api/test"))
        assert result.p50_ms >= 0.0

    def test_empty_endpoint_returns_zeros(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_latency_adapter import (
            OTelPrometheusLatencyAdapter,
        )
        from hexawyn.domain.models.p99_latency import LatencyPercentileRequest

        adapter = OTelPrometheusLatencyAdapter()
        result = adapter.fetch_percentiles(LatencyPercentileRequest(endpoint=""))
        assert result.p50_ms == 0.0
        assert result.p95_ms == 0.0
        assert result.p99_ms == 0.0
        assert result.sample_count == 0

    def test_prometheus_exception_returns_zeros(self) -> None:
        from hexawyn.adapters.secondary.gitops.otel_latency_adapter import (
            OTelPrometheusLatencyAdapter,
        )
        from hexawyn.domain.models.p99_latency import LatencyPercentileRequest

        with patch(
            "hexawyn.adapters.secondary.gitops.otel_latency_adapter.query_prometheus_instant",
            side_effect=RuntimeError("prometheus unreachable"),
        ):
            adapter = OTelPrometheusLatencyAdapter()
            result = adapter.fetch_percentiles(LatencyPercentileRequest(endpoint="/api/test"))
            assert result.p50_ms == 0.0
            assert result.p99_ms == 0.0
            assert result.sample_count == 0
