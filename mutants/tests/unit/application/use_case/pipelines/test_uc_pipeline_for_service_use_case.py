from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.pipelines.pipeline_for_service.command import (
    PipelineForServiceCommand,
)
from hexawyn.application.use_case.pipelines.pipeline_for_service.pipeline_for_service_use_case import (  # noqa: E501
    PipelineForUseCaseUseCase,
)
from hexawyn.application.use_case.pipelines.pipeline_for_service.response import (
    PipelineForServiceResponse,
)


class TestPipelineForServiceUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.find_pipelines.return_value = []

        use_case = PipelineForUseCaseUseCase(port=port)
        result = use_case.execute(PipelineForServiceCommand(service_name="api"))

        assert isinstance(result, PipelineForServiceResponse)

    def test_execute_no_pipelines_found(self) -> None:
        port = MagicMock()
        port.find_pipelines.return_value = []

        use_case = PipelineForUseCaseUseCase(port=port)
        result = use_case.execute(PipelineForServiceCommand(service_name="nonexistent"))

        assert result.pipelines_found == 0
