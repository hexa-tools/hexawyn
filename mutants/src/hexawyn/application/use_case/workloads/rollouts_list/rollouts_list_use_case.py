from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.rollouts_port import RolloutsPort
from hexawyn.application.use_case.workloads.rollouts_list.command import (
    RolloutsListCommand,
)
from hexawyn.application.use_case.workloads.rollouts_list.response import (
    RolloutsListResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁRolloutsListUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁRolloutsListUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class RolloutsListUseCase:
    @_mutmut_mutated(mutants_xǁRolloutsListUseCaseǁ__init____mutmut)
    def __init__(self, rollouts_port: RolloutsPort) -> None:
        self._rollouts = rollouts_port
    def xǁRolloutsListUseCaseǁ__init____mutmut_orig(self, rollouts_port: RolloutsPort) -> None:
        self._rollouts = rollouts_port
    def xǁRolloutsListUseCaseǁ__init____mutmut_1(self, rollouts_port: RolloutsPort) -> None:
        self._rollouts = None

    @_mutmut_mutated(mutants_xǁRolloutsListUseCaseǁexecute__mutmut)
    def execute(self, command: RolloutsListCommand) -> RolloutsListResponse:
        rollouts = self._rollouts.list_rollouts(namespace=command.namespace)
        return RolloutsListResponse(
            rollouts=[asdict(r) for r in rollouts],
        )

    def xǁRolloutsListUseCaseǁexecute__mutmut_orig(self, command: RolloutsListCommand) -> RolloutsListResponse:
        rollouts = self._rollouts.list_rollouts(namespace=command.namespace)
        return RolloutsListResponse(
            rollouts=[asdict(r) for r in rollouts],
        )

    def xǁRolloutsListUseCaseǁexecute__mutmut_1(self, command: RolloutsListCommand) -> RolloutsListResponse:
        rollouts = None
        return RolloutsListResponse(
            rollouts=[asdict(r) for r in rollouts],
        )

    def xǁRolloutsListUseCaseǁexecute__mutmut_2(self, command: RolloutsListCommand) -> RolloutsListResponse:
        rollouts = self._rollouts.list_rollouts(namespace=None)
        return RolloutsListResponse(
            rollouts=[asdict(r) for r in rollouts],
        )

    def xǁRolloutsListUseCaseǁexecute__mutmut_3(self, command: RolloutsListCommand) -> RolloutsListResponse:
        rollouts = self._rollouts.list_rollouts(namespace=command.namespace)
        return RolloutsListResponse(
            rollouts=None,
        )

    def xǁRolloutsListUseCaseǁexecute__mutmut_4(self, command: RolloutsListCommand) -> RolloutsListResponse:
        rollouts = self._rollouts.list_rollouts(namespace=command.namespace)
        return RolloutsListResponse(
            rollouts=[asdict(None) for r in rollouts],
        )

mutants_xǁRolloutsListUseCaseǁ__init____mutmut['_mutmut_orig'] = RolloutsListUseCase.xǁRolloutsListUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁRolloutsListUseCaseǁ__init____mutmut['xǁRolloutsListUseCaseǁ__init____mutmut_1'] = RolloutsListUseCase.xǁRolloutsListUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁRolloutsListUseCaseǁexecute__mutmut['_mutmut_orig'] = RolloutsListUseCase.xǁRolloutsListUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRolloutsListUseCaseǁexecute__mutmut['xǁRolloutsListUseCaseǁexecute__mutmut_1'] = RolloutsListUseCase.xǁRolloutsListUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRolloutsListUseCaseǁexecute__mutmut['xǁRolloutsListUseCaseǁexecute__mutmut_2'] = RolloutsListUseCase.xǁRolloutsListUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRolloutsListUseCaseǁexecute__mutmut['xǁRolloutsListUseCaseǁexecute__mutmut_3'] = RolloutsListUseCase.xǁRolloutsListUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRolloutsListUseCaseǁexecute__mutmut['xǁRolloutsListUseCaseǁexecute__mutmut_4'] = RolloutsListUseCase.xǁRolloutsListUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
