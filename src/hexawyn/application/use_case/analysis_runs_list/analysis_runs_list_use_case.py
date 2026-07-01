from __future__ import annotations

from hexawyn.application.ports.driving.analysis_runs_list.analysis_runs_list_command import (
    AnalysisRunsListCommand,
)
from hexawyn.application.ports.driving.analysis_runs_list.analysis_runs_list_response import (
    AnalysisRunsListResponse,
)
from hexawyn.application.ports.driving.analysis_runs_list.analysis_runs_list_service_port import (
    AnalysisRunsListServicePort,
)


class AnalysisRunsListUseCase:
    def __init__(self, service: AnalysisRunsListServicePort) -> None:
        self._service = service

    def execute(self, command: AnalysisRunsListCommand) -> AnalysisRunsListResponse:
        return self._service.list_analysis_runs(command)
