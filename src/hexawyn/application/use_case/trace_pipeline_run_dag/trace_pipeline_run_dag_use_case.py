from __future__ import annotations

from hexawyn.application.ports.driving.trace_pipeline_run_dag.trace_pipeline_run_dag_command import (
    TracePipelineRunDAGCommand,
)
from hexawyn.application.ports.driving.trace_pipeline_run_dag.trace_pipeline_run_dag_response import (
    TracePipelineRunDAGResponse,
)
from hexawyn.application.ports.driving.trace_pipeline_run_dag.trace_pipeline_run_dag_service_port import (
    TracePipelineRunDAGServicePort,
)


class TracePipelineRunDAGUseCase:
    def __init__(self, service: TracePipelineRunDAGServicePort) -> None:
        self._service = service

    def execute(self, command: TracePipelineRunDAGCommand) -> TracePipelineRunDAGResponse:
        return self._service.trace_pipeline_run_dag(command)
