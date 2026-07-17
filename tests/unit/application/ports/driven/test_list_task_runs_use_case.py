from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driven.tekton_port import TaskRunInfo, TektonPort
from hexawyn.application.ports.driving.list_task_runs.list_task_runs_command import (
    ListTaskRunsCommand,
)
from hexawyn.application.ports.driving.list_task_runs.list_task_runs_response import (
    ListTaskRunsResponse,
)
from hexawyn.application.ports.driving.list_task_runs.list_task_runs_service_port import (
    ListTaskRunsServicePort,
)
from hexawyn.application.service.list_task_runs_service import ListTaskRunsService
from hexawyn.application.use_case.list_task_runs.list_task_runs_use_case import (
    ListTaskRunsUseCase,
)
from hexawyn.domain.errors import PipelineNotFoundError

_SUCCEEDED_RUN: TaskRunInfo = {
    "name": "build-deploy-clone-repo-abc",
    "task_ref": "clone-repo",
    "status": "Succeeded",
    "start_time": "2024-01-01T10:00:00Z",
    "duration": "12s",
    "failing_step": None,
    "failing_step_error": None,
}

_FAILED_RUN: TaskRunInfo = {
    "name": "build-deploy-unit-tests-xyz",
    "task_ref": "unit-tests",
    "status": "Failed",
    "start_time": "2024-01-01T10:00:15Z",
    "duration": "30s",
    "failing_step": "run-tests",
    "failing_step_error": "exit code 1",
}

_NOT_STARTED_RUN: TaskRunInfo = {
    "name": "build-deploy-build-image-def",
    "task_ref": "build-image",
    "status": "NotStarted",
    "start_time": None,
    "duration": None,
    "failing_step": None,
    "failing_step_error": None,
}

_RUNNING_RUN: TaskRunInfo = {
    "name": "build-deploy-lint-running",
    "task_ref": "lint",
    "status": "Running",
    "start_time": "2024-01-01T10:01:00Z",
    "duration": None,
    "failing_step": None,
    "failing_step_error": None,
}


class TestListTaskRunsCommand:
    def test_is_frozen(self) -> None:
        cmd = ListTaskRunsCommand(pipeline_name="build-deploy", namespace="default")
        with pytest.raises(AttributeError):
            cmd.pipeline_name = "other"  # type: ignore[misc]

    def test_fields(self) -> None:
        cmd = ListTaskRunsCommand(pipeline_name="build-deploy", namespace="production")
        assert cmd.pipeline_name == "build-deploy"
        assert cmd.namespace == "production"


class TestListTaskRunsResponse:
    def test_default_task_runs_is_empty(self) -> None:
        resp = ListTaskRunsResponse()
        assert resp.task_runs == []

    def test_accepts_task_runs_list(self) -> None:
        resp = ListTaskRunsResponse(task_runs=[_SUCCEEDED_RUN])
        assert len(resp.task_runs) == 1
        assert resp.task_runs[0]["name"] == "build-deploy-clone-repo-abc"


class TestListTaskRunsServicePort:
    def test_is_abstract(self) -> None:
        from abc import ABC

        assert issubclass(ListTaskRunsServicePort, ABC)

    def test_cannot_instantiate_directly(self) -> None:
        with pytest.raises(TypeError):
            ListTaskRunsServicePort()  # type: ignore[abstract]


class TestListTaskRunsUseCase:
    def test_delegates_to_service_port(self) -> None:
        fake_service = MagicMock(spec=ListTaskRunsServicePort)
        expected = ListTaskRunsResponse(task_runs=[_FAILED_RUN])
        fake_service.list_task_runs.return_value = expected

        use_case = ListTaskRunsUseCase(service=fake_service)
        result = use_case.execute(
            ListTaskRunsCommand(pipeline_name="build-deploy", namespace="default")
        )

        assert result.task_runs == [_FAILED_RUN]
        fake_service.list_task_runs.assert_called_once()

    def test_passes_command_to_service(self) -> None:
        fake_service = MagicMock(spec=ListTaskRunsServicePort)
        fake_service.list_task_runs.return_value = ListTaskRunsResponse()

        cmd = ListTaskRunsCommand(pipeline_name="build-deploy", namespace="production")
        use_case = ListTaskRunsUseCase(service=fake_service)
        use_case.execute(cmd)

        fake_service.list_task_runs.assert_called_once_with(cmd)


class TestListTaskRunsService:
    def test_implements_service_port(self) -> None:
        service = ListTaskRunsService(tekton_port=MagicMock())
        assert isinstance(service, ListTaskRunsServicePort)

    # TC1: pipeline with a failed TaskRun exposes step name and error message
    def test_failed_task_run_exposes_failing_step_and_error(self) -> None:
        tekton = MagicMock(spec=TektonPort)
        tekton.list_task_runs.return_value = [_SUCCEEDED_RUN, _FAILED_RUN, _NOT_STARTED_RUN]
        service = ListTaskRunsService(tekton_port=tekton)

        result = service.list_task_runs(
            ListTaskRunsCommand(pipeline_name="build-deploy", namespace="default")
        )

        failed = next(r for r in result.task_runs if r["status"] == "Failed")
        assert failed["failing_step"] == "run-tests"
        assert failed["failing_step_error"] == "exit code 1"

    # TC2: all TaskRuns succeeded → no failing step info on any entry
    def test_all_succeeded_no_failing_step(self) -> None:
        second: TaskRunInfo = {
            "name": "build-deploy-lint-abc",
            "task_ref": "lint",
            "status": "Succeeded",
            "start_time": "2024-01-01T10:01:00Z",
            "duration": "8s",
            "failing_step": None,
            "failing_step_error": None,
        }
        tekton = MagicMock(spec=TektonPort)
        tekton.list_task_runs.return_value = [_SUCCEEDED_RUN, second]
        service = ListTaskRunsService(tekton_port=tekton)

        result = service.list_task_runs(
            ListTaskRunsCommand(pipeline_name="build-deploy", namespace="default")
        )

        assert all(r["failing_step"] is None for r in result.task_runs)

    # TC3: running TaskRun has start_time but no duration
    def test_running_task_run_has_start_time_and_no_duration(self) -> None:
        tekton = MagicMock(spec=TektonPort)
        tekton.list_task_runs.return_value = [_RUNNING_RUN]
        service = ListTaskRunsService(tekton_port=tekton)

        result = service.list_task_runs(
            ListTaskRunsCommand(pipeline_name="build-deploy", namespace="default")
        )

        running = result.task_runs[0]
        assert running["status"] == "Running"
        assert running["start_time"] is not None
        assert running["duration"] is None

    # TC4: PipelineNotFoundError from the port propagates — service never catches
    def test_pipeline_not_found_propagates(self) -> None:
        tekton = MagicMock(spec=TektonPort)
        tekton.list_task_runs.side_effect = PipelineNotFoundError(pipeline_name="ghost-pipeline")
        service = ListTaskRunsService(tekton_port=tekton)

        with pytest.raises(PipelineNotFoundError):
            service.list_task_runs(
                ListTaskRunsCommand(pipeline_name="ghost-pipeline", namespace="default")
            )

    # Ordering: most recent start_time first, NotStarted (None) last
    def test_sorted_by_start_time_descending(self) -> None:
        tekton = MagicMock(spec=TektonPort)
        tekton.list_task_runs.return_value = [_SUCCEEDED_RUN, _FAILED_RUN, _NOT_STARTED_RUN]
        service = ListTaskRunsService(tekton_port=tekton)

        result = service.list_task_runs(
            ListTaskRunsCommand(pipeline_name="build-deploy", namespace="default")
        )

        # _FAILED_RUN  → 10:00:15
        # _SUCCEEDED_RUN → 10:00:00
        # _NOT_STARTED_RUN → None (last)
        times = [r["start_time"] for r in result.task_runs]
        assert times == ["2024-01-01T10:00:15Z", "2024-01-01T10:00:00Z", None]
