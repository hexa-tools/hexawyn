from __future__ import annotations

from hexawyn.application.ports.driving.list_pipeline_runs.list_pipeline_runs_command import (
    ListPipelineRunsCommand,
)
from hexawyn.application.ports.driving.list_pipeline_runs.list_pipeline_runs_response import (
    ListPipelineRunsResponse,
)
from hexawyn.application.ports.driving.list_pipeline_runs.list_pipeline_runs_service_port import (
    ListPipelineRunsServicePort,
)


class ListPipelineRunsUseCase:
    """Entry point — depends on the service port abstraction."""

    def __init__(self, service: ListPipelineRunsServicePort) -> None:
        self._service = service

    def execute(self, command: ListPipelineRunsCommand) -> ListPipelineRunsResponse:
        return self._service.list_pipeline_runs(command)
