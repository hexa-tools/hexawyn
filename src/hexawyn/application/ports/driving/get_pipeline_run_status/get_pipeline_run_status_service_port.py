from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.get_pipeline_run_status.command import (
    GetPipelineRunStatusCommand,
)
from hexawyn.application.use_case.get_pipeline_run_status.response import (
    GetPipelineRunStatusResponse,
)


class GetPipelineRunStatusServicePort(ABC):
    @abstractmethod
    def get_pipeline_run_status(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse: ...
