from __future__ import annotations

from hexawyn.application.ports.driving.policy_detect.policy_detect_command import (
    PolicyDetectCommand,
)
from hexawyn.application.ports.driving.policy_detect.policy_detect_response import (
    PolicyDetectResponse,
)
from hexawyn.application.ports.driving.policy_detect.policy_detect_service_port import (
    PolicyDetectServicePort,
)


class PolicyDetectUseCase:
    def __init__(self, service: PolicyDetectServicePort) -> None:
        self._service = service

    def execute(self, command: PolicyDetectCommand) -> PolicyDetectResponse:
        return self._service.detect(command)
