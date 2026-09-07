from __future__ import annotations

from hexawyn.application.ports.driven.unauthorized_access_port import UnauthorizedAccessPort
from hexawyn.application.use_case.security.report_unauthorized_access.command import (  # noqa: E501
    ReportUnauthorizedAccessCommand,
)
from hexawyn.application.use_case.security.report_unauthorized_access.response import (  # noqa: E501
    ReportUnauthorizedAccessResponse,
)
from hexawyn.domain.services.unauthorized_access.unauthorized_access_service import (
    compute_unauthorized_access_report,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁReportUnauthorizedAccessUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class ReportUnauthorizedAccessUseCase:
    @_mutmut_mutated(mutants_xǁReportUnauthorizedAccessUseCaseǁ__init____mutmut)
    def __init__(self, access_port: UnauthorizedAccessPort) -> None:
        self._port = access_port
    def xǁReportUnauthorizedAccessUseCaseǁ__init____mutmut_orig(self, access_port: UnauthorizedAccessPort) -> None:
        self._port = access_port
    def xǁReportUnauthorizedAccessUseCaseǁ__init____mutmut_1(self, access_port: UnauthorizedAccessPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut)
    def execute(self, command: ReportUnauthorizedAccessCommand) -> ReportUnauthorizedAccessResponse:
        raw = self._port.get_unauthorized_access_data()
        result = compute_unauthorized_access_report(
            raw, has_data=True, period="Dernieres 30 minutes"
        )
        return ReportUnauthorizedAccessResponse(result=result)

    def xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut_orig(self, command: ReportUnauthorizedAccessCommand) -> ReportUnauthorizedAccessResponse:
        raw = self._port.get_unauthorized_access_data()
        result = compute_unauthorized_access_report(
            raw, has_data=True, period="Dernieres 30 minutes"
        )
        return ReportUnauthorizedAccessResponse(result=result)

    def xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut_1(self, command: ReportUnauthorizedAccessCommand) -> ReportUnauthorizedAccessResponse:
        raw = None
        result = compute_unauthorized_access_report(
            raw, has_data=True, period="Dernieres 30 minutes"
        )
        return ReportUnauthorizedAccessResponse(result=result)

    def xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut_2(self, command: ReportUnauthorizedAccessCommand) -> ReportUnauthorizedAccessResponse:
        raw = self._port.get_unauthorized_access_data()
        result = None
        return ReportUnauthorizedAccessResponse(result=result)

    def xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut_3(self, command: ReportUnauthorizedAccessCommand) -> ReportUnauthorizedAccessResponse:
        raw = self._port.get_unauthorized_access_data()
        result = compute_unauthorized_access_report(
            None, has_data=True, period="Dernieres 30 minutes"
        )
        return ReportUnauthorizedAccessResponse(result=result)

    def xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut_4(self, command: ReportUnauthorizedAccessCommand) -> ReportUnauthorizedAccessResponse:
        raw = self._port.get_unauthorized_access_data()
        result = compute_unauthorized_access_report(
            raw, has_data=None, period="Dernieres 30 minutes"
        )
        return ReportUnauthorizedAccessResponse(result=result)

    def xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut_5(self, command: ReportUnauthorizedAccessCommand) -> ReportUnauthorizedAccessResponse:
        raw = self._port.get_unauthorized_access_data()
        result = compute_unauthorized_access_report(
            raw, has_data=True, period=None
        )
        return ReportUnauthorizedAccessResponse(result=result)

    def xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut_6(self, command: ReportUnauthorizedAccessCommand) -> ReportUnauthorizedAccessResponse:
        raw = self._port.get_unauthorized_access_data()
        result = compute_unauthorized_access_report(
            has_data=True, period="Dernieres 30 minutes"
        )
        return ReportUnauthorizedAccessResponse(result=result)

    def xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut_7(self, command: ReportUnauthorizedAccessCommand) -> ReportUnauthorizedAccessResponse:
        raw = self._port.get_unauthorized_access_data()
        result = compute_unauthorized_access_report(
            raw, period="Dernieres 30 minutes"
        )
        return ReportUnauthorizedAccessResponse(result=result)

    def xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut_8(self, command: ReportUnauthorizedAccessCommand) -> ReportUnauthorizedAccessResponse:
        raw = self._port.get_unauthorized_access_data()
        result = compute_unauthorized_access_report(
            raw, has_data=True, )
        return ReportUnauthorizedAccessResponse(result=result)

    def xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut_9(self, command: ReportUnauthorizedAccessCommand) -> ReportUnauthorizedAccessResponse:
        raw = self._port.get_unauthorized_access_data()
        result = compute_unauthorized_access_report(
            raw, has_data=False, period="Dernieres 30 minutes"
        )
        return ReportUnauthorizedAccessResponse(result=result)

    def xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut_10(self, command: ReportUnauthorizedAccessCommand) -> ReportUnauthorizedAccessResponse:
        raw = self._port.get_unauthorized_access_data()
        result = compute_unauthorized_access_report(
            raw, has_data=True, period="XXDernieres 30 minutesXX"
        )
        return ReportUnauthorizedAccessResponse(result=result)

    def xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut_11(self, command: ReportUnauthorizedAccessCommand) -> ReportUnauthorizedAccessResponse:
        raw = self._port.get_unauthorized_access_data()
        result = compute_unauthorized_access_report(
            raw, has_data=True, period="dernieres 30 minutes"
        )
        return ReportUnauthorizedAccessResponse(result=result)

    def xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut_12(self, command: ReportUnauthorizedAccessCommand) -> ReportUnauthorizedAccessResponse:
        raw = self._port.get_unauthorized_access_data()
        result = compute_unauthorized_access_report(
            raw, has_data=True, period="DERNIERES 30 MINUTES"
        )
        return ReportUnauthorizedAccessResponse(result=result)

    def xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut_13(self, command: ReportUnauthorizedAccessCommand) -> ReportUnauthorizedAccessResponse:
        raw = self._port.get_unauthorized_access_data()
        result = compute_unauthorized_access_report(
            raw, has_data=True, period="Dernieres 30 minutes"
        )
        return ReportUnauthorizedAccessResponse(result=None)

mutants_xǁReportUnauthorizedAccessUseCaseǁ__init____mutmut['_mutmut_orig'] = ReportUnauthorizedAccessUseCase.xǁReportUnauthorizedAccessUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁReportUnauthorizedAccessUseCaseǁ__init____mutmut['xǁReportUnauthorizedAccessUseCaseǁ__init____mutmut_1'] = ReportUnauthorizedAccessUseCase.xǁReportUnauthorizedAccessUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut['_mutmut_orig'] = ReportUnauthorizedAccessUseCase.xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut['xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut_1'] = ReportUnauthorizedAccessUseCase.xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut['xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut_2'] = ReportUnauthorizedAccessUseCase.xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut['xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut_3'] = ReportUnauthorizedAccessUseCase.xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut['xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut_4'] = ReportUnauthorizedAccessUseCase.xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut['xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut_5'] = ReportUnauthorizedAccessUseCase.xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut['xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut_6'] = ReportUnauthorizedAccessUseCase.xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut['xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut_7'] = ReportUnauthorizedAccessUseCase.xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut['xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut_8'] = ReportUnauthorizedAccessUseCase.xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut['xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut_9'] = ReportUnauthorizedAccessUseCase.xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut['xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut_10'] = ReportUnauthorizedAccessUseCase.xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut['xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut_11'] = ReportUnauthorizedAccessUseCase.xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut['xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut_12'] = ReportUnauthorizedAccessUseCase.xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut['xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut_13'] = ReportUnauthorizedAccessUseCase.xǁReportUnauthorizedAccessUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
