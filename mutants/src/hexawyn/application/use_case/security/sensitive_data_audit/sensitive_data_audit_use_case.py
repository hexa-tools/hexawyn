from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.compliance_audit_port import ComplianceAuditPort
from hexawyn.application.use_case.security.sensitive_data_audit.command import (
    SensitiveDataAuditCommand,
)
from hexawyn.application.use_case.security.sensitive_data_audit.response import (
    SensitiveDataAuditResponse,
)
from hexawyn.domain.models.sensitive_data_audit import SensitiveAccessRequest, SensitiveAuditResult


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁSensitiveDataAuditUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁSensitiveDataAuditUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class SensitiveDataAuditUseCase:
    @_mutmut_mutated(mutants_xǁSensitiveDataAuditUseCaseǁ__init____mutmut)
    def __init__(self, port: ComplianceAuditPort) -> None:
        self._port = port
    def xǁSensitiveDataAuditUseCaseǁ__init____mutmut_orig(self, port: ComplianceAuditPort) -> None:
        self._port = port
    def xǁSensitiveDataAuditUseCaseǁ__init____mutmut_1(self, port: ComplianceAuditPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁSensitiveDataAuditUseCaseǁexecute__mutmut)
    def execute(self, command: SensitiveDataAuditCommand) -> SensitiveDataAuditResponse:
        req = SensitiveAccessRequest(
            pattern=command.pattern,
            time_window_minutes=command.time_window_minutes,
            allowlist=command.allowlist,
        )
        matches = self._port.fetch_access_matches(req)
        r = SensitiveAuditResult.compute(request=req, matches=matches)
        return SensitiveDataAuditResponse(
            pattern=r.pattern,
            total_matches=r.total_matches,
            flagged=[asdict(f) for f in r.flagged],
            unflagged=[asdict(u) for u in r.unflagged],
            alert_level=r.alert_level.value,
        )

    def xǁSensitiveDataAuditUseCaseǁexecute__mutmut_orig(self, command: SensitiveDataAuditCommand) -> SensitiveDataAuditResponse:
        req = SensitiveAccessRequest(
            pattern=command.pattern,
            time_window_minutes=command.time_window_minutes,
            allowlist=command.allowlist,
        )
        matches = self._port.fetch_access_matches(req)
        r = SensitiveAuditResult.compute(request=req, matches=matches)
        return SensitiveDataAuditResponse(
            pattern=r.pattern,
            total_matches=r.total_matches,
            flagged=[asdict(f) for f in r.flagged],
            unflagged=[asdict(u) for u in r.unflagged],
            alert_level=r.alert_level.value,
        )

    def xǁSensitiveDataAuditUseCaseǁexecute__mutmut_1(self, command: SensitiveDataAuditCommand) -> SensitiveDataAuditResponse:
        req = None
        matches = self._port.fetch_access_matches(req)
        r = SensitiveAuditResult.compute(request=req, matches=matches)
        return SensitiveDataAuditResponse(
            pattern=r.pattern,
            total_matches=r.total_matches,
            flagged=[asdict(f) for f in r.flagged],
            unflagged=[asdict(u) for u in r.unflagged],
            alert_level=r.alert_level.value,
        )

    def xǁSensitiveDataAuditUseCaseǁexecute__mutmut_2(self, command: SensitiveDataAuditCommand) -> SensitiveDataAuditResponse:
        req = SensitiveAccessRequest(
            pattern=None,
            time_window_minutes=command.time_window_minutes,
            allowlist=command.allowlist,
        )
        matches = self._port.fetch_access_matches(req)
        r = SensitiveAuditResult.compute(request=req, matches=matches)
        return SensitiveDataAuditResponse(
            pattern=r.pattern,
            total_matches=r.total_matches,
            flagged=[asdict(f) for f in r.flagged],
            unflagged=[asdict(u) for u in r.unflagged],
            alert_level=r.alert_level.value,
        )

    def xǁSensitiveDataAuditUseCaseǁexecute__mutmut_3(self, command: SensitiveDataAuditCommand) -> SensitiveDataAuditResponse:
        req = SensitiveAccessRequest(
            pattern=command.pattern,
            time_window_minutes=None,
            allowlist=command.allowlist,
        )
        matches = self._port.fetch_access_matches(req)
        r = SensitiveAuditResult.compute(request=req, matches=matches)
        return SensitiveDataAuditResponse(
            pattern=r.pattern,
            total_matches=r.total_matches,
            flagged=[asdict(f) for f in r.flagged],
            unflagged=[asdict(u) for u in r.unflagged],
            alert_level=r.alert_level.value,
        )

    def xǁSensitiveDataAuditUseCaseǁexecute__mutmut_4(self, command: SensitiveDataAuditCommand) -> SensitiveDataAuditResponse:
        req = SensitiveAccessRequest(
            pattern=command.pattern,
            time_window_minutes=command.time_window_minutes,
            allowlist=None,
        )
        matches = self._port.fetch_access_matches(req)
        r = SensitiveAuditResult.compute(request=req, matches=matches)
        return SensitiveDataAuditResponse(
            pattern=r.pattern,
            total_matches=r.total_matches,
            flagged=[asdict(f) for f in r.flagged],
            unflagged=[asdict(u) for u in r.unflagged],
            alert_level=r.alert_level.value,
        )

    def xǁSensitiveDataAuditUseCaseǁexecute__mutmut_5(self, command: SensitiveDataAuditCommand) -> SensitiveDataAuditResponse:
        req = SensitiveAccessRequest(
            time_window_minutes=command.time_window_minutes,
            allowlist=command.allowlist,
        )
        matches = self._port.fetch_access_matches(req)
        r = SensitiveAuditResult.compute(request=req, matches=matches)
        return SensitiveDataAuditResponse(
            pattern=r.pattern,
            total_matches=r.total_matches,
            flagged=[asdict(f) for f in r.flagged],
            unflagged=[asdict(u) for u in r.unflagged],
            alert_level=r.alert_level.value,
        )

    def xǁSensitiveDataAuditUseCaseǁexecute__mutmut_6(self, command: SensitiveDataAuditCommand) -> SensitiveDataAuditResponse:
        req = SensitiveAccessRequest(
            pattern=command.pattern,
            allowlist=command.allowlist,
        )
        matches = self._port.fetch_access_matches(req)
        r = SensitiveAuditResult.compute(request=req, matches=matches)
        return SensitiveDataAuditResponse(
            pattern=r.pattern,
            total_matches=r.total_matches,
            flagged=[asdict(f) for f in r.flagged],
            unflagged=[asdict(u) for u in r.unflagged],
            alert_level=r.alert_level.value,
        )

    def xǁSensitiveDataAuditUseCaseǁexecute__mutmut_7(self, command: SensitiveDataAuditCommand) -> SensitiveDataAuditResponse:
        req = SensitiveAccessRequest(
            pattern=command.pattern,
            time_window_minutes=command.time_window_minutes,
            )
        matches = self._port.fetch_access_matches(req)
        r = SensitiveAuditResult.compute(request=req, matches=matches)
        return SensitiveDataAuditResponse(
            pattern=r.pattern,
            total_matches=r.total_matches,
            flagged=[asdict(f) for f in r.flagged],
            unflagged=[asdict(u) for u in r.unflagged],
            alert_level=r.alert_level.value,
        )

    def xǁSensitiveDataAuditUseCaseǁexecute__mutmut_8(self, command: SensitiveDataAuditCommand) -> SensitiveDataAuditResponse:
        req = SensitiveAccessRequest(
            pattern=command.pattern,
            time_window_minutes=command.time_window_minutes,
            allowlist=command.allowlist,
        )
        matches = None
        r = SensitiveAuditResult.compute(request=req, matches=matches)
        return SensitiveDataAuditResponse(
            pattern=r.pattern,
            total_matches=r.total_matches,
            flagged=[asdict(f) for f in r.flagged],
            unflagged=[asdict(u) for u in r.unflagged],
            alert_level=r.alert_level.value,
        )

    def xǁSensitiveDataAuditUseCaseǁexecute__mutmut_9(self, command: SensitiveDataAuditCommand) -> SensitiveDataAuditResponse:
        req = SensitiveAccessRequest(
            pattern=command.pattern,
            time_window_minutes=command.time_window_minutes,
            allowlist=command.allowlist,
        )
        matches = self._port.fetch_access_matches(None)
        r = SensitiveAuditResult.compute(request=req, matches=matches)
        return SensitiveDataAuditResponse(
            pattern=r.pattern,
            total_matches=r.total_matches,
            flagged=[asdict(f) for f in r.flagged],
            unflagged=[asdict(u) for u in r.unflagged],
            alert_level=r.alert_level.value,
        )

    def xǁSensitiveDataAuditUseCaseǁexecute__mutmut_10(self, command: SensitiveDataAuditCommand) -> SensitiveDataAuditResponse:
        req = SensitiveAccessRequest(
            pattern=command.pattern,
            time_window_minutes=command.time_window_minutes,
            allowlist=command.allowlist,
        )
        matches = self._port.fetch_access_matches(req)
        r = None
        return SensitiveDataAuditResponse(
            pattern=r.pattern,
            total_matches=r.total_matches,
            flagged=[asdict(f) for f in r.flagged],
            unflagged=[asdict(u) for u in r.unflagged],
            alert_level=r.alert_level.value,
        )

    def xǁSensitiveDataAuditUseCaseǁexecute__mutmut_11(self, command: SensitiveDataAuditCommand) -> SensitiveDataAuditResponse:
        req = SensitiveAccessRequest(
            pattern=command.pattern,
            time_window_minutes=command.time_window_minutes,
            allowlist=command.allowlist,
        )
        matches = self._port.fetch_access_matches(req)
        r = SensitiveAuditResult.compute(request=None, matches=matches)
        return SensitiveDataAuditResponse(
            pattern=r.pattern,
            total_matches=r.total_matches,
            flagged=[asdict(f) for f in r.flagged],
            unflagged=[asdict(u) for u in r.unflagged],
            alert_level=r.alert_level.value,
        )

    def xǁSensitiveDataAuditUseCaseǁexecute__mutmut_12(self, command: SensitiveDataAuditCommand) -> SensitiveDataAuditResponse:
        req = SensitiveAccessRequest(
            pattern=command.pattern,
            time_window_minutes=command.time_window_minutes,
            allowlist=command.allowlist,
        )
        matches = self._port.fetch_access_matches(req)
        r = SensitiveAuditResult.compute(request=req, matches=None)
        return SensitiveDataAuditResponse(
            pattern=r.pattern,
            total_matches=r.total_matches,
            flagged=[asdict(f) for f in r.flagged],
            unflagged=[asdict(u) for u in r.unflagged],
            alert_level=r.alert_level.value,
        )

    def xǁSensitiveDataAuditUseCaseǁexecute__mutmut_13(self, command: SensitiveDataAuditCommand) -> SensitiveDataAuditResponse:
        req = SensitiveAccessRequest(
            pattern=command.pattern,
            time_window_minutes=command.time_window_minutes,
            allowlist=command.allowlist,
        )
        matches = self._port.fetch_access_matches(req)
        r = SensitiveAuditResult.compute(matches=matches)
        return SensitiveDataAuditResponse(
            pattern=r.pattern,
            total_matches=r.total_matches,
            flagged=[asdict(f) for f in r.flagged],
            unflagged=[asdict(u) for u in r.unflagged],
            alert_level=r.alert_level.value,
        )

    def xǁSensitiveDataAuditUseCaseǁexecute__mutmut_14(self, command: SensitiveDataAuditCommand) -> SensitiveDataAuditResponse:
        req = SensitiveAccessRequest(
            pattern=command.pattern,
            time_window_minutes=command.time_window_minutes,
            allowlist=command.allowlist,
        )
        matches = self._port.fetch_access_matches(req)
        r = SensitiveAuditResult.compute(request=req, )
        return SensitiveDataAuditResponse(
            pattern=r.pattern,
            total_matches=r.total_matches,
            flagged=[asdict(f) for f in r.flagged],
            unflagged=[asdict(u) for u in r.unflagged],
            alert_level=r.alert_level.value,
        )

    def xǁSensitiveDataAuditUseCaseǁexecute__mutmut_15(self, command: SensitiveDataAuditCommand) -> SensitiveDataAuditResponse:
        req = SensitiveAccessRequest(
            pattern=command.pattern,
            time_window_minutes=command.time_window_minutes,
            allowlist=command.allowlist,
        )
        matches = self._port.fetch_access_matches(req)
        r = SensitiveAuditResult.compute(request=req, matches=matches)
        return SensitiveDataAuditResponse(
            pattern=None,
            total_matches=r.total_matches,
            flagged=[asdict(f) for f in r.flagged],
            unflagged=[asdict(u) for u in r.unflagged],
            alert_level=r.alert_level.value,
        )

    def xǁSensitiveDataAuditUseCaseǁexecute__mutmut_16(self, command: SensitiveDataAuditCommand) -> SensitiveDataAuditResponse:
        req = SensitiveAccessRequest(
            pattern=command.pattern,
            time_window_minutes=command.time_window_minutes,
            allowlist=command.allowlist,
        )
        matches = self._port.fetch_access_matches(req)
        r = SensitiveAuditResult.compute(request=req, matches=matches)
        return SensitiveDataAuditResponse(
            pattern=r.pattern,
            total_matches=None,
            flagged=[asdict(f) for f in r.flagged],
            unflagged=[asdict(u) for u in r.unflagged],
            alert_level=r.alert_level.value,
        )

    def xǁSensitiveDataAuditUseCaseǁexecute__mutmut_17(self, command: SensitiveDataAuditCommand) -> SensitiveDataAuditResponse:
        req = SensitiveAccessRequest(
            pattern=command.pattern,
            time_window_minutes=command.time_window_minutes,
            allowlist=command.allowlist,
        )
        matches = self._port.fetch_access_matches(req)
        r = SensitiveAuditResult.compute(request=req, matches=matches)
        return SensitiveDataAuditResponse(
            pattern=r.pattern,
            total_matches=r.total_matches,
            flagged=None,
            unflagged=[asdict(u) for u in r.unflagged],
            alert_level=r.alert_level.value,
        )

    def xǁSensitiveDataAuditUseCaseǁexecute__mutmut_18(self, command: SensitiveDataAuditCommand) -> SensitiveDataAuditResponse:
        req = SensitiveAccessRequest(
            pattern=command.pattern,
            time_window_minutes=command.time_window_minutes,
            allowlist=command.allowlist,
        )
        matches = self._port.fetch_access_matches(req)
        r = SensitiveAuditResult.compute(request=req, matches=matches)
        return SensitiveDataAuditResponse(
            pattern=r.pattern,
            total_matches=r.total_matches,
            flagged=[asdict(f) for f in r.flagged],
            unflagged=None,
            alert_level=r.alert_level.value,
        )

    def xǁSensitiveDataAuditUseCaseǁexecute__mutmut_19(self, command: SensitiveDataAuditCommand) -> SensitiveDataAuditResponse:
        req = SensitiveAccessRequest(
            pattern=command.pattern,
            time_window_minutes=command.time_window_minutes,
            allowlist=command.allowlist,
        )
        matches = self._port.fetch_access_matches(req)
        r = SensitiveAuditResult.compute(request=req, matches=matches)
        return SensitiveDataAuditResponse(
            pattern=r.pattern,
            total_matches=r.total_matches,
            flagged=[asdict(f) for f in r.flagged],
            unflagged=[asdict(u) for u in r.unflagged],
            alert_level=None,
        )

    def xǁSensitiveDataAuditUseCaseǁexecute__mutmut_20(self, command: SensitiveDataAuditCommand) -> SensitiveDataAuditResponse:
        req = SensitiveAccessRequest(
            pattern=command.pattern,
            time_window_minutes=command.time_window_minutes,
            allowlist=command.allowlist,
        )
        matches = self._port.fetch_access_matches(req)
        r = SensitiveAuditResult.compute(request=req, matches=matches)
        return SensitiveDataAuditResponse(
            total_matches=r.total_matches,
            flagged=[asdict(f) for f in r.flagged],
            unflagged=[asdict(u) for u in r.unflagged],
            alert_level=r.alert_level.value,
        )

    def xǁSensitiveDataAuditUseCaseǁexecute__mutmut_21(self, command: SensitiveDataAuditCommand) -> SensitiveDataAuditResponse:
        req = SensitiveAccessRequest(
            pattern=command.pattern,
            time_window_minutes=command.time_window_minutes,
            allowlist=command.allowlist,
        )
        matches = self._port.fetch_access_matches(req)
        r = SensitiveAuditResult.compute(request=req, matches=matches)
        return SensitiveDataAuditResponse(
            pattern=r.pattern,
            flagged=[asdict(f) for f in r.flagged],
            unflagged=[asdict(u) for u in r.unflagged],
            alert_level=r.alert_level.value,
        )

    def xǁSensitiveDataAuditUseCaseǁexecute__mutmut_22(self, command: SensitiveDataAuditCommand) -> SensitiveDataAuditResponse:
        req = SensitiveAccessRequest(
            pattern=command.pattern,
            time_window_minutes=command.time_window_minutes,
            allowlist=command.allowlist,
        )
        matches = self._port.fetch_access_matches(req)
        r = SensitiveAuditResult.compute(request=req, matches=matches)
        return SensitiveDataAuditResponse(
            pattern=r.pattern,
            total_matches=r.total_matches,
            unflagged=[asdict(u) for u in r.unflagged],
            alert_level=r.alert_level.value,
        )

    def xǁSensitiveDataAuditUseCaseǁexecute__mutmut_23(self, command: SensitiveDataAuditCommand) -> SensitiveDataAuditResponse:
        req = SensitiveAccessRequest(
            pattern=command.pattern,
            time_window_minutes=command.time_window_minutes,
            allowlist=command.allowlist,
        )
        matches = self._port.fetch_access_matches(req)
        r = SensitiveAuditResult.compute(request=req, matches=matches)
        return SensitiveDataAuditResponse(
            pattern=r.pattern,
            total_matches=r.total_matches,
            flagged=[asdict(f) for f in r.flagged],
            alert_level=r.alert_level.value,
        )

    def xǁSensitiveDataAuditUseCaseǁexecute__mutmut_24(self, command: SensitiveDataAuditCommand) -> SensitiveDataAuditResponse:
        req = SensitiveAccessRequest(
            pattern=command.pattern,
            time_window_minutes=command.time_window_minutes,
            allowlist=command.allowlist,
        )
        matches = self._port.fetch_access_matches(req)
        r = SensitiveAuditResult.compute(request=req, matches=matches)
        return SensitiveDataAuditResponse(
            pattern=r.pattern,
            total_matches=r.total_matches,
            flagged=[asdict(f) for f in r.flagged],
            unflagged=[asdict(u) for u in r.unflagged],
            )

    def xǁSensitiveDataAuditUseCaseǁexecute__mutmut_25(self, command: SensitiveDataAuditCommand) -> SensitiveDataAuditResponse:
        req = SensitiveAccessRequest(
            pattern=command.pattern,
            time_window_minutes=command.time_window_minutes,
            allowlist=command.allowlist,
        )
        matches = self._port.fetch_access_matches(req)
        r = SensitiveAuditResult.compute(request=req, matches=matches)
        return SensitiveDataAuditResponse(
            pattern=r.pattern,
            total_matches=r.total_matches,
            flagged=[asdict(None) for f in r.flagged],
            unflagged=[asdict(u) for u in r.unflagged],
            alert_level=r.alert_level.value,
        )

    def xǁSensitiveDataAuditUseCaseǁexecute__mutmut_26(self, command: SensitiveDataAuditCommand) -> SensitiveDataAuditResponse:
        req = SensitiveAccessRequest(
            pattern=command.pattern,
            time_window_minutes=command.time_window_minutes,
            allowlist=command.allowlist,
        )
        matches = self._port.fetch_access_matches(req)
        r = SensitiveAuditResult.compute(request=req, matches=matches)
        return SensitiveDataAuditResponse(
            pattern=r.pattern,
            total_matches=r.total_matches,
            flagged=[asdict(f) for f in r.flagged],
            unflagged=[asdict(None) for u in r.unflagged],
            alert_level=r.alert_level.value,
        )

mutants_xǁSensitiveDataAuditUseCaseǁ__init____mutmut['_mutmut_orig'] = SensitiveDataAuditUseCase.xǁSensitiveDataAuditUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁSensitiveDataAuditUseCaseǁ__init____mutmut['xǁSensitiveDataAuditUseCaseǁ__init____mutmut_1'] = SensitiveDataAuditUseCase.xǁSensitiveDataAuditUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁSensitiveDataAuditUseCaseǁexecute__mutmut['_mutmut_orig'] = SensitiveDataAuditUseCase.xǁSensitiveDataAuditUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSensitiveDataAuditUseCaseǁexecute__mutmut['xǁSensitiveDataAuditUseCaseǁexecute__mutmut_1'] = SensitiveDataAuditUseCase.xǁSensitiveDataAuditUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSensitiveDataAuditUseCaseǁexecute__mutmut['xǁSensitiveDataAuditUseCaseǁexecute__mutmut_2'] = SensitiveDataAuditUseCase.xǁSensitiveDataAuditUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁSensitiveDataAuditUseCaseǁexecute__mutmut['xǁSensitiveDataAuditUseCaseǁexecute__mutmut_3'] = SensitiveDataAuditUseCase.xǁSensitiveDataAuditUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁSensitiveDataAuditUseCaseǁexecute__mutmut['xǁSensitiveDataAuditUseCaseǁexecute__mutmut_4'] = SensitiveDataAuditUseCase.xǁSensitiveDataAuditUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁSensitiveDataAuditUseCaseǁexecute__mutmut['xǁSensitiveDataAuditUseCaseǁexecute__mutmut_5'] = SensitiveDataAuditUseCase.xǁSensitiveDataAuditUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁSensitiveDataAuditUseCaseǁexecute__mutmut['xǁSensitiveDataAuditUseCaseǁexecute__mutmut_6'] = SensitiveDataAuditUseCase.xǁSensitiveDataAuditUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁSensitiveDataAuditUseCaseǁexecute__mutmut['xǁSensitiveDataAuditUseCaseǁexecute__mutmut_7'] = SensitiveDataAuditUseCase.xǁSensitiveDataAuditUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁSensitiveDataAuditUseCaseǁexecute__mutmut['xǁSensitiveDataAuditUseCaseǁexecute__mutmut_8'] = SensitiveDataAuditUseCase.xǁSensitiveDataAuditUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁSensitiveDataAuditUseCaseǁexecute__mutmut['xǁSensitiveDataAuditUseCaseǁexecute__mutmut_9'] = SensitiveDataAuditUseCase.xǁSensitiveDataAuditUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁSensitiveDataAuditUseCaseǁexecute__mutmut['xǁSensitiveDataAuditUseCaseǁexecute__mutmut_10'] = SensitiveDataAuditUseCase.xǁSensitiveDataAuditUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁSensitiveDataAuditUseCaseǁexecute__mutmut['xǁSensitiveDataAuditUseCaseǁexecute__mutmut_11'] = SensitiveDataAuditUseCase.xǁSensitiveDataAuditUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁSensitiveDataAuditUseCaseǁexecute__mutmut['xǁSensitiveDataAuditUseCaseǁexecute__mutmut_12'] = SensitiveDataAuditUseCase.xǁSensitiveDataAuditUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁSensitiveDataAuditUseCaseǁexecute__mutmut['xǁSensitiveDataAuditUseCaseǁexecute__mutmut_13'] = SensitiveDataAuditUseCase.xǁSensitiveDataAuditUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁSensitiveDataAuditUseCaseǁexecute__mutmut['xǁSensitiveDataAuditUseCaseǁexecute__mutmut_14'] = SensitiveDataAuditUseCase.xǁSensitiveDataAuditUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁSensitiveDataAuditUseCaseǁexecute__mutmut['xǁSensitiveDataAuditUseCaseǁexecute__mutmut_15'] = SensitiveDataAuditUseCase.xǁSensitiveDataAuditUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁSensitiveDataAuditUseCaseǁexecute__mutmut['xǁSensitiveDataAuditUseCaseǁexecute__mutmut_16'] = SensitiveDataAuditUseCase.xǁSensitiveDataAuditUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁSensitiveDataAuditUseCaseǁexecute__mutmut['xǁSensitiveDataAuditUseCaseǁexecute__mutmut_17'] = SensitiveDataAuditUseCase.xǁSensitiveDataAuditUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁSensitiveDataAuditUseCaseǁexecute__mutmut['xǁSensitiveDataAuditUseCaseǁexecute__mutmut_18'] = SensitiveDataAuditUseCase.xǁSensitiveDataAuditUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁSensitiveDataAuditUseCaseǁexecute__mutmut['xǁSensitiveDataAuditUseCaseǁexecute__mutmut_19'] = SensitiveDataAuditUseCase.xǁSensitiveDataAuditUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁSensitiveDataAuditUseCaseǁexecute__mutmut['xǁSensitiveDataAuditUseCaseǁexecute__mutmut_20'] = SensitiveDataAuditUseCase.xǁSensitiveDataAuditUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁSensitiveDataAuditUseCaseǁexecute__mutmut['xǁSensitiveDataAuditUseCaseǁexecute__mutmut_21'] = SensitiveDataAuditUseCase.xǁSensitiveDataAuditUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁSensitiveDataAuditUseCaseǁexecute__mutmut['xǁSensitiveDataAuditUseCaseǁexecute__mutmut_22'] = SensitiveDataAuditUseCase.xǁSensitiveDataAuditUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁSensitiveDataAuditUseCaseǁexecute__mutmut['xǁSensitiveDataAuditUseCaseǁexecute__mutmut_23'] = SensitiveDataAuditUseCase.xǁSensitiveDataAuditUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁSensitiveDataAuditUseCaseǁexecute__mutmut['xǁSensitiveDataAuditUseCaseǁexecute__mutmut_24'] = SensitiveDataAuditUseCase.xǁSensitiveDataAuditUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁSensitiveDataAuditUseCaseǁexecute__mutmut['xǁSensitiveDataAuditUseCaseǁexecute__mutmut_25'] = SensitiveDataAuditUseCase.xǁSensitiveDataAuditUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁSensitiveDataAuditUseCaseǁexecute__mutmut['xǁSensitiveDataAuditUseCaseǁexecute__mutmut_26'] = SensitiveDataAuditUseCase.xǁSensitiveDataAuditUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
