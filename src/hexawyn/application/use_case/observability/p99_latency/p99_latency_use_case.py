from __future__ import annotations

from hexawyn.application.ports.driven.latency_percentile_port import LatencyPercentilePort
from hexawyn.application.use_case.observability.p99_latency.command import P99LatencyCommand
from hexawyn.application.use_case.observability.p99_latency.response import P99LatencyResponse
from hexawyn.domain.models.p99_latency import LatencyPercentileRequest, P99Result


class P99LatencyUseCase:
    def __init__(self, port: LatencyPercentilePort) -> None:
        self._port = port

    def execute(self, command: P99LatencyCommand) -> P99LatencyResponse:
        req = LatencyPercentileRequest(
            endpoint=command.endpoint,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            slo_threshold_ms=command.slo_threshold_ms,  # type: ignore
        )
        lp = self._port.fetch_percentiles(req)
        r = P99Result.compute(request=req, percentiles=lp)
        return P99LatencyResponse(
            endpoint=r.endpoint,
            time_window_minutes=r.time_window_minutes,  # type: ignore
            p50_ms=r.p50_ms,  # type: ignore
            p95_ms=r.p95_ms,  # type: ignore
            p99_ms=r.p99_ms,  # type: ignore
            slo_threshold_ms=r.slo_threshold_ms,  # type: ignore
            slo_status=r.slo_status.value,
            slo_delta_ms=r.slo_delta_ms,  # type: ignore
            sample_count=r.sample_count,
        )
