"""Unit tests for MCP tool: deployment_latency."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestDeploymentLatencyTool:
    def test_deployment_latency_returns_dict(self) -> None:
        from hexawyn.mcp.tools.deployment_latency import deployment_latency

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch(
                "hexawyn.mcp.server.build_deployment_latency_comparison_adapter",
                return_value=MagicMock(),
            ),
        ):
            result = deployment_latency(service_name="test-service_name")

        assert isinstance(result, dict)

    def test_deployment_latency_handles_error(self) -> None:
        from hexawyn.mcp.tools.deployment_latency import deployment_latency

        with (
            patch(
                "hexawyn.mcp.server.build_deployment_latency_comparison_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = deployment_latency(service_name="test-service_name")

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.deployment_latency")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
