"""Unit tests for MCP tool: live_topology_mapper."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestLiveTopologyMapperTool:
    def test_live_topology_mapper_returns_dict(self) -> None:
        from hexawyn.mcp.tools.live_topology_mapper import live_topology_mapper

        mock_response = MagicMock()
        mock_response.nodes = []
        mock_response.edges = []
        mock_response.single_points_of_failure = []
        mock_response.orphan_nodes = []
        mock_response.cycles = []
        mock_response.inference_source = "istio"
        mock_response.truncated = False
        mock_response.namespace_scope = None
        mock_response.mermaid_diagram = ""
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch(
                "hexawyn.mcp.server.build_kubernetes_topology_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.server.build_istio_topology_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.server.build_topology_snapshot_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.tools.live_topology_mapper.LiveTopologyMapperUseCase",
                return_value=mock_uc,
            ),
        ):
            result = live_topology_mapper()

        assert isinstance(result, dict)
        assert "nodes" in result

    def test_live_topology_mapper_handles_error(self) -> None:
        from hexawyn.mcp.tools.live_topology_mapper import live_topology_mapper

        with (
            patch("hexawyn.mcp.server.context_name", "test-cluster"),
            patch(
                "hexawyn.mcp.server.build_kubernetes_topology_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch(
                "hexawyn.mcp.server.build_istio_topology_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch(
                "hexawyn.mcp.server.build_topology_snapshot_adapter",
                side_effect=RuntimeError("test error"),
            ),
        ):
            result = live_topology_mapper()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.live_topology_mapper")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
