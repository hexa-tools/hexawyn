"""Unit tests for MCP tool: service_dependency_graph."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestServiceDependencyGraphTool:
    def test_service_dependency_graph_returns_dict(self) -> None:
        from hexawyn.mcp.tools.service_dependency_graph import service_dependency_graph

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.server.build_service_dependency_graph_adapter",
                return_value=MagicMock(),
            ),
        ):
            result = service_dependency_graph()

        assert isinstance(result, dict)

    def test_service_dependency_graph_handles_error(self) -> None:
        from hexawyn.mcp.tools.service_dependency_graph import service_dependency_graph

        with (
            patch(
                "hexawyn.mcp.server.build_service_dependency_graph_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = service_dependency_graph()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.service_dependency_graph")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
