from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestAuditRBACPermissionsTool:
    def test_returns_report(self) -> None:
        from hexawyn.mcp.tools.rbac_permission_audit import audit_rbac_permissions

        with patch("hexawyn.mcp.server.build_rbac_audit_adapter") as build_adapter:
            port = MagicMock()
            port.list_service_accounts.return_value = []
            port.list_role_bindings.return_value = []
            port.list_roles.return_value = []
            port.list_pods_by_service_account.return_value = []
            port.fetch_api_usage.return_value = {"available": False, "events": []}
            build_adapter.return_value = port

            result = audit_rbac_permissions()

        assert result["error"] is None
        assert result["findings"] == []

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.rbac_permission_audit import audit_rbac_permissions

        with patch(
            "hexawyn.mcp.server.build_rbac_audit_adapter",
            side_effect=RuntimeError("cluster unreachable"),
        ):
            result = audit_rbac_permissions()

        assert "cluster unreachable" in result["error"]


class TestBuildRBACAuditAdapterFactory:
    def test_build_rbac_audit_adapter_returns_rbac_security_audit_port(self) -> None:
        from hexawyn.application.ports.driven.rbac_security_audit_port import (
            RBACSecurityAuditPort,
        )
        from hexawyn.mcp.server import build_rbac_audit_adapter

        result = build_rbac_audit_adapter()

        assert isinstance(result, RBACSecurityAuditPort)


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.rbac_permission_audit")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
