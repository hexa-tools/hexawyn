from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.use_case.pipelines.pipeline_performance_baseline.command import (
    PipelinePerformanceBaselineCommand,
)
from hexawyn.application.use_case.pipelines.pipeline_performance_baseline.pipeline_performance_baseline_use_case import (  # noqa: E501
    PipelinePerformanceBaselineUseCase,
)
from hexawyn.application.use_case.pipelines.pipeline_performance_baseline.response import (
    PipelinePerformanceBaselineResponse,
)


class TestPipelinePerformanceBaselineUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.list_pipeline_runs.return_value = []

        use_case = PipelinePerformanceBaselineUseCase(port=port)
        result = use_case.execute(PipelinePerformanceBaselineCommand(pipeline_name="build"))

        assert isinstance(result, PipelinePerformanceBaselineResponse)
