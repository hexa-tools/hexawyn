"""Unit tests for MCP tool: calico_connectivity_health."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestCalicoConnectivityHealthTool:
    def test_returns_dict(self) -> None:
        from hexawyn.mcp.tools.calico_connectivity_health import calico_connectivity_health

        mock_response = MagicMock()
        mock_response.installed = True
        mock_response.not_installed_marker = None
        mock_response.verdict = "healthy"
        mock_response.ready_agents = 3
        mock_response.total_agents = 3
        mock_response.dataplane_mode = "IPIP"
        mock_response.tunnel_summary = "IPIP tunnel"
        mock_response.bgp_summary = "BGP node-to-node mesh reachable"
        mock_response.connectivity_probe = "healthy"
        mock_response.nodes = []
        mock_response.degraded_nodes = []
        mock_response.summary = "Calico dataplane healthy: 3/3 calico-node agents ready"
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_calico_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.calico_connectivity_health.CalicoConnectivityHealthUseCase",
                return_value=mock_uc,
            ),
        ):
            result = calico_connectivity_health()

        assert isinstance(result, dict)
        assert result["installed"] is True
        assert result["verdict"] == "healthy"
        assert result["tunnel_summary"] == "IPIP tunnel"
        assert result["error"] is None

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.calico_connectivity_health import calico_connectivity_health

        with patch(
            "hexawyn.mcp.server.build_calico_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = calico_connectivity_health()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"
        assert result.get("installed") is False
        assert result.get("verdict") == "unknown"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.calico_connectivity_health")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))

    def test_node_dict(self) -> None:
        from hexawyn.domain.models.calico import CalicoNodeConnectivity
        from hexawyn.mcp.tools.calico_connectivity_health import _node_dict

        node = CalicoNodeConnectivity(node="node-1", ready=True)
        result = _node_dict(node)

        assert result["node"] == "node-1"
        assert result["ready"] is True
