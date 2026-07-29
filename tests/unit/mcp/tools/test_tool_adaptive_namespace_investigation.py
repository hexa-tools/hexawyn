"""Unit tests for MCP tool: adaptive_namespace_investigation."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestAdaptiveNamespaceInvestigationTool:
    def test_adaptive_namespace_investigation_returns_dict(self) -> None:
        from hexawyn.mcp.tools.adaptive_namespace_investigation import (
            adaptive_namespace_investigation,
        )

        mock_response = MagicMock()
        mock_response.namespace = "test-ns"
        mock_response.namespace_status = "healthy"
        mock_response.health_status = {}
        mock_response.overview_summary = {}
        mock_response.investigated_resources = []
        mock_response.root_cause_candidates = []
        mock_response.recommended_actions = []
        mock_response.skipped_resources = []
        mock_response.node_pressure_context = {}
        mock_response.has_more_failing = False
        mock_response.remaining_failing_count = 0
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch(
                "hexawyn.mcp.server.build_adaptive_investigation_adapter", return_value=MagicMock()
            ),
            patch("hexawyn.mcp.server.build_k8s_adapter", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_namespace_overview_adapter", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.tools.adaptive_namespace_investigation.AdaptiveNamespaceInvestigationUseCase",
                return_value=mock_uc,
            ),
        ):
            result = adaptive_namespace_investigation("test-ns")

        assert isinstance(result, dict)
        assert result["namespace"] == "test-ns"

    def test_adaptive_namespace_investigation_handles_error(self) -> None:
        from hexawyn.mcp.tools.adaptive_namespace_investigation import (
            adaptive_namespace_investigation,
        )

        with (
            patch(
                "hexawyn.mcp.server.build_k8s_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch(
                "hexawyn.mcp.server.build_adaptive_investigation_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch(
                "hexawyn.mcp.server.build_namespace_overview_adapter",
                side_effect=RuntimeError("test error"),
            ),
        ):
            result = adaptive_namespace_investigation("test-ns")

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.adaptive_namespace_investigation")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
