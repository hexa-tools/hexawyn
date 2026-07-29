"""Unit tests for MCP tool: audit_secret_rotation."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestAuditSecretRotationTool:
    def test_audit_secret_rotation_returns_dict(self) -> None:
        from hexawyn.mcp.tools.audit_secret_rotation import audit_secret_rotation

        with patch(
            "hexawyn.mcp.server.build_secret_rotation_audit_adapter",
            return_value=MagicMock(),
        ):
            result = audit_secret_rotation()

        assert isinstance(result, dict)
        assert "error" in result

    def test_audit_secret_rotation_handles_error(self) -> None:
        from hexawyn.mcp.tools.audit_secret_rotation import audit_secret_rotation

        with patch(
            "hexawyn.mcp.server.build_secret_rotation_audit_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = audit_secret_rotation()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.audit_secret_rotation")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
