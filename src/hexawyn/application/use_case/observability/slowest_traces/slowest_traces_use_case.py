from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.slow_trace_search_port import SlowTraceSearchPort
from hexawyn.application.use_case.observability.slowest_traces.command import (
    SlowestTracesCommand,
)
from hexawyn.application.use_case.observability.slowest_traces.response import (
    SlowestTracesResponse,
)
from hexawyn.domain.models.slowest_traces import SlowestTracesRequest, SlowestTracesResult


class SlowestTracesUseCase:
    def __init__(self, port: SlowTraceSearchPort) -> None:
        self._port = port

    def execute(self, command: SlowestTracesCommand) -> SlowestTracesResponse:
        req = SlowestTracesRequest(
            pod_name=command.pod_name,
            time_window_minutes=command.time_window_minutes,  # type: ignore
            top_n=command.top_n,  # type: ignore
        )
        traces = self._port.search_pod_traces(req)
        r = SlowestTracesResult.compute(request=req, traces=traces)
        return SlowestTracesResponse(
            pod_name=r.pod_name,
            slowest_traces=[asdict(t) for t in r.slowest_traces],  # type: ignore
            total_traces_found=r.total_traces_found,
            note=r.note,
        )
