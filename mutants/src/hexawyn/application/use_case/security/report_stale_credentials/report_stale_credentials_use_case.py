from __future__ import annotations

from hexawyn.application.ports.driven.stale_credentials_port import StaleCredentialsPort
from hexawyn.application.use_case.security.report_stale_credentials.command import (  # noqa: E501
    ReportStaleCredentialsCommand,
)
from hexawyn.application.use_case.security.report_stale_credentials.response import (  # noqa: E501
    ReportStaleCredentialsResponse,
)
from hexawyn.domain.services.stale_credentials.stale_credentials_service import (
    compute_stale_credentials_report,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁReportStaleCredentialsUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁReportStaleCredentialsUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class ReportStaleCredentialsUseCase:
    @_mutmut_mutated(mutants_xǁReportStaleCredentialsUseCaseǁ__init____mutmut)
    def __init__(self, credentials_port: StaleCredentialsPort) -> None:
        self._port = credentials_port
    def xǁReportStaleCredentialsUseCaseǁ__init____mutmut_orig(self, credentials_port: StaleCredentialsPort) -> None:
        self._port = credentials_port
    def xǁReportStaleCredentialsUseCaseǁ__init____mutmut_1(self, credentials_port: StaleCredentialsPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁReportStaleCredentialsUseCaseǁexecute__mutmut)
    def execute(self, command: ReportStaleCredentialsCommand) -> ReportStaleCredentialsResponse:
        creds = self._port.get_stale_credentials(command.min_days)
        has_data = bool(creds)
        result = compute_stale_credentials_report(
            creds, has_data=has_data, period="Rotation en cours"
        )
        return ReportStaleCredentialsResponse(result=result)

    def xǁReportStaleCredentialsUseCaseǁexecute__mutmut_orig(self, command: ReportStaleCredentialsCommand) -> ReportStaleCredentialsResponse:
        creds = self._port.get_stale_credentials(command.min_days)
        has_data = bool(creds)
        result = compute_stale_credentials_report(
            creds, has_data=has_data, period="Rotation en cours"
        )
        return ReportStaleCredentialsResponse(result=result)

    def xǁReportStaleCredentialsUseCaseǁexecute__mutmut_1(self, command: ReportStaleCredentialsCommand) -> ReportStaleCredentialsResponse:
        creds = None
        has_data = bool(creds)
        result = compute_stale_credentials_report(
            creds, has_data=has_data, period="Rotation en cours"
        )
        return ReportStaleCredentialsResponse(result=result)

    def xǁReportStaleCredentialsUseCaseǁexecute__mutmut_2(self, command: ReportStaleCredentialsCommand) -> ReportStaleCredentialsResponse:
        creds = self._port.get_stale_credentials(None)
        has_data = bool(creds)
        result = compute_stale_credentials_report(
            creds, has_data=has_data, period="Rotation en cours"
        )
        return ReportStaleCredentialsResponse(result=result)

    def xǁReportStaleCredentialsUseCaseǁexecute__mutmut_3(self, command: ReportStaleCredentialsCommand) -> ReportStaleCredentialsResponse:
        creds = self._port.get_stale_credentials(command.min_days)
        has_data = None
        result = compute_stale_credentials_report(
            creds, has_data=has_data, period="Rotation en cours"
        )
        return ReportStaleCredentialsResponse(result=result)

    def xǁReportStaleCredentialsUseCaseǁexecute__mutmut_4(self, command: ReportStaleCredentialsCommand) -> ReportStaleCredentialsResponse:
        creds = self._port.get_stale_credentials(command.min_days)
        has_data = bool(None)
        result = compute_stale_credentials_report(
            creds, has_data=has_data, period="Rotation en cours"
        )
        return ReportStaleCredentialsResponse(result=result)

    def xǁReportStaleCredentialsUseCaseǁexecute__mutmut_5(self, command: ReportStaleCredentialsCommand) -> ReportStaleCredentialsResponse:
        creds = self._port.get_stale_credentials(command.min_days)
        has_data = bool(creds)
        result = None
        return ReportStaleCredentialsResponse(result=result)

    def xǁReportStaleCredentialsUseCaseǁexecute__mutmut_6(self, command: ReportStaleCredentialsCommand) -> ReportStaleCredentialsResponse:
        creds = self._port.get_stale_credentials(command.min_days)
        has_data = bool(creds)
        result = compute_stale_credentials_report(
            None, has_data=has_data, period="Rotation en cours"
        )
        return ReportStaleCredentialsResponse(result=result)

    def xǁReportStaleCredentialsUseCaseǁexecute__mutmut_7(self, command: ReportStaleCredentialsCommand) -> ReportStaleCredentialsResponse:
        creds = self._port.get_stale_credentials(command.min_days)
        has_data = bool(creds)
        result = compute_stale_credentials_report(
            creds, has_data=None, period="Rotation en cours"
        )
        return ReportStaleCredentialsResponse(result=result)

    def xǁReportStaleCredentialsUseCaseǁexecute__mutmut_8(self, command: ReportStaleCredentialsCommand) -> ReportStaleCredentialsResponse:
        creds = self._port.get_stale_credentials(command.min_days)
        has_data = bool(creds)
        result = compute_stale_credentials_report(
            creds, has_data=has_data, period=None
        )
        return ReportStaleCredentialsResponse(result=result)

    def xǁReportStaleCredentialsUseCaseǁexecute__mutmut_9(self, command: ReportStaleCredentialsCommand) -> ReportStaleCredentialsResponse:
        creds = self._port.get_stale_credentials(command.min_days)
        has_data = bool(creds)
        result = compute_stale_credentials_report(
            has_data=has_data, period="Rotation en cours"
        )
        return ReportStaleCredentialsResponse(result=result)

    def xǁReportStaleCredentialsUseCaseǁexecute__mutmut_10(self, command: ReportStaleCredentialsCommand) -> ReportStaleCredentialsResponse:
        creds = self._port.get_stale_credentials(command.min_days)
        has_data = bool(creds)
        result = compute_stale_credentials_report(
            creds, period="Rotation en cours"
        )
        return ReportStaleCredentialsResponse(result=result)

    def xǁReportStaleCredentialsUseCaseǁexecute__mutmut_11(self, command: ReportStaleCredentialsCommand) -> ReportStaleCredentialsResponse:
        creds = self._port.get_stale_credentials(command.min_days)
        has_data = bool(creds)
        result = compute_stale_credentials_report(
            creds, has_data=has_data, )
        return ReportStaleCredentialsResponse(result=result)

    def xǁReportStaleCredentialsUseCaseǁexecute__mutmut_12(self, command: ReportStaleCredentialsCommand) -> ReportStaleCredentialsResponse:
        creds = self._port.get_stale_credentials(command.min_days)
        has_data = bool(creds)
        result = compute_stale_credentials_report(
            creds, has_data=has_data, period="XXRotation en coursXX"
        )
        return ReportStaleCredentialsResponse(result=result)

    def xǁReportStaleCredentialsUseCaseǁexecute__mutmut_13(self, command: ReportStaleCredentialsCommand) -> ReportStaleCredentialsResponse:
        creds = self._port.get_stale_credentials(command.min_days)
        has_data = bool(creds)
        result = compute_stale_credentials_report(
            creds, has_data=has_data, period="rotation en cours"
        )
        return ReportStaleCredentialsResponse(result=result)

    def xǁReportStaleCredentialsUseCaseǁexecute__mutmut_14(self, command: ReportStaleCredentialsCommand) -> ReportStaleCredentialsResponse:
        creds = self._port.get_stale_credentials(command.min_days)
        has_data = bool(creds)
        result = compute_stale_credentials_report(
            creds, has_data=has_data, period="ROTATION EN COURS"
        )
        return ReportStaleCredentialsResponse(result=result)

    def xǁReportStaleCredentialsUseCaseǁexecute__mutmut_15(self, command: ReportStaleCredentialsCommand) -> ReportStaleCredentialsResponse:
        creds = self._port.get_stale_credentials(command.min_days)
        has_data = bool(creds)
        result = compute_stale_credentials_report(
            creds, has_data=has_data, period="Rotation en cours"
        )
        return ReportStaleCredentialsResponse(result=None)

mutants_xǁReportStaleCredentialsUseCaseǁ__init____mutmut['_mutmut_orig'] = ReportStaleCredentialsUseCase.xǁReportStaleCredentialsUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁReportStaleCredentialsUseCaseǁ__init____mutmut['xǁReportStaleCredentialsUseCaseǁ__init____mutmut_1'] = ReportStaleCredentialsUseCase.xǁReportStaleCredentialsUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁReportStaleCredentialsUseCaseǁexecute__mutmut['_mutmut_orig'] = ReportStaleCredentialsUseCase.xǁReportStaleCredentialsUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁReportStaleCredentialsUseCaseǁexecute__mutmut['xǁReportStaleCredentialsUseCaseǁexecute__mutmut_1'] = ReportStaleCredentialsUseCase.xǁReportStaleCredentialsUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁReportStaleCredentialsUseCaseǁexecute__mutmut['xǁReportStaleCredentialsUseCaseǁexecute__mutmut_2'] = ReportStaleCredentialsUseCase.xǁReportStaleCredentialsUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁReportStaleCredentialsUseCaseǁexecute__mutmut['xǁReportStaleCredentialsUseCaseǁexecute__mutmut_3'] = ReportStaleCredentialsUseCase.xǁReportStaleCredentialsUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁReportStaleCredentialsUseCaseǁexecute__mutmut['xǁReportStaleCredentialsUseCaseǁexecute__mutmut_4'] = ReportStaleCredentialsUseCase.xǁReportStaleCredentialsUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁReportStaleCredentialsUseCaseǁexecute__mutmut['xǁReportStaleCredentialsUseCaseǁexecute__mutmut_5'] = ReportStaleCredentialsUseCase.xǁReportStaleCredentialsUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁReportStaleCredentialsUseCaseǁexecute__mutmut['xǁReportStaleCredentialsUseCaseǁexecute__mutmut_6'] = ReportStaleCredentialsUseCase.xǁReportStaleCredentialsUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁReportStaleCredentialsUseCaseǁexecute__mutmut['xǁReportStaleCredentialsUseCaseǁexecute__mutmut_7'] = ReportStaleCredentialsUseCase.xǁReportStaleCredentialsUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁReportStaleCredentialsUseCaseǁexecute__mutmut['xǁReportStaleCredentialsUseCaseǁexecute__mutmut_8'] = ReportStaleCredentialsUseCase.xǁReportStaleCredentialsUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁReportStaleCredentialsUseCaseǁexecute__mutmut['xǁReportStaleCredentialsUseCaseǁexecute__mutmut_9'] = ReportStaleCredentialsUseCase.xǁReportStaleCredentialsUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁReportStaleCredentialsUseCaseǁexecute__mutmut['xǁReportStaleCredentialsUseCaseǁexecute__mutmut_10'] = ReportStaleCredentialsUseCase.xǁReportStaleCredentialsUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁReportStaleCredentialsUseCaseǁexecute__mutmut['xǁReportStaleCredentialsUseCaseǁexecute__mutmut_11'] = ReportStaleCredentialsUseCase.xǁReportStaleCredentialsUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁReportStaleCredentialsUseCaseǁexecute__mutmut['xǁReportStaleCredentialsUseCaseǁexecute__mutmut_12'] = ReportStaleCredentialsUseCase.xǁReportStaleCredentialsUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁReportStaleCredentialsUseCaseǁexecute__mutmut['xǁReportStaleCredentialsUseCaseǁexecute__mutmut_13'] = ReportStaleCredentialsUseCase.xǁReportStaleCredentialsUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁReportStaleCredentialsUseCaseǁexecute__mutmut['xǁReportStaleCredentialsUseCaseǁexecute__mutmut_14'] = ReportStaleCredentialsUseCase.xǁReportStaleCredentialsUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁReportStaleCredentialsUseCaseǁexecute__mutmut['xǁReportStaleCredentialsUseCaseǁexecute__mutmut_15'] = ReportStaleCredentialsUseCase.xǁReportStaleCredentialsUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
