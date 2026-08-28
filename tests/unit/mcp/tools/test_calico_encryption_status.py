"""Unit tests for MCP tool: calico_encryption_status."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestCalicoEncryptionStatusTool:
    def test_returns_dict(self) -> None:
        from hexawyn.mcp.tools.calico_encryption_status import calico_encryption_status

        mock_response = MagicMock()
        mock_response.installed = True
        mock_response.not_installed_marker = None
        mock_response.wireguard_enabled = True
        mock_response.mode = "IPIP"
        mock_response.per_node = []
        mock_response.summary = "WireGuard enabled (IPIP)"
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_calico_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.calico_encryption_status.CalicoEncryptionStatusUseCase",
                return_value=mock_uc,
            ),
        ):
            result = calico_encryption_status()

        assert isinstance(result, dict)
        assert result["installed"] is True
        assert result["wireguard_enabled"] is True
        assert result["mode"] == "IPIP"
        assert result["error"] is None

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.calico_encryption_status import calico_encryption_status

        with patch(
            "hexawyn.mcp.server.build_calico_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = calico_encryption_status()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"
        assert result.get("installed") is False

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.calico_encryption_status")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))

    def test_node_dict(self) -> None:
        from hexawyn.domain.models.calico import CalicoEncryptionNodeStatus
        from hexawyn.mcp.tools.calico_encryption_status import _node_dict

        node = CalicoEncryptionNodeStatus(node="node-1", wireguard_enabled=True)
        result = _node_dict(node)

        assert result["node"] == "node-1"
        assert result["wireguard_enabled"] is True
