from __future__ import annotations

from hexawyn.application.ports.driving.analyze_pod_logs.analyze_pod_logs_command import (
    AnalyzePodLogsCommand,
)
from hexawyn.application.ports.driving.analyze_pod_logs.analyze_pod_logs_response import (
    AnalyzePodLogsResponse,
)
from hexawyn.application.ports.driving.analyze_pod_logs.analyze_pod_logs_service_port import (
    AnalyzePodLogsServicePort,
)


class AnalyzePodLogsUseCase:
    def __init__(self, service: AnalyzePodLogsServicePort) -> None:
        self._svc = service

    def execute(self, command: AnalyzePodLogsCommand) -> AnalyzePodLogsResponse:
        return self._svc.analyze(command)
