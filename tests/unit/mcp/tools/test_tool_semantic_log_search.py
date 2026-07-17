"""Unit tests for MCP tool: semantic_log_search."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestSemanticLogSearchTool:
    def test_semantic_log_search_returns_dict(self) -> None:
        from hexawyn.mcp.tools.semantic_log_search import semantic_log_search

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_k8s_adapter", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_log_search_adapter", return_value=MagicMock()),
        ):
            result = semantic_log_search(pattern="test")

        assert isinstance(result, dict)

    def test_semantic_log_search_handles_error(self) -> None:
        from hexawyn.mcp.tools.semantic_log_search import semantic_log_search

        with (
            patch("hexawyn.mcp.server.build_k8s_adapter", side_effect=RuntimeError("test error")),
            patch(
                "hexawyn.mcp.server.build_log_search_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = semantic_log_search(pattern="test")

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.semantic_log_search")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
