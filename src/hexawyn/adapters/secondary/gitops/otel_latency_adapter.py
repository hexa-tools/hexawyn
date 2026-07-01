from __future__ import annotations

from hexawyn.application.ports.driven.latency_percentile_port import LatencyPercentilePort
from hexawyn.domain.models.p99_latency import LatencyPercentileRequest, LatencyPercentiles


class OTelPrometheusLatencyAdapter(LatencyPercentilePort):
    def fetch_percentiles(self, request: LatencyPercentileRequest) -> LatencyPercentiles:
        return LatencyPercentiles(p50_ms=0.0, p95_ms=0.0, p99_ms=0.0, sample_count=0)
