from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driven.tekton_port import TaskRunInfo
from hexawyn.application.use_case.pipelines.list_task_runs.command import (
    ListTaskRunsCommand,
)
from hexawyn.application.use_case.pipelines.list_task_runs.list_task_runs_use_case import (
    ListTaskRunsUseCase,
)
from hexawyn.application.use_case.pipelines.list_task_runs.response import (
    ListTaskRunsResponse,
)


def _task_run(name: str, start_time: str | None = "2025-01-15T10:00:00Z") -> TaskRunInfo:
    return TaskRunInfo(
        name=name,
        task_ref="build",
        status="Succeeded",
        start_time=start_time,
        duration="5m",
        failing_step=None,
        failing_step_error=None,
    )


class TestListTaskRunsUseCase:
    def test_execute_returns_list_task_runs_response(self) -> None:
        port = MagicMock()
        port.list_task_runs.return_value = []

        use_case = ListTaskRunsUseCase(tekton_port=port)
        result = use_case.execute(ListTaskRunsCommand(pipeline_name="build-pipeline"))

        assert isinstance(result, ListTaskRunsResponse)

    def test_execute_returns_task_runs_from_port(self) -> None:
        tr = _task_run("build-run-1")
        port = MagicMock()
        port.list_task_runs.return_value = [tr]

        use_case = ListTaskRunsUseCase(tekton_port=port)
        result = use_case.execute(ListTaskRunsCommand(pipeline_name="build-pipeline"))

        assert len(result.task_runs) == 1
        assert result.task_runs[0]["name"] == "build-run-1"

    def test_execute_sorts_by_start_time_desc(self) -> None:
        older = _task_run("older", "2025-01-15T09:00:00Z")
        newer = _task_run("newer", "2025-01-15T10:00:00Z")
        port = MagicMock()
        port.list_task_runs.return_value = [older, newer]

        use_case = ListTaskRunsUseCase(tekton_port=port)
        result = use_case.execute(ListTaskRunsCommand(pipeline_name="build-pipeline"))

        assert result.task_runs[0]["name"] == "newer"
        assert result.task_runs[1]["name"] == "older"

    def test_execute_nulls_sorted_last(self) -> None:
        with_time = _task_run("with-time", "2025-01-15T10:00:00Z")
        null_time = _task_run("null-time", None)
        port = MagicMock()
        port.list_task_runs.return_value = [null_time, with_time]

        use_case = ListTaskRunsUseCase(tekton_port=port)
        result = use_case.execute(ListTaskRunsCommand(pipeline_name="build-pipeline"))

        assert result.task_runs[0]["name"] == "with-time"

    def test_execute_passes_pipeline_name_to_port(self) -> None:
        port = MagicMock()
        port.list_task_runs.return_value = []

        use_case = ListTaskRunsUseCase(tekton_port=port)
        use_case.execute(
            ListTaskRunsCommand(pipeline_name="deploy-pipeline", namespace="production")
        )

        port.list_task_runs.assert_called_once_with(
            pipeline_name="deploy-pipeline", namespace="production"
        )

    def test_execute_with_null_start_times(self) -> None:
        tr1 = _task_run("run-1", None)
        tr2 = _task_run("run-2", "2025-01-15T10:00:00Z")
        port = MagicMock()
        port.list_task_runs.return_value = [tr1, tr2]

        use_case = ListTaskRunsUseCase(tekton_port=port)
        result = use_case.execute(ListTaskRunsCommand(pipeline_name="build"))

        assert result.task_runs[0]["name"] == "run-2"
