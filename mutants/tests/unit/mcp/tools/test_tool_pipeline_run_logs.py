"""Unit tests for MCP tool: pipeline_run_logs."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestPipelineRunLogsTool:
    def test_pipeline_run_logs_returns_dict(self) -> None:
        from hexawyn.mcp.tools.pipeline_run_logs import pipeline_run_logs

        mock_response = MagicMock()
        mock_response.pipeline_run_name = "test-run"
        mock_response.namespace = "test-ns"
        mock_response.pipeline_run_found = True
        mock_response.is_still_running = False
        mock_response.failed_step_count = 1
        mock_response.total_step_count = 5
        mock_response.steps = []
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch(
                "hexawyn.mcp.server.build_pipeline_run_logs_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.tools.pipeline_run_logs.PipelineRunLogsUseCase",
                return_value=mock_uc,
            ),
        ):
            result = pipeline_run_logs("test-run", "test-ns")

        assert isinstance(result, dict)
        assert result["pipeline_run_name"] == "test-run"

    def test_pipeline_run_logs_handles_error(self) -> None:
        from hexawyn.mcp.tools.pipeline_run_logs import pipeline_run_logs

        with patch(
            "hexawyn.mcp.server.build_pipeline_run_logs_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = pipeline_run_logs("test-run", "test-ns")

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.pipeline_run_logs")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
