from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestAuditSecretRotationTool:
    def test_returns_report(self) -> None:
        from hexawyn.mcp.tools.audit_secret_rotation import audit_secret_rotation

        with patch("hexawyn.mcp.server.build_secret_rotation_audit_adapter") as build_adapter:
            port = MagicMock()
            port.list_secrets.return_value = []
            port.list_secret_references.return_value = []
            port.get_namespace_rotation_exemptions.return_value = set()
            build_adapter.return_value = port

            result = audit_secret_rotation()

        assert result["error"] is None
        assert result["findings"] == []

    def test_handles_error(self) -> None:
        from hexawyn.mcp.tools.audit_secret_rotation import audit_secret_rotation

        with patch(
            "hexawyn.mcp.server.build_secret_rotation_audit_adapter",
            side_effect=RuntimeError("cluster unreachable"),
        ):
            result = audit_secret_rotation()

        assert "cluster unreachable" in result["error"]


class TestBuildSecretRotationAuditAdapterFactory:
    def test_build_secret_rotation_audit_adapter_returns_secret_rotation_audit_port(self) -> None:
        from hexawyn.application.ports.driven.secret_rotation_audit_port import (
            SecretRotationAuditPort,
        )
        from hexawyn.mcp.server import build_secret_rotation_audit_adapter

        result = build_secret_rotation_audit_adapter()

        assert isinstance(result, SecretRotationAuditPort)


class TestRegister:
    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.audit_secret_rotation")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
