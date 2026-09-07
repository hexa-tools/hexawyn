from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.pipelines.analyze_failed_pipeline.command import (
    AnalyzeFailedPipelineCommand,
)
from hexawyn.application.use_case.pipelines.analyze_failed_pipeline.response import (
    AnalyzeFailedPipelineResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class AnalyzeFailedPipelineServicePort(ABC):
    @abstractmethod
    def analyze(self, command: AnalyzeFailedPipelineCommand) -> AnalyzeFailedPipelineResponse: ...
