from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.rollouts_port import RolloutsPort
from hexawyn.application.use_case.analysis_runs_list.command import (
    AnalysisRunsListCommand,
)
from hexawyn.application.use_case.analysis_runs_list.response import (
    AnalysisRunsListResponse,
)
from hexawyn.application.ports.driving.analysis_runs_list.analysis_runs_list_service_port import (
    AnalysisRunsListServicePort,
)


class AnalysisRunsListService(AnalysisRunsListServicePort):
    def __init__(self, rollouts_port: RolloutsPort) -> None:
        self._rollouts = rollouts_port

    def list_analysis_runs(self, command: AnalysisRunsListCommand) -> AnalysisRunsListResponse:
        runs = self._rollouts.list_analysis_runs(
            namespace=command.namespace,
            rollout_name=command.rollout_name,
        )
        return AnalysisRunsListResponse(
            analysis_runs=[asdict(r) for r in runs],
        )
