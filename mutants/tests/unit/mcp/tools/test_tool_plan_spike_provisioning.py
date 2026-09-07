"""Unit tests for MCP tool: plan_spike_provisioning."""

from __future__ import annotations

from unittest.mock import MagicMock, patch


class TestPlanSpikeProvisioningTool:
    def test_plan_spike_provisioning_returns_dict(self) -> None:
        from hexawyn.mcp.tools.plan_spike_provisioning import plan_spike_provisioning

        with patch(
            "hexawyn.mcp.server.build_spike_provisioning_adapter",
            return_value=MagicMock(),
        ):
            result = plan_spike_provisioning()

        assert isinstance(result, dict)
        assert "error" in result

    def test_plan_spike_provisioning_handles_error(self) -> None:
        from hexawyn.mcp.tools.plan_spike_provisioning import plan_spike_provisioning

        with patch(
            "hexawyn.mcp.server.build_spike_provisioning_adapter",
            side_effect=RuntimeError("test error"),
        ):
            result = plan_spike_provisioning()

        assert isinstance(result, dict)
        assert result.get("error") == "test error"

    def test_plan_spike_provisioning_success_path(self) -> None:
        from hexawyn.mcp.tools.plan_spike_provisioning import plan_spike_provisioning

        with (
            patch(
                "hexawyn.mcp.server.build_spike_provisioning_adapter",
                return_value=MagicMock(),
            ),
            patch("hexawyn.mcp.tools.plan_spike_provisioning.PlanSpikeProvisioningUseCase"),
            patch("hexawyn.mcp.tools.plan_spike_provisioning.PlanSpikeProvisioningCommand"),
        ):
            result = plan_spike_provisioning()

        assert isinstance(result, dict)
        assert result.get("error") is None

    def test_has_register(self) -> None:
        import importlib

        from fastmcp import FastMCP

        mod = importlib.import_module("hexawyn.mcp.tools.plan_spike_provisioning")
        assert callable(getattr(mod, "register"))
        getattr(mod, "register")(FastMCP("test"))
