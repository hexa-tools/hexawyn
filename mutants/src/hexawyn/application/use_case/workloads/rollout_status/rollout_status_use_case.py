from __future__ import annotations

from hexawyn.application.ports.driven.rollouts_port import RolloutsPort
from hexawyn.application.use_case.workloads.rollout_status.command import (
    RolloutStatusCommand,
)
from hexawyn.application.use_case.workloads.rollout_status.response import (
    RolloutStatusResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁRolloutStatusUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁRolloutStatusUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class RolloutStatusUseCase:
    @_mutmut_mutated(mutants_xǁRolloutStatusUseCaseǁ__init____mutmut)
    def __init__(self, rollouts_port: RolloutsPort) -> None:
        self._rollouts = rollouts_port
    def xǁRolloutStatusUseCaseǁ__init____mutmut_orig(self, rollouts_port: RolloutsPort) -> None:
        self._rollouts = rollouts_port
    def xǁRolloutStatusUseCaseǁ__init____mutmut_1(self, rollouts_port: RolloutsPort) -> None:
        self._rollouts = None

    @_mutmut_mutated(mutants_xǁRolloutStatusUseCaseǁexecute__mutmut)
    def execute(self, command: RolloutStatusCommand) -> RolloutStatusResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=command.namespace)
        step = rollout.current_step
        return RolloutStatusResponse(
            name=rollout.name,
            namespace=rollout.namespace,
            phase=rollout.phase.value,
            strategy=rollout.strategy.value,
            canary_weight=step.canary_weight if step else None,  # type: ignore
            step_index=step.step_index if step else None,
            total_steps=step.total_steps if step else None,
            current_step_type=step.current_step_type if step else None,
            paused_at=step.paused_at if step else None,
            pause_reason=step.pause_reason if step else None,
            message=rollout.message,  # type: ignore
        )

    def xǁRolloutStatusUseCaseǁexecute__mutmut_orig(self, command: RolloutStatusCommand) -> RolloutStatusResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=command.namespace)
        step = rollout.current_step
        return RolloutStatusResponse(
            name=rollout.name,
            namespace=rollout.namespace,
            phase=rollout.phase.value,
            strategy=rollout.strategy.value,
            canary_weight=step.canary_weight if step else None,  # type: ignore
            step_index=step.step_index if step else None,
            total_steps=step.total_steps if step else None,
            current_step_type=step.current_step_type if step else None,
            paused_at=step.paused_at if step else None,
            pause_reason=step.pause_reason if step else None,
            message=rollout.message,  # type: ignore
        )

    def xǁRolloutStatusUseCaseǁexecute__mutmut_1(self, command: RolloutStatusCommand) -> RolloutStatusResponse:
        rollout = None
        step = rollout.current_step
        return RolloutStatusResponse(
            name=rollout.name,
            namespace=rollout.namespace,
            phase=rollout.phase.value,
            strategy=rollout.strategy.value,
            canary_weight=step.canary_weight if step else None,  # type: ignore
            step_index=step.step_index if step else None,
            total_steps=step.total_steps if step else None,
            current_step_type=step.current_step_type if step else None,
            paused_at=step.paused_at if step else None,
            pause_reason=step.pause_reason if step else None,
            message=rollout.message,  # type: ignore
        )

    def xǁRolloutStatusUseCaseǁexecute__mutmut_2(self, command: RolloutStatusCommand) -> RolloutStatusResponse:
        rollout = self._rollouts.get_rollout(name=None, namespace=command.namespace)
        step = rollout.current_step
        return RolloutStatusResponse(
            name=rollout.name,
            namespace=rollout.namespace,
            phase=rollout.phase.value,
            strategy=rollout.strategy.value,
            canary_weight=step.canary_weight if step else None,  # type: ignore
            step_index=step.step_index if step else None,
            total_steps=step.total_steps if step else None,
            current_step_type=step.current_step_type if step else None,
            paused_at=step.paused_at if step else None,
            pause_reason=step.pause_reason if step else None,
            message=rollout.message,  # type: ignore
        )

    def xǁRolloutStatusUseCaseǁexecute__mutmut_3(self, command: RolloutStatusCommand) -> RolloutStatusResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=None)
        step = rollout.current_step
        return RolloutStatusResponse(
            name=rollout.name,
            namespace=rollout.namespace,
            phase=rollout.phase.value,
            strategy=rollout.strategy.value,
            canary_weight=step.canary_weight if step else None,  # type: ignore
            step_index=step.step_index if step else None,
            total_steps=step.total_steps if step else None,
            current_step_type=step.current_step_type if step else None,
            paused_at=step.paused_at if step else None,
            pause_reason=step.pause_reason if step else None,
            message=rollout.message,  # type: ignore
        )

    def xǁRolloutStatusUseCaseǁexecute__mutmut_4(self, command: RolloutStatusCommand) -> RolloutStatusResponse:
        rollout = self._rollouts.get_rollout(namespace=command.namespace)
        step = rollout.current_step
        return RolloutStatusResponse(
            name=rollout.name,
            namespace=rollout.namespace,
            phase=rollout.phase.value,
            strategy=rollout.strategy.value,
            canary_weight=step.canary_weight if step else None,  # type: ignore
            step_index=step.step_index if step else None,
            total_steps=step.total_steps if step else None,
            current_step_type=step.current_step_type if step else None,
            paused_at=step.paused_at if step else None,
            pause_reason=step.pause_reason if step else None,
            message=rollout.message,  # type: ignore
        )

    def xǁRolloutStatusUseCaseǁexecute__mutmut_5(self, command: RolloutStatusCommand) -> RolloutStatusResponse:
        rollout = self._rollouts.get_rollout(name=command.name, )
        step = rollout.current_step
        return RolloutStatusResponse(
            name=rollout.name,
            namespace=rollout.namespace,
            phase=rollout.phase.value,
            strategy=rollout.strategy.value,
            canary_weight=step.canary_weight if step else None,  # type: ignore
            step_index=step.step_index if step else None,
            total_steps=step.total_steps if step else None,
            current_step_type=step.current_step_type if step else None,
            paused_at=step.paused_at if step else None,
            pause_reason=step.pause_reason if step else None,
            message=rollout.message,  # type: ignore
        )

    def xǁRolloutStatusUseCaseǁexecute__mutmut_6(self, command: RolloutStatusCommand) -> RolloutStatusResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=command.namespace)
        step = None
        return RolloutStatusResponse(
            name=rollout.name,
            namespace=rollout.namespace,
            phase=rollout.phase.value,
            strategy=rollout.strategy.value,
            canary_weight=step.canary_weight if step else None,  # type: ignore
            step_index=step.step_index if step else None,
            total_steps=step.total_steps if step else None,
            current_step_type=step.current_step_type if step else None,
            paused_at=step.paused_at if step else None,
            pause_reason=step.pause_reason if step else None,
            message=rollout.message,  # type: ignore
        )

    def xǁRolloutStatusUseCaseǁexecute__mutmut_7(self, command: RolloutStatusCommand) -> RolloutStatusResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=command.namespace)
        step = rollout.current_step
        return RolloutStatusResponse(
            name=None,
            namespace=rollout.namespace,
            phase=rollout.phase.value,
            strategy=rollout.strategy.value,
            canary_weight=step.canary_weight if step else None,  # type: ignore
            step_index=step.step_index if step else None,
            total_steps=step.total_steps if step else None,
            current_step_type=step.current_step_type if step else None,
            paused_at=step.paused_at if step else None,
            pause_reason=step.pause_reason if step else None,
            message=rollout.message,  # type: ignore
        )

    def xǁRolloutStatusUseCaseǁexecute__mutmut_8(self, command: RolloutStatusCommand) -> RolloutStatusResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=command.namespace)
        step = rollout.current_step
        return RolloutStatusResponse(
            name=rollout.name,
            namespace=None,
            phase=rollout.phase.value,
            strategy=rollout.strategy.value,
            canary_weight=step.canary_weight if step else None,  # type: ignore
            step_index=step.step_index if step else None,
            total_steps=step.total_steps if step else None,
            current_step_type=step.current_step_type if step else None,
            paused_at=step.paused_at if step else None,
            pause_reason=step.pause_reason if step else None,
            message=rollout.message,  # type: ignore
        )

    def xǁRolloutStatusUseCaseǁexecute__mutmut_9(self, command: RolloutStatusCommand) -> RolloutStatusResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=command.namespace)
        step = rollout.current_step
        return RolloutStatusResponse(
            name=rollout.name,
            namespace=rollout.namespace,
            phase=None,
            strategy=rollout.strategy.value,
            canary_weight=step.canary_weight if step else None,  # type: ignore
            step_index=step.step_index if step else None,
            total_steps=step.total_steps if step else None,
            current_step_type=step.current_step_type if step else None,
            paused_at=step.paused_at if step else None,
            pause_reason=step.pause_reason if step else None,
            message=rollout.message,  # type: ignore
        )

    def xǁRolloutStatusUseCaseǁexecute__mutmut_10(self, command: RolloutStatusCommand) -> RolloutStatusResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=command.namespace)
        step = rollout.current_step
        return RolloutStatusResponse(
            name=rollout.name,
            namespace=rollout.namespace,
            phase=rollout.phase.value,
            strategy=None,
            canary_weight=step.canary_weight if step else None,  # type: ignore
            step_index=step.step_index if step else None,
            total_steps=step.total_steps if step else None,
            current_step_type=step.current_step_type if step else None,
            paused_at=step.paused_at if step else None,
            pause_reason=step.pause_reason if step else None,
            message=rollout.message,  # type: ignore
        )

    def xǁRolloutStatusUseCaseǁexecute__mutmut_11(self, command: RolloutStatusCommand) -> RolloutStatusResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=command.namespace)
        step = rollout.current_step
        return RolloutStatusResponse(
            name=rollout.name,
            namespace=rollout.namespace,
            phase=rollout.phase.value,
            strategy=rollout.strategy.value,
            canary_weight=None,  # type: ignore
            step_index=step.step_index if step else None,
            total_steps=step.total_steps if step else None,
            current_step_type=step.current_step_type if step else None,
            paused_at=step.paused_at if step else None,
            pause_reason=step.pause_reason if step else None,
            message=rollout.message,  # type: ignore
        )

    def xǁRolloutStatusUseCaseǁexecute__mutmut_12(self, command: RolloutStatusCommand) -> RolloutStatusResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=command.namespace)
        step = rollout.current_step
        return RolloutStatusResponse(
            name=rollout.name,
            namespace=rollout.namespace,
            phase=rollout.phase.value,
            strategy=rollout.strategy.value,
            canary_weight=step.canary_weight if step else None,  # type: ignore
            step_index=None,
            total_steps=step.total_steps if step else None,
            current_step_type=step.current_step_type if step else None,
            paused_at=step.paused_at if step else None,
            pause_reason=step.pause_reason if step else None,
            message=rollout.message,  # type: ignore
        )

    def xǁRolloutStatusUseCaseǁexecute__mutmut_13(self, command: RolloutStatusCommand) -> RolloutStatusResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=command.namespace)
        step = rollout.current_step
        return RolloutStatusResponse(
            name=rollout.name,
            namespace=rollout.namespace,
            phase=rollout.phase.value,
            strategy=rollout.strategy.value,
            canary_weight=step.canary_weight if step else None,  # type: ignore
            step_index=step.step_index if step else None,
            total_steps=None,
            current_step_type=step.current_step_type if step else None,
            paused_at=step.paused_at if step else None,
            pause_reason=step.pause_reason if step else None,
            message=rollout.message,  # type: ignore
        )

    def xǁRolloutStatusUseCaseǁexecute__mutmut_14(self, command: RolloutStatusCommand) -> RolloutStatusResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=command.namespace)
        step = rollout.current_step
        return RolloutStatusResponse(
            name=rollout.name,
            namespace=rollout.namespace,
            phase=rollout.phase.value,
            strategy=rollout.strategy.value,
            canary_weight=step.canary_weight if step else None,  # type: ignore
            step_index=step.step_index if step else None,
            total_steps=step.total_steps if step else None,
            current_step_type=None,
            paused_at=step.paused_at if step else None,
            pause_reason=step.pause_reason if step else None,
            message=rollout.message,  # type: ignore
        )

    def xǁRolloutStatusUseCaseǁexecute__mutmut_15(self, command: RolloutStatusCommand) -> RolloutStatusResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=command.namespace)
        step = rollout.current_step
        return RolloutStatusResponse(
            name=rollout.name,
            namespace=rollout.namespace,
            phase=rollout.phase.value,
            strategy=rollout.strategy.value,
            canary_weight=step.canary_weight if step else None,  # type: ignore
            step_index=step.step_index if step else None,
            total_steps=step.total_steps if step else None,
            current_step_type=step.current_step_type if step else None,
            paused_at=None,
            pause_reason=step.pause_reason if step else None,
            message=rollout.message,  # type: ignore
        )

    def xǁRolloutStatusUseCaseǁexecute__mutmut_16(self, command: RolloutStatusCommand) -> RolloutStatusResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=command.namespace)
        step = rollout.current_step
        return RolloutStatusResponse(
            name=rollout.name,
            namespace=rollout.namespace,
            phase=rollout.phase.value,
            strategy=rollout.strategy.value,
            canary_weight=step.canary_weight if step else None,  # type: ignore
            step_index=step.step_index if step else None,
            total_steps=step.total_steps if step else None,
            current_step_type=step.current_step_type if step else None,
            paused_at=step.paused_at if step else None,
            pause_reason=None,
            message=rollout.message,  # type: ignore
        )

    def xǁRolloutStatusUseCaseǁexecute__mutmut_17(self, command: RolloutStatusCommand) -> RolloutStatusResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=command.namespace)
        step = rollout.current_step
        return RolloutStatusResponse(
            name=rollout.name,
            namespace=rollout.namespace,
            phase=rollout.phase.value,
            strategy=rollout.strategy.value,
            canary_weight=step.canary_weight if step else None,  # type: ignore
            step_index=step.step_index if step else None,
            total_steps=step.total_steps if step else None,
            current_step_type=step.current_step_type if step else None,
            paused_at=step.paused_at if step else None,
            pause_reason=step.pause_reason if step else None,
            message=None,  # type: ignore
        )

    def xǁRolloutStatusUseCaseǁexecute__mutmut_18(self, command: RolloutStatusCommand) -> RolloutStatusResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=command.namespace)
        step = rollout.current_step
        return RolloutStatusResponse(
            namespace=rollout.namespace,
            phase=rollout.phase.value,
            strategy=rollout.strategy.value,
            canary_weight=step.canary_weight if step else None,  # type: ignore
            step_index=step.step_index if step else None,
            total_steps=step.total_steps if step else None,
            current_step_type=step.current_step_type if step else None,
            paused_at=step.paused_at if step else None,
            pause_reason=step.pause_reason if step else None,
            message=rollout.message,  # type: ignore
        )

    def xǁRolloutStatusUseCaseǁexecute__mutmut_19(self, command: RolloutStatusCommand) -> RolloutStatusResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=command.namespace)
        step = rollout.current_step
        return RolloutStatusResponse(
            name=rollout.name,
            phase=rollout.phase.value,
            strategy=rollout.strategy.value,
            canary_weight=step.canary_weight if step else None,  # type: ignore
            step_index=step.step_index if step else None,
            total_steps=step.total_steps if step else None,
            current_step_type=step.current_step_type if step else None,
            paused_at=step.paused_at if step else None,
            pause_reason=step.pause_reason if step else None,
            message=rollout.message,  # type: ignore
        )

    def xǁRolloutStatusUseCaseǁexecute__mutmut_20(self, command: RolloutStatusCommand) -> RolloutStatusResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=command.namespace)
        step = rollout.current_step
        return RolloutStatusResponse(
            name=rollout.name,
            namespace=rollout.namespace,
            strategy=rollout.strategy.value,
            canary_weight=step.canary_weight if step else None,  # type: ignore
            step_index=step.step_index if step else None,
            total_steps=step.total_steps if step else None,
            current_step_type=step.current_step_type if step else None,
            paused_at=step.paused_at if step else None,
            pause_reason=step.pause_reason if step else None,
            message=rollout.message,  # type: ignore
        )

    def xǁRolloutStatusUseCaseǁexecute__mutmut_21(self, command: RolloutStatusCommand) -> RolloutStatusResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=command.namespace)
        step = rollout.current_step
        return RolloutStatusResponse(
            name=rollout.name,
            namespace=rollout.namespace,
            phase=rollout.phase.value,
            canary_weight=step.canary_weight if step else None,  # type: ignore
            step_index=step.step_index if step else None,
            total_steps=step.total_steps if step else None,
            current_step_type=step.current_step_type if step else None,
            paused_at=step.paused_at if step else None,
            pause_reason=step.pause_reason if step else None,
            message=rollout.message,  # type: ignore
        )

    def xǁRolloutStatusUseCaseǁexecute__mutmut_22(self, command: RolloutStatusCommand) -> RolloutStatusResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=command.namespace)
        step = rollout.current_step
        return RolloutStatusResponse(
            name=rollout.name,
            namespace=rollout.namespace,
            phase=rollout.phase.value,
            strategy=rollout.strategy.value,
            step_index=step.step_index if step else None,
            total_steps=step.total_steps if step else None,
            current_step_type=step.current_step_type if step else None,
            paused_at=step.paused_at if step else None,
            pause_reason=step.pause_reason if step else None,
            message=rollout.message,  # type: ignore
        )

    def xǁRolloutStatusUseCaseǁexecute__mutmut_23(self, command: RolloutStatusCommand) -> RolloutStatusResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=command.namespace)
        step = rollout.current_step
        return RolloutStatusResponse(
            name=rollout.name,
            namespace=rollout.namespace,
            phase=rollout.phase.value,
            strategy=rollout.strategy.value,
            canary_weight=step.canary_weight if step else None,  # type: ignore
            total_steps=step.total_steps if step else None,
            current_step_type=step.current_step_type if step else None,
            paused_at=step.paused_at if step else None,
            pause_reason=step.pause_reason if step else None,
            message=rollout.message,  # type: ignore
        )

    def xǁRolloutStatusUseCaseǁexecute__mutmut_24(self, command: RolloutStatusCommand) -> RolloutStatusResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=command.namespace)
        step = rollout.current_step
        return RolloutStatusResponse(
            name=rollout.name,
            namespace=rollout.namespace,
            phase=rollout.phase.value,
            strategy=rollout.strategy.value,
            canary_weight=step.canary_weight if step else None,  # type: ignore
            step_index=step.step_index if step else None,
            current_step_type=step.current_step_type if step else None,
            paused_at=step.paused_at if step else None,
            pause_reason=step.pause_reason if step else None,
            message=rollout.message,  # type: ignore
        )

    def xǁRolloutStatusUseCaseǁexecute__mutmut_25(self, command: RolloutStatusCommand) -> RolloutStatusResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=command.namespace)
        step = rollout.current_step
        return RolloutStatusResponse(
            name=rollout.name,
            namespace=rollout.namespace,
            phase=rollout.phase.value,
            strategy=rollout.strategy.value,
            canary_weight=step.canary_weight if step else None,  # type: ignore
            step_index=step.step_index if step else None,
            total_steps=step.total_steps if step else None,
            paused_at=step.paused_at if step else None,
            pause_reason=step.pause_reason if step else None,
            message=rollout.message,  # type: ignore
        )

    def xǁRolloutStatusUseCaseǁexecute__mutmut_26(self, command: RolloutStatusCommand) -> RolloutStatusResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=command.namespace)
        step = rollout.current_step
        return RolloutStatusResponse(
            name=rollout.name,
            namespace=rollout.namespace,
            phase=rollout.phase.value,
            strategy=rollout.strategy.value,
            canary_weight=step.canary_weight if step else None,  # type: ignore
            step_index=step.step_index if step else None,
            total_steps=step.total_steps if step else None,
            current_step_type=step.current_step_type if step else None,
            pause_reason=step.pause_reason if step else None,
            message=rollout.message,  # type: ignore
        )

    def xǁRolloutStatusUseCaseǁexecute__mutmut_27(self, command: RolloutStatusCommand) -> RolloutStatusResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=command.namespace)
        step = rollout.current_step
        return RolloutStatusResponse(
            name=rollout.name,
            namespace=rollout.namespace,
            phase=rollout.phase.value,
            strategy=rollout.strategy.value,
            canary_weight=step.canary_weight if step else None,  # type: ignore
            step_index=step.step_index if step else None,
            total_steps=step.total_steps if step else None,
            current_step_type=step.current_step_type if step else None,
            paused_at=step.paused_at if step else None,
            message=rollout.message,  # type: ignore
        )

    def xǁRolloutStatusUseCaseǁexecute__mutmut_28(self, command: RolloutStatusCommand) -> RolloutStatusResponse:
        rollout = self._rollouts.get_rollout(name=command.name, namespace=command.namespace)
        step = rollout.current_step
        return RolloutStatusResponse(
            name=rollout.name,
            namespace=rollout.namespace,
            phase=rollout.phase.value,
            strategy=rollout.strategy.value,
            canary_weight=step.canary_weight if step else None,  # type: ignore
            step_index=step.step_index if step else None,
            total_steps=step.total_steps if step else None,
            current_step_type=step.current_step_type if step else None,
            paused_at=step.paused_at if step else None,
            pause_reason=step.pause_reason if step else None,
            )

mutants_xǁRolloutStatusUseCaseǁ__init____mutmut['_mutmut_orig'] = RolloutStatusUseCase.xǁRolloutStatusUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁRolloutStatusUseCaseǁ__init____mutmut['xǁRolloutStatusUseCaseǁ__init____mutmut_1'] = RolloutStatusUseCase.xǁRolloutStatusUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁRolloutStatusUseCaseǁexecute__mutmut['_mutmut_orig'] = RolloutStatusUseCase.xǁRolloutStatusUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRolloutStatusUseCaseǁexecute__mutmut['xǁRolloutStatusUseCaseǁexecute__mutmut_1'] = RolloutStatusUseCase.xǁRolloutStatusUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRolloutStatusUseCaseǁexecute__mutmut['xǁRolloutStatusUseCaseǁexecute__mutmut_2'] = RolloutStatusUseCase.xǁRolloutStatusUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRolloutStatusUseCaseǁexecute__mutmut['xǁRolloutStatusUseCaseǁexecute__mutmut_3'] = RolloutStatusUseCase.xǁRolloutStatusUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRolloutStatusUseCaseǁexecute__mutmut['xǁRolloutStatusUseCaseǁexecute__mutmut_4'] = RolloutStatusUseCase.xǁRolloutStatusUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRolloutStatusUseCaseǁexecute__mutmut['xǁRolloutStatusUseCaseǁexecute__mutmut_5'] = RolloutStatusUseCase.xǁRolloutStatusUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRolloutStatusUseCaseǁexecute__mutmut['xǁRolloutStatusUseCaseǁexecute__mutmut_6'] = RolloutStatusUseCase.xǁRolloutStatusUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁRolloutStatusUseCaseǁexecute__mutmut['xǁRolloutStatusUseCaseǁexecute__mutmut_7'] = RolloutStatusUseCase.xǁRolloutStatusUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁRolloutStatusUseCaseǁexecute__mutmut['xǁRolloutStatusUseCaseǁexecute__mutmut_8'] = RolloutStatusUseCase.xǁRolloutStatusUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁRolloutStatusUseCaseǁexecute__mutmut['xǁRolloutStatusUseCaseǁexecute__mutmut_9'] = RolloutStatusUseCase.xǁRolloutStatusUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁRolloutStatusUseCaseǁexecute__mutmut['xǁRolloutStatusUseCaseǁexecute__mutmut_10'] = RolloutStatusUseCase.xǁRolloutStatusUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁRolloutStatusUseCaseǁexecute__mutmut['xǁRolloutStatusUseCaseǁexecute__mutmut_11'] = RolloutStatusUseCase.xǁRolloutStatusUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁRolloutStatusUseCaseǁexecute__mutmut['xǁRolloutStatusUseCaseǁexecute__mutmut_12'] = RolloutStatusUseCase.xǁRolloutStatusUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁRolloutStatusUseCaseǁexecute__mutmut['xǁRolloutStatusUseCaseǁexecute__mutmut_13'] = RolloutStatusUseCase.xǁRolloutStatusUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁRolloutStatusUseCaseǁexecute__mutmut['xǁRolloutStatusUseCaseǁexecute__mutmut_14'] = RolloutStatusUseCase.xǁRolloutStatusUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁRolloutStatusUseCaseǁexecute__mutmut['xǁRolloutStatusUseCaseǁexecute__mutmut_15'] = RolloutStatusUseCase.xǁRolloutStatusUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁRolloutStatusUseCaseǁexecute__mutmut['xǁRolloutStatusUseCaseǁexecute__mutmut_16'] = RolloutStatusUseCase.xǁRolloutStatusUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁRolloutStatusUseCaseǁexecute__mutmut['xǁRolloutStatusUseCaseǁexecute__mutmut_17'] = RolloutStatusUseCase.xǁRolloutStatusUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁRolloutStatusUseCaseǁexecute__mutmut['xǁRolloutStatusUseCaseǁexecute__mutmut_18'] = RolloutStatusUseCase.xǁRolloutStatusUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁRolloutStatusUseCaseǁexecute__mutmut['xǁRolloutStatusUseCaseǁexecute__mutmut_19'] = RolloutStatusUseCase.xǁRolloutStatusUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁRolloutStatusUseCaseǁexecute__mutmut['xǁRolloutStatusUseCaseǁexecute__mutmut_20'] = RolloutStatusUseCase.xǁRolloutStatusUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁRolloutStatusUseCaseǁexecute__mutmut['xǁRolloutStatusUseCaseǁexecute__mutmut_21'] = RolloutStatusUseCase.xǁRolloutStatusUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁRolloutStatusUseCaseǁexecute__mutmut['xǁRolloutStatusUseCaseǁexecute__mutmut_22'] = RolloutStatusUseCase.xǁRolloutStatusUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁRolloutStatusUseCaseǁexecute__mutmut['xǁRolloutStatusUseCaseǁexecute__mutmut_23'] = RolloutStatusUseCase.xǁRolloutStatusUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁRolloutStatusUseCaseǁexecute__mutmut['xǁRolloutStatusUseCaseǁexecute__mutmut_24'] = RolloutStatusUseCase.xǁRolloutStatusUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁRolloutStatusUseCaseǁexecute__mutmut['xǁRolloutStatusUseCaseǁexecute__mutmut_25'] = RolloutStatusUseCase.xǁRolloutStatusUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁRolloutStatusUseCaseǁexecute__mutmut['xǁRolloutStatusUseCaseǁexecute__mutmut_26'] = RolloutStatusUseCase.xǁRolloutStatusUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁRolloutStatusUseCaseǁexecute__mutmut['xǁRolloutStatusUseCaseǁexecute__mutmut_27'] = RolloutStatusUseCase.xǁRolloutStatusUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁRolloutStatusUseCaseǁexecute__mutmut['xǁRolloutStatusUseCaseǁexecute__mutmut_28'] = RolloutStatusUseCase.xǁRolloutStatusUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
