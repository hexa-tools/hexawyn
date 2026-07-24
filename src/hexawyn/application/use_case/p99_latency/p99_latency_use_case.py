from hexawyn.application.ports.driven.latency_percentile_port import LatencyPercentilePort
from hexawyn.application.use_case.p99_latency.command import P99LatencyCommand
from hexawyn.application.use_case.p99_latency.response import P99LatencyResponse


class P99LatencyUseCase:
    def __init__(self, port: LatencyPercentilePort) -> None:
        self._port = port

    def execute(self, command: P99LatencyCommand) -> P99LatencyResponse:
        return P99LatencyResponse()
