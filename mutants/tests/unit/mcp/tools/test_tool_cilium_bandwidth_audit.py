"""Unit tests for MCP tool: cilium_bandwidth_audit."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestCiliumBandwidthAuditTool:
    def test_cilium_bandwidth_audit_returns_dict(self) -> None:
        from hexawyn.mcp.tools.cilium_bandwidth_audit import cilium_bandwidth_audit

        mock_entry = MagicMock()
        mock_entry.pod = "db-0"
        mock_response = MagicMock()
        mock_response.installed = True
        mock_response.status = "anomalies"
        mock_response.total_pods = 1
        mock_response.entries = [mock_entry]
        mock_response.note = None
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_cilium_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.cilium_bandwidth_audit.CiliumBandwidthAuditUseCase",
                return_value=mock_uc,
            ),
        ):
            result = cilium_bandwidth_audit()

        assert isinstance(result, dict)
        assert result["installed"] is True
        assert result["status"] == "anomalies"
        assert result["error"] is None

    def test_cilium_bandwidth_audit_error_returns_unknown(self) -> None:
        from hexawyn.mcp.tools.cilium_bandwidth_audit import cilium_bandwidth_audit

        with patch(
            "hexawyn.mcp.server.build_cilium_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = cilium_bandwidth_audit()

        assert isinstance(result, dict)
        assert result["installed"] is False
        assert result["status"] == "unknown"
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.cilium_bandwidth_audit")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
