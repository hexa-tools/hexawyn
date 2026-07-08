from __future__ import annotations

from hexawyn.application.ports.driving.get_pipeline_run_status.get_pipeline_run_status_command import (
    GetPipelineRunStatusCommand,
)
from hexawyn.application.ports.driving.get_pipeline_run_status.get_pipeline_run_status_response import (
    GetPipelineRunStatusResponse,
)
from hexawyn.application.ports.driving.get_pipeline_run_status.get_pipeline_run_status_service_port import (
    GetPipelineRunStatusServicePort,
)


class GetPipelineRunStatusUseCase:
    def __init__(self, service: GetPipelineRunStatusServicePort) -> None:
        self._service = service

    def execute(self, command: GetPipelineRunStatusCommand) -> GetPipelineRunStatusResponse:
        return self._service.get_pipeline_run_status(command)
