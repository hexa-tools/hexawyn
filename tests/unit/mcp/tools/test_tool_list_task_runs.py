"""Unit tests for MCP tool: list_task_runs."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestListTaskRunsTool:
    def test_list_task_runs_returns_dict(self) -> None:
        from hexawyn.mcp.tools.list_task_runs import list_task_runs

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_tekton_adapter", return_value=MagicMock()),
        ):
            result = list_task_runs(pipeline_name="test-pipeline_name")

        assert isinstance(result, dict)

    def test_list_task_runs_handles_error(self) -> None:
        from hexawyn.mcp.tools.list_task_runs import list_task_runs

        with (
            patch(
                "hexawyn.mcp.server.build_tekton_adapter", side_effect=RuntimeError("test error")
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = list_task_runs(pipeline_name="test-pipeline_name")

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.list_task_runs")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
