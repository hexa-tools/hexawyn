from __future__ import annotations

from hexawyn.application.ports.driven.critical_cve_port import CriticalCvePort
from hexawyn.application.use_case.security.report_critical_vulnerabilities.command import (  # noqa: E501
    ReportCriticalVulnerabilitiesCommand,
)
from hexawyn.application.use_case.security.report_critical_vulnerabilities.response import (  # noqa: E501
    ReportCriticalVulnerabilitiesResponse,
)
from hexawyn.domain.services.critical_cve.critical_cve_service import (
    compute_critical_cve_report,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁReportCriticalVulnerabilitiesUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class ReportCriticalVulnerabilitiesUseCase:
    @_mutmut_mutated(mutants_xǁReportCriticalVulnerabilitiesUseCaseǁ__init____mutmut)
    def __init__(self, cve_port: CriticalCvePort) -> None:
        self._port = cve_port
    def xǁReportCriticalVulnerabilitiesUseCaseǁ__init____mutmut_orig(self, cve_port: CriticalCvePort) -> None:
        self._port = cve_port
    def xǁReportCriticalVulnerabilitiesUseCaseǁ__init____mutmut_1(self, cve_port: CriticalCvePort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut)
    def execute(
        self, command: ReportCriticalVulnerabilitiesCommand
    ) -> ReportCriticalVulnerabilitiesResponse:
        cves = self._port.get_critical_cves()
        has_data = bool(cves)
        result = compute_critical_cve_report(
            cves, total_scanned=len(cves), has_data=has_data, period="Dernier scan"
        )
        return ReportCriticalVulnerabilitiesResponse(result=result)

    def xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_orig(
        self, command: ReportCriticalVulnerabilitiesCommand
    ) -> ReportCriticalVulnerabilitiesResponse:
        cves = self._port.get_critical_cves()
        has_data = bool(cves)
        result = compute_critical_cve_report(
            cves, total_scanned=len(cves), has_data=has_data, period="Dernier scan"
        )
        return ReportCriticalVulnerabilitiesResponse(result=result)

    def xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_1(
        self, command: ReportCriticalVulnerabilitiesCommand
    ) -> ReportCriticalVulnerabilitiesResponse:
        cves = None
        has_data = bool(cves)
        result = compute_critical_cve_report(
            cves, total_scanned=len(cves), has_data=has_data, period="Dernier scan"
        )
        return ReportCriticalVulnerabilitiesResponse(result=result)

    def xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_2(
        self, command: ReportCriticalVulnerabilitiesCommand
    ) -> ReportCriticalVulnerabilitiesResponse:
        cves = self._port.get_critical_cves()
        has_data = None
        result = compute_critical_cve_report(
            cves, total_scanned=len(cves), has_data=has_data, period="Dernier scan"
        )
        return ReportCriticalVulnerabilitiesResponse(result=result)

    def xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_3(
        self, command: ReportCriticalVulnerabilitiesCommand
    ) -> ReportCriticalVulnerabilitiesResponse:
        cves = self._port.get_critical_cves()
        has_data = bool(None)
        result = compute_critical_cve_report(
            cves, total_scanned=len(cves), has_data=has_data, period="Dernier scan"
        )
        return ReportCriticalVulnerabilitiesResponse(result=result)

    def xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_4(
        self, command: ReportCriticalVulnerabilitiesCommand
    ) -> ReportCriticalVulnerabilitiesResponse:
        cves = self._port.get_critical_cves()
        has_data = bool(cves)
        result = None
        return ReportCriticalVulnerabilitiesResponse(result=result)

    def xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_5(
        self, command: ReportCriticalVulnerabilitiesCommand
    ) -> ReportCriticalVulnerabilitiesResponse:
        cves = self._port.get_critical_cves()
        has_data = bool(cves)
        result = compute_critical_cve_report(
            None, total_scanned=len(cves), has_data=has_data, period="Dernier scan"
        )
        return ReportCriticalVulnerabilitiesResponse(result=result)

    def xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_6(
        self, command: ReportCriticalVulnerabilitiesCommand
    ) -> ReportCriticalVulnerabilitiesResponse:
        cves = self._port.get_critical_cves()
        has_data = bool(cves)
        result = compute_critical_cve_report(
            cves, total_scanned=None, has_data=has_data, period="Dernier scan"
        )
        return ReportCriticalVulnerabilitiesResponse(result=result)

    def xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_7(
        self, command: ReportCriticalVulnerabilitiesCommand
    ) -> ReportCriticalVulnerabilitiesResponse:
        cves = self._port.get_critical_cves()
        has_data = bool(cves)
        result = compute_critical_cve_report(
            cves, total_scanned=len(cves), has_data=None, period="Dernier scan"
        )
        return ReportCriticalVulnerabilitiesResponse(result=result)

    def xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_8(
        self, command: ReportCriticalVulnerabilitiesCommand
    ) -> ReportCriticalVulnerabilitiesResponse:
        cves = self._port.get_critical_cves()
        has_data = bool(cves)
        result = compute_critical_cve_report(
            cves, total_scanned=len(cves), has_data=has_data, period=None
        )
        return ReportCriticalVulnerabilitiesResponse(result=result)

    def xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_9(
        self, command: ReportCriticalVulnerabilitiesCommand
    ) -> ReportCriticalVulnerabilitiesResponse:
        cves = self._port.get_critical_cves()
        has_data = bool(cves)
        result = compute_critical_cve_report(
            total_scanned=len(cves), has_data=has_data, period="Dernier scan"
        )
        return ReportCriticalVulnerabilitiesResponse(result=result)

    def xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_10(
        self, command: ReportCriticalVulnerabilitiesCommand
    ) -> ReportCriticalVulnerabilitiesResponse:
        cves = self._port.get_critical_cves()
        has_data = bool(cves)
        result = compute_critical_cve_report(
            cves, has_data=has_data, period="Dernier scan"
        )
        return ReportCriticalVulnerabilitiesResponse(result=result)

    def xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_11(
        self, command: ReportCriticalVulnerabilitiesCommand
    ) -> ReportCriticalVulnerabilitiesResponse:
        cves = self._port.get_critical_cves()
        has_data = bool(cves)
        result = compute_critical_cve_report(
            cves, total_scanned=len(cves), period="Dernier scan"
        )
        return ReportCriticalVulnerabilitiesResponse(result=result)

    def xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_12(
        self, command: ReportCriticalVulnerabilitiesCommand
    ) -> ReportCriticalVulnerabilitiesResponse:
        cves = self._port.get_critical_cves()
        has_data = bool(cves)
        result = compute_critical_cve_report(
            cves, total_scanned=len(cves), has_data=has_data, )
        return ReportCriticalVulnerabilitiesResponse(result=result)

    def xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_13(
        self, command: ReportCriticalVulnerabilitiesCommand
    ) -> ReportCriticalVulnerabilitiesResponse:
        cves = self._port.get_critical_cves()
        has_data = bool(cves)
        result = compute_critical_cve_report(
            cves, total_scanned=len(cves), has_data=has_data, period="XXDernier scanXX"
        )
        return ReportCriticalVulnerabilitiesResponse(result=result)

    def xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_14(
        self, command: ReportCriticalVulnerabilitiesCommand
    ) -> ReportCriticalVulnerabilitiesResponse:
        cves = self._port.get_critical_cves()
        has_data = bool(cves)
        result = compute_critical_cve_report(
            cves, total_scanned=len(cves), has_data=has_data, period="dernier scan"
        )
        return ReportCriticalVulnerabilitiesResponse(result=result)

    def xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_15(
        self, command: ReportCriticalVulnerabilitiesCommand
    ) -> ReportCriticalVulnerabilitiesResponse:
        cves = self._port.get_critical_cves()
        has_data = bool(cves)
        result = compute_critical_cve_report(
            cves, total_scanned=len(cves), has_data=has_data, period="DERNIER SCAN"
        )
        return ReportCriticalVulnerabilitiesResponse(result=result)

    def xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_16(
        self, command: ReportCriticalVulnerabilitiesCommand
    ) -> ReportCriticalVulnerabilitiesResponse:
        cves = self._port.get_critical_cves()
        has_data = bool(cves)
        result = compute_critical_cve_report(
            cves, total_scanned=len(cves), has_data=has_data, period="Dernier scan"
        )
        return ReportCriticalVulnerabilitiesResponse(result=None)

mutants_xǁReportCriticalVulnerabilitiesUseCaseǁ__init____mutmut['_mutmut_orig'] = ReportCriticalVulnerabilitiesUseCase.xǁReportCriticalVulnerabilitiesUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁReportCriticalVulnerabilitiesUseCaseǁ__init____mutmut['xǁReportCriticalVulnerabilitiesUseCaseǁ__init____mutmut_1'] = ReportCriticalVulnerabilitiesUseCase.xǁReportCriticalVulnerabilitiesUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut['_mutmut_orig'] = ReportCriticalVulnerabilitiesUseCase.xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut['xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_1'] = ReportCriticalVulnerabilitiesUseCase.xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut['xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_2'] = ReportCriticalVulnerabilitiesUseCase.xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut['xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_3'] = ReportCriticalVulnerabilitiesUseCase.xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut['xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_4'] = ReportCriticalVulnerabilitiesUseCase.xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut['xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_5'] = ReportCriticalVulnerabilitiesUseCase.xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut['xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_6'] = ReportCriticalVulnerabilitiesUseCase.xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut['xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_7'] = ReportCriticalVulnerabilitiesUseCase.xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut['xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_8'] = ReportCriticalVulnerabilitiesUseCase.xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut['xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_9'] = ReportCriticalVulnerabilitiesUseCase.xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut['xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_10'] = ReportCriticalVulnerabilitiesUseCase.xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut['xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_11'] = ReportCriticalVulnerabilitiesUseCase.xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut['xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_12'] = ReportCriticalVulnerabilitiesUseCase.xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut['xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_13'] = ReportCriticalVulnerabilitiesUseCase.xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut['xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_14'] = ReportCriticalVulnerabilitiesUseCase.xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut['xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_15'] = ReportCriticalVulnerabilitiesUseCase.xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut['xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_16'] = ReportCriticalVulnerabilitiesUseCase.xǁReportCriticalVulnerabilitiesUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
