from __future__ import annotations

from unittest.mock import Mock

from hexawyn.adapters.secondary.gitops.spike_provisioning_adapter import (
    SpikeProvisioningAdapter,
)


class TestSpikeProvisioningAdapter:
    def test_get_cluster_capacity_delegates(self) -> None:
        headroom_port = Mock()
        headroom_port.get_node_capacity_info.return_value = {
            "node_count": 10,
            "total_allocatable_cpu_cores": 100.0,
            "total_allocatable_memory_gb": 512.0,
            "largest_node_cpu_cores": 16.0,
            "largest_node_memory_gb": 64.0,
            "autoscaler_enabled": True,
        }
        adapter = SpikeProvisioningAdapter(
            headroom_port=headroom_port,
            current_cpu_used_cores=45.0,
            current_memory_used_gb=200.0,
        )
        result = adapter.get_cluster_capacity()
        assert result["node_count"] == 10  # noqa: PLR2004
        assert result["allocatable_cpu_cores"] == 100.0  # noqa: PLR2004
        assert result["used_cpu_cores"] == 45.0  # noqa: PLR2004
        assert result["used_memory_gb"] == 200.0  # noqa: PLR2004
        assert result["autoscaler_enabled"] is True

    def test_get_historical_spike_multiplier_returns_none_when_not_set(self) -> None:
        adapter = SpikeProvisioningAdapter(
            headroom_port=Mock(),
            current_cpu_used_cores=0.0,
            current_memory_used_gb=0.0,
        )
        assert adapter.get_historical_spike_multiplier() is None

    def test_get_historical_spike_multiplier_returns_value(self) -> None:
        adapter = SpikeProvisioningAdapter(
            headroom_port=Mock(),
            current_cpu_used_cores=0.0,
            current_memory_used_gb=0.0,
            historical_multiplier=2.5,
        )
        assert adapter.get_historical_spike_multiplier() == 2.5  # noqa: PLR2004
