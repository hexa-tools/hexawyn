"""Unit tests for MCP tool: deployment_latency."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestDeploymentLatencyTool:
    def test_deployment_latency_returns_dict(self) -> None:
        from hexawyn.mcp.tools.deployment_latency import deployment_latency

        mock_response = MagicMock()
        mock_response.service_name = "test-svc"
        mock_response.verdict = "stable"
        mock_response.p50_delta_pct = 1.0
        mock_response.p95_delta_pct = 2.0
        mock_response.p99_delta_pct = 3.0
        mock_response.before_p99_ms = 100.0
        mock_response.after_p99_ms = 103.0
        mock_response.suggestion = "no action"
        mock_response.error = None
        mock_uc = MagicMock()
        mock_uc.execute.return_value = mock_response

        with (
            patch(
                "hexawyn.mcp.server.build_deployment_latency_comparison_adapter",
                return_value=MagicMock(),
            ),
            patch(
                "hexawyn.mcp.tools.deployment_latency.DeploymentLatencyUseCase",
                return_value=mock_uc,
            ),
        ):
            result = deployment_latency("test-svc")

        assert isinstance(result, dict)
        assert result["service_name"] == "test-svc"

    def test_deployment_latency_handles_error(self) -> None:
        from hexawyn.mcp.tools.deployment_latency import deployment_latency

        with patch(
            "hexawyn.mcp.server.build_deployment_latency_comparison_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = deployment_latency("test-svc")

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.deployment_latency")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
