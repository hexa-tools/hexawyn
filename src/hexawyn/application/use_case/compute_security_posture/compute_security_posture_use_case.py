from __future__ import annotations

from hexawyn.application.ports.driving.compute_security_posture.compute_security_posture_command import (  # noqa: E501
    ComputeSecurityPostureCommand,
)
from hexawyn.application.ports.driving.compute_security_posture.compute_security_posture_response import (  # noqa: E501
    ComputeSecurityPostureResponse,
)
from hexawyn.application.ports.driving.compute_security_posture.compute_security_posture_service_port import (  # noqa: E501
    ComputeSecurityPostureServicePort,
)


class ComputeSecurityPostureUseCase:
    def __init__(self, service: ComputeSecurityPostureServicePort) -> None:
        self._service = service

    def execute(self, command: ComputeSecurityPostureCommand) -> ComputeSecurityPostureResponse:
        return self._service.compute(command)
