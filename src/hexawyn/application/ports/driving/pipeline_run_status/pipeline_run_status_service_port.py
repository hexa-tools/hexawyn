from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.pipelines.get_pipeline_run_status.command import (
    GetPipelineRunStatusCommand,
)
from hexawyn.application.use_case.pipelines.get_pipeline_run_status.response import (
    GetPipelineRunStatusResponse,
)


class PipelineRunStatusServicePort(ABC):
    @abstractmethod
    def get_pipeline_run_status(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse: ...
