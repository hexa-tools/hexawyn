from __future__ import annotations

from hexawyn.adapters.secondary.gitops.otel_latency_adapter import (
    OTelPrometheusLatencyAdapter,
)
from hexawyn.application.ports.driven.latency_percentile_port import LatencyPercentilePort
from hexawyn.domain.models.p99_latency import LatencyPercentileRequest


class TestOTelLatencyAdapter:
    def test_implements_port(self) -> None:
        assert isinstance(OTelPrometheusLatencyAdapter(), LatencyPercentilePort)

    def test_fetch_returns_default(self) -> None:
        result = OTelPrometheusLatencyAdapter().fetch_percentiles(
            LatencyPercentileRequest(endpoint="/v1/test")
        )
        assert result.sample_count == 0
        assert result.p99_ms == 0.0
