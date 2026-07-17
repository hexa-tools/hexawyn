import dataclasses


class TestCheckMachineConfigPoolStatusCommand:
    def test_is_instantiable(self) -> None:
        from hexawyn.application.ports.driving.check_machine_config_pool_status.check_machine_config_pool_status_command import (  # noqa: E501
            CheckMachineConfigPoolStatusCommand,
        )

        assert CheckMachineConfigPoolStatusCommand() is not None

    def test_is_dataclass(self) -> None:
        from hexawyn.application.ports.driving.check_machine_config_pool_status.check_machine_config_pool_status_command import (  # noqa: E501
            CheckMachineConfigPoolStatusCommand,
        )

        assert dataclasses.is_dataclass(CheckMachineConfigPoolStatusCommand)
