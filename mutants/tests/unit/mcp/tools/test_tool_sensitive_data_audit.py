"""Unit tests for MCP tool: sensitive_data_audit."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestSensitiveDataAuditTool:
    def test_sensitive_data_audit_returns_dict(self) -> None:
        from hexawyn.mcp.tools.sensitive_data_audit import sensitive_data_audit

        mock_response = MagicMock()
        mock_response.pattern = "password"
        mock_response.total_matches = 0
        mock_response.flagged = []
        mock_response.unflagged = 0
        mock_response.alert_level = "none"
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch(
                "hexawyn.mcp.server.build_compliance_audit_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.tools.sensitive_data_audit.SensitiveDataAuditUseCase",
                return_value=mock_uc,
            ),
        ):
            result = sensitive_data_audit("password")

        assert isinstance(result, dict)
        assert result["pattern"] == "password"

    def test_sensitive_data_audit_handles_error(self) -> None:
        from hexawyn.mcp.tools.sensitive_data_audit import sensitive_data_audit

        with patch(
            "hexawyn.mcp.server.build_compliance_audit_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = sensitive_data_audit("password")

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.sensitive_data_audit")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
