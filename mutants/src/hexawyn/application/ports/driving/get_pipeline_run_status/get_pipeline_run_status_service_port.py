from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.pipelines.get_pipeline_run_status.command import (
    GetPipelineRunStatusCommand,
)
from hexawyn.application.use_case.pipelines.get_pipeline_run_status.response import (
    GetPipelineRunStatusResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class GetPipelineRunStatusServicePort(ABC):
    @abstractmethod
    def get_pipeline_run_status(
        self, command: GetPipelineRunStatusCommand
    ) -> GetPipelineRunStatusResponse: ...
