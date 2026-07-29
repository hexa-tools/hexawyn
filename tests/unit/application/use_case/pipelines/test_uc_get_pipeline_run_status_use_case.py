from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.pipelines.get_pipeline_run_status.command import (
    GetPipelineRunStatusCommand,
)
from hexawyn.application.use_case.pipelines.get_pipeline_run_status.get_pipeline_run_status_use_case import (  # noqa: E501
    GetPipelineRunStatusUseCase,
)
from hexawyn.application.use_case.pipelines.get_pipeline_run_status.response import (
    GetPipelineRunStatusResponse,
)


class TestGetPipelineRunStatusUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.list_pods.return_value = []
        use_case = GetPipelineRunStatusUseCase(port=port)
        result = use_case.execute(GetPipelineRunStatusCommand())
        assert isinstance(result, GetPipelineRunStatusResponse)

    def test_execute_empty_data(self) -> None:
        port = MagicMock()
        port.list_pods.return_value = []
        use_case = GetPipelineRunStatusUseCase(port=port)
        result = use_case.execute(GetPipelineRunStatusCommand())
        assert isinstance(result, GetPipelineRunStatusResponse)
