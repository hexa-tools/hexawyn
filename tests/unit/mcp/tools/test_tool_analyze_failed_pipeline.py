"""Unit tests for MCP tool: analyze_failed_pipeline."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestAnalyzeFailedPipelineTool:
    def test_analyze_failed_pipeline_returns_dict(self) -> None:
        from hexawyn.mcp.tools.analyze_failed_pipeline import analyze_failed_pipeline

        mock_response = MagicMock()
        mock_response.analysis = "test analysis"
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_tekton_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.analyze_failed_pipeline.AnalyzeFailedPipelineUseCase",
                return_value=mock_uc,
            ),
        ):
            result = analyze_failed_pipeline("test-pipeline")

        assert isinstance(result, dict)
        assert "analysis" in result

    def test_analyze_failed_pipeline_handles_error(self) -> None:
        from hexawyn.mcp.tools.analyze_failed_pipeline import analyze_failed_pipeline

        with patch(
            "hexawyn.mcp.server.build_tekton_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = analyze_failed_pipeline("test-pipeline")

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.analyze_failed_pipeline")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
