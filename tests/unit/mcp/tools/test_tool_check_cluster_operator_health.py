"""Unit tests for MCP tool: check_cluster_operator_health."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestCheckClusterOperatorHealthTool:
    def test_check_cluster_operator_health_returns_dict(self) -> None:
        from hexawyn.mcp.tools.check_cluster_operator_health import check_cluster_operator_health

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.server.build_cluster_operator_status_adapter", return_value=MagicMock()
            ),
        ):
            result = check_cluster_operator_health()

        assert isinstance(result, dict)

    def test_check_cluster_operator_health_handles_error(self) -> None:
        from hexawyn.mcp.tools.check_cluster_operator_health import check_cluster_operator_health

        with (
            patch(
                "hexawyn.mcp.server.build_cluster_operator_status_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = check_cluster_operator_health()

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.check_cluster_operator_health")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
