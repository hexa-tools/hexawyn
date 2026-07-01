from __future__ import annotations

from hexawyn.application.ports.driven.rollouts_port import RolloutsPort
from hexawyn.application.ports.driving.rollout_status.rollout_status_command import (
    RolloutStatusCommand,
)
from hexawyn.application.ports.driving.rollout_status.rollout_status_response import (
    RolloutStatusResponse,
)
from hexawyn.application.ports.driving.rollout_status.rollout_status_service_port import (
    RolloutStatusServicePort,
)


class RolloutStatusService(RolloutStatusServicePort):
    def __init__(self, rollouts_port: RolloutsPort) -> None:
        self._rollouts = rollouts_port

    def get_status(self, command: RolloutStatusCommand) -> RolloutStatusResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=command.namespace)
        step = rollout.current_step
        return RolloutStatusResponse(
            name=rollout.name,
            namespace=rollout.namespace,
            phase=rollout.phase.value,
            strategy=rollout.strategy.value,
            canary_weight=step.canary_weight if step else None,
            step_index=step.step_index if step else None,
            total_steps=step.total_steps if step else None,
            current_step_type=step.current_step_type if step else None,
            paused_at=step.paused_at if step else None,
            pause_reason=step.pause_reason if step else None,
            message=rollout.message,
        )
