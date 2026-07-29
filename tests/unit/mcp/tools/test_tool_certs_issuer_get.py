"""Unit tests for MCP tool: certs_issuer_get."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestCertsIssuerGetTool:
    def test_certs_issuer_get_returns_dict(self) -> None:
        from hexawyn.mcp.tools.certs_issuer_get import certs_issuer_get

        with patch("hexawyn.mcp.server.build_cert_manager_adapter", return_value=MagicMock()):
            result = certs_issuer_get(name="test-issuer")

        assert isinstance(result, dict)
        assert "error" in result

    def test_certs_issuer_get_handles_error(self) -> None:
        from hexawyn.mcp.tools.certs_issuer_get import certs_issuer_get

        with patch(
            "hexawyn.mcp.server.build_cert_manager_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = certs_issuer_get(name="test-issuer")

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_certs_issuer_get_success_path(self) -> None:
        from hexawyn.mcp.tools.certs_issuer_get import certs_issuer_get

        mock_response = MagicMock()
        mock_response.name = "test-issuer"
        mock_response.namespace = "test-ns"
        mock_response.kind = "Issuer"
        mock_response.issuer_type = "CA"
        mock_response.ready = True
        mock_response.server = "https://example.com"
        mock_response.message = "ok"
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_cert_manager_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.certs_issuer_get.CertsIssuerGetUseCase",
                return_value=mock_uc,
            ),
        ):
            result = certs_issuer_get(name="test-issuer")

        assert isinstance(result, dict)
        assert result.get("error") is None

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.certs_issuer_get")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
