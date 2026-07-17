"""Unit tests for MCP tool: diff_cluster_resources."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestDiffClusterResourcesTool:
    def test_diff_cluster_resources_returns_dict(self) -> None:
        from hexawyn.mcp.tools.diff_cluster_resources import diff_cluster_resources

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_cluster_diff_adapter", return_value=MagicMock()),
        ):
            result = diff_cluster_resources(source_context="test", target_context="test")

        assert isinstance(result, dict)

    def test_diff_cluster_resources_handles_error(self) -> None:
        from hexawyn.mcp.tools.diff_cluster_resources import diff_cluster_resources

        with (
            patch(
                "hexawyn.mcp.server.build_cluster_diff_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = diff_cluster_resources(source_context="test", target_context="test")

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.diff_cluster_resources")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
