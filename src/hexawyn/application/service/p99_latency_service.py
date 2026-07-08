from __future__ import annotations

from hexawyn.application.ports.driven.latency_percentile_port import LatencyPercentilePort
from hexawyn.application.ports.driving.p99_latency.p99_latency_command import P99LatencyCommand
from hexawyn.application.ports.driving.p99_latency.p99_latency_response import P99LatencyResponse
from hexawyn.application.ports.driving.p99_latency.p99_latency_service_port import (
    P99LatencyServicePort,
)
from hexawyn.domain.models.p99_latency import LatencyPercentileRequest, P99Result


class P99LatencyService(P99LatencyServicePort):
    def __init__(self, port: LatencyPercentilePort) -> None:
        self._port = port

    def compute_p99(self, command: P99LatencyCommand) -> P99LatencyResponse:
        req = LatencyPercentileRequest(
            endpoint=command.endpoint,
            time_window_minutes=command.time_window_minutes,
            slo_threshold_ms=command.slo_threshold_ms,
        )
        lp = self._port.fetch_percentiles(req)
        r = P99Result.compute(request=req, percentiles=lp)
        return P99LatencyResponse(
            endpoint=r.endpoint,
            time_window_minutes=r.time_window_minutes,
            p50_ms=r.p50_ms,
            p95_ms=r.p95_ms,
            p99_ms=r.p99_ms,
            slo_threshold_ms=r.slo_threshold_ms,
            slo_status=r.slo_status.value,
            slo_delta_ms=r.slo_delta_ms,
            sample_count=r.sample_count,
        )
