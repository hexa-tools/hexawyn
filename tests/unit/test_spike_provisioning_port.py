from abc import ABC


class TestSpikeProvisioningPortContract:
    def test_is_abstract_base_class(self) -> None:
        from hexawyn.application.ports.driven.spike_provisioning_port import (
            SpikeProvisioningPort,
        )

        assert issubclass(SpikeProvisioningPort, ABC)

    def test_declares_required_methods(self) -> None:
        from hexawyn.application.ports.driven.spike_provisioning_port import (
            SpikeProvisioningPort,
        )

        expected = {"get_cluster_capacity", "get_historical_spike_multiplier"}

        assert expected <= SpikeProvisioningPort.__abstractmethods__


class TestClusterCapacityRaw:
    def test_shape(self) -> None:
        from hexawyn.application.ports.driven.spike_provisioning_port import (
            ClusterCapacityRaw,
        )

        raw: ClusterCapacityRaw = {
            "node_count": 10,
            "allocatable_cpu_cores": 100.0,
            "allocatable_memory_gb": 200.0,
            "used_cpu_cores": 70.0,
            "used_memory_gb": 130.0,
            "autoscaler_enabled": False,
        }

        assert raw["node_count"] == 10
        assert raw["used_cpu_cores"] == 70.0
        assert raw["autoscaler_enabled"] is False
