"""Unit tests for MCP tool: get_pipeline_run_status."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestGetPipelineRunStatusTool:
    def test_get_pipeline_run_status_returns_dict(self) -> None:
        from hexawyn.mcp.tools.get_pipeline_run_status import get_pipeline_run_status

        with patch("hexawyn.mcp.server.build_k8s_adapter", return_value=MagicMock()):
            result = get_pipeline_run_status()

        assert isinstance(result, dict)
        assert "error" in result

    def test_get_pipeline_run_status_handles_error(self) -> None:
        from hexawyn.mcp.tools.get_pipeline_run_status import get_pipeline_run_status

        with patch(
            "hexawyn.mcp.server.build_k8s_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = get_pipeline_run_status()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.get_pipeline_run_status")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
