"""Unit tests for MCP tool: list_namespaces."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestListNamespacesTool:
    def test_list_namespaces_returns_dict(self) -> None:
        from hexawyn.mcp.tools.list_namespaces import list_namespaces

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_k8s_adapter", return_value=MagicMock()),
        ):
            result = list_namespaces()

        assert isinstance(result, dict)

    def test_list_namespaces_handles_error(self) -> None:
        from hexawyn.mcp.tools.list_namespaces import list_namespaces

        with (
            patch("hexawyn.mcp.server.build_k8s_adapter", side_effect=RuntimeError("test error")),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = list_namespaces()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.list_namespaces")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
