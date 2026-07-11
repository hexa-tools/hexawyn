"""RED → GREEN — MCP tool: plan_spike_provisioning."""

from unittest.mock import MagicMock, patch

from hexawyn.application.ports.driven.spike_provisioning_port import (
    ClusterCapacityRaw,
    SpikeProvisioningPort,
)
from hexawyn.domain.errors import ClusterUnreachableError


def _capacity(used_cpu: float = 70.0, autoscaler: bool = False) -> ClusterCapacityRaw:
    return ClusterCapacityRaw(
        node_count=10,
        allocatable_cpu_cores=100.0,
        allocatable_memory_gb=200.0,
        used_cpu_cores=used_cpu,
        used_memory_gb=130.0,
        autoscaler_enabled=autoscaler,
    )


def _port(capacity: ClusterCapacityRaw, historical: float | None = None) -> MagicMock:
    port = MagicMock(spec=SpikeProvisioningPort)
    port.get_cluster_capacity.return_value = capacity
    port.get_historical_spike_multiplier.return_value = historical
    return port


class TestPlanSpikeProvisioningTool:
    def test_provision_recommendation(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_spike_provisioning_adapter",
            return_value=_port(_capacity(used_cpu=70.0), historical=2.8),
        ):
            from hexawyn.mcp.tools.plan_spike_provisioning import plan_spike_provisioning

            result = plan_spike_provisioning(event_date="2026-11-27")

        assert result["verdict"] == "provision"
        assert result["recommended_nodes"] >= 1
        assert result["recommended_node_type"] == "compute_optimized"
        assert result["provisioning_deadline"] is not None
        assert result["error"] is None

    def test_no_action_when_headroom_sufficient(self) -> None:
        capacity = ClusterCapacityRaw(
            node_count=10,
            allocatable_cpu_cores=100.0,
            allocatable_memory_gb=200.0,
            used_cpu_cores=20.0,
            used_memory_gb=40.0,
            autoscaler_enabled=False,
        )
        with patch(
            "hexawyn.mcp.server.build_spike_provisioning_adapter",
            return_value=_port(capacity, historical=2.0),
        ):
            from hexawyn.mcp.tools.plan_spike_provisioning import plan_spike_provisioning

            result = plan_spike_provisioning(event_date="2026-11-27")

        assert result["verdict"] == "no_action"
        assert result["recommended_nodes"] == 0

    def test_autoscaler_handles(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_spike_provisioning_adapter",
            return_value=_port(_capacity(used_cpu=70.0, autoscaler=True), historical=2.8),
        ):
            from hexawyn.mcp.tools.plan_spike_provisioning import plan_spike_provisioning

            result = plan_spike_provisioning(event_date="2026-11-27")

        assert result["verdict"] == "autoscaler_handles"
        assert result["autoscaler_sufficient"] is True

    def test_generic_fallback_warning(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_spike_provisioning_adapter",
            return_value=_port(_capacity(), historical=None),
        ):
            from hexawyn.mcp.tools.plan_spike_provisioning import plan_spike_provisioning

            result = plan_spike_provisioning(event_date="2026-11-27")

        assert result["multiplier_source"] == "generic_fallback"
        assert result["warning"] != ""

    def test_handles_error_gracefully(self) -> None:
        with patch(
            "hexawyn.mcp.server.build_spike_provisioning_adapter",
            side_effect=ClusterUnreachableError("down"),
        ):
            from hexawyn.mcp.tools.plan_spike_provisioning import plan_spike_provisioning

            result = plan_spike_provisioning(event_date="2026-11-27")

        assert result["verdict"] == "no_action"
        assert "down" in result["error"]

    def test_has_register_function(self) -> None:
        from hexawyn.mcp.tools.plan_spike_provisioning import register

        assert callable(register)
