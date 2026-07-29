"""Unit tests for MCP tool: pipeline_performance_baseline."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestPipelinePerformanceBaselineTool:
    def test_pipeline_performance_baseline_returns_dict(self) -> None:
        from hexawyn.mcp.tools.pipeline_performance_baseline import (
            pipeline_performance_baseline,
        )

        mock_stage = MagicMock()
        mock_stage.avg = 10.0
        mock_stage.p50 = 10.0
        mock_stage.p95 = 20.0
        mock_stage.max = 30.0
        mock_stage.unit = "s"

        mock_total_duration = MagicMock()
        mock_total_duration.avg = 100.0
        mock_total_duration.p50 = 100.0
        mock_total_duration.p95 = 150.0
        mock_total_duration.max = 200.0
        mock_total_duration.unit = "s"

        mock_response = MagicMock()
        mock_response.pipeline = "test-pipeline"
        mock_response.runs_analyzed = 10
        mock_response.requested_limit = 30
        mock_response.stages = {"build": mock_stage}
        mock_response.total_duration = mock_total_duration
        mock_response.outliers = []
        mock_response.excluded_running = 0
        mock_response.excluded_failed = 0
        mock_response.trend = "stable"
        mock_response.note = ""
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch(
                "hexawyn.mcp.server.build_pipeline_baseline_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.tools.pipeline_performance_baseline.PipelinePerformanceBaselineUseCase",
                return_value=mock_uc,
            ),
        ):
            result = pipeline_performance_baseline("test-pipeline")

        assert isinstance(result, dict)
        assert result["pipeline"] == "test-pipeline"

    def test_pipeline_performance_baseline_handles_error(self) -> None:
        from hexawyn.mcp.tools.pipeline_performance_baseline import (
            pipeline_performance_baseline,
        )

        with patch(
            "hexawyn.mcp.server.build_pipeline_baseline_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = pipeline_performance_baseline("test-pipeline")

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.pipeline_performance_baseline")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
