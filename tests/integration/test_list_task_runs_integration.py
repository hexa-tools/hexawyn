"""Integration tests for list_task_runs — require a real Tekton cluster via KUBECONFIG."""

from unittest.mock import MagicMock

import pytest
from hexawyn.adapters.secondary.vanilla.vanilla_adapter import VanillaAdapter
from hexawyn.application.ports.driven.tekton_port import TektonPort
from hexawyn.application.use_case.pipelines.list_task_runs.command import ListTaskRunsCommand
from hexawyn.application.use_case.pipelines.list_task_runs.list_task_runs_use_case import (
    ListTaskRunsUseCase,
)
from hexawyn.domain.errors import PipelineNotFoundError


class TestListTaskRunsUseCaseIntegration:
    @pytest.mark.integration
    def test_full_stack_with_mock_tekton_port_returns_sorted_runs(self) -> None:
        from hexawyn.application.ports.driven.tekton_port import TaskRunInfo

        run_old: TaskRunInfo = {
            "name": "build-deploy-clone-repo",
            "task_ref": "clone-repo",
            "status": "Succeeded",
            "start_time": "2024-01-01T10:00:00Z",
            "duration": "12s",
            "failing_step": None,
            "failing_step_error": None,
        }
        run_new: TaskRunInfo = {
            "name": "build-deploy-unit-tests",
            "task_ref": "unit-tests",
            "status": "Failed",
            "start_time": "2024-01-01T10:00:15Z",
            "duration": "30s",
            "failing_step": "run-tests",
            "failing_step_error": "exit code 1",
        }
        run_none: TaskRunInfo = {
            "name": "build-deploy-build-image",
            "task_ref": "build-image",
            "status": "NotStarted",
            "start_time": None,
            "duration": None,
            "failing_step": None,
            "failing_step_error": None,
        }

        mock_port = MagicMock(spec=TektonPort)
        mock_port.list_task_runs.return_value = [run_old, run_none, run_new]

        use_case = ListTaskRunsUseCase(tekton_port=mock_port)
        response = use_case.execute(
            ListTaskRunsCommand(pipeline_name="build-deploy", namespace="ci")
        )

        assert len(response.task_runs) == 3  # noqa: PLR2004
        assert response.task_runs[0]["name"] == "build-deploy-unit-tests"
        assert response.task_runs[1]["name"] == "build-deploy-clone-repo"
        assert response.task_runs[2]["name"] == "build-deploy-build-image"

    @pytest.mark.integration
    def test_full_stack_pipeline_not_found_propagates_to_use_case(self) -> None:
        mock_port = MagicMock(spec=TektonPort)
        mock_port.list_task_runs.side_effect = PipelineNotFoundError(
            pipeline_name="missing-pipeline"
        )

        use_case = ListTaskRunsUseCase(tekton_port=mock_port)

        with pytest.raises(PipelineNotFoundError) as exc_info:
            use_case.execute(ListTaskRunsCommand(pipeline_name="missing-pipeline", namespace="ci"))

        assert exc_info.value.pipeline_name == "missing-pipeline"

    @pytest.mark.integration
    def test_vanilla_adapter_implements_tekton_port(self) -> None:
        adapter = VanillaAdapter("test-cluster")
        assert isinstance(adapter, TektonPort)
