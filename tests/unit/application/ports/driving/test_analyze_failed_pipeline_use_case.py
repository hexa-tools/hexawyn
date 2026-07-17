from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driving.analyze_failed_pipeline.analyze_failed_pipeline_command import (
    AnalyzeFailedPipelineCommand,
)
from hexawyn.application.ports.driving.analyze_failed_pipeline.analyze_failed_pipeline_response import (
    AnalyzeFailedPipelineResponse,
)
from hexawyn.application.ports.driving.analyze_failed_pipeline.analyze_failed_pipeline_service_port import (
    AnalyzeFailedPipelineServicePort,
)
from hexawyn.application.use_case.analyze_failed_pipeline.analyze_failed_pipeline_use_case import (
    AnalyzeFailedPipelineUseCase,
)


class TestAnalyzeFailedPipelineUseCase:
    def test_execute_delegates_to_service(self) -> None:
        service = MagicMock(spec=AnalyzeFailedPipelineServicePort)
        expected = AnalyzeFailedPipelineResponse(pipeline_name="deploy-payment-v3")
        service.analyze.return_value = expected
        use_case = AnalyzeFailedPipelineUseCase(service=service)
        command = AnalyzeFailedPipelineCommand(pipeline_name="deploy-payment-v3")

        result = use_case.execute(command)

        service.analyze.assert_called_once_with(command)
        assert result is expected
