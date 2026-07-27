from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.use_case.pipelines.analysis_runs_list.command import (
    AnalysisRunsListCommand,
)
from hexawyn.application.use_case.pipelines.analysis_runs_list.response import (
    AnalysisRunsListResponse,
)


class AnalysisRunsListServicePort(ABC):
    @abstractmethod
    def list_analysis_runs(self, command: AnalysisRunsListCommand) -> AnalysisRunsListResponse: ...
