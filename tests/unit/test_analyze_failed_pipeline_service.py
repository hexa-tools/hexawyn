"""Unit tests for AnalyzeFailedPipelineService (mocks TektonPort and PipelineRunLogsPort)."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from hexawyn.application.ports.driving.analyze_failed_pipeline.analyze_failed_pipeline_command import (
    AnalyzeFailedPipelineCommand,
)
from hexawyn.application.service.analyze_failed_pipeline_service import (
    AnalyzeFailedPipelineService,
)
from hexawyn.domain.errors import PipelineNotFoundError


def _task_run(status: str = "Failed") -> dict[str, object]:
    return {
        "name": "run-tests",
        "task_ref": "integration-tests",
        "status": status,
        "start_time": "2024-01-10T15:00:00Z",
        "duration": "10s",
        "failing_step": "integration-tests",
        "failing_step_error": "AssertionError: expected 200 got 500",
    }


class TestAnalyzeFailedPipelineService:
    def test_analyze_returns_response_from_domain_computation(self) -> None:
        tekton_port = MagicMock()
        tekton_port.list_task_runs.return_value = [_task_run()]
        logs_port = MagicMock()
        logs_port.fetch_step_logs.return_value = []
        service = AnalyzeFailedPipelineService(
            tekton_port=tekton_port, pipeline_run_logs_port=logs_port
        )

        response = service.analyze(AnalyzeFailedPipelineCommand(pipeline_name="deploy-payment-v3"))

        assert response.pipeline_name == "deploy-payment-v3"
        assert response.pipeline_run_found is True
        assert len(response.failures) == 1
        assert response.failures[0]["failure_type"] == "regression"
        tekton_port.list_task_runs.assert_called_once()
        logs_port.fetch_step_logs.assert_called_once()

    def test_analyze_propagates_pipeline_not_found(self) -> None:
        """TC4: PipelineRun not found → clear error with suggestion to check pipeline name."""
        tekton_port = MagicMock()
        tekton_port.list_task_runs.side_effect = PipelineNotFoundError(pipeline_name="ghost")
        logs_port = MagicMock()
        service = AnalyzeFailedPipelineService(
            tekton_port=tekton_port, pipeline_run_logs_port=logs_port
        )

        with pytest.raises(PipelineNotFoundError) as exc_info:
            service.analyze(AnalyzeFailedPipelineCommand(pipeline_name="ghost"))

        assert "ghost" in str(exc_info.value)
