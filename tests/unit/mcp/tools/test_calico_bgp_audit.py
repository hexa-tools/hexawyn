"""Unit tests for MCP tool: calico_bgp_audit."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestCalicoBgpAuditTool:
    def test_returns_dict(self) -> None:
        from hexawyn.mcp.tools.calico_bgp_audit import calico_bgp_audit

        mock_response = MagicMock()
        mock_response.installed = True
        mock_response.not_installed_marker = None
        mock_response.as_number = "64512"
        mock_response.node_to_node_mesh_enabled = True
        mock_response.service_cluster_ips = ["10.96.0.0/16"]
        mock_response.peer_count = 1
        mock_response.peers = []
        mock_response.session_state = "reachable"
        mock_response.session_note = "All calico-node agents ready"
        mock_response.summary = "BGP ASN 64512, 1 peer"
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_calico_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.calico_bgp_audit.CalicoBgpAuditUseCase",
                return_value=mock_uc,
            ),
        ):
            result = calico_bgp_audit()

        assert isinstance(result, dict)
        assert result["installed"] is True
        assert result["as_number"] == "64512"
        assert result["peer_count"] == 1  # noqa: PLR2004
        assert result["error"] is None

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.calico_bgp_audit import calico_bgp_audit

        with patch(
            "hexawyn.mcp.server.build_calico_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = calico_bgp_audit()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"
        assert result.get("installed") is False

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.calico_bgp_audit")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))

    def test_peer_dict(self) -> None:
        from hexawyn.domain.models.calico import CalicoBgpPeer
        from hexawyn.mcp.tools.calico_bgp_audit import _peer_dict

        peer = CalicoBgpPeer(
            name="p1", peer_ip="10.0.0.2", as_number="64513", node_selector="all()"
        )
        result = _peer_dict(peer)

        assert result["name"] == "p1"
        assert result["peer_ip"] == "10.0.0.2"
        assert result["as_number"] == "64513"
        assert result["node_selector"] == "all()"
