from unittest.mock import MagicMock

from hexawyn.application.ports.driven.machine_config_pool_port import (
    MachineConfigPoolPort,
    MachineConfigPoolRawData,
)
from hexawyn.application.ports.driving.check_machine_config_pool_status.check_machine_config_pool_status_command import (  # noqa: E501
    CheckMachineConfigPoolStatusCommand,
)


def _raw(name: str, degraded: bool = False) -> MachineConfigPoolRawData:
    return MachineConfigPoolRawData(
        name=name,
        machine_count=3,
        ready_machine_count=3 if not degraded else 2,
        updated_machine_count=3,
        degraded_machine_count=1 if degraded else 0,
        updating=False,
        degraded=degraded,
        paused=False,
        current_config="rendered-abc",
        desired_config="rendered-abc",
        reason="failed to apply MachineConfig" if degraded else "",
        updating_since=None,
    )


class TestCheckMachineConfigPoolStatusService:
    def test_implements_service_port(self) -> None:
        from hexawyn.application.ports.driving.check_machine_config_pool_status.check_machine_config_pool_status_service_port import (  # noqa: E501
            CheckMachineConfigPoolStatusServicePort,
        )
        from hexawyn.application.service.check_machine_config_pool_status_service import (
            CheckMachineConfigPoolStatusService,
        )

        service = CheckMachineConfigPoolStatusService(
            machine_config_pool_port=MagicMock(spec=MachineConfigPoolPort)
        )

        assert isinstance(service, CheckMachineConfigPoolStatusServicePort)

    def test_check_returns_report_from_port_data(self) -> None:
        from hexawyn.application.service.check_machine_config_pool_status_service import (
            CheckMachineConfigPoolStatusService,
        )

        port = MagicMock(spec=MachineConfigPoolPort)
        port.list_machine_config_pools.return_value = [
            _raw("master"),
            _raw("infra", degraded=True),
        ]
        service = CheckMachineConfigPoolStatusService(machine_config_pool_port=port)

        response = service.check(CheckMachineConfigPoolStatusCommand())

        port.list_machine_config_pools.assert_called_once_with()
        assert response.result.total == 2
        assert response.result.degraded == 1
        assert response.result.all_healthy is False

    def test_check_lets_domain_error_propagate(self) -> None:
        import pytest
        from hexawyn.application.service.check_machine_config_pool_status_service import (
            CheckMachineConfigPoolStatusService,
        )
        from hexawyn.domain.errors import MachineConfigPoolCRDNotFoundError

        port = MagicMock(spec=MachineConfigPoolPort)
        port.list_machine_config_pools.side_effect = MachineConfigPoolCRDNotFoundError()
        service = CheckMachineConfigPoolStatusService(machine_config_pool_port=port)

        with pytest.raises(MachineConfigPoolCRDNotFoundError):
            service.check(CheckMachineConfigPoolStatusCommand())
