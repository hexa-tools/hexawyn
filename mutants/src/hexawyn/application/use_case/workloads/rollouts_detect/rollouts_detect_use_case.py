from __future__ import annotations

from hexawyn.application.ports.driven.rollouts_port import RolloutsPort
from hexawyn.application.use_case.workloads.rollouts_detect.command import (
    RolloutsDetectCommand,
)
from hexawyn.application.use_case.workloads.rollouts_detect.response import (
    RolloutsDetectResponse,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁRolloutsDetectUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁRolloutsDetectUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class RolloutsDetectUseCase:
    @_mutmut_mutated(mutants_xǁRolloutsDetectUseCaseǁ__init____mutmut)
    def __init__(self, rollouts_port: RolloutsPort) -> None:
        self._rollouts = rollouts_port
    def xǁRolloutsDetectUseCaseǁ__init____mutmut_orig(self, rollouts_port: RolloutsPort) -> None:
        self._rollouts = rollouts_port
    def xǁRolloutsDetectUseCaseǁ__init____mutmut_1(self, rollouts_port: RolloutsPort) -> None:
        self._rollouts = None

    @_mutmut_mutated(mutants_xǁRolloutsDetectUseCaseǁexecute__mutmut)
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

    def xǁRolloutsDetectUseCaseǁexecute__mutmut_orig(self, command: RolloutsDetectCommand) -> RolloutsDetectResponse:
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

    def xǁRolloutsDetectUseCaseǁexecute__mutmut_1(self, command: RolloutsDetectCommand) -> RolloutsDetectResponse:
        result = None
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

    def xǁRolloutsDetectUseCaseǁexecute__mutmut_2(self, command: RolloutsDetectCommand) -> RolloutsDetectResponse:
        result = self._rollouts.detect_rollouts()
        return RolloutsDetectResponse(
            installed=None,
            version=result.version,
            namespace=result.namespace,
            total_rollouts=result.total_rollouts,
            healthy=result.healthy,
            progressing=result.progressing,
            degraded=result.degraded,
            paused=result.paused,
        )

    def xǁRolloutsDetectUseCaseǁexecute__mutmut_3(self, command: RolloutsDetectCommand) -> RolloutsDetectResponse:
        result = self._rollouts.detect_rollouts()
        return RolloutsDetectResponse(
            installed=result.installed,
            version=None,
            namespace=result.namespace,
            total_rollouts=result.total_rollouts,
            healthy=result.healthy,
            progressing=result.progressing,
            degraded=result.degraded,
            paused=result.paused,
        )

    def xǁRolloutsDetectUseCaseǁexecute__mutmut_4(self, command: RolloutsDetectCommand) -> RolloutsDetectResponse:
        result = self._rollouts.detect_rollouts()
        return RolloutsDetectResponse(
            installed=result.installed,
            version=result.version,
            namespace=None,
            total_rollouts=result.total_rollouts,
            healthy=result.healthy,
            progressing=result.progressing,
            degraded=result.degraded,
            paused=result.paused,
        )

    def xǁRolloutsDetectUseCaseǁexecute__mutmut_5(self, command: RolloutsDetectCommand) -> RolloutsDetectResponse:
        result = self._rollouts.detect_rollouts()
        return RolloutsDetectResponse(
            installed=result.installed,
            version=result.version,
            namespace=result.namespace,
            total_rollouts=None,
            healthy=result.healthy,
            progressing=result.progressing,
            degraded=result.degraded,
            paused=result.paused,
        )

    def xǁRolloutsDetectUseCaseǁexecute__mutmut_6(self, command: RolloutsDetectCommand) -> RolloutsDetectResponse:
        result = self._rollouts.detect_rollouts()
        return RolloutsDetectResponse(
            installed=result.installed,
            version=result.version,
            namespace=result.namespace,
            total_rollouts=result.total_rollouts,
            healthy=None,
            progressing=result.progressing,
            degraded=result.degraded,
            paused=result.paused,
        )

    def xǁRolloutsDetectUseCaseǁexecute__mutmut_7(self, command: RolloutsDetectCommand) -> RolloutsDetectResponse:
        result = self._rollouts.detect_rollouts()
        return RolloutsDetectResponse(
            installed=result.installed,
            version=result.version,
            namespace=result.namespace,
            total_rollouts=result.total_rollouts,
            healthy=result.healthy,
            progressing=None,
            degraded=result.degraded,
            paused=result.paused,
        )

    def xǁRolloutsDetectUseCaseǁexecute__mutmut_8(self, command: RolloutsDetectCommand) -> RolloutsDetectResponse:
        result = self._rollouts.detect_rollouts()
        return RolloutsDetectResponse(
            installed=result.installed,
            version=result.version,
            namespace=result.namespace,
            total_rollouts=result.total_rollouts,
            healthy=result.healthy,
            progressing=result.progressing,
            degraded=None,
            paused=result.paused,
        )

    def xǁRolloutsDetectUseCaseǁexecute__mutmut_9(self, command: RolloutsDetectCommand) -> RolloutsDetectResponse:
        result = self._rollouts.detect_rollouts()
        return RolloutsDetectResponse(
            installed=result.installed,
            version=result.version,
            namespace=result.namespace,
            total_rollouts=result.total_rollouts,
            healthy=result.healthy,
            progressing=result.progressing,
            degraded=result.degraded,
            paused=None,
        )

    def xǁRolloutsDetectUseCaseǁexecute__mutmut_10(self, command: RolloutsDetectCommand) -> RolloutsDetectResponse:
        result = self._rollouts.detect_rollouts()
        return RolloutsDetectResponse(
            version=result.version,
            namespace=result.namespace,
            total_rollouts=result.total_rollouts,
            healthy=result.healthy,
            progressing=result.progressing,
            degraded=result.degraded,
            paused=result.paused,
        )

    def xǁRolloutsDetectUseCaseǁexecute__mutmut_11(self, command: RolloutsDetectCommand) -> RolloutsDetectResponse:
        result = self._rollouts.detect_rollouts()
        return RolloutsDetectResponse(
            installed=result.installed,
            namespace=result.namespace,
            total_rollouts=result.total_rollouts,
            healthy=result.healthy,
            progressing=result.progressing,
            degraded=result.degraded,
            paused=result.paused,
        )

    def xǁRolloutsDetectUseCaseǁexecute__mutmut_12(self, command: RolloutsDetectCommand) -> RolloutsDetectResponse:
        result = self._rollouts.detect_rollouts()
        return RolloutsDetectResponse(
            installed=result.installed,
            version=result.version,
            total_rollouts=result.total_rollouts,
            healthy=result.healthy,
            progressing=result.progressing,
            degraded=result.degraded,
            paused=result.paused,
        )

    def xǁRolloutsDetectUseCaseǁexecute__mutmut_13(self, command: RolloutsDetectCommand) -> RolloutsDetectResponse:
        result = self._rollouts.detect_rollouts()
        return RolloutsDetectResponse(
            installed=result.installed,
            version=result.version,
            namespace=result.namespace,
            healthy=result.healthy,
            progressing=result.progressing,
            degraded=result.degraded,
            paused=result.paused,
        )

    def xǁRolloutsDetectUseCaseǁexecute__mutmut_14(self, command: RolloutsDetectCommand) -> RolloutsDetectResponse:
        result = self._rollouts.detect_rollouts()
        return RolloutsDetectResponse(
            installed=result.installed,
            version=result.version,
            namespace=result.namespace,
            total_rollouts=result.total_rollouts,
            progressing=result.progressing,
            degraded=result.degraded,
            paused=result.paused,
        )

    def xǁRolloutsDetectUseCaseǁexecute__mutmut_15(self, command: RolloutsDetectCommand) -> RolloutsDetectResponse:
        result = self._rollouts.detect_rollouts()
        return RolloutsDetectResponse(
            installed=result.installed,
            version=result.version,
            namespace=result.namespace,
            total_rollouts=result.total_rollouts,
            healthy=result.healthy,
            degraded=result.degraded,
            paused=result.paused,
        )

    def xǁRolloutsDetectUseCaseǁexecute__mutmut_16(self, command: RolloutsDetectCommand) -> RolloutsDetectResponse:
        result = self._rollouts.detect_rollouts()
        return RolloutsDetectResponse(
            installed=result.installed,
            version=result.version,
            namespace=result.namespace,
            total_rollouts=result.total_rollouts,
            healthy=result.healthy,
            progressing=result.progressing,
            paused=result.paused,
        )

    def xǁRolloutsDetectUseCaseǁexecute__mutmut_17(self, command: RolloutsDetectCommand) -> RolloutsDetectResponse:
        result = self._rollouts.detect_rollouts()
        return RolloutsDetectResponse(
            installed=result.installed,
            version=result.version,
            namespace=result.namespace,
            total_rollouts=result.total_rollouts,
            healthy=result.healthy,
            progressing=result.progressing,
            degraded=result.degraded,
            )

mutants_xǁRolloutsDetectUseCaseǁ__init____mutmut['_mutmut_orig'] = RolloutsDetectUseCase.xǁRolloutsDetectUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁRolloutsDetectUseCaseǁ__init____mutmut['xǁRolloutsDetectUseCaseǁ__init____mutmut_1'] = RolloutsDetectUseCase.xǁRolloutsDetectUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁRolloutsDetectUseCaseǁexecute__mutmut['_mutmut_orig'] = RolloutsDetectUseCase.xǁRolloutsDetectUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRolloutsDetectUseCaseǁexecute__mutmut['xǁRolloutsDetectUseCaseǁexecute__mutmut_1'] = RolloutsDetectUseCase.xǁRolloutsDetectUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRolloutsDetectUseCaseǁexecute__mutmut['xǁRolloutsDetectUseCaseǁexecute__mutmut_2'] = RolloutsDetectUseCase.xǁRolloutsDetectUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRolloutsDetectUseCaseǁexecute__mutmut['xǁRolloutsDetectUseCaseǁexecute__mutmut_3'] = RolloutsDetectUseCase.xǁRolloutsDetectUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRolloutsDetectUseCaseǁexecute__mutmut['xǁRolloutsDetectUseCaseǁexecute__mutmut_4'] = RolloutsDetectUseCase.xǁRolloutsDetectUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRolloutsDetectUseCaseǁexecute__mutmut['xǁRolloutsDetectUseCaseǁexecute__mutmut_5'] = RolloutsDetectUseCase.xǁRolloutsDetectUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRolloutsDetectUseCaseǁexecute__mutmut['xǁRolloutsDetectUseCaseǁexecute__mutmut_6'] = RolloutsDetectUseCase.xǁRolloutsDetectUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁRolloutsDetectUseCaseǁexecute__mutmut['xǁRolloutsDetectUseCaseǁexecute__mutmut_7'] = RolloutsDetectUseCase.xǁRolloutsDetectUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁRolloutsDetectUseCaseǁexecute__mutmut['xǁRolloutsDetectUseCaseǁexecute__mutmut_8'] = RolloutsDetectUseCase.xǁRolloutsDetectUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁRolloutsDetectUseCaseǁexecute__mutmut['xǁRolloutsDetectUseCaseǁexecute__mutmut_9'] = RolloutsDetectUseCase.xǁRolloutsDetectUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁRolloutsDetectUseCaseǁexecute__mutmut['xǁRolloutsDetectUseCaseǁexecute__mutmut_10'] = RolloutsDetectUseCase.xǁRolloutsDetectUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁRolloutsDetectUseCaseǁexecute__mutmut['xǁRolloutsDetectUseCaseǁexecute__mutmut_11'] = RolloutsDetectUseCase.xǁRolloutsDetectUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁRolloutsDetectUseCaseǁexecute__mutmut['xǁRolloutsDetectUseCaseǁexecute__mutmut_12'] = RolloutsDetectUseCase.xǁRolloutsDetectUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁRolloutsDetectUseCaseǁexecute__mutmut['xǁRolloutsDetectUseCaseǁexecute__mutmut_13'] = RolloutsDetectUseCase.xǁRolloutsDetectUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁRolloutsDetectUseCaseǁexecute__mutmut['xǁRolloutsDetectUseCaseǁexecute__mutmut_14'] = RolloutsDetectUseCase.xǁRolloutsDetectUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁRolloutsDetectUseCaseǁexecute__mutmut['xǁRolloutsDetectUseCaseǁexecute__mutmut_15'] = RolloutsDetectUseCase.xǁRolloutsDetectUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁRolloutsDetectUseCaseǁexecute__mutmut['xǁRolloutsDetectUseCaseǁexecute__mutmut_16'] = RolloutsDetectUseCase.xǁRolloutsDetectUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁRolloutsDetectUseCaseǁexecute__mutmut['xǁRolloutsDetectUseCaseǁexecute__mutmut_17'] = RolloutsDetectUseCase.xǁRolloutsDetectUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
