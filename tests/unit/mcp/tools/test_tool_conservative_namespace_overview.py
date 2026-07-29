"""Unit tests for MCP tool: conservative_namespace_overview."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestConservativeNamespaceOverviewTool:
    def test_conservative_namespace_overview_returns_dict(self) -> None:
        from hexawyn.mcp.tools.conservative_namespace_overview import (
            conservative_namespace_overview,
        )

        mock_response = MagicMock()
        mock_response.namespace = "test-ns"
        mock_response.namespace_status = "healthy"
        mock_response.counts = {}
        mock_response.health_status = {}
        mock_response.root_cause = "none"
        mock_response.recommendations = []
        mock_response.cost_impact = {"monthly": 0}
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch("hexawyn.mcp.server.build_k8s_adapter", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_namespace_overview_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.conservative_namespace_overview.ConservativeNamespaceOverviewUseCase",
                return_value=mock_uc,
            ),
        ):
            result = conservative_namespace_overview("test-ns")

        assert isinstance(result, dict)
        assert result["namespace"] == "test-ns"

    def test_conservative_namespace_overview_handles_error(self) -> None:
        from hexawyn.mcp.tools.conservative_namespace_overview import (
            conservative_namespace_overview,
        )

        with (
            patch(
                "hexawyn.mcp.server.build_k8s_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch(
                "hexawyn.mcp.server.build_namespace_overview_adapter",
                side_effect=RuntimeError("test error"),
            ),
        ):
            result = conservative_namespace_overview("test-ns")

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.conservative_namespace_overview")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
