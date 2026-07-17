"""Unit tests for MCP tool: certs_get."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestCertsGetTool:
    def test_certs_get_returns_dict(self) -> None:
        from hexawyn.mcp.tools.certs_get import certs_get

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_cert_manager_adapter", return_value=MagicMock()),
        ):
            result = certs_get(name="test-name", namespace="test-ns")

        assert isinstance(result, dict)

    def test_certs_get_handles_error(self) -> None:
        from hexawyn.mcp.tools.certs_get import certs_get

        with (
            patch(
                "hexawyn.mcp.server.build_cert_manager_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = certs_get(name="test-name", namespace="test-ns")

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.certs_get")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
