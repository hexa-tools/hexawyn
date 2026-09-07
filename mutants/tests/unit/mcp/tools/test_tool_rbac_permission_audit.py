"""Unit tests for MCP tool: audit_rbac_permissions."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestRbacPermissionAuditTool:
    def test_audit_rbac_permissions_returns_dict(self) -> None:
        from hexawyn.mcp.tools.rbac_permission_audit import audit_rbac_permissions

        mock_response = MagicMock()
        mock_response.findings = []
        mock_response.unused_service_accounts = []
        mock_response.total_audited = 0
        mock_response.summary = "ok"
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_rbac_audit_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.rbac_permission_audit.AuditRbacPermissionsUseCase",
                return_value=mock_uc,
            ),
        ):
            result = audit_rbac_permissions()

        assert isinstance(result, dict)
        assert "findings" in result

    def test_audit_rbac_permissions_handles_error(self) -> None:
        from hexawyn.mcp.tools.rbac_permission_audit import audit_rbac_permissions

        with patch(
            "hexawyn.mcp.server.build_rbac_audit_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = audit_rbac_permissions()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.rbac_permission_audit")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
