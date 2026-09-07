from __future__ import annotations

from hexawyn.application.ports.driven.platform_reliability_port import (
    PlatformReliabilityPort,
)
from hexawyn.application.use_case.workloads.report_platform_reliability.command import (  # noqa: E501
    ReportPlatformReliabilityCommand,
)
from hexawyn.application.use_case.workloads.report_platform_reliability.response import (  # noqa: E501
    ReportPlatformReliabilityResponse,
)
from hexawyn.domain.services.platform_reliability.platform_reliability_service import (
    PlatformReliabilityService,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁReportPlatformReliabilityUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁReportPlatformReliabilityUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class ReportPlatformReliabilityUseCase:
    @_mutmut_mutated(mutants_xǁReportPlatformReliabilityUseCaseǁ__init____mutmut)
    def __init__(self, reliability_port: PlatformReliabilityPort) -> None:
        self._port = reliability_port
        self._engine = PlatformReliabilityService()
    def xǁReportPlatformReliabilityUseCaseǁ__init____mutmut_orig(self, reliability_port: PlatformReliabilityPort) -> None:
        self._port = reliability_port
        self._engine = PlatformReliabilityService()
    def xǁReportPlatformReliabilityUseCaseǁ__init____mutmut_1(self, reliability_port: PlatformReliabilityPort) -> None:
        self._port = None
        self._engine = PlatformReliabilityService()
    def xǁReportPlatformReliabilityUseCaseǁ__init____mutmut_2(self, reliability_port: PlatformReliabilityPort) -> None:
        self._port = reliability_port
        self._engine = None

    @_mutmut_mutated(mutants_xǁReportPlatformReliabilityUseCaseǁexecute__mutmut)
    def execute(
        self, command: ReportPlatformReliabilityCommand
    ) -> ReportPlatformReliabilityResponse:
        data = self._port.get_reliability_data(command.period)
        result = self._engine.generate(data, period=command.period)
        return ReportPlatformReliabilityResponse(result=result)

    def xǁReportPlatformReliabilityUseCaseǁexecute__mutmut_orig(
        self, command: ReportPlatformReliabilityCommand
    ) -> ReportPlatformReliabilityResponse:
        data = self._port.get_reliability_data(command.period)
        result = self._engine.generate(data, period=command.period)
        return ReportPlatformReliabilityResponse(result=result)

    def xǁReportPlatformReliabilityUseCaseǁexecute__mutmut_1(
        self, command: ReportPlatformReliabilityCommand
    ) -> ReportPlatformReliabilityResponse:
        data = None
        result = self._engine.generate(data, period=command.period)
        return ReportPlatformReliabilityResponse(result=result)

    def xǁReportPlatformReliabilityUseCaseǁexecute__mutmut_2(
        self, command: ReportPlatformReliabilityCommand
    ) -> ReportPlatformReliabilityResponse:
        data = self._port.get_reliability_data(None)
        result = self._engine.generate(data, period=command.period)
        return ReportPlatformReliabilityResponse(result=result)

    def xǁReportPlatformReliabilityUseCaseǁexecute__mutmut_3(
        self, command: ReportPlatformReliabilityCommand
    ) -> ReportPlatformReliabilityResponse:
        data = self._port.get_reliability_data(command.period)
        result = None
        return ReportPlatformReliabilityResponse(result=result)

    def xǁReportPlatformReliabilityUseCaseǁexecute__mutmut_4(
        self, command: ReportPlatformReliabilityCommand
    ) -> ReportPlatformReliabilityResponse:
        data = self._port.get_reliability_data(command.period)
        result = self._engine.generate(None, period=command.period)
        return ReportPlatformReliabilityResponse(result=result)

    def xǁReportPlatformReliabilityUseCaseǁexecute__mutmut_5(
        self, command: ReportPlatformReliabilityCommand
    ) -> ReportPlatformReliabilityResponse:
        data = self._port.get_reliability_data(command.period)
        result = self._engine.generate(data, period=None)
        return ReportPlatformReliabilityResponse(result=result)

    def xǁReportPlatformReliabilityUseCaseǁexecute__mutmut_6(
        self, command: ReportPlatformReliabilityCommand
    ) -> ReportPlatformReliabilityResponse:
        data = self._port.get_reliability_data(command.period)
        result = self._engine.generate(period=command.period)
        return ReportPlatformReliabilityResponse(result=result)

    def xǁReportPlatformReliabilityUseCaseǁexecute__mutmut_7(
        self, command: ReportPlatformReliabilityCommand
    ) -> ReportPlatformReliabilityResponse:
        data = self._port.get_reliability_data(command.period)
        result = self._engine.generate(data, )
        return ReportPlatformReliabilityResponse(result=result)

    def xǁReportPlatformReliabilityUseCaseǁexecute__mutmut_8(
        self, command: ReportPlatformReliabilityCommand
    ) -> ReportPlatformReliabilityResponse:
        data = self._port.get_reliability_data(command.period)
        result = self._engine.generate(data, period=command.period)
        return ReportPlatformReliabilityResponse(result=None)

mutants_xǁReportPlatformReliabilityUseCaseǁ__init____mutmut['_mutmut_orig'] = ReportPlatformReliabilityUseCase.xǁReportPlatformReliabilityUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁReportPlatformReliabilityUseCaseǁ__init____mutmut['xǁReportPlatformReliabilityUseCaseǁ__init____mutmut_1'] = ReportPlatformReliabilityUseCase.xǁReportPlatformReliabilityUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁReportPlatformReliabilityUseCaseǁ__init____mutmut['xǁReportPlatformReliabilityUseCaseǁ__init____mutmut_2'] = ReportPlatformReliabilityUseCase.xǁReportPlatformReliabilityUseCaseǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁReportPlatformReliabilityUseCaseǁexecute__mutmut['_mutmut_orig'] = ReportPlatformReliabilityUseCase.xǁReportPlatformReliabilityUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁReportPlatformReliabilityUseCaseǁexecute__mutmut['xǁReportPlatformReliabilityUseCaseǁexecute__mutmut_1'] = ReportPlatformReliabilityUseCase.xǁReportPlatformReliabilityUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁReportPlatformReliabilityUseCaseǁexecute__mutmut['xǁReportPlatformReliabilityUseCaseǁexecute__mutmut_2'] = ReportPlatformReliabilityUseCase.xǁReportPlatformReliabilityUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁReportPlatformReliabilityUseCaseǁexecute__mutmut['xǁReportPlatformReliabilityUseCaseǁexecute__mutmut_3'] = ReportPlatformReliabilityUseCase.xǁReportPlatformReliabilityUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁReportPlatformReliabilityUseCaseǁexecute__mutmut['xǁReportPlatformReliabilityUseCaseǁexecute__mutmut_4'] = ReportPlatformReliabilityUseCase.xǁReportPlatformReliabilityUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁReportPlatformReliabilityUseCaseǁexecute__mutmut['xǁReportPlatformReliabilityUseCaseǁexecute__mutmut_5'] = ReportPlatformReliabilityUseCase.xǁReportPlatformReliabilityUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁReportPlatformReliabilityUseCaseǁexecute__mutmut['xǁReportPlatformReliabilityUseCaseǁexecute__mutmut_6'] = ReportPlatformReliabilityUseCase.xǁReportPlatformReliabilityUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁReportPlatformReliabilityUseCaseǁexecute__mutmut['xǁReportPlatformReliabilityUseCaseǁexecute__mutmut_7'] = ReportPlatformReliabilityUseCase.xǁReportPlatformReliabilityUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁReportPlatformReliabilityUseCaseǁexecute__mutmut['xǁReportPlatformReliabilityUseCaseǁexecute__mutmut_8'] = ReportPlatformReliabilityUseCase.xǁReportPlatformReliabilityUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
