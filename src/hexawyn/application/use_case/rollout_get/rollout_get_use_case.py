from __future__ import annotations

from hexawyn.application.ports.driven.rollouts_port import RolloutsPort
from hexawyn.application.use_case.rollout_get.command import RolloutGetCommand
from hexawyn.application.use_case.rollout_get.response import RolloutGetResponse


class RolloutGetUseCase:
    def __init__(self, port: RolloutsPort) -> None:
        self._port = port

    def execute(self, command: RolloutGetCommand) -> RolloutGetResponse:
        rollout = self._port.get_rollout(command.name, command.namespace)

        current_step = rollout.current_step
        current_image = rollout.current_image
        stable_image = rollout.stable_image

        if not current_image:
            current_image = ""
        if not stable_image:
            stable_image = current_image

        return RolloutGetResponse(
            name=rollout.name,
            namespace=rollout.namespace,
            strategy=rollout.strategy.value if rollout.strategy else "",
            phase=rollout.phase.value if rollout.phase else "",
            desired_replicas=rollout.desired_replicas,
            ready_replicas=rollout.ready_replicas,
            canary_replicas=rollout.canary_replicas,
            stable_replicas=rollout.stable_replicas,
            current_image=current_image,
            stable_image=stable_image,
            step_index=current_step.step_index if current_step else None,
            total_steps=current_step.total_steps if current_step else None,
            current_step_type=current_step.current_step_type if current_step else None,
            canary_weight=current_step.canary_weight if current_step else None,
            paused_at=current_step.paused_at if current_step else None,
            pause_reason=current_step.pause_reason if current_step else None,
            message=rollout.message,
            analysis_run_name=rollout.analysis_run_name,
        )
