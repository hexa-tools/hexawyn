from __future__ import annotations

from hexawyn.application.ports.driven.rollouts_port import RolloutsPort
from hexawyn.application.use_case.workloads.rollout_get.command import (
    RolloutGetCommand,
)
from hexawyn.application.use_case.workloads.rollout_get.response import (
    RolloutGetResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁRolloutGetUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁRolloutGetUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class RolloutGetUseCase:
    @_mutmut_mutated(mutants_xǁRolloutGetUseCaseǁ__init____mutmut)
    def __init__(self, rollouts_port: RolloutsPort) -> None:
        self._rollouts = rollouts_port
    def xǁRolloutGetUseCaseǁ__init____mutmut_orig(self, rollouts_port: RolloutsPort) -> None:
        self._rollouts = rollouts_port
    def xǁRolloutGetUseCaseǁ__init____mutmut_1(self, rollouts_port: RolloutsPort) -> None:
        self._rollouts = None

    @_mutmut_mutated(mutants_xǁRolloutGetUseCaseǁexecute__mutmut)
    def execute(self, command: RolloutGetCommand) -> RolloutGetResponse:
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

    def xǁRolloutGetUseCaseǁexecute__mutmut_orig(self, command: RolloutGetCommand) -> RolloutGetResponse:
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

    def xǁRolloutGetUseCaseǁexecute__mutmut_1(self, command: RolloutGetCommand) -> RolloutGetResponse:
        rollout = None
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

    def xǁRolloutGetUseCaseǁexecute__mutmut_2(self, command: RolloutGetCommand) -> RolloutGetResponse:
        rollout = self._rollouts.get_rollout(name=None, namespace=command.namespace)
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

    def xǁRolloutGetUseCaseǁexecute__mutmut_3(self, command: RolloutGetCommand) -> RolloutGetResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=None)
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

    def xǁRolloutGetUseCaseǁexecute__mutmut_4(self, command: RolloutGetCommand) -> RolloutGetResponse:
        rollout = self._rollouts.get_rollout(namespace=command.namespace)
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

    def xǁRolloutGetUseCaseǁexecute__mutmut_5(self, command: RolloutGetCommand) -> RolloutGetResponse:
        rollout = self._rollouts.get_rollout(name=command.name, )
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

    def xǁRolloutGetUseCaseǁexecute__mutmut_6(self, command: RolloutGetCommand) -> RolloutGetResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=command.namespace)
        step = None
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

    def xǁRolloutGetUseCaseǁexecute__mutmut_7(self, command: RolloutGetCommand) -> RolloutGetResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=command.namespace)
        step = rollout.current_step
        return RolloutGetResponse(
            name=None,
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

    def xǁRolloutGetUseCaseǁexecute__mutmut_8(self, command: RolloutGetCommand) -> RolloutGetResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=command.namespace)
        step = rollout.current_step
        return RolloutGetResponse(
            name=rollout.name,
            namespace=None,
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

    def xǁRolloutGetUseCaseǁexecute__mutmut_9(self, command: RolloutGetCommand) -> RolloutGetResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=command.namespace)
        step = rollout.current_step
        return RolloutGetResponse(
            name=rollout.name,
            namespace=rollout.namespace,
            strategy=None,
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

    def xǁRolloutGetUseCaseǁexecute__mutmut_10(self, command: RolloutGetCommand) -> RolloutGetResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=command.namespace)
        step = rollout.current_step
        return RolloutGetResponse(
            name=rollout.name,
            namespace=rollout.namespace,
            strategy=rollout.strategy.value,
            phase=None,
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

    def xǁRolloutGetUseCaseǁexecute__mutmut_11(self, command: RolloutGetCommand) -> RolloutGetResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=command.namespace)
        step = rollout.current_step
        return RolloutGetResponse(
            name=rollout.name,
            namespace=rollout.namespace,
            strategy=rollout.strategy.value,
            phase=rollout.phase.value,
            desired_replicas=None,
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

    def xǁRolloutGetUseCaseǁexecute__mutmut_12(self, command: RolloutGetCommand) -> RolloutGetResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=command.namespace)
        step = rollout.current_step
        return RolloutGetResponse(
            name=rollout.name,
            namespace=rollout.namespace,
            strategy=rollout.strategy.value,
            phase=rollout.phase.value,
            desired_replicas=rollout.desired_replicas,
            ready_replicas=None,
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

    def xǁRolloutGetUseCaseǁexecute__mutmut_13(self, command: RolloutGetCommand) -> RolloutGetResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=command.namespace)
        step = rollout.current_step
        return RolloutGetResponse(
            name=rollout.name,
            namespace=rollout.namespace,
            strategy=rollout.strategy.value,
            phase=rollout.phase.value,
            desired_replicas=rollout.desired_replicas,
            ready_replicas=rollout.ready_replicas,
            canary_replicas=None,
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

    def xǁRolloutGetUseCaseǁexecute__mutmut_14(self, command: RolloutGetCommand) -> RolloutGetResponse:
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
            stable_replicas=None,
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

    def xǁRolloutGetUseCaseǁexecute__mutmut_15(self, command: RolloutGetCommand) -> RolloutGetResponse:
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
            current_image=None,
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

    def xǁRolloutGetUseCaseǁexecute__mutmut_16(self, command: RolloutGetCommand) -> RolloutGetResponse:
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
            stable_image=None,
            step_index=step.step_index if step else None,
            total_steps=step.total_steps if step else None,
            current_step_type=step.current_step_type if step else None,
            canary_weight=step.canary_weight if step else None,
            paused_at=step.paused_at if step else None,
            pause_reason=step.pause_reason if step else None,
            message=rollout.message,
            analysis_run_name=rollout.analysis_run_name,
        )

    def xǁRolloutGetUseCaseǁexecute__mutmut_17(self, command: RolloutGetCommand) -> RolloutGetResponse:
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
            step_index=None,
            total_steps=step.total_steps if step else None,
            current_step_type=step.current_step_type if step else None,
            canary_weight=step.canary_weight if step else None,
            paused_at=step.paused_at if step else None,
            pause_reason=step.pause_reason if step else None,
            message=rollout.message,
            analysis_run_name=rollout.analysis_run_name,
        )

    def xǁRolloutGetUseCaseǁexecute__mutmut_18(self, command: RolloutGetCommand) -> RolloutGetResponse:
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
            total_steps=None,
            current_step_type=step.current_step_type if step else None,
            canary_weight=step.canary_weight if step else None,
            paused_at=step.paused_at if step else None,
            pause_reason=step.pause_reason if step else None,
            message=rollout.message,
            analysis_run_name=rollout.analysis_run_name,
        )

    def xǁRolloutGetUseCaseǁexecute__mutmut_19(self, command: RolloutGetCommand) -> RolloutGetResponse:
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
            current_step_type=None,
            canary_weight=step.canary_weight if step else None,
            paused_at=step.paused_at if step else None,
            pause_reason=step.pause_reason if step else None,
            message=rollout.message,
            analysis_run_name=rollout.analysis_run_name,
        )

    def xǁRolloutGetUseCaseǁexecute__mutmut_20(self, command: RolloutGetCommand) -> RolloutGetResponse:
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
            canary_weight=None,
            paused_at=step.paused_at if step else None,
            pause_reason=step.pause_reason if step else None,
            message=rollout.message,
            analysis_run_name=rollout.analysis_run_name,
        )

    def xǁRolloutGetUseCaseǁexecute__mutmut_21(self, command: RolloutGetCommand) -> RolloutGetResponse:
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
            paused_at=None,
            pause_reason=step.pause_reason if step else None,
            message=rollout.message,
            analysis_run_name=rollout.analysis_run_name,
        )

    def xǁRolloutGetUseCaseǁexecute__mutmut_22(self, command: RolloutGetCommand) -> RolloutGetResponse:
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
            pause_reason=None,
            message=rollout.message,
            analysis_run_name=rollout.analysis_run_name,
        )

    def xǁRolloutGetUseCaseǁexecute__mutmut_23(self, command: RolloutGetCommand) -> RolloutGetResponse:
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
            message=None,
            analysis_run_name=rollout.analysis_run_name,
        )

    def xǁRolloutGetUseCaseǁexecute__mutmut_24(self, command: RolloutGetCommand) -> RolloutGetResponse:
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
            analysis_run_name=None,
        )

    def xǁRolloutGetUseCaseǁexecute__mutmut_25(self, command: RolloutGetCommand) -> RolloutGetResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=command.namespace)
        step = rollout.current_step
        return RolloutGetResponse(
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

    def xǁRolloutGetUseCaseǁexecute__mutmut_26(self, command: RolloutGetCommand) -> RolloutGetResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=command.namespace)
        step = rollout.current_step
        return RolloutGetResponse(
            name=rollout.name,
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

    def xǁRolloutGetUseCaseǁexecute__mutmut_27(self, command: RolloutGetCommand) -> RolloutGetResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=command.namespace)
        step = rollout.current_step
        return RolloutGetResponse(
            name=rollout.name,
            namespace=rollout.namespace,
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

    def xǁRolloutGetUseCaseǁexecute__mutmut_28(self, command: RolloutGetCommand) -> RolloutGetResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=command.namespace)
        step = rollout.current_step
        return RolloutGetResponse(
            name=rollout.name,
            namespace=rollout.namespace,
            strategy=rollout.strategy.value,
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

    def xǁRolloutGetUseCaseǁexecute__mutmut_29(self, command: RolloutGetCommand) -> RolloutGetResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=command.namespace)
        step = rollout.current_step
        return RolloutGetResponse(
            name=rollout.name,
            namespace=rollout.namespace,
            strategy=rollout.strategy.value,
            phase=rollout.phase.value,
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

    def xǁRolloutGetUseCaseǁexecute__mutmut_30(self, command: RolloutGetCommand) -> RolloutGetResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=command.namespace)
        step = rollout.current_step
        return RolloutGetResponse(
            name=rollout.name,
            namespace=rollout.namespace,
            strategy=rollout.strategy.value,
            phase=rollout.phase.value,
            desired_replicas=rollout.desired_replicas,
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

    def xǁRolloutGetUseCaseǁexecute__mutmut_31(self, command: RolloutGetCommand) -> RolloutGetResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=command.namespace)
        step = rollout.current_step
        return RolloutGetResponse(
            name=rollout.name,
            namespace=rollout.namespace,
            strategy=rollout.strategy.value,
            phase=rollout.phase.value,
            desired_replicas=rollout.desired_replicas,
            ready_replicas=rollout.ready_replicas,
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

    def xǁRolloutGetUseCaseǁexecute__mutmut_32(self, command: RolloutGetCommand) -> RolloutGetResponse:
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

    def xǁRolloutGetUseCaseǁexecute__mutmut_33(self, command: RolloutGetCommand) -> RolloutGetResponse:
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

    def xǁRolloutGetUseCaseǁexecute__mutmut_34(self, command: RolloutGetCommand) -> RolloutGetResponse:
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
            step_index=step.step_index if step else None,
            total_steps=step.total_steps if step else None,
            current_step_type=step.current_step_type if step else None,
            canary_weight=step.canary_weight if step else None,
            paused_at=step.paused_at if step else None,
            pause_reason=step.pause_reason if step else None,
            message=rollout.message,
            analysis_run_name=rollout.analysis_run_name,
        )

    def xǁRolloutGetUseCaseǁexecute__mutmut_35(self, command: RolloutGetCommand) -> RolloutGetResponse:
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
            total_steps=step.total_steps if step else None,
            current_step_type=step.current_step_type if step else None,
            canary_weight=step.canary_weight if step else None,
            paused_at=step.paused_at if step else None,
            pause_reason=step.pause_reason if step else None,
            message=rollout.message,
            analysis_run_name=rollout.analysis_run_name,
        )

    def xǁRolloutGetUseCaseǁexecute__mutmut_36(self, command: RolloutGetCommand) -> RolloutGetResponse:
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
            current_step_type=step.current_step_type if step else None,
            canary_weight=step.canary_weight if step else None,
            paused_at=step.paused_at if step else None,
            pause_reason=step.pause_reason if step else None,
            message=rollout.message,
            analysis_run_name=rollout.analysis_run_name,
        )

    def xǁRolloutGetUseCaseǁexecute__mutmut_37(self, command: RolloutGetCommand) -> RolloutGetResponse:
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
            canary_weight=step.canary_weight if step else None,
            paused_at=step.paused_at if step else None,
            pause_reason=step.pause_reason if step else None,
            message=rollout.message,
            analysis_run_name=rollout.analysis_run_name,
        )

    def xǁRolloutGetUseCaseǁexecute__mutmut_38(self, command: RolloutGetCommand) -> RolloutGetResponse:
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
            paused_at=step.paused_at if step else None,
            pause_reason=step.pause_reason if step else None,
            message=rollout.message,
            analysis_run_name=rollout.analysis_run_name,
        )

    def xǁRolloutGetUseCaseǁexecute__mutmut_39(self, command: RolloutGetCommand) -> RolloutGetResponse:
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
            pause_reason=step.pause_reason if step else None,
            message=rollout.message,
            analysis_run_name=rollout.analysis_run_name,
        )

    def xǁRolloutGetUseCaseǁexecute__mutmut_40(self, command: RolloutGetCommand) -> RolloutGetResponse:
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
            message=rollout.message,
            analysis_run_name=rollout.analysis_run_name,
        )

    def xǁRolloutGetUseCaseǁexecute__mutmut_41(self, command: RolloutGetCommand) -> RolloutGetResponse:
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
            analysis_run_name=rollout.analysis_run_name,
        )

    def xǁRolloutGetUseCaseǁexecute__mutmut_42(self, command: RolloutGetCommand) -> RolloutGetResponse:
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
            )

mutants_xǁRolloutGetUseCaseǁ__init____mutmut['_mutmut_orig'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁRolloutGetUseCaseǁ__init____mutmut['xǁRolloutGetUseCaseǁ__init____mutmut_1'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁRolloutGetUseCaseǁexecute__mutmut['_mutmut_orig'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRolloutGetUseCaseǁexecute__mutmut['xǁRolloutGetUseCaseǁexecute__mutmut_1'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRolloutGetUseCaseǁexecute__mutmut['xǁRolloutGetUseCaseǁexecute__mutmut_2'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRolloutGetUseCaseǁexecute__mutmut['xǁRolloutGetUseCaseǁexecute__mutmut_3'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRolloutGetUseCaseǁexecute__mutmut['xǁRolloutGetUseCaseǁexecute__mutmut_4'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRolloutGetUseCaseǁexecute__mutmut['xǁRolloutGetUseCaseǁexecute__mutmut_5'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRolloutGetUseCaseǁexecute__mutmut['xǁRolloutGetUseCaseǁexecute__mutmut_6'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁRolloutGetUseCaseǁexecute__mutmut['xǁRolloutGetUseCaseǁexecute__mutmut_7'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁRolloutGetUseCaseǁexecute__mutmut['xǁRolloutGetUseCaseǁexecute__mutmut_8'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁRolloutGetUseCaseǁexecute__mutmut['xǁRolloutGetUseCaseǁexecute__mutmut_9'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁRolloutGetUseCaseǁexecute__mutmut['xǁRolloutGetUseCaseǁexecute__mutmut_10'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁRolloutGetUseCaseǁexecute__mutmut['xǁRolloutGetUseCaseǁexecute__mutmut_11'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁRolloutGetUseCaseǁexecute__mutmut['xǁRolloutGetUseCaseǁexecute__mutmut_12'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁRolloutGetUseCaseǁexecute__mutmut['xǁRolloutGetUseCaseǁexecute__mutmut_13'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁRolloutGetUseCaseǁexecute__mutmut['xǁRolloutGetUseCaseǁexecute__mutmut_14'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁRolloutGetUseCaseǁexecute__mutmut['xǁRolloutGetUseCaseǁexecute__mutmut_15'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁRolloutGetUseCaseǁexecute__mutmut['xǁRolloutGetUseCaseǁexecute__mutmut_16'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁRolloutGetUseCaseǁexecute__mutmut['xǁRolloutGetUseCaseǁexecute__mutmut_17'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁRolloutGetUseCaseǁexecute__mutmut['xǁRolloutGetUseCaseǁexecute__mutmut_18'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁRolloutGetUseCaseǁexecute__mutmut['xǁRolloutGetUseCaseǁexecute__mutmut_19'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁRolloutGetUseCaseǁexecute__mutmut['xǁRolloutGetUseCaseǁexecute__mutmut_20'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁRolloutGetUseCaseǁexecute__mutmut['xǁRolloutGetUseCaseǁexecute__mutmut_21'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁRolloutGetUseCaseǁexecute__mutmut['xǁRolloutGetUseCaseǁexecute__mutmut_22'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁRolloutGetUseCaseǁexecute__mutmut['xǁRolloutGetUseCaseǁexecute__mutmut_23'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁRolloutGetUseCaseǁexecute__mutmut['xǁRolloutGetUseCaseǁexecute__mutmut_24'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁRolloutGetUseCaseǁexecute__mutmut['xǁRolloutGetUseCaseǁexecute__mutmut_25'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁRolloutGetUseCaseǁexecute__mutmut['xǁRolloutGetUseCaseǁexecute__mutmut_26'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁRolloutGetUseCaseǁexecute__mutmut['xǁRolloutGetUseCaseǁexecute__mutmut_27'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁRolloutGetUseCaseǁexecute__mutmut['xǁRolloutGetUseCaseǁexecute__mutmut_28'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁRolloutGetUseCaseǁexecute__mutmut['xǁRolloutGetUseCaseǁexecute__mutmut_29'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁRolloutGetUseCaseǁexecute__mutmut['xǁRolloutGetUseCaseǁexecute__mutmut_30'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁexecute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁRolloutGetUseCaseǁexecute__mutmut['xǁRolloutGetUseCaseǁexecute__mutmut_31'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁexecute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁRolloutGetUseCaseǁexecute__mutmut['xǁRolloutGetUseCaseǁexecute__mutmut_32'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁexecute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁRolloutGetUseCaseǁexecute__mutmut['xǁRolloutGetUseCaseǁexecute__mutmut_33'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁexecute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁRolloutGetUseCaseǁexecute__mutmut['xǁRolloutGetUseCaseǁexecute__mutmut_34'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁexecute__mutmut_34 # type: ignore # mutmut generated
mutants_xǁRolloutGetUseCaseǁexecute__mutmut['xǁRolloutGetUseCaseǁexecute__mutmut_35'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁexecute__mutmut_35 # type: ignore # mutmut generated
mutants_xǁRolloutGetUseCaseǁexecute__mutmut['xǁRolloutGetUseCaseǁexecute__mutmut_36'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁexecute__mutmut_36 # type: ignore # mutmut generated
mutants_xǁRolloutGetUseCaseǁexecute__mutmut['xǁRolloutGetUseCaseǁexecute__mutmut_37'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁexecute__mutmut_37 # type: ignore # mutmut generated
mutants_xǁRolloutGetUseCaseǁexecute__mutmut['xǁRolloutGetUseCaseǁexecute__mutmut_38'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁexecute__mutmut_38 # type: ignore # mutmut generated
mutants_xǁRolloutGetUseCaseǁexecute__mutmut['xǁRolloutGetUseCaseǁexecute__mutmut_39'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁexecute__mutmut_39 # type: ignore # mutmut generated
mutants_xǁRolloutGetUseCaseǁexecute__mutmut['xǁRolloutGetUseCaseǁexecute__mutmut_40'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁexecute__mutmut_40 # type: ignore # mutmut generated
mutants_xǁRolloutGetUseCaseǁexecute__mutmut['xǁRolloutGetUseCaseǁexecute__mutmut_41'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁexecute__mutmut_41 # type: ignore # mutmut generated
mutants_xǁRolloutGetUseCaseǁexecute__mutmut['xǁRolloutGetUseCaseǁexecute__mutmut_42'] = RolloutGetUseCase.xǁRolloutGetUseCaseǁexecute__mutmut_42 # type: ignore # mutmut generated
