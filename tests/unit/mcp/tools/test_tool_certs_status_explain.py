"""Unit tests for MCP tool: certs_status_explain."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestCertsStatusExplainTool:
    def test_certs_status_explain_returns_dict(self) -> None:
        from hexawyn.mcp.tools.certs_status_explain import certs_status_explain

        with patch("hexawyn.mcp.server.build_cert_manager_adapter", return_value=MagicMock()):
            result = certs_status_explain(name="test-cert", namespace="test-ns")

        assert isinstance(result, dict)
        assert "error" in result

    def test_certs_status_explain_handles_error(self) -> None:
        from hexawyn.mcp.tools.certs_status_explain import certs_status_explain

        with patch(
            "hexawyn.mcp.server.build_cert_manager_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = certs_status_explain(name="test-cert", namespace="test-ns")

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_certs_status_explain_success_path(self) -> None:
        from hexawyn.mcp.tools.certs_status_explain import certs_status_explain

        mock_response = MagicMock()
        mock_response.status = "Ready"
        mock_response.message = "Certificate is valid"
        mock_response.explanation = "All checks passed"
        mock_response.fix_suggestion = ""
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_cert_manager_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.certs_status_explain.CertsStatusExplainUseCase",
                return_value=mock_uc,
            ),
        ):
            result = certs_status_explain(name="test-cert", namespace="test-ns")

        assert isinstance(result, dict)
        assert result.get("error") is None

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.certs_status_explain")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
