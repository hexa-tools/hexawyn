from hexawyn.application.ports.driven.security_posture_port import SecurityPosturePort
from hexawyn.application.use_case.compute_security_posture.command import (
    ComputeSecurityPostureCommand,
)
from hexawyn.application.use_case.compute_security_posture.response import (
    ComputeSecurityPostureResponse,
)


class ComputeSecurityPostureUseCase:
    def __init__(self, port: SecurityPosturePort) -> None:
        self._port = port

    def execute(self, command: ComputeSecurityPostureCommand) -> ComputeSecurityPostureResponse:
        return ComputeSecurityPostureResponse()
