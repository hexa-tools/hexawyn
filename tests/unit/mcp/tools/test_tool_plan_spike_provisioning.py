"""Unit tests for MCP tool: plan_spike_provisioning."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestPlanSpikeProvisioningTool:
    def test_plan_spike_provisioning_returns_dict(self) -> None:
        from hexawyn.mcp.tools.plan_spike_provisioning import plan_spike_provisioning

        with (
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
            patch("hexawyn.mcp.server.build_spike_provisioning_adapter", return_value=MagicMock()),
        ):
            result = plan_spike_provisioning(event_date="test")

        assert isinstance(result, dict)

    def test_plan_spike_provisioning_handles_error(self) -> None:
        from hexawyn.mcp.tools.plan_spike_provisioning import plan_spike_provisioning

        with (
            patch(
                "hexawyn.mcp.server.build_spike_provisioning_adapter",
                side_effect=RuntimeError("test error"),
            ),
            patch("hexawyn.mcp.server.get_connection", return_value=MagicMock()),
        ):
            result = plan_spike_provisioning(event_date="test")

        assert isinstance(result, dict)

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.plan_spike_provisioning")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
