"""Unit tests for MCP tool: cilium_encryption_status."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestCiliumEncryptionStatusTool:
    def test_cilium_encryption_status_returns_dict(self) -> None:
        from hexawyn.mcp.tools.cilium_encryption_status import (
            cilium_encryption_status,
        )

        mock_response = MagicMock()
        mock_response.installed = True
        mock_response.status = "enabled"
        mock_response.mode = "wireguard"
        mock_response.encrypted_nodes = 3
        mock_response.total_nodes = 4
        mock_response.coverage = "3/4"
        mock_response.note = None
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_cilium_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.cilium_encryption_status.CiliumEncryptionStatusUseCase",
                return_value=mock_uc,
            ),
        ):
            result = cilium_encryption_status()

        assert isinstance(result, dict)
        assert result["installed"] is True
        assert result["mode"] == "wireguard"
        assert result["coverage"] == "3/4"
        assert result["error"] is None

    def test_cilium_encryption_status_error_returns_unknown(self) -> None:
        from hexawyn.mcp.tools.cilium_encryption_status import (
            cilium_encryption_status,
        )

        with patch(
            "hexawyn.mcp.server.build_cilium_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = cilium_encryption_status()

        assert isinstance(result, dict)
        assert result["installed"] is False
        assert result["status"] == "unknown"
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.cilium_encryption_status")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
