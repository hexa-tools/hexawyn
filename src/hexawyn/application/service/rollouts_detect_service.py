from __future__ import annotations

from hexawyn.application.ports.driven.rollouts_port import RolloutsPort
from hexawyn.application.use_case.rollouts_detect.command import (
    RolloutsDetectCommand,
)
from hexawyn.application.use_case.rollouts_detect.response import (
    RolloutsDetectResponse,
)
from hexawyn.application.ports.driving.rollouts_detect.rollouts_detect_service_port import (
    RolloutsDetectServicePort,
)


class RolloutsDetectService(RolloutsDetectServicePort):
    def __init__(self, rollouts_port: RolloutsPort) -> None:
        self._rollouts = rollouts_port

    def detect(self, command: RolloutsDetectCommand) -> RolloutsDetectResponse:
        result = self._rollouts.detect_rollouts()
        return RolloutsDetectResponse(
            installed=result.installed,
            version=result.version,
            namespace=result.namespace,
            total_rollouts=result.total_rollouts,
            healthy=result.healthy,
            progressing=result.progressing,
            degraded=result.degraded,
            paused=result.paused,
        )
