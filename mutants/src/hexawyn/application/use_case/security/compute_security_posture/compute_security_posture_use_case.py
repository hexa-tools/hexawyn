from __future__ import annotations

from hexawyn.application.ports.driven.security_posture_port import SecurityPosturePort
from hexawyn.application.use_case.security.compute_security_posture.command import (  # noqa: E501
    ComputeSecurityPostureCommand,
)
from hexawyn.application.use_case.security.compute_security_posture.response import (  # noqa: E501
    ComputeSecurityPostureResponse,
)
from hexawyn.domain.services.security_posture.security_posture_service import (
    SecurityPostureService,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁComputeSecurityPostureUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁComputeSecurityPostureUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class ComputeSecurityPostureUseCase:
    @_mutmut_mutated(mutants_xǁComputeSecurityPostureUseCaseǁ__init____mutmut)
    def __init__(self, posture_port: SecurityPosturePort) -> None:
        self._port = posture_port
        self._engine = SecurityPostureService()
    def xǁComputeSecurityPostureUseCaseǁ__init____mutmut_orig(self, posture_port: SecurityPosturePort) -> None:
        self._port = posture_port
        self._engine = SecurityPostureService()
    def xǁComputeSecurityPostureUseCaseǁ__init____mutmut_1(self, posture_port: SecurityPosturePort) -> None:
        self._port = None
        self._engine = SecurityPostureService()
    def xǁComputeSecurityPostureUseCaseǁ__init____mutmut_2(self, posture_port: SecurityPosturePort) -> None:
        self._port = posture_port
        self._engine = None

    @_mutmut_mutated(mutants_xǁComputeSecurityPostureUseCaseǁexecute__mutmut)
    def execute(self, command: ComputeSecurityPostureCommand) -> ComputeSecurityPostureResponse:
        records = self._port.list_workload_compliance()
        defined_categories = self._port.get_defined_categories()
        partial = self._port.is_partial()
        result = self._engine.build_report(
            records=records,
            defined_categories=defined_categories,
            partial=partial,
            previous_score_pct=command.previous_score_pct,
        )
        return ComputeSecurityPostureResponse(result=result)

    def xǁComputeSecurityPostureUseCaseǁexecute__mutmut_orig(self, command: ComputeSecurityPostureCommand) -> ComputeSecurityPostureResponse:
        records = self._port.list_workload_compliance()
        defined_categories = self._port.get_defined_categories()
        partial = self._port.is_partial()
        result = self._engine.build_report(
            records=records,
            defined_categories=defined_categories,
            partial=partial,
            previous_score_pct=command.previous_score_pct,
        )
        return ComputeSecurityPostureResponse(result=result)

    def xǁComputeSecurityPostureUseCaseǁexecute__mutmut_1(self, command: ComputeSecurityPostureCommand) -> ComputeSecurityPostureResponse:
        records = None
        defined_categories = self._port.get_defined_categories()
        partial = self._port.is_partial()
        result = self._engine.build_report(
            records=records,
            defined_categories=defined_categories,
            partial=partial,
            previous_score_pct=command.previous_score_pct,
        )
        return ComputeSecurityPostureResponse(result=result)

    def xǁComputeSecurityPostureUseCaseǁexecute__mutmut_2(self, command: ComputeSecurityPostureCommand) -> ComputeSecurityPostureResponse:
        records = self._port.list_workload_compliance()
        defined_categories = None
        partial = self._port.is_partial()
        result = self._engine.build_report(
            records=records,
            defined_categories=defined_categories,
            partial=partial,
            previous_score_pct=command.previous_score_pct,
        )
        return ComputeSecurityPostureResponse(result=result)

    def xǁComputeSecurityPostureUseCaseǁexecute__mutmut_3(self, command: ComputeSecurityPostureCommand) -> ComputeSecurityPostureResponse:
        records = self._port.list_workload_compliance()
        defined_categories = self._port.get_defined_categories()
        partial = None
        result = self._engine.build_report(
            records=records,
            defined_categories=defined_categories,
            partial=partial,
            previous_score_pct=command.previous_score_pct,
        )
        return ComputeSecurityPostureResponse(result=result)

    def xǁComputeSecurityPostureUseCaseǁexecute__mutmut_4(self, command: ComputeSecurityPostureCommand) -> ComputeSecurityPostureResponse:
        records = self._port.list_workload_compliance()
        defined_categories = self._port.get_defined_categories()
        partial = self._port.is_partial()
        result = None
        return ComputeSecurityPostureResponse(result=result)

    def xǁComputeSecurityPostureUseCaseǁexecute__mutmut_5(self, command: ComputeSecurityPostureCommand) -> ComputeSecurityPostureResponse:
        records = self._port.list_workload_compliance()
        defined_categories = self._port.get_defined_categories()
        partial = self._port.is_partial()
        result = self._engine.build_report(
            records=None,
            defined_categories=defined_categories,
            partial=partial,
            previous_score_pct=command.previous_score_pct,
        )
        return ComputeSecurityPostureResponse(result=result)

    def xǁComputeSecurityPostureUseCaseǁexecute__mutmut_6(self, command: ComputeSecurityPostureCommand) -> ComputeSecurityPostureResponse:
        records = self._port.list_workload_compliance()
        defined_categories = self._port.get_defined_categories()
        partial = self._port.is_partial()
        result = self._engine.build_report(
            records=records,
            defined_categories=None,
            partial=partial,
            previous_score_pct=command.previous_score_pct,
        )
        return ComputeSecurityPostureResponse(result=result)

    def xǁComputeSecurityPostureUseCaseǁexecute__mutmut_7(self, command: ComputeSecurityPostureCommand) -> ComputeSecurityPostureResponse:
        records = self._port.list_workload_compliance()
        defined_categories = self._port.get_defined_categories()
        partial = self._port.is_partial()
        result = self._engine.build_report(
            records=records,
            defined_categories=defined_categories,
            partial=None,
            previous_score_pct=command.previous_score_pct,
        )
        return ComputeSecurityPostureResponse(result=result)

    def xǁComputeSecurityPostureUseCaseǁexecute__mutmut_8(self, command: ComputeSecurityPostureCommand) -> ComputeSecurityPostureResponse:
        records = self._port.list_workload_compliance()
        defined_categories = self._port.get_defined_categories()
        partial = self._port.is_partial()
        result = self._engine.build_report(
            records=records,
            defined_categories=defined_categories,
            partial=partial,
            previous_score_pct=None,
        )
        return ComputeSecurityPostureResponse(result=result)

    def xǁComputeSecurityPostureUseCaseǁexecute__mutmut_9(self, command: ComputeSecurityPostureCommand) -> ComputeSecurityPostureResponse:
        records = self._port.list_workload_compliance()
        defined_categories = self._port.get_defined_categories()
        partial = self._port.is_partial()
        result = self._engine.build_report(
            defined_categories=defined_categories,
            partial=partial,
            previous_score_pct=command.previous_score_pct,
        )
        return ComputeSecurityPostureResponse(result=result)

    def xǁComputeSecurityPostureUseCaseǁexecute__mutmut_10(self, command: ComputeSecurityPostureCommand) -> ComputeSecurityPostureResponse:
        records = self._port.list_workload_compliance()
        defined_categories = self._port.get_defined_categories()
        partial = self._port.is_partial()
        result = self._engine.build_report(
            records=records,
            partial=partial,
            previous_score_pct=command.previous_score_pct,
        )
        return ComputeSecurityPostureResponse(result=result)

    def xǁComputeSecurityPostureUseCaseǁexecute__mutmut_11(self, command: ComputeSecurityPostureCommand) -> ComputeSecurityPostureResponse:
        records = self._port.list_workload_compliance()
        defined_categories = self._port.get_defined_categories()
        partial = self._port.is_partial()
        result = self._engine.build_report(
            records=records,
            defined_categories=defined_categories,
            previous_score_pct=command.previous_score_pct,
        )
        return ComputeSecurityPostureResponse(result=result)

    def xǁComputeSecurityPostureUseCaseǁexecute__mutmut_12(self, command: ComputeSecurityPostureCommand) -> ComputeSecurityPostureResponse:
        records = self._port.list_workload_compliance()
        defined_categories = self._port.get_defined_categories()
        partial = self._port.is_partial()
        result = self._engine.build_report(
            records=records,
            defined_categories=defined_categories,
            partial=partial,
            )
        return ComputeSecurityPostureResponse(result=result)

    def xǁComputeSecurityPostureUseCaseǁexecute__mutmut_13(self, command: ComputeSecurityPostureCommand) -> ComputeSecurityPostureResponse:
        records = self._port.list_workload_compliance()
        defined_categories = self._port.get_defined_categories()
        partial = self._port.is_partial()
        result = self._engine.build_report(
            records=records,
            defined_categories=defined_categories,
            partial=partial,
            previous_score_pct=command.previous_score_pct,
        )
        return ComputeSecurityPostureResponse(result=None)

mutants_xǁComputeSecurityPostureUseCaseǁ__init____mutmut['_mutmut_orig'] = ComputeSecurityPostureUseCase.xǁComputeSecurityPostureUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁComputeSecurityPostureUseCaseǁ__init____mutmut['xǁComputeSecurityPostureUseCaseǁ__init____mutmut_1'] = ComputeSecurityPostureUseCase.xǁComputeSecurityPostureUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁComputeSecurityPostureUseCaseǁ__init____mutmut['xǁComputeSecurityPostureUseCaseǁ__init____mutmut_2'] = ComputeSecurityPostureUseCase.xǁComputeSecurityPostureUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁComputeSecurityPostureUseCaseǁexecute__mutmut['_mutmut_orig'] = ComputeSecurityPostureUseCase.xǁComputeSecurityPostureUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁComputeSecurityPostureUseCaseǁexecute__mutmut['xǁComputeSecurityPostureUseCaseǁexecute__mutmut_1'] = ComputeSecurityPostureUseCase.xǁComputeSecurityPostureUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁComputeSecurityPostureUseCaseǁexecute__mutmut['xǁComputeSecurityPostureUseCaseǁexecute__mutmut_2'] = ComputeSecurityPostureUseCase.xǁComputeSecurityPostureUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁComputeSecurityPostureUseCaseǁexecute__mutmut['xǁComputeSecurityPostureUseCaseǁexecute__mutmut_3'] = ComputeSecurityPostureUseCase.xǁComputeSecurityPostureUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁComputeSecurityPostureUseCaseǁexecute__mutmut['xǁComputeSecurityPostureUseCaseǁexecute__mutmut_4'] = ComputeSecurityPostureUseCase.xǁComputeSecurityPostureUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁComputeSecurityPostureUseCaseǁexecute__mutmut['xǁComputeSecurityPostureUseCaseǁexecute__mutmut_5'] = ComputeSecurityPostureUseCase.xǁComputeSecurityPostureUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁComputeSecurityPostureUseCaseǁexecute__mutmut['xǁComputeSecurityPostureUseCaseǁexecute__mutmut_6'] = ComputeSecurityPostureUseCase.xǁComputeSecurityPostureUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁComputeSecurityPostureUseCaseǁexecute__mutmut['xǁComputeSecurityPostureUseCaseǁexecute__mutmut_7'] = ComputeSecurityPostureUseCase.xǁComputeSecurityPostureUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁComputeSecurityPostureUseCaseǁexecute__mutmut['xǁComputeSecurityPostureUseCaseǁexecute__mutmut_8'] = ComputeSecurityPostureUseCase.xǁComputeSecurityPostureUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁComputeSecurityPostureUseCaseǁexecute__mutmut['xǁComputeSecurityPostureUseCaseǁexecute__mutmut_9'] = ComputeSecurityPostureUseCase.xǁComputeSecurityPostureUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁComputeSecurityPostureUseCaseǁexecute__mutmut['xǁComputeSecurityPostureUseCaseǁexecute__mutmut_10'] = ComputeSecurityPostureUseCase.xǁComputeSecurityPostureUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁComputeSecurityPostureUseCaseǁexecute__mutmut['xǁComputeSecurityPostureUseCaseǁexecute__mutmut_11'] = ComputeSecurityPostureUseCase.xǁComputeSecurityPostureUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁComputeSecurityPostureUseCaseǁexecute__mutmut['xǁComputeSecurityPostureUseCaseǁexecute__mutmut_12'] = ComputeSecurityPostureUseCase.xǁComputeSecurityPostureUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁComputeSecurityPostureUseCaseǁexecute__mutmut['xǁComputeSecurityPostureUseCaseǁexecute__mutmut_13'] = ComputeSecurityPostureUseCase.xǁComputeSecurityPostureUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
