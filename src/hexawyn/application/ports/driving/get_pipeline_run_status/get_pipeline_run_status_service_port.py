from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.get_pipeline_run_status.get_pipeline_run_status_command import (
    GetPipelineRunStatusCommand,
)
from hexawyn.application.ports.driving.get_pipeline_run_status.get_pipeline_run_status_response import (
    GetPipelineRunStatusResponse,
)


class GetPipelineRunStatusServicePort(ABC):
    @abstractmethod
    def get_pipeline_run_status(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse: ...
