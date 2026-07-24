from dataclasses import asdict

from hexawyn.application.ports.driven.slow_trace_search_port import SlowTraceSearchPort
from hexawyn.application.use_case.slowest_traces.command import SlowestTracesCommand
from hexawyn.application.use_case.slowest_traces.response import SlowestTracesResponse


class SlowestTracesUseCase:
    def __init__(self, port: SlowTraceSearchPort) -> None:
        self._port = port

    def execute(self, c: SlowestTracesCommand) -> SlowestTracesResponse:
        traces = self._port.find_slowest_traces(limit=c.limit)
        return SlowestTracesResponse(traces=[asdict(t) for t in traces])
