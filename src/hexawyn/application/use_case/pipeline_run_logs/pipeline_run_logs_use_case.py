from __future__ import annotations

from hexawyn.application.ports.driving.pipeline_run_logs.pipeline_run_logs_command import (
    PipelineRunLogsCommand,
)
from hexawyn.application.ports.driving.pipeline_run_logs.pipeline_run_logs_response import (
    PipelineRunLogsResponse,
)
from hexawyn.application.ports.driving.pipeline_run_logs.pipeline_run_logs_service_port import (
    PipelineRunLogsServicePort,
)


class PipelineRunLogsUseCase:
    def __init__(self, service: PipelineRunLogsServicePort) -> None:
        self._svc = service

    def execute(self, cmd: PipelineRunLogsCommand) -> PipelineRunLogsResponse:
        return self._svc.get_logs(cmd)
