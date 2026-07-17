"""Unit tests for MCP tool: certs_issuers_list."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestCertsIssuersListTool:
    def test_certs_issuers_list_returns_dict(self) -> None:
        from hexawyn.mcp.tools.certs_issuers_list import certs_issuers_list

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_cert_manager_adapter", return_value=MagicMock()),
        ):
            result = certs_issuers_list()

        assert isinstance(result, dict)

    def test_certs_issuers_list_handles_error(self) -> None:
        from hexawyn.mcp.tools.certs_issuers_list import certs_issuers_list

        with (
            patch(
                "hexawyn.mcp.server.build_cert_manager_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = certs_issuers_list()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.certs_issuers_list")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
