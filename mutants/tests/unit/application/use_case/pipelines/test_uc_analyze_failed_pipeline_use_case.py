from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.pipelines.analyze_failed_pipeline.analyze_failed_pipeline_use_case import (  # noqa: E501
    AnalyzeFailedPipelineUseCase,
)
from hexawyn.application.use_case.pipelines.analyze_failed_pipeline.command import (
    AnalyzeFailedPipelineCommand,
)
from hexawyn.application.use_case.pipelines.analyze_failed_pipeline.response import (
    AnalyzeFailedPipelineResponse,
)


class TestAnalyzeFailedPipelineUseCase:
    def test_execute_returns_response(self) -> None:
        tekton = MagicMock()
        tekton.list_task_runs.return_value = []
        logs_port = MagicMock()
        logs_port.fetch_step_logs.return_value = []

        use_case = AnalyzeFailedPipelineUseCase(
            tekton_port=tekton,
            pipeline_run_logs_port=logs_port,
        )
        result = use_case.execute(
            AnalyzeFailedPipelineCommand(
                pipeline_name="build-pipeline",
                namespace="default",
            )
        )

        assert isinstance(result, AnalyzeFailedPipelineResponse)
        assert result.pipeline_name == "build-pipeline"

    def test_execute_pipeline_not_found(self) -> None:
        tekton = MagicMock()
        tekton.list_task_runs.return_value = []
        logs_port = MagicMock()
        logs_port.fetch_step_logs.return_value = []

        use_case = AnalyzeFailedPipelineUseCase(
            tekton_port=tekton,
            pipeline_run_logs_port=logs_port,
        )
        result = use_case.execute(
            AnalyzeFailedPipelineCommand(
                pipeline_name="nonexistent",
                namespace="default",
            )
        )

        assert isinstance(result, AnalyzeFailedPipelineResponse)
        assert result.pipeline_run_found is False
