from abc import ABC


class TestCheckMachineConfigPoolStatusServicePort:
    def test_is_abstract_base_class(self) -> None:
        from hexawyn.application.ports.driving.check_machine_config_pool_status.check_machine_config_pool_status_service_port import (  # noqa: E501
            CheckMachineConfigPoolStatusServicePort,
        )

        assert issubclass(CheckMachineConfigPoolStatusServicePort, ABC)

    def test_declares_check_method(self) -> None:
        from hexawyn.application.ports.driving.check_machine_config_pool_status.check_machine_config_pool_status_service_port import (  # noqa: E501
            CheckMachineConfigPoolStatusServicePort,
        )

        assert "check" in CheckMachineConfigPoolStatusServicePort.__abstractmethods__
