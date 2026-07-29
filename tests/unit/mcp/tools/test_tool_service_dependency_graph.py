"""Unit tests for MCP tool: service_dependency_graph."""

from __future__ import annotations

import sys
from unittest.mock import MagicMock, patch


class TestServiceDependencyGraphTool:
    def _mock_imports(self) -> None:
        sys.modules[
            "hexawyn.application.use_case.observability.service_dependency_graph.service_dependency_graph_use_case"
        ] = MagicMock()
        sys.modules[
            "hexawyn.application.use_case.observability.service_dependency_graph.command"
        ] = MagicMock()

    def test_service_dependency_graph_returns_dict(self) -> None:
        self._mock_imports()
        from hexawyn.mcp.tools.service_dependency_graph import service_dependency_graph

        with patch(
            "hexawyn.mcp.server.build_service_dependency_graph_adapter",
            return_value=MagicMock(),
        ):
            result = service_dependency_graph()

        assert isinstance(result, dict)
        assert "error" in result

    def test_service_dependency_graph_handles_error(self) -> None:
        self._mock_imports()
        from hexawyn.mcp.tools.service_dependency_graph import service_dependency_graph

        with patch(
            "hexawyn.mcp.server.build_service_dependency_graph_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = service_dependency_graph()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        self._mock_imports()
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.service_dependency_graph")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
