"""Unit tests for MCP tool: audit_tls_compliance."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestAuditTlsComplianceTool:
    def test_audit_tls_compliance_returns_dict(self) -> None:
        from hexawyn.mcp.tools.audit_tls_compliance import audit_tls_compliance

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_tls_compliance_adapter", return_value=MagicMock()),
        ):
            result = audit_tls_compliance()

        assert isinstance(result, dict)

    def test_audit_tls_compliance_handles_error(self) -> None:
        from hexawyn.mcp.tools.audit_tls_compliance import audit_tls_compliance

        with (
            patch(
                "hexawyn.mcp.server.build_tls_compliance_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = audit_tls_compliance()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.audit_tls_compliance")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
