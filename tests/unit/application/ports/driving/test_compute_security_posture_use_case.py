from unittest.mock import MagicMock

from hexawyn.application.ports.driving.compute_security_posture.compute_security_posture_command import (  # noqa: E501
    ComputeSecurityPostureCommand,
)
from hexawyn.application.ports.driving.compute_security_posture.compute_security_posture_response import (  # noqa: E501
    ComputeSecurityPostureResponse,
)
from hexawyn.application.ports.driving.compute_security_posture.compute_security_posture_service_port import (  # noqa: E501
    ComputeSecurityPostureServicePort,
)
from hexawyn.domain.models.security_posture import SecurityPostureReport


class TestComputeSecurityPostureUseCase:
    def test_execute_delegates_to_service(self) -> None:
        from hexawyn.application.use_case.compute_security_posture.compute_security_posture_use_case import (  # noqa: E501
            ComputeSecurityPostureUseCase,
        )

        service = MagicMock(spec=ComputeSecurityPostureServicePort)
        expected = ComputeSecurityPostureResponse(
            result=SecurityPostureReport(overall_score_pct=80.0)
        )
        service.compute.return_value = expected
        use_case = ComputeSecurityPostureUseCase(service=service)
        command = ComputeSecurityPostureCommand()

        response = use_case.execute(command)

        service.compute.assert_called_once_with(command)
        assert response is expected
        assert response.result.overall_score_pct == 80.0
