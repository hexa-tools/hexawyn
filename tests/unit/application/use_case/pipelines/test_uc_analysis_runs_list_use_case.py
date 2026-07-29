from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.pipelines.analysis_runs_list.analysis_runs_list_use_case import (  # noqa: E501
    AnalysisRunsListUseCase,
)
from hexawyn.application.use_case.pipelines.analysis_runs_list.command import (
    AnalysisRunsListCommand,
)
from hexawyn.application.use_case.pipelines.analysis_runs_list.response import (
    AnalysisRunsListResponse,
)


class TestAnalysisRunsListUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.list_analysis_runs.return_value = []

        use_case = AnalysisRunsListUseCase(rollouts_port=port)
        result = use_case.execute(AnalysisRunsListCommand())

        assert isinstance(result, AnalysisRunsListResponse)

    def test_execute_filters_by_rollout_name(self) -> None:
        port = MagicMock()
        port.list_analysis_runs.return_value = []

        use_case = AnalysisRunsListUseCase(rollouts_port=port)
        result = use_case.execute(
            AnalysisRunsListCommand(
                namespace="default",
                rollout_name="canary-deploy",
            )
        )

        port.list_analysis_runs.assert_called_once_with(
            namespace="default",
            rollout_name="canary-deploy",
        )
        assert isinstance(result, AnalysisRunsListResponse)
