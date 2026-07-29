"""Unit tests for MCP tool: list_pipeline_runs helper functions."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestListPipelineRunsHelpers:
    def test_compute_outliers_with_few_runs(self) -> None:
        from hexawyn.mcp.tools.list_pipeline_runs import _compute_outliers

        result = _compute_outliers([])
        assert result == []

        result = _compute_outliers([{"name": "r1", "duration_seconds": 10}])
        assert result == []

    def test_compute_outliers_detects_slow_run(self) -> None:
        from hexawyn.mcp.tools.list_pipeline_runs import _compute_outliers

        runs: list[dict[str, object]] = [
            {"name": "r1", "duration_seconds": 10},
            {"name": "r2", "duration_seconds": 12},
            {"name": "r3", "duration_seconds": 250},
        ]
        result = _compute_outliers(runs)
        assert "r3" in result

    def test_compute_outliers_no_outliers(self) -> None:
        from hexawyn.mcp.tools.list_pipeline_runs import _compute_outliers

        runs: list[dict[str, object]] = [
            {"name": "r1", "duration_seconds": 10},
            {"name": "r2", "duration_seconds": 12},
            {"name": "r3", "duration_seconds": 11},
        ]
        result = _compute_outliers(runs)
        assert result == []

    def test_compute_outliers_skips_none_duration(self) -> None:
        from hexawyn.mcp.tools.list_pipeline_runs import _compute_outliers

        runs: list[dict[str, object]] = [
            {"name": "r1", "duration_seconds": None},
            {"name": "r2", "duration_seconds": 10},
            {"name": "r3", "duration_seconds": 200},
        ]
        result = _compute_outliers(runs)
        assert "r3" in result

    def test_compute_duration_stats_empty(self) -> None:
        from hexawyn.mcp.tools.list_pipeline_runs import _compute_duration_stats

        result = _compute_duration_stats([])
        assert result["mean_s"] == 0  # noqa: PLR2004
        assert result["median_s"] == 0  # noqa: PLR2004

    def test_compute_duration_stats_odd_count(self) -> None:
        from hexawyn.mcp.tools.list_pipeline_runs import _compute_duration_stats

        runs: list[dict[str, object]] = [
            {"duration_seconds": 10},
            {"duration_seconds": 20},
            {"duration_seconds": 30},
        ]
        result = _compute_duration_stats(runs)
        assert result["mean_s"] == 20.0  # noqa: PLR2004
        assert result["median_s"] == 20.0  # noqa: PLR2004

    def test_compute_duration_stats_even_count(self) -> None:
        from hexawyn.mcp.tools.list_pipeline_runs import _compute_duration_stats

        runs: list[dict[str, object]] = [
            {"duration_seconds": 10},
            {"duration_seconds": 20},
            {"duration_seconds": 30},
            {"duration_seconds": 40},
        ]
        result = _compute_duration_stats(runs)
        assert result["mean_s"] == 25.0  # noqa: PLR2004
        assert result["median_s"] == 25.0  # noqa: PLR2004

    def test_compute_duration_stats_skips_none(self) -> None:
        from hexawyn.mcp.tools.list_pipeline_runs import _compute_duration_stats

        runs: list[dict[str, object]] = [
            {"duration_seconds": None},
            {"duration_seconds": 10},
        ]
        result = _compute_duration_stats(runs)
        assert result["mean_s"] == 10.0  # noqa: PLR2004


class TestListPipelineRunsTool:
    def test_list_pipeline_runs_returns_dict(self) -> None:
        from hexawyn.mcp.tools.list_pipeline_runs import list_pipeline_runs

        mock_response = MagicMock()
        mock_response.runs = []
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
