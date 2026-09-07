"""Unit tests for MCP tool: admin_endpoint_audit."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestAdminEndpointAuditTool:
    def test_admin_endpoint_audit_returns_dict(self) -> None:
        from hexawyn.mcp.tools.admin_endpoint_audit import admin_endpoint_audit

        mock_response = MagicMock()
        mock_response.endpoint_pattern = "/admin"
        mock_response.total_requests = 100
        mock_response.total_403s = 5
        mock_response.rate_403_pct = 5.0
        mock_response.flagged_callers = []
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_security_audit_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.admin_endpoint_audit.AdminEndpointAuditUseCase",
                return_value=mock_uc,
            ),
        ):
            result = admin_endpoint_audit()

        assert isinstance(result, dict)
        assert result["endpoint_pattern"] == "/admin"

    def test_admin_endpoint_audit_handles_error(self) -> None:
        from hexawyn.mcp.tools.admin_endpoint_audit import admin_endpoint_audit

        with patch(
            "hexawyn.mcp.server.build_security_audit_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = admin_endpoint_audit()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.admin_endpoint_audit")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
