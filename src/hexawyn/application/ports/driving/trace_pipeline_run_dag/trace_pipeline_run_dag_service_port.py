from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.trace_pipeline_run_dag.trace_pipeline_run_dag_command import (
    TracePipelineRunDAGCommand,
)
from hexawyn.application.ports.driving.trace_pipeline_run_dag.trace_pipeline_run_dag_response import (
    TracePipelineRunDAGResponse,
)


class TracePipelineRunDAGServicePort(ABC):
    @abstractmethod
    def trace_pipeline_run_dag(
        self, command: TracePipelineRunDAGCommand
    ) -> TracePipelineRunDAGResponse: ...
