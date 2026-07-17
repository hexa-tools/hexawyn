"""Unit tests for MCP tool: adaptive_namespace_investigation."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestAdaptiveNamespaceInvestigationTool:
    def test_adaptive_namespace_investigation_returns_dict(self) -> None:
        from hexawyn.mcp.tools.adaptive_namespace_investigation import (
            adaptive_namespace_investigation,
        )

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.server.build_adaptive_investigation_adapter", return_value=MagicMock()
            ),
            patch("hexawyn.mcp.server.build_k8s_adapter", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_namespace_overview_adapter", return_value=MagicMock()),
        ):
            result = adaptive_namespace_investigation(namespace="test-ns")

        assert isinstance(result, dict)

    def test_adaptive_namespace_investigation_handles_error(self) -> None:
        from hexawyn.mcp.tools.adaptive_namespace_investigation import (
            adaptive_namespace_investigation,
        )

        with (
            patch(
                "hexawyn.mcp.server.build_adaptive_investigation_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.build_k8s_adapter", side_effect=RuntimeError("test error")),
            patch(
                "hexawyn.mcp.server.build_namespace_overview_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = adaptive_namespace_investigation(namespace="test-ns")

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.adaptive_namespace_investigation")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
