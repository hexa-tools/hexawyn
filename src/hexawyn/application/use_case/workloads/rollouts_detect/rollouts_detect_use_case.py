from __future__ import annotations

from hexawyn.application.ports.driven.rollouts_port import RolloutsPort
from hexawyn.application.use_case.workloads.rollouts_detect.command import (
    RolloutsDetectCommand,
)
from hexawyn.application.use_case.workloads.rollouts_detect.response import (
    RolloutsDetectResponse,
)


class RolloutsDetectUseCase:
    def __init__(self, rollouts_port: RolloutsPort) -> None:
        self._rollouts = rollouts_port

    def execute(self, command: RolloutsDetectCommand) -> RolloutsDetectResponse:
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
