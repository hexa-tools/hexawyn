from __future__ import annotations

from datetime import UTC, datetime, timedelta
from unittest.mock import MagicMock

from hexawyn.application.use_case.pipelines.get_pipeline_run_status.command import (
    GetPipelineRunStatusCommand,
)
from hexawyn.application.use_case.pipelines.get_pipeline_run_status.response import (
    GetPipelineRunStatusResponse,
)
from hexawyn.application.use_case.pipelines.pipeline_run_status.pipeline_run_status_use_case import (  # noqa: E501
    PipelineRunStatusUseCase,
    _filter_by_window,
)


class TestPipelineRunStatusUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.list_pipeline_runs.return_value = []

        use_case = PipelineRunStatusUseCase(port=port)
        result = use_case.get_pipeline_run_status(GetPipelineRunStatusCommand(namespace="default"))

        assert isinstance(result, GetPipelineRunStatusResponse)

    def test_execute_with_runs(self) -> None:
        port = MagicMock()
        recent = (datetime.now(UTC) - timedelta(hours=2)).isoformat()
        port.list_pipeline_runs.return_value = [
            {
                "name": "run-1",
                "status": "Succeeded",
                "start_time": recent,
                "duration_seconds": 300,
                "failure_reason": None,
                "pipeline_ref": "build",
            },
            {
                "name": "run-2",
                "status": "Failed",
                "start_time": recent,
                "duration_seconds": 120,
                "failure_reason": "test failure",
                "pipeline_ref": "build",
            },
            {
                "name": "run-3",
                "status": "Running",
                "start_time": recent,
                "duration_seconds": None,
                "failure_reason": None,
                "pipeline_ref": "deploy",
            },
        ]

        use_case = PipelineRunStatusUseCase(port=port)
        result = use_case.get_pipeline_run_status(GetPipelineRunStatusCommand(namespace="default"))

        assert isinstance(result, GetPipelineRunStatusResponse)
        assert result.report is not None
        expected_total = 3
        assert result.report.succeeded == 1
        assert result.report.failed == 1
        assert result.report.running == 1
        assert result.report.total == expected_total

    def test_execute_with_runs_outside_window(self) -> None:
        port = MagicMock()
        port.list_pipeline_runs.return_value = [
            {
                "name": "old-run",
                "status": "Succeeded",
                "start_time": "2020-01-01T00:00:00Z",
                "duration_seconds": 300,
                "failure_reason": None,
                "pipeline_ref": "build",
            },
        ]

        use_case = PipelineRunStatusUseCase(port=port)
        result = use_case.get_pipeline_run_status(
            GetPipelineRunStatusCommand(namespace="default", hours_window=1)
        )

        assert result.report is not None
        assert result.report.total == 0

    def test_filter_by_window_keeps_runs_with_none_start_time(self) -> None:
        runs = [
            {
                "name": "no-start",
                "status": "Running",
                "start_time": None,
                "duration_seconds": None,
                "failure_reason": None,
                "pipeline_ref": "deploy",
            },
        ]

        filtered = _filter_by_window(runs, hours=24)

        assert len(filtered) == 1
        assert filtered[0]["name"] == "no-start"

    def test_filter_by_window_skips_invalid_start_time(self) -> None:
        runs = [
            {
                "name": "bad-time",
                "status": "Succeeded",
                "start_time": "not-a-valid-iso-date",
                "duration_seconds": 300,
                "failure_reason": None,
                "pipeline_ref": "build",
            },
        ]

        filtered = _filter_by_window(runs, hours=24)

        assert len(filtered) == 0

    def test_execute_with_none_start_time_and_cancelled_status(self) -> None:
        port = MagicMock()
        port.list_pipeline_runs.return_value = [
            {
                "name": "run-cancelled",
                "status": "Cancelled",
                "start_time": None,
                "duration_seconds": None,
                "failure_reason": "timeout",
                "pipeline_ref": "build",
            },
        ]

        use_case = PipelineRunStatusUseCase(port=port)
        result = use_case.get_pipeline_run_status(GetPipelineRunStatusCommand(namespace="default"))

        assert result.report is not None
        assert result.report.cancelled == 1
        assert result.report.total == 1
