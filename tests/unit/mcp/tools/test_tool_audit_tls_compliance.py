"""Unit tests for MCP tool: audit_tls_compliance."""

from __future__ import annotations

import sys
from unittest.mock import MagicMock, patch


class TestAuditTlsComplianceTool:
    def _mock_imports(self) -> None:
        mock_uc_mod = MagicMock()
        mock_uc_mod.AuditTlsComplianceUseCase = MagicMock()
        mock_uc_mod.AuditTLSComplianceUseCase = MagicMock()
        sys.modules[
            "hexawyn.application.use_case.security.audit_tls_compliance.audit_tls_compliance_use_case"
        ] = mock_uc_mod
        sys.modules["hexawyn.application.use_case.security.audit_tls_compliance.command"] = (
            MagicMock()
        )

    def test_audit_tls_compliance_returns_dict(self) -> None:
        self._mock_imports()
        from hexawyn.mcp.tools.audit_tls_compliance import audit_tls_compliance

        with patch(
            "hexawyn.mcp.server.build_tls_compliance_adapter",
            return_value=MagicMock(),
        ):
            result = audit_tls_compliance()

        assert isinstance(result, dict)
        assert "error" in result

    def test_audit_tls_compliance_handles_error(self) -> None:
        self._mock_imports()
        from hexawyn.mcp.tools.audit_tls_compliance import audit_tls_compliance

        with patch(
            "hexawyn.mcp.server.build_tls_compliance_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = audit_tls_compliance()

        assert isinstance(result, dict)
        assert result.get("error") is not None

    def test_has_register(self) -> None:
        self._mock_imports()
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.audit_tls_compliance")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
