"""Unit tests for MCP tool: run_consolidation."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestRunConsolidationTool:
    def test_run_consolidation_returns_dict(self) -> None:
        from hexawyn.mcp.tools.run_consolidation import run_consolidation

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_consolidation_adapter", return_value=MagicMock()),
        ):
            result = run_consolidation()

        assert isinstance(result, dict)

    def test_run_consolidation_handles_error(self) -> None:
        from hexawyn.mcp.tools.run_consolidation import run_consolidation

        with (
            patch(
                "hexawyn.mcp.server.build_consolidation_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = run_consolidation()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.run_consolidation")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
