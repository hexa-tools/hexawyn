"""Unit tests for MCP tool: analyze_failed_pipeline."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestAnalyzeFailedPipelineTool:
    def test_analyze_failed_pipeline_returns_dict(self) -> None:
        from hexawyn.mcp.tools.analyze_failed_pipeline import analyze_failed_pipeline

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_pipeline_run_logs_adapter", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_tekton_adapter", return_value=MagicMock()),
        ):
            result = analyze_failed_pipeline(pipeline_name="test-pipeline_name")

        assert isinstance(result, dict)

    def test_analyze_failed_pipeline_handles_error(self) -> None:
        from hexawyn.mcp.tools.analyze_failed_pipeline import analyze_failed_pipeline

        with (
            patch(
                "hexawyn.mcp.server.build_pipeline_run_logs_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch(
                "hexawyn.mcp.server.build_tekton_adapter", side_effect=RuntimeError("test error")
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = analyze_failed_pipeline(pipeline_name="test-pipeline_name")

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.analyze_failed_pipeline")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
