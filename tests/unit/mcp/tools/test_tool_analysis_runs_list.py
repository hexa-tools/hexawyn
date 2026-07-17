"""Unit tests for MCP tool: analysis_runs_list."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestAnalysisRunsListTool:
    def test_analysis_runs_list_returns_dict(self) -> None:
        from hexawyn.mcp.tools.analysis_runs_list import analysis_runs_list

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_rollouts_adapter", return_value=MagicMock()),
        ):
            result = analysis_runs_list()

        assert isinstance(result, dict)

    def test_analysis_runs_list_handles_error(self) -> None:
        from hexawyn.mcp.tools.analysis_runs_list import analysis_runs_list

        with (
            patch(
                "hexawyn.mcp.server.build_rollouts_adapter", side_effect=RuntimeError("test error")
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = analysis_runs_list()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.analysis_runs_list")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
