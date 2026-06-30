from __future__ import annotations

from hexawyn.application.ports.driving.list_pipeline_runs_in_namespace.list_pipeline_runs_in_namespace_command import (
    ListPipelineRunsInNamespaceCommand,
)
from hexawyn.application.ports.driving.list_pipeline_runs_in_namespace.list_pipeline_runs_in_namespace_response import (
    ListPipelineRunsInNamespaceResponse,
)
from hexawyn.application.ports.driving.list_pipeline_runs_in_namespace.list_pipeline_runs_in_namespace_service_port import (
    ListPipelineRunsInNamespaceServicePort,
)


class ListPipelineRunsInNamespaceUseCase:
    """Entry point — depends on the service port abstraction."""

    def __init__(self, service: ListPipelineRunsInNamespaceServicePort) -> None:
        self._service = service

    def execute(
        self, command: ListPipelineRunsInNamespaceCommand
    ) -> ListPipelineRunsInNamespaceResponse:
        return self._service.list_pipeline_runs_in_namespace(command)
