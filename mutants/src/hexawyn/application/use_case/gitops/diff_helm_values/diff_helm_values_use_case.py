from __future__ import annotations

from hexawyn.application.ports.driven.helm_values_diff_port import HelmValuesDiffPort
from hexawyn.application.use_case.gitops.diff_helm_values.command import (
    DiffHelmValuesCommand,
)
from hexawyn.application.use_case.gitops.diff_helm_values.response import (
    DiffHelmValuesResponse,
)
from hexawyn.domain.services.helm_values_diff.helm_values_diff_service import (
    HelmValuesDiffService,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁDiffHelmValuesUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁDiffHelmValuesUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class DiffHelmValuesUseCase:
    @_mutmut_mutated(mutants_xǁDiffHelmValuesUseCaseǁ__init____mutmut)
    def __init__(self, helm_values_port: HelmValuesDiffPort) -> None:
        self._port = helm_values_port
        self._engine = HelmValuesDiffService()
    def xǁDiffHelmValuesUseCaseǁ__init____mutmut_orig(self, helm_values_port: HelmValuesDiffPort) -> None:
        self._port = helm_values_port
        self._engine = HelmValuesDiffService()
    def xǁDiffHelmValuesUseCaseǁ__init____mutmut_1(self, helm_values_port: HelmValuesDiffPort) -> None:
        self._port = None
        self._engine = HelmValuesDiffService()
    def xǁDiffHelmValuesUseCaseǁ__init____mutmut_2(self, helm_values_port: HelmValuesDiffPort) -> None:
        self._port = helm_values_port
        self._engine = None

    @_mutmut_mutated(mutants_xǁDiffHelmValuesUseCaseǁexecute__mutmut)
    def execute(self, command: DiffHelmValuesCommand) -> DiffHelmValuesResponse:
        source = self._port.get_effective_values(command.release, command.source_namespace)  # type: ignore
        target = self._port.get_effective_values(command.release, command.target_namespace)  # type: ignore
        result = self._engine.diff(
            release=command.release,
            source_env=command.source_env,  # type: ignore
            target_env=command.target_env,  # type: ignore
            source_values=source["values"],
            target_values=target["values"],
        )
        return DiffHelmValuesResponse(result=result)  # type: ignore

    def xǁDiffHelmValuesUseCaseǁexecute__mutmut_orig(self, command: DiffHelmValuesCommand) -> DiffHelmValuesResponse:
        source = self._port.get_effective_values(command.release, command.source_namespace)  # type: ignore
        target = self._port.get_effective_values(command.release, command.target_namespace)  # type: ignore
        result = self._engine.diff(
            release=command.release,
            source_env=command.source_env,  # type: ignore
            target_env=command.target_env,  # type: ignore
            source_values=source["values"],
            target_values=target["values"],
        )
        return DiffHelmValuesResponse(result=result)  # type: ignore

    def xǁDiffHelmValuesUseCaseǁexecute__mutmut_1(self, command: DiffHelmValuesCommand) -> DiffHelmValuesResponse:
        source = None  # type: ignore
        target = self._port.get_effective_values(command.release, command.target_namespace)  # type: ignore
        result = self._engine.diff(
            release=command.release,
            source_env=command.source_env,  # type: ignore
            target_env=command.target_env,  # type: ignore
            source_values=source["values"],
            target_values=target["values"],
        )
        return DiffHelmValuesResponse(result=result)  # type: ignore

    def xǁDiffHelmValuesUseCaseǁexecute__mutmut_2(self, command: DiffHelmValuesCommand) -> DiffHelmValuesResponse:
        source = self._port.get_effective_values(None, command.source_namespace)  # type: ignore
        target = self._port.get_effective_values(command.release, command.target_namespace)  # type: ignore
        result = self._engine.diff(
            release=command.release,
            source_env=command.source_env,  # type: ignore
            target_env=command.target_env,  # type: ignore
            source_values=source["values"],
            target_values=target["values"],
        )
        return DiffHelmValuesResponse(result=result)  # type: ignore

    def xǁDiffHelmValuesUseCaseǁexecute__mutmut_3(self, command: DiffHelmValuesCommand) -> DiffHelmValuesResponse:
        source = self._port.get_effective_values(command.release, None)  # type: ignore
        target = self._port.get_effective_values(command.release, command.target_namespace)  # type: ignore
        result = self._engine.diff(
            release=command.release,
            source_env=command.source_env,  # type: ignore
            target_env=command.target_env,  # type: ignore
            source_values=source["values"],
            target_values=target["values"],
        )
        return DiffHelmValuesResponse(result=result)  # type: ignore

    def xǁDiffHelmValuesUseCaseǁexecute__mutmut_4(self, command: DiffHelmValuesCommand) -> DiffHelmValuesResponse:
        source = self._port.get_effective_values(command.source_namespace)  # type: ignore
        target = self._port.get_effective_values(command.release, command.target_namespace)  # type: ignore
        result = self._engine.diff(
            release=command.release,
            source_env=command.source_env,  # type: ignore
            target_env=command.target_env,  # type: ignore
            source_values=source["values"],
            target_values=target["values"],
        )
        return DiffHelmValuesResponse(result=result)  # type: ignore

    def xǁDiffHelmValuesUseCaseǁexecute__mutmut_5(self, command: DiffHelmValuesCommand) -> DiffHelmValuesResponse:
        source = self._port.get_effective_values(command.release, )  # type: ignore
        target = self._port.get_effective_values(command.release, command.target_namespace)  # type: ignore
        result = self._engine.diff(
            release=command.release,
            source_env=command.source_env,  # type: ignore
            target_env=command.target_env,  # type: ignore
            source_values=source["values"],
            target_values=target["values"],
        )
        return DiffHelmValuesResponse(result=result)  # type: ignore

    def xǁDiffHelmValuesUseCaseǁexecute__mutmut_6(self, command: DiffHelmValuesCommand) -> DiffHelmValuesResponse:
        source = self._port.get_effective_values(command.release, command.source_namespace)  # type: ignore
        target = None  # type: ignore
        result = self._engine.diff(
            release=command.release,
            source_env=command.source_env,  # type: ignore
            target_env=command.target_env,  # type: ignore
            source_values=source["values"],
            target_values=target["values"],
        )
        return DiffHelmValuesResponse(result=result)  # type: ignore

    def xǁDiffHelmValuesUseCaseǁexecute__mutmut_7(self, command: DiffHelmValuesCommand) -> DiffHelmValuesResponse:
        source = self._port.get_effective_values(command.release, command.source_namespace)  # type: ignore
        target = self._port.get_effective_values(None, command.target_namespace)  # type: ignore
        result = self._engine.diff(
            release=command.release,
            source_env=command.source_env,  # type: ignore
            target_env=command.target_env,  # type: ignore
            source_values=source["values"],
            target_values=target["values"],
        )
        return DiffHelmValuesResponse(result=result)  # type: ignore

    def xǁDiffHelmValuesUseCaseǁexecute__mutmut_8(self, command: DiffHelmValuesCommand) -> DiffHelmValuesResponse:
        source = self._port.get_effective_values(command.release, command.source_namespace)  # type: ignore
        target = self._port.get_effective_values(command.release, None)  # type: ignore
        result = self._engine.diff(
            release=command.release,
            source_env=command.source_env,  # type: ignore
            target_env=command.target_env,  # type: ignore
            source_values=source["values"],
            target_values=target["values"],
        )
        return DiffHelmValuesResponse(result=result)  # type: ignore

    def xǁDiffHelmValuesUseCaseǁexecute__mutmut_9(self, command: DiffHelmValuesCommand) -> DiffHelmValuesResponse:
        source = self._port.get_effective_values(command.release, command.source_namespace)  # type: ignore
        target = self._port.get_effective_values(command.target_namespace)  # type: ignore
        result = self._engine.diff(
            release=command.release,
            source_env=command.source_env,  # type: ignore
            target_env=command.target_env,  # type: ignore
            source_values=source["values"],
            target_values=target["values"],
        )
        return DiffHelmValuesResponse(result=result)  # type: ignore

    def xǁDiffHelmValuesUseCaseǁexecute__mutmut_10(self, command: DiffHelmValuesCommand) -> DiffHelmValuesResponse:
        source = self._port.get_effective_values(command.release, command.source_namespace)  # type: ignore
        target = self._port.get_effective_values(command.release, )  # type: ignore
        result = self._engine.diff(
            release=command.release,
            source_env=command.source_env,  # type: ignore
            target_env=command.target_env,  # type: ignore
            source_values=source["values"],
            target_values=target["values"],
        )
        return DiffHelmValuesResponse(result=result)  # type: ignore

    def xǁDiffHelmValuesUseCaseǁexecute__mutmut_11(self, command: DiffHelmValuesCommand) -> DiffHelmValuesResponse:
        source = self._port.get_effective_values(command.release, command.source_namespace)  # type: ignore
        target = self._port.get_effective_values(command.release, command.target_namespace)  # type: ignore
        result = None
        return DiffHelmValuesResponse(result=result)  # type: ignore

    def xǁDiffHelmValuesUseCaseǁexecute__mutmut_12(self, command: DiffHelmValuesCommand) -> DiffHelmValuesResponse:
        source = self._port.get_effective_values(command.release, command.source_namespace)  # type: ignore
        target = self._port.get_effective_values(command.release, command.target_namespace)  # type: ignore
        result = self._engine.diff(
            release=None,
            source_env=command.source_env,  # type: ignore
            target_env=command.target_env,  # type: ignore
            source_values=source["values"],
            target_values=target["values"],
        )
        return DiffHelmValuesResponse(result=result)  # type: ignore

    def xǁDiffHelmValuesUseCaseǁexecute__mutmut_13(self, command: DiffHelmValuesCommand) -> DiffHelmValuesResponse:
        source = self._port.get_effective_values(command.release, command.source_namespace)  # type: ignore
        target = self._port.get_effective_values(command.release, command.target_namespace)  # type: ignore
        result = self._engine.diff(
            release=command.release,
            source_env=None,  # type: ignore
            target_env=command.target_env,  # type: ignore
            source_values=source["values"],
            target_values=target["values"],
        )
        return DiffHelmValuesResponse(result=result)  # type: ignore

    def xǁDiffHelmValuesUseCaseǁexecute__mutmut_14(self, command: DiffHelmValuesCommand) -> DiffHelmValuesResponse:
        source = self._port.get_effective_values(command.release, command.source_namespace)  # type: ignore
        target = self._port.get_effective_values(command.release, command.target_namespace)  # type: ignore
        result = self._engine.diff(
            release=command.release,
            source_env=command.source_env,  # type: ignore
            target_env=None,  # type: ignore
            source_values=source["values"],
            target_values=target["values"],
        )
        return DiffHelmValuesResponse(result=result)  # type: ignore

    def xǁDiffHelmValuesUseCaseǁexecute__mutmut_15(self, command: DiffHelmValuesCommand) -> DiffHelmValuesResponse:
        source = self._port.get_effective_values(command.release, command.source_namespace)  # type: ignore
        target = self._port.get_effective_values(command.release, command.target_namespace)  # type: ignore
        result = self._engine.diff(
            release=command.release,
            source_env=command.source_env,  # type: ignore
            target_env=command.target_env,  # type: ignore
            source_values=None,
            target_values=target["values"],
        )
        return DiffHelmValuesResponse(result=result)  # type: ignore

    def xǁDiffHelmValuesUseCaseǁexecute__mutmut_16(self, command: DiffHelmValuesCommand) -> DiffHelmValuesResponse:
        source = self._port.get_effective_values(command.release, command.source_namespace)  # type: ignore
        target = self._port.get_effective_values(command.release, command.target_namespace)  # type: ignore
        result = self._engine.diff(
            release=command.release,
            source_env=command.source_env,  # type: ignore
            target_env=command.target_env,  # type: ignore
            source_values=source["values"],
            target_values=None,
        )
        return DiffHelmValuesResponse(result=result)  # type: ignore

    def xǁDiffHelmValuesUseCaseǁexecute__mutmut_17(self, command: DiffHelmValuesCommand) -> DiffHelmValuesResponse:
        source = self._port.get_effective_values(command.release, command.source_namespace)  # type: ignore
        target = self._port.get_effective_values(command.release, command.target_namespace)  # type: ignore
        result = self._engine.diff(
            source_env=command.source_env,  # type: ignore
            target_env=command.target_env,  # type: ignore
            source_values=source["values"],
            target_values=target["values"],
        )
        return DiffHelmValuesResponse(result=result)  # type: ignore

    def xǁDiffHelmValuesUseCaseǁexecute__mutmut_18(self, command: DiffHelmValuesCommand) -> DiffHelmValuesResponse:
        source = self._port.get_effective_values(command.release, command.source_namespace)  # type: ignore
        target = self._port.get_effective_values(command.release, command.target_namespace)  # type: ignore
        result = self._engine.diff(
            release=command.release,
            target_env=command.target_env,  # type: ignore
            source_values=source["values"],
            target_values=target["values"],
        )
        return DiffHelmValuesResponse(result=result)  # type: ignore

    def xǁDiffHelmValuesUseCaseǁexecute__mutmut_19(self, command: DiffHelmValuesCommand) -> DiffHelmValuesResponse:
        source = self._port.get_effective_values(command.release, command.source_namespace)  # type: ignore
        target = self._port.get_effective_values(command.release, command.target_namespace)  # type: ignore
        result = self._engine.diff(
            release=command.release,
            source_env=command.source_env,  # type: ignore
            source_values=source["values"],
            target_values=target["values"],
        )
        return DiffHelmValuesResponse(result=result)  # type: ignore

    def xǁDiffHelmValuesUseCaseǁexecute__mutmut_20(self, command: DiffHelmValuesCommand) -> DiffHelmValuesResponse:
        source = self._port.get_effective_values(command.release, command.source_namespace)  # type: ignore
        target = self._port.get_effective_values(command.release, command.target_namespace)  # type: ignore
        result = self._engine.diff(
            release=command.release,
            source_env=command.source_env,  # type: ignore
            target_env=command.target_env,  # type: ignore
            target_values=target["values"],
        )
        return DiffHelmValuesResponse(result=result)  # type: ignore

    def xǁDiffHelmValuesUseCaseǁexecute__mutmut_21(self, command: DiffHelmValuesCommand) -> DiffHelmValuesResponse:
        source = self._port.get_effective_values(command.release, command.source_namespace)  # type: ignore
        target = self._port.get_effective_values(command.release, command.target_namespace)  # type: ignore
        result = self._engine.diff(
            release=command.release,
            source_env=command.source_env,  # type: ignore
            target_env=command.target_env,  # type: ignore
            source_values=source["values"],
            )
        return DiffHelmValuesResponse(result=result)  # type: ignore

    def xǁDiffHelmValuesUseCaseǁexecute__mutmut_22(self, command: DiffHelmValuesCommand) -> DiffHelmValuesResponse:
        source = self._port.get_effective_values(command.release, command.source_namespace)  # type: ignore
        target = self._port.get_effective_values(command.release, command.target_namespace)  # type: ignore
        result = self._engine.diff(
            release=command.release,
            source_env=command.source_env,  # type: ignore
            target_env=command.target_env,  # type: ignore
            source_values=source["XXvaluesXX"],
            target_values=target["values"],
        )
        return DiffHelmValuesResponse(result=result)  # type: ignore

    def xǁDiffHelmValuesUseCaseǁexecute__mutmut_23(self, command: DiffHelmValuesCommand) -> DiffHelmValuesResponse:
        source = self._port.get_effective_values(command.release, command.source_namespace)  # type: ignore
        target = self._port.get_effective_values(command.release, command.target_namespace)  # type: ignore
        result = self._engine.diff(
            release=command.release,
            source_env=command.source_env,  # type: ignore
            target_env=command.target_env,  # type: ignore
            source_values=source["VALUES"],
            target_values=target["values"],
        )
        return DiffHelmValuesResponse(result=result)  # type: ignore

    def xǁDiffHelmValuesUseCaseǁexecute__mutmut_24(self, command: DiffHelmValuesCommand) -> DiffHelmValuesResponse:
        source = self._port.get_effective_values(command.release, command.source_namespace)  # type: ignore
        target = self._port.get_effective_values(command.release, command.target_namespace)  # type: ignore
        result = self._engine.diff(
            release=command.release,
            source_env=command.source_env,  # type: ignore
            target_env=command.target_env,  # type: ignore
            source_values=source["values"],
            target_values=target["XXvaluesXX"],
        )
        return DiffHelmValuesResponse(result=result)  # type: ignore

    def xǁDiffHelmValuesUseCaseǁexecute__mutmut_25(self, command: DiffHelmValuesCommand) -> DiffHelmValuesResponse:
        source = self._port.get_effective_values(command.release, command.source_namespace)  # type: ignore
        target = self._port.get_effective_values(command.release, command.target_namespace)  # type: ignore
        result = self._engine.diff(
            release=command.release,
            source_env=command.source_env,  # type: ignore
            target_env=command.target_env,  # type: ignore
            source_values=source["values"],
            target_values=target["VALUES"],
        )
        return DiffHelmValuesResponse(result=result)  # type: ignore

    def xǁDiffHelmValuesUseCaseǁexecute__mutmut_26(self, command: DiffHelmValuesCommand) -> DiffHelmValuesResponse:
        source = self._port.get_effective_values(command.release, command.source_namespace)  # type: ignore
        target = self._port.get_effective_values(command.release, command.target_namespace)  # type: ignore
        result = self._engine.diff(
            release=command.release,
            source_env=command.source_env,  # type: ignore
            target_env=command.target_env,  # type: ignore
            source_values=source["values"],
            target_values=target["values"],
        )
        return DiffHelmValuesResponse(result=None)  # type: ignore

mutants_xǁDiffHelmValuesUseCaseǁ__init____mutmut['_mutmut_orig'] = DiffHelmValuesUseCase.xǁDiffHelmValuesUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁDiffHelmValuesUseCaseǁ__init____mutmut['xǁDiffHelmValuesUseCaseǁ__init____mutmut_1'] = DiffHelmValuesUseCase.xǁDiffHelmValuesUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁDiffHelmValuesUseCaseǁ__init____mutmut['xǁDiffHelmValuesUseCaseǁ__init____mutmut_2'] = DiffHelmValuesUseCase.xǁDiffHelmValuesUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁDiffHelmValuesUseCaseǁexecute__mutmut['_mutmut_orig'] = DiffHelmValuesUseCase.xǁDiffHelmValuesUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁDiffHelmValuesUseCaseǁexecute__mutmut['xǁDiffHelmValuesUseCaseǁexecute__mutmut_1'] = DiffHelmValuesUseCase.xǁDiffHelmValuesUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁDiffHelmValuesUseCaseǁexecute__mutmut['xǁDiffHelmValuesUseCaseǁexecute__mutmut_2'] = DiffHelmValuesUseCase.xǁDiffHelmValuesUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁDiffHelmValuesUseCaseǁexecute__mutmut['xǁDiffHelmValuesUseCaseǁexecute__mutmut_3'] = DiffHelmValuesUseCase.xǁDiffHelmValuesUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁDiffHelmValuesUseCaseǁexecute__mutmut['xǁDiffHelmValuesUseCaseǁexecute__mutmut_4'] = DiffHelmValuesUseCase.xǁDiffHelmValuesUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁDiffHelmValuesUseCaseǁexecute__mutmut['xǁDiffHelmValuesUseCaseǁexecute__mutmut_5'] = DiffHelmValuesUseCase.xǁDiffHelmValuesUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁDiffHelmValuesUseCaseǁexecute__mutmut['xǁDiffHelmValuesUseCaseǁexecute__mutmut_6'] = DiffHelmValuesUseCase.xǁDiffHelmValuesUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁDiffHelmValuesUseCaseǁexecute__mutmut['xǁDiffHelmValuesUseCaseǁexecute__mutmut_7'] = DiffHelmValuesUseCase.xǁDiffHelmValuesUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁDiffHelmValuesUseCaseǁexecute__mutmut['xǁDiffHelmValuesUseCaseǁexecute__mutmut_8'] = DiffHelmValuesUseCase.xǁDiffHelmValuesUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁDiffHelmValuesUseCaseǁexecute__mutmut['xǁDiffHelmValuesUseCaseǁexecute__mutmut_9'] = DiffHelmValuesUseCase.xǁDiffHelmValuesUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁDiffHelmValuesUseCaseǁexecute__mutmut['xǁDiffHelmValuesUseCaseǁexecute__mutmut_10'] = DiffHelmValuesUseCase.xǁDiffHelmValuesUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁDiffHelmValuesUseCaseǁexecute__mutmut['xǁDiffHelmValuesUseCaseǁexecute__mutmut_11'] = DiffHelmValuesUseCase.xǁDiffHelmValuesUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁDiffHelmValuesUseCaseǁexecute__mutmut['xǁDiffHelmValuesUseCaseǁexecute__mutmut_12'] = DiffHelmValuesUseCase.xǁDiffHelmValuesUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁDiffHelmValuesUseCaseǁexecute__mutmut['xǁDiffHelmValuesUseCaseǁexecute__mutmut_13'] = DiffHelmValuesUseCase.xǁDiffHelmValuesUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁDiffHelmValuesUseCaseǁexecute__mutmut['xǁDiffHelmValuesUseCaseǁexecute__mutmut_14'] = DiffHelmValuesUseCase.xǁDiffHelmValuesUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁDiffHelmValuesUseCaseǁexecute__mutmut['xǁDiffHelmValuesUseCaseǁexecute__mutmut_15'] = DiffHelmValuesUseCase.xǁDiffHelmValuesUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁDiffHelmValuesUseCaseǁexecute__mutmut['xǁDiffHelmValuesUseCaseǁexecute__mutmut_16'] = DiffHelmValuesUseCase.xǁDiffHelmValuesUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁDiffHelmValuesUseCaseǁexecute__mutmut['xǁDiffHelmValuesUseCaseǁexecute__mutmut_17'] = DiffHelmValuesUseCase.xǁDiffHelmValuesUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁDiffHelmValuesUseCaseǁexecute__mutmut['xǁDiffHelmValuesUseCaseǁexecute__mutmut_18'] = DiffHelmValuesUseCase.xǁDiffHelmValuesUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁDiffHelmValuesUseCaseǁexecute__mutmut['xǁDiffHelmValuesUseCaseǁexecute__mutmut_19'] = DiffHelmValuesUseCase.xǁDiffHelmValuesUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁDiffHelmValuesUseCaseǁexecute__mutmut['xǁDiffHelmValuesUseCaseǁexecute__mutmut_20'] = DiffHelmValuesUseCase.xǁDiffHelmValuesUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁDiffHelmValuesUseCaseǁexecute__mutmut['xǁDiffHelmValuesUseCaseǁexecute__mutmut_21'] = DiffHelmValuesUseCase.xǁDiffHelmValuesUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁDiffHelmValuesUseCaseǁexecute__mutmut['xǁDiffHelmValuesUseCaseǁexecute__mutmut_22'] = DiffHelmValuesUseCase.xǁDiffHelmValuesUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁDiffHelmValuesUseCaseǁexecute__mutmut['xǁDiffHelmValuesUseCaseǁexecute__mutmut_23'] = DiffHelmValuesUseCase.xǁDiffHelmValuesUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁDiffHelmValuesUseCaseǁexecute__mutmut['xǁDiffHelmValuesUseCaseǁexecute__mutmut_24'] = DiffHelmValuesUseCase.xǁDiffHelmValuesUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁDiffHelmValuesUseCaseǁexecute__mutmut['xǁDiffHelmValuesUseCaseǁexecute__mutmut_25'] = DiffHelmValuesUseCase.xǁDiffHelmValuesUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁDiffHelmValuesUseCaseǁexecute__mutmut['xǁDiffHelmValuesUseCaseǁexecute__mutmut_26'] = DiffHelmValuesUseCase.xǁDiffHelmValuesUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
