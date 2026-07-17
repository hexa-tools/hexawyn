"""Unit tests for MCP tool: rbac_permission_audit."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestRbacPermissionAuditTool:
    def test_audit_rbac_permissions_returns_dict(self) -> None:
        from hexawyn.mcp.tools.rbac_permission_audit import audit_rbac_permissions

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_rbac_audit_adapter", return_value=MagicMock()),
        ):
            result = audit_rbac_permissions()

        assert isinstance(result, dict)

    def test_audit_rbac_permissions_handles_error(self) -> None:
        from hexawyn.mcp.tools.rbac_permission_audit import audit_rbac_permissions

        with (
            patch(
                "hexawyn.mcp.server.build_rbac_audit_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = audit_rbac_permissions()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.rbac_permission_audit")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
