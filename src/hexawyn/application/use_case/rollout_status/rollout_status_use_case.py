from hexawyn.application.ports.driven.rollouts_port import RolloutsPort
from hexawyn.application.use_case.rollout_status.command import RolloutStatusCommand
from hexawyn.application.use_case.rollout_status.response import RolloutStatusResponse


class RolloutStatusUseCase:
    def __init__(self, rollouts_port: RolloutsPort) -> None:
        self._rollouts = rollouts_port

    def execute(self, c: RolloutStatusCommand) -> RolloutStatusResponse:
        r = self._rollouts.get_rollout(name=c.name, namespace=c.namespace)
        return RolloutStatusResponse(
            name=r.name,
            namespace=r.namespace,
            phase=r.phase.value,
            strategy=r.strategy.value,
            message=r.message,
        )
