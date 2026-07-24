from hexawyn.application.ports.driven.pod_logs_port import PodLogsPort
from hexawyn.application.use_case.analyze_pod_logs.command import AnalyzePodLogsCommand
from hexawyn.application.use_case.analyze_pod_logs.response import AnalyzePodLogsResponse


class AnalyzePodLogsUseCase:
    def __init__(self, port: PodLogsPort) -> None:
        self._port = port

    def execute(self, command: AnalyzePodLogsCommand) -> AnalyzePodLogsResponse:
        return AnalyzePodLogsResponse()
