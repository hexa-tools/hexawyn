"""Unit tests for MCP tool: list_task_runs."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestListTaskRunsTool:
    def test_list_task_runs_returns_dict(self) -> None:
        from hexawyn.mcp.tools.list_task_runs import list_task_runs

        mock_response = MagicMock()
        mock_response.task_runs = []
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_tekton_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.list_task_runs.ListTaskRunsUseCase",
                return_value=mock_uc,
            ),
        ):
            result = list_task_runs()

        assert isinstance(result, dict)
        assert "task_runs" in result

    def test_list_task_runs_handles_error(self) -> None:
        from hexawyn.mcp.tools.list_task_runs import list_task_runs

        with patch(
            "hexawyn.mcp.server.build_tekton_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = list_task_runs()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.list_task_runs")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
