"""Unit tests for MCP tool: conservative_namespace_overview."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestConservativeNamespaceOverviewTool:
    def test_conservative_namespace_overview_returns_dict(self) -> None:
        from hexawyn.mcp.tools.conservative_namespace_overview import (
            conservative_namespace_overview,
        )

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_k8s_adapter", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_namespace_overview_adapter", return_value=MagicMock()),
        ):
            result = conservative_namespace_overview(namespace="test-ns")

        assert isinstance(result, dict)

    def test_conservative_namespace_overview_handles_error(self) -> None:
        from hexawyn.mcp.tools.conservative_namespace_overview import (
            conservative_namespace_overview,
        )

        with (
            patch("hexawyn.mcp.server.build_k8s_adapter", side_effect=RuntimeError("test error")),
            patch(
                "hexawyn.mcp.server.build_namespace_overview_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = conservative_namespace_overview(namespace="test-ns")

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.conservative_namespace_overview")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
