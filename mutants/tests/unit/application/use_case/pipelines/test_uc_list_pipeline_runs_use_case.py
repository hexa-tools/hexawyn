from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driven.tekton_port import PipelineRunInfo
from hexawyn.application.use_case.pipelines.list_pipeline_runs.command import (
    ListPipelineRunsCommand,
)
from hexawyn.application.use_case.pipelines.list_pipeline_runs.list_pipeline_runs_use_case import (  # noqa: E501
    ListPipelineRunsUseCase,
)
from hexawyn.application.use_case.pipelines.list_pipeline_runs.response import (
    ListPipelineRunsResponse,
)


def _run(
    name: str,
    status: str = "Succeeded",
    duration_seconds: int | None = 120,
    start_time: str = "2025-01-15T10:00:00Z",
) -> PipelineRunInfo:
    return PipelineRunInfo(
        name=name,
        status=status,
        start_time=start_time,
        duration=f"{duration_seconds}s" if duration_seconds else None,
        duration_seconds=duration_seconds,
        triggered_by=None,
    )


class TestListPipelineRunsUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.list_pipeline_runs.return_value = []

        use_case = ListPipelineRunsUseCase(tekton_port=port)
        result = use_case.execute(ListPipelineRunsCommand())

        assert isinstance(result, ListPipelineRunsResponse)

    def test_execute_with_runs_computes_stats(self) -> None:
        port = MagicMock()
        port.list_pipeline_runs.return_value = [
            _run("run-1", "Succeeded", 100),
            _run("run-2", "Failed", 200),
            _run("run-3", "Succeeded", 300),
        ]

        use_case = ListPipelineRunsUseCase(tekton_port=port)
        result = use_case.execute(ListPipelineRunsCommand(service_name="api", limit=10))

        assert result.stats.total_runs == 3  # noqa: PLR2004
        assert result.stats.succeeded_runs == 2  # noqa: PLR2004
        assert result.stats.failed_runs == 1

    def test_execute_empty_runs_no_crash(self) -> None:
        port = MagicMock()
        port.list_pipeline_runs.return_value = []

        use_case = ListPipelineRunsUseCase(tekton_port=port)
        result = use_case.execute(ListPipelineRunsCommand())

        assert result.stats.total_runs == 0
        assert result.stats.average_duration_seconds is None

    def test_execute_sorts_by_start_time_desc(self) -> None:
        port = MagicMock()
        port.list_pipeline_runs.return_value = [
            _run("older", start_time="2025-01-15T09:00:00Z"),
            _run("newer", start_time="2025-01-15T10:00:00Z"),
        ]

        use_case = ListPipelineRunsUseCase(tekton_port=port)
        result = use_case.execute(ListPipelineRunsCommand(limit=10))

        assert result.runs[0]["name"] == "newer"

    def test_execute_flags_outliers(self) -> None:
        port = MagicMock()
        port.list_pipeline_runs.return_value = [
            _run("fast", "Succeeded", 10),
            _run("slow", "Succeeded", 500),
            _run("normal", "Succeeded", 10),
        ]

        use_case = ListPipelineRunsUseCase(tekton_port=port)
        result = use_case.execute(ListPipelineRunsCommand(limit=10))

        assert "slow" in result.outliers
        assert "fast" not in result.outliers
