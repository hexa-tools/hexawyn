from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.pipelines.analysis_runs_list.command import (
    AnalysisRunsListCommand,
)
from hexawyn.application.use_case.pipelines.analysis_runs_list.response import (
    AnalysisRunsListResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class AnalysisRunsListServicePort(ABC):
    @abstractmethod
    def list_analysis_runs(self, command: AnalysisRunsListCommand) -> AnalysisRunsListResponse: ...
