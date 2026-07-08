from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.pipeline_run_logs.pipeline_run_logs_command import (
    PipelineRunLogsCommand,
)
from hexawyn.application.ports.driving.pipeline_run_logs.pipeline_run_logs_response import (
    PipelineRunLogsResponse,
)


class PipelineRunLogsServicePort(ABC):
    @abstractmethod
    def get_logs(self, command: PipelineRunLogsCommand) -> PipelineRunLogsResponse: ...
