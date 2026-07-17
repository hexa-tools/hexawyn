"""Unit tests for MCP tool: list_pipeline_runs."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestListPipelineRunsTool:
    def test_list_pipeline_runs_returns_dict(self) -> None:
        from hexawyn.mcp.tools.list_pipeline_runs import list_pipeline_runs

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_tekton_adapter", return_value=MagicMock()),
        ):
            result = list_pipeline_runs(service_name="test-service_name")

        assert isinstance(result, dict)

    def test_list_pipeline_runs_handles_error(self) -> None:
        from hexawyn.mcp.tools.list_pipeline_runs import list_pipeline_runs

        with (
            patch(
                "hexawyn.mcp.server.build_tekton_adapter", side_effect=RuntimeError("test error")
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = list_pipeline_runs(service_name="test-service_name")

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.list_pipeline_runs")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
