"""Unit tests for MCP tool: certs_requests_list."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestCertsRequestsListTool:
    def test_certs_requests_list_returns_dict(self) -> None:
        from hexawyn.mcp.tools.certs_requests_list import certs_requests_list

        with patch("hexawyn.mcp.server.build_cert_manager_adapter", return_value=MagicMock()):
            result = certs_requests_list()

        assert isinstance(result, dict)
        assert "error" in result

    def test_certs_requests_list_handles_error(self) -> None:
        from hexawyn.mcp.tools.certs_requests_list import certs_requests_list

        with patch(
            "hexawyn.mcp.server.build_cert_manager_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = certs_requests_list()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_certs_requests_list_success_path(self) -> None:
        from hexawyn.mcp.tools.certs_requests_list import certs_requests_list

        mock_response = MagicMock()
        mock_response.requests = []
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_cert_manager_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.certs_requests_list.CertsRequestsListUseCase",
                return_value=mock_uc,
            ),
        ):
            result = certs_requests_list()

        assert isinstance(result, dict)
        assert result.get("error") is None

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.certs_requests_list")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
