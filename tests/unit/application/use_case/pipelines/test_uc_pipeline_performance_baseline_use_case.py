from __future__ import annotations

from unittest.mock import MagicMock, patch

from hexawyn.application.use_case.pipelines.pipeline_performance_baseline.command import (
    PipelinePerformanceBaselineCommand,
)
from hexawyn.application.use_case.pipelines.pipeline_performance_baseline.pipeline_performance_baseline_use_case import (  # noqa: E501
    PipelinePerformanceBaselineUseCase,
)
from hexawyn.application.use_case.pipelines.pipeline_performance_baseline.response import (
    PipelinePerformanceBaselineResponse,
)
from hexawyn.domain.models.pipeline_baseline import PipelineBaselineResult


class TestPipelinePerformanceBaselineUseCase:
    def test_execute_returns_response(self) -> None:
        port = MagicMock()
        port.list_pipeline_runs.return_value = []

        use_case = PipelinePerformanceBaselineUseCase(port=port)
        result = use_case.execute(PipelinePerformanceBaselineCommand(pipeline_name="build"))

        assert isinstance(result, PipelinePerformanceBaselineResponse)

    def test_execute_with_task_runs_returns_from_result(self) -> None:
        port = MagicMock()
        port.list_pipeline_runs.return_value = [{"name": "run-1"}]
        port.list_task_runs_for_pipeline.return_value = []

        use_case = PipelinePerformanceBaselineUseCase(port=port)
        result = use_case.execute(PipelinePerformanceBaselineCommand(pipeline_name="build"))

        assert isinstance(result, PipelinePerformanceBaselineResponse)
        assert result.pipeline == "build"

    def test_execute_continues_on_task_runs_failure(self) -> None:
        port = MagicMock()
        port.list_pipeline_runs.return_value = [{"name": "run-1"}]
        port.list_task_runs_for_pipeline.side_effect = Exception("boom")

        use_case = PipelinePerformanceBaselineUseCase(port=port)
        result = use_case.execute(PipelinePerformanceBaselineCommand(pipeline_name="build"))

        assert isinstance(result, PipelinePerformanceBaselineResponse)

    def test_execute_handles_outer_exception(self) -> None:
        port = MagicMock()
        port.list_pipeline_runs.side_effect = Exception("boom")

        use_case = PipelinePerformanceBaselineUseCase(port=port)
        result = use_case.execute(PipelinePerformanceBaselineCommand(pipeline_name="build"))

        assert result.error == "boom"

    def test_execute_with_compute_baseline_result_uses_from_result(self) -> None:
        port = MagicMock()
        port.list_pipeline_runs.return_value = [{"name": "run-1"}]
        port.list_task_runs_for_pipeline.return_value = []

        fake_result = PipelineBaselineResult(
            pipeline="build",
            runs_analyzed=1,
            requested_limit=30,
            trend="degrading",
            trend_pct=15.4,
            bottleneck_stage="test",
            note="All good",
        )

        with patch(
            "hexawyn.application.use_case.pipelines.pipeline_performance_baseline.pipeline_performance_baseline_use_case.compute_baseline",  # noqa: E501
            return_value=fake_result,
        ):
            use_case = PipelinePerformanceBaselineUseCase(port=port)
            result = use_case.execute(PipelinePerformanceBaselineCommand(pipeline_name="build"))

        assert isinstance(result, PipelinePerformanceBaselineResponse)
        assert result.pipeline == "build"
        assert result.runs_analyzed == 1
        assert result.trend == "degrading"
        assert result.trend_pct == 15.4  # noqa: PLR2004
        assert result.bottleneck_stage == "test"
        assert result.note == "All good"
