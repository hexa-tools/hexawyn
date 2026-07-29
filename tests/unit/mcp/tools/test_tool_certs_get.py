"""Unit tests for MCP tool: certs_get."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestCertsGetTool:
    def test_certs_get_returns_dict(self) -> None:
        from hexawyn.mcp.tools.certs_get import certs_get

        with patch("hexawyn.mcp.server.build_cert_manager_adapter", return_value=MagicMock()):
            result = certs_get(name="test-cert", namespace="test-ns")

        assert isinstance(result, dict)
        assert "error" in result

    def test_certs_get_handles_error(self) -> None:
        from hexawyn.mcp.tools.certs_get import certs_get

        with patch(
            "hexawyn.mcp.server.build_cert_manager_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = certs_get(name="test-cert", namespace="test-ns")

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_certs_get_success_path(self) -> None:
        from hexawyn.mcp.tools.certs_get import certs_get

        mock_response = MagicMock()
        mock_response.name = "test-cert"
        mock_response.namespace = "test-ns"
        mock_response.status = "Ready"
        mock_response.issuer_name = "test-issuer"
        mock_response.issuer_type = "CA"
        mock_response.dns_names = []
        mock_response.not_before = "2024-01-01"
        mock_response.not_after = "2025-01-01"
        mock_response.days_until_expiry = 365
        mock_response.renewal_time = None
        mock_response.auto_renew = True
        mock_response.message = "ok"
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_cert_manager_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.certs_get.CertsGetUseCase",
                return_value=mock_uc,
            ),
        ):
            result = certs_get(name="test-cert", namespace="test-ns")

        assert isinstance(result, dict)
        assert result.get("error") is None

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.certs_get")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
