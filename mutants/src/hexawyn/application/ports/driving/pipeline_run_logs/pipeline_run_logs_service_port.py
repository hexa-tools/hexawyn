from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.pipelines.pipeline_run_logs.command import (
    PipelineRunLogsCommand,
)
from hexawyn.application.use_case.pipelines.pipeline_run_logs.response import (
    PipelineRunLogsResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class PipelineRunLogsServicePort(ABC):
    @abstractmethod
    def get_logs(self, command: PipelineRunLogsCommand) -> PipelineRunLogsResponse: ...
