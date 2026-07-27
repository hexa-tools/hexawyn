from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.pipelines.pipeline_run_logs.command import (
    PipelineRunLogsCommand,
)
from hexawyn.application.use_case.pipelines.pipeline_run_logs.response import (
    PipelineRunLogsResponse,
)


class PipelineRunLogsServicePort(ABC):
    @abstractmethod
    def get_logs(self, command: PipelineRunLogsCommand) -> PipelineRunLogsResponse: ...
