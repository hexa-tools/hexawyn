"""Unit tests for MCP tool: etcd_logs."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestEtcdLogsTool:
    def test_etcd_logs_returns_dict(self) -> None:
        from hexawyn.mcp.tools.etcd_logs import etcd_logs

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_etcd_logs_adapter", return_value=MagicMock()),
        ):
            result = etcd_logs()

        assert isinstance(result, dict)

    def test_etcd_logs_handles_error(self) -> None:
        from hexawyn.mcp.tools.etcd_logs import etcd_logs

        with (
            patch(
                "hexawyn.mcp.server.build_etcd_logs_adapter", side_effect=RuntimeError("test error")
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = etcd_logs()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.etcd_logs")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
