from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.pipelines.pipeline_run_logs.command import (
    PipelineRunLogsCommand,
)
from hexawyn.application.use_case.pipelines.pipeline_run_logs.pipeline_run_logs_use_case import (  # noqa: E501
    PipelineRunLogsUseCase,
)
from hexawyn.application.use_case.pipelines.pipeline_run_logs.response import (
    PipelineRunLogsResponse,
)


class TestPipelineRunLogsUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.fetch_step_logs.return_value = []

        use_case = PipelineRunLogsUseCase(port=port)
        result = use_case.execute(
            PipelineRunLogsCommand(
                pipeline_run_name="run-1",
                namespace="default",
            )
        )

        assert isinstance(result, PipelineRunLogsResponse)
        assert result.pipeline_run_name == "run-1"

    def test_execute_pipeline_not_found(self) -> None:
        port = MagicMock()
        port.fetch_step_logs.return_value = []

        use_case = PipelineRunLogsUseCase(port=port)
        result = use_case.execute(
            PipelineRunLogsCommand(
                pipeline_run_name="nonexistent",
                namespace="default",
            )
        )

        assert result.pipeline_run_found is False
