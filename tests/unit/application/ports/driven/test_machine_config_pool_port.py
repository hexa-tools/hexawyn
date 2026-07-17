from abc import ABC


class TestMachineConfigPoolPortContract:
    def test_is_abstract_base_class(self) -> None:
        from hexawyn.application.ports.driven.machine_config_pool_port import (
            MachineConfigPoolPort,
        )

        assert issubclass(MachineConfigPoolPort, ABC)

    def test_declares_list_machine_config_pools(self) -> None:
        from hexawyn.application.ports.driven.machine_config_pool_port import (
            MachineConfigPoolPort,
        )

        assert "list_machine_config_pools" in MachineConfigPoolPort.__abstractmethods__


class TestMachineConfigPoolRawData:
    def test_shape(self) -> None:
        from hexawyn.application.ports.driven.machine_config_pool_port import (
            MachineConfigPoolRawData,
        )

        raw: MachineConfigPoolRawData = {
            "name": "worker",
            "machine_count": 5,
            "ready_machine_count": 3,
            "updated_machine_count": 2,
            "degraded_machine_count": 0,
            "updating": True,
            "degraded": False,
            "paused": False,
            "current_config": "rendered-worker-old456",
            "desired_config": "rendered-worker-new789",
            "reason": "",
            "updating_since": "2026-06-16T01:00:00Z",
        }

        assert raw["name"] == "worker"
        assert raw["updating"] is True
        assert raw["updating_since"] == "2026-06-16T01:00:00Z"
