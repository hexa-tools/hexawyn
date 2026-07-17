"""Unit tests for MCP tool: sensitive_data_audit."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestSensitiveDataAuditTool:
    def test_sensitive_data_audit_returns_dict(self) -> None:
        from hexawyn.mcp.tools.sensitive_data_audit import sensitive_data_audit

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_compliance_audit_adapter", return_value=MagicMock()),
        ):
            result = sensitive_data_audit(pattern="test")

        assert isinstance(result, dict)

    def test_sensitive_data_audit_handles_error(self) -> None:
        from hexawyn.mcp.tools.sensitive_data_audit import sensitive_data_audit

        with (
            patch(
                "hexawyn.mcp.server.build_compliance_audit_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = sensitive_data_audit(pattern="test")

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.sensitive_data_audit")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
