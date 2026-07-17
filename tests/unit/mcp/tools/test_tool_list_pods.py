"""Unit tests for MCP tool: list_pods."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestListPodsTool:
    def test_list_pods_returns_dict(self) -> None:
        from hexawyn.mcp.tools.list_pods import list_pods

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_k8s_adapter", return_value=MagicMock()),
        ):
            result = list_pods(namespace="test-ns")

        assert isinstance(result, dict)

    def test_list_pods_handles_error(self) -> None:
        from hexawyn.mcp.tools.list_pods import list_pods

        with (
            patch("hexawyn.mcp.server.build_k8s_adapter", side_effect=RuntimeError("test error")),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = list_pods(namespace="test-ns")

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.list_pods")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
