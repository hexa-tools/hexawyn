from unittest.mock import MagicMock

from hexawyn.application.ports.driving.check_machine_config_pool_status.check_machine_config_pool_status_command import (  # noqa: E501
    CheckMachineConfigPoolStatusCommand,
)
from hexawyn.application.ports.driving.check_machine_config_pool_status.check_machine_config_pool_status_response import (  # noqa: E501
    CheckMachineConfigPoolStatusResponse,
)
from hexawyn.application.ports.driving.check_machine_config_pool_status.check_machine_config_pool_status_service_port import (  # noqa: E501
    CheckMachineConfigPoolStatusServicePort,
)
from hexawyn.domain.models.machine_config_pool_health import (
    MachineConfigPoolHealthReport,
)


class TestCheckMachineConfigPoolStatusUseCase:
    def test_execute_delegates_to_service(self) -> None:
        from hexawyn.application.use_case.check_machine_config_pool_status.check_machine_config_pool_status_use_case import (  # noqa: E501
            CheckMachineConfigPoolStatusUseCase,
        )

        service = MagicMock(spec=CheckMachineConfigPoolStatusServicePort)
        expected = CheckMachineConfigPoolStatusResponse(
            result=MachineConfigPoolHealthReport(total=3, healthy=1, degraded=1, updating=1)
        )
        service.check.return_value = expected
        use_case = CheckMachineConfigPoolStatusUseCase(service=service)
        command = CheckMachineConfigPoolStatusCommand()

        response = use_case.execute(command)

        service.check.assert_called_once_with(command)
        assert response is expected
        assert response.result.total == 3
