"""Unit tests for MCP tool: admin_endpoint_audit."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestAdminEndpointAuditTool:
    def test_admin_endpoint_audit_returns_dict(self) -> None:
        from hexawyn.mcp.tools.admin_endpoint_audit import admin_endpoint_audit

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_security_audit_adapter", return_value=MagicMock()),
        ):
            result = admin_endpoint_audit()

        assert isinstance(result, dict)

    def test_admin_endpoint_audit_handles_error(self) -> None:
        from hexawyn.mcp.tools.admin_endpoint_audit import admin_endpoint_audit

        with (
            patch(
                "hexawyn.mcp.server.build_security_audit_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = admin_endpoint_audit()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.admin_endpoint_audit")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
