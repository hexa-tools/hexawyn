from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driven.headroom_simulation_port import (
    HeadroomCapacityInfoRaw,
    HeadroomSimulationPort,
)
from hexawyn.application.ports.driven.spike_provisioning_port import SpikeProvisioningPort


def _capacity_info(autoscaler: bool = False) -> HeadroomCapacityInfoRaw:
    return HeadroomCapacityInfoRaw(
        total_allocatable_cpu_cores=100.0,
        total_allocatable_memory_gb=200.0,
        node_count=10,
        largest_node_cpu_cores=10.0,
        largest_node_memory_gb=20.0,
        autoscaler_enabled=autoscaler,
    )


class TestPortImplementation:
    def test_is_a_spike_provisioning_port(self) -> None:
        from hexawyn.adapters.secondary.gitops.spike_provisioning_adapter import (
            SpikeProvisioningAdapter,
        )

        adapter = SpikeProvisioningAdapter(
            headroom_port=MagicMock(spec=HeadroomSimulationPort),
            current_cpu_used_cores=70.0,
            current_memory_used_gb=130.0,
        )

        assert isinstance(adapter, SpikeProvisioningPort)


class TestGetClusterCapacity:
    def test_maps_capacity_info(self) -> None:
        from hexawyn.adapters.secondary.gitops.spike_provisioning_adapter import (
            SpikeProvisioningAdapter,
        )

        headroom = MagicMock(spec=HeadroomSimulationPort)
        headroom.get_node_capacity_info.return_value = _capacity_info(autoscaler=True)
        adapter = SpikeProvisioningAdapter(
            headroom_port=headroom,
            current_cpu_used_cores=70.0,
            current_memory_used_gb=130.0,
        )

        capacity = adapter.get_cluster_capacity()

        assert capacity["node_count"] == 10
        assert capacity["allocatable_cpu_cores"] == 100.0
        assert capacity["used_cpu_cores"] == 70.0
        assert capacity["used_memory_gb"] == 130.0
        assert capacity["autoscaler_enabled"] is True


class TestHistoricalMultiplier:
    def test_defaults_to_none_when_not_provided(self) -> None:
        from hexawyn.adapters.secondary.gitops.spike_provisioning_adapter import (
            SpikeProvisioningAdapter,
        )

        adapter = SpikeProvisioningAdapter(
            headroom_port=MagicMock(spec=HeadroomSimulationPort),
            current_cpu_used_cores=70.0,
            current_memory_used_gb=130.0,
        )

        assert adapter.get_historical_spike_multiplier() is None

    def test_returns_injected_multiplier(self) -> None:
        from hexawyn.adapters.secondary.gitops.spike_provisioning_adapter import (
            SpikeProvisioningAdapter,
        )

        adapter = SpikeProvisioningAdapter(
            headroom_port=MagicMock(spec=HeadroomSimulationPort),
            current_cpu_used_cores=70.0,
            current_memory_used_gb=130.0,
            historical_multiplier=2.8,
        )

        assert adapter.get_historical_spike_multiplier() == 2.8
