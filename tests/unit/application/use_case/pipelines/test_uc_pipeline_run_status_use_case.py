from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.pipelines.get_pipeline_run_status.command import (
    GetPipelineRunStatusCommand,
)
from hexawyn.application.use_case.pipelines.get_pipeline_run_status.response import (
    GetPipelineRunStatusResponse,
)
from hexawyn.application.use_case.pipelines.pipeline_run_status.pipeline_run_status_use_case import (  # noqa: E501
    PipelineRunStatusUseCase,
)


class TestPipelineRunStatusUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.list_pipeline_runs.return_value = []

        use_case = PipelineRunStatusUseCase(port=port)
        result = use_case.get_pipeline_run_status(GetPipelineRunStatusCommand(namespace="default"))

        assert isinstance(result, GetPipelineRunStatusResponse)
