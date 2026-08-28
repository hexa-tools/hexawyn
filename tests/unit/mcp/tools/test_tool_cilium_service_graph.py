"""Unit tests for MCP tool: cilium_service_graph."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestCiliumServiceGraphTool:
    def test_cilium_service_graph_returns_dict(self) -> None:
        from hexawyn.mcp.tools.cilium_service_graph import cilium_service_graph

        mock_response = MagicMock()
        mock_response.time_window_minutes = 60
        mock_response.nodes = ["web-0", "db-0"]
        mock_response.edges = [{"source": "web-0", "target": "db-0"}]
        mock_response.note = None
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch(
                "hexawyn.mcp.server.build_cilium_service_graph_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.tools.cilium_service_graph.CiliumServiceGraphUseCase",
                return_value=mock_uc,
            ),
        ):
            result = cilium_service_graph()

        assert isinstance(result, dict)
        assert result["nodes"] == ["web-0", "db-0"]
        assert result["error"] is None

    def test_cilium_service_graph_error_returns_empty(self) -> None:
        from hexawyn.mcp.tools.cilium_service_graph import cilium_service_graph

        with patch(
            "hexawyn.mcp.server.build_cilium_service_graph_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = cilium_service_graph()

        assert isinstance(result, dict)
        assert result["nodes"] == []
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.cilium_service_graph")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
