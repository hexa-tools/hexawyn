from hexawyn.application.ports.driven.rollouts_port import RolloutsPort
from hexawyn.application.use_case.rollouts_detect.command import RolloutsDetectCommand
from hexawyn.application.use_case.rollouts_detect.response import RolloutsDetectResponse


class RolloutsDetectUseCase:
    def __init__(self, rollouts_port: RolloutsPort) -> None:
        self._rollouts = rollouts_port

    def execute(self, command: RolloutsDetectCommand) -> RolloutsDetectResponse:
        r = self._rollouts.detect_engine()
        return RolloutsDetectResponse(
            installed=r.installed, version=r.version, namespace=r.namespace
        )
