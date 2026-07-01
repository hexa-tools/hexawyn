from __future__ import annotations

from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.analysis_runs_list.analysis_runs_list_command import (
    AnalysisRunsListCommand,
)
from hexawyn.application.ports.driving.analysis_runs_list.analysis_runs_list_response import (
    AnalysisRunsListResponse,
)


class AnalysisRunsListServicePort(ABC):
    @abstractmethod
    def list_analysis_runs(self, command: AnalysisRunsListCommand) -> AnalysisRunsListResponse:
        """List AnalysisRuns associated with Rollouts."""
