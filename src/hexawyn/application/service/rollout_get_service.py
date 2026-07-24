from __future__ import annotations

from hexawyn.application.ports.driven.rollouts_port import RolloutsPort
from hexawyn.application.use_case.rollout_get.command import (
    RolloutGetCommand,
)
from hexawyn.application.use_case.rollout_get.response import (
    RolloutGetResponse,
)
from hexawyn.application.ports.driving.rollout_get.rollout_get_service_port import (
    RolloutGetServicePort,
)


class RolloutGetService(RolloutGetServicePort):
    def __init__(self, rollouts_port: RolloutsPort) -> None:
        self._rollouts = rollouts_port

    def get_rollout(self, command: RolloutGetCommand) -> RolloutGetResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=command.namespace)
        step = rollout.current_step
        return RolloutGetResponse(
            name=rollout.name,
            namespace=rollout.namespace,
            strategy=rollout.strategy.value,
            phase=rollout.phase.value,
            desired_replicas=rollout.desired_replicas,
            ready_replicas=rollout.ready_replicas,
            canary_replicas=rollout.canary_replicas,
            stable_replicas=rollout.stable_replicas,
            current_image=rollout.current_image,
            stable_image=rollout.stable_image,
            step_index=step.step_index if step else None,
            total_steps=step.total_steps if step else None,
            current_step_type=step.current_step_type if step else None,
            canary_weight=step.canary_weight if step else None,
            paused_at=step.paused_at if step else None,
            pause_reason=step.pause_reason if step else None,
            message=rollout.message,
            analysis_run_name=rollout.analysis_run_name,
        )
