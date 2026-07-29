"""Unit tests for MCP tool: list_pipeline_runs."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestListPipelineRunsTool:
    def test_list_pipeline_runs_returns_dict(self) -> None:
        from hexawyn.application.use_case.pipelines.list_pipeline_runs.response import (
            PipelineRunStats,
        )
        from hexawyn.mcp.tools.list_pipeline_runs import list_pipeline_runs

        mock_response = MagicMock()
        mock_response.runs = []
        mock_response.stats = PipelineRunStats()
        mock_response.outliers = []
        mock_response.note = None
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_tekton_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.list_pipeline_runs.ListPipelineRunsUseCase",
                return_value=mock_uc,
            ),
        ):
            result = list_pipeline_runs("test-svc")

        assert isinstance(result, dict)
        assert "runs" in result

    def test_list_pipeline_runs_handles_error(self) -> None:
        from hexawyn.mcp.tools.list_pipeline_runs import list_pipeline_runs

        with patch(
            "hexawyn.mcp.server.build_tekton_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = list_pipeline_runs("test-svc")

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.list_pipeline_runs")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))


class TestListPipelineRunsExposesUseCaseStats:
    """The use case already computes success_rate, succeeded/failed/cancelled
    counts, and real outliers (via find_outliers) — this must reach the LLM
    instead of being silently discarded and replaced by a locally recomputed,
    partial mean/median-only stats dict.
    """

    def test_success_rate_and_counts_are_exposed(self) -> None:
        from hexawyn.application.use_case.pipelines.list_pipeline_runs.response import (
            PipelineRunStats,
        )
        from hexawyn.mcp.tools.list_pipeline_runs import list_pipeline_runs

        mock_response = MagicMock()
        mock_response.runs = [
            {"name": "r1", "status": "Succeeded", "duration_seconds": 100},
            {"name": "r2", "status": "Failed", "duration_seconds": 50},
        ]
        mock_response.stats = PipelineRunStats(
            total_runs=2,
            succeeded_runs=1,
            failed_runs=1,
            cancelled_runs=0,
            success_rate=50.0,
            average_duration_seconds=75.0,
            fastest_run_name="r2",
            slowest_run_name="r1",
        )
        mock_response.outliers = ["r1"]
        mock_response.note = None
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_tekton_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.list_pipeline_runs.ListPipelineRunsUseCase",
                return_value=mock_uc,
            ),
        ):
            result = list_pipeline_runs("test-svc")

        stats = result["stats"]
        assert stats["success_rate"] == 50.0  # noqa: PLR2004
        assert stats["succeeded_runs"] == 1
        assert stats["failed_runs"] == 1
        assert stats["cancelled_runs"] == 0
        assert stats["total_runs"] == 2  # noqa: PLR2004
        assert stats["fastest_run_name"] == "r2"
        assert stats["slowest_run_name"] == "r1"
        assert result["outliers"] == ["r1"]

    def test_no_rated_runs_gives_zero_percent(self) -> None:
        from hexawyn.application.use_case.pipelines.list_pipeline_runs.response import (
            PipelineRunStats,
        )
        from hexawyn.mcp.tools.list_pipeline_runs import list_pipeline_runs

        mock_response = MagicMock()
        mock_response.runs = []
        mock_response.stats = PipelineRunStats()
        mock_response.outliers = []
        mock_response.note = None
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_tekton_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.list_pipeline_runs.ListPipelineRunsUseCase",
                return_value=mock_uc,
            ),
        ):
            result = list_pipeline_runs("test-svc")

        assert result["stats"]["success_rate"] == 0.0
