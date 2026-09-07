from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.security_audit_port import SecurityAuditPort
from hexawyn.application.use_case.security.admin_endpoint_audit.command import (
    AdminEndpointAuditCommand,
)
from hexawyn.application.use_case.security.admin_endpoint_audit.response import (
    AdminEndpointAuditResponse,
)
from hexawyn.domain.models.admin_endpoint_audit import AdminAuditRequest, AdminAuditResult


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁAdminEndpointAuditUseCaseǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁAdminEndpointAuditUseCaseǁexecute__mutmut: MutantDict = {}  # type: ignore


class AdminEndpointAuditUseCase:
    @_mutmut_mutated(mutants_xǁAdminEndpointAuditUseCaseǁ__init____mutmut)
    def __init__(self, port: SecurityAuditPort) -> None:
        self._port = port
    def xǁAdminEndpointAuditUseCaseǁ__init____mutmut_orig(self, port: SecurityAuditPort) -> None:
        self._port = port
    def xǁAdminEndpointAuditUseCaseǁ__init____mutmut_1(self, port: SecurityAuditPort) -> None:
        self._port = None

    @_mutmut_mutated(mutants_xǁAdminEndpointAuditUseCaseǁexecute__mutmut)
    def execute(self, command: AdminEndpointAuditCommand) -> AdminEndpointAuditResponse:
        req = AdminAuditRequest(
            endpoint_pattern=command.endpoint_pattern,
            time_window_minutes=command.time_window_minutes,
            flag_threshold=command.flag_threshold,
        )
        calls = self._port.fetch_failed_admin_calls(req)
        total = self._port.fetch_total_requests(req)
        r = AdminAuditResult.compute(request=req, calls=calls, total_requests=total)
        return AdminEndpointAuditResponse(
            endpoint_pattern=r.endpoint_pattern,
            total_requests=r.total_requests,
            total_403s=r.total_403s,
            rate_403_pct=r.rate_403_pct,
            flagged_callers=[asdict(c) for c in r.flagged_callers],
        )

    def xǁAdminEndpointAuditUseCaseǁexecute__mutmut_orig(self, command: AdminEndpointAuditCommand) -> AdminEndpointAuditResponse:
        req = AdminAuditRequest(
            endpoint_pattern=command.endpoint_pattern,
            time_window_minutes=command.time_window_minutes,
            flag_threshold=command.flag_threshold,
        )
        calls = self._port.fetch_failed_admin_calls(req)
        total = self._port.fetch_total_requests(req)
        r = AdminAuditResult.compute(request=req, calls=calls, total_requests=total)
        return AdminEndpointAuditResponse(
            endpoint_pattern=r.endpoint_pattern,
            total_requests=r.total_requests,
            total_403s=r.total_403s,
            rate_403_pct=r.rate_403_pct,
            flagged_callers=[asdict(c) for c in r.flagged_callers],
        )

    def xǁAdminEndpointAuditUseCaseǁexecute__mutmut_1(self, command: AdminEndpointAuditCommand) -> AdminEndpointAuditResponse:
        req = None
        calls = self._port.fetch_failed_admin_calls(req)
        total = self._port.fetch_total_requests(req)
        r = AdminAuditResult.compute(request=req, calls=calls, total_requests=total)
        return AdminEndpointAuditResponse(
            endpoint_pattern=r.endpoint_pattern,
            total_requests=r.total_requests,
            total_403s=r.total_403s,
            rate_403_pct=r.rate_403_pct,
            flagged_callers=[asdict(c) for c in r.flagged_callers],
        )

    def xǁAdminEndpointAuditUseCaseǁexecute__mutmut_2(self, command: AdminEndpointAuditCommand) -> AdminEndpointAuditResponse:
        req = AdminAuditRequest(
            endpoint_pattern=None,
            time_window_minutes=command.time_window_minutes,
            flag_threshold=command.flag_threshold,
        )
        calls = self._port.fetch_failed_admin_calls(req)
        total = self._port.fetch_total_requests(req)
        r = AdminAuditResult.compute(request=req, calls=calls, total_requests=total)
        return AdminEndpointAuditResponse(
            endpoint_pattern=r.endpoint_pattern,
            total_requests=r.total_requests,
            total_403s=r.total_403s,
            rate_403_pct=r.rate_403_pct,
            flagged_callers=[asdict(c) for c in r.flagged_callers],
        )

    def xǁAdminEndpointAuditUseCaseǁexecute__mutmut_3(self, command: AdminEndpointAuditCommand) -> AdminEndpointAuditResponse:
        req = AdminAuditRequest(
            endpoint_pattern=command.endpoint_pattern,
            time_window_minutes=None,
            flag_threshold=command.flag_threshold,
        )
        calls = self._port.fetch_failed_admin_calls(req)
        total = self._port.fetch_total_requests(req)
        r = AdminAuditResult.compute(request=req, calls=calls, total_requests=total)
        return AdminEndpointAuditResponse(
            endpoint_pattern=r.endpoint_pattern,
            total_requests=r.total_requests,
            total_403s=r.total_403s,
            rate_403_pct=r.rate_403_pct,
            flagged_callers=[asdict(c) for c in r.flagged_callers],
        )

    def xǁAdminEndpointAuditUseCaseǁexecute__mutmut_4(self, command: AdminEndpointAuditCommand) -> AdminEndpointAuditResponse:
        req = AdminAuditRequest(
            endpoint_pattern=command.endpoint_pattern,
            time_window_minutes=command.time_window_minutes,
            flag_threshold=None,
        )
        calls = self._port.fetch_failed_admin_calls(req)
        total = self._port.fetch_total_requests(req)
        r = AdminAuditResult.compute(request=req, calls=calls, total_requests=total)
        return AdminEndpointAuditResponse(
            endpoint_pattern=r.endpoint_pattern,
            total_requests=r.total_requests,
            total_403s=r.total_403s,
            rate_403_pct=r.rate_403_pct,
            flagged_callers=[asdict(c) for c in r.flagged_callers],
        )

    def xǁAdminEndpointAuditUseCaseǁexecute__mutmut_5(self, command: AdminEndpointAuditCommand) -> AdminEndpointAuditResponse:
        req = AdminAuditRequest(
            time_window_minutes=command.time_window_minutes,
            flag_threshold=command.flag_threshold,
        )
        calls = self._port.fetch_failed_admin_calls(req)
        total = self._port.fetch_total_requests(req)
        r = AdminAuditResult.compute(request=req, calls=calls, total_requests=total)
        return AdminEndpointAuditResponse(
            endpoint_pattern=r.endpoint_pattern,
            total_requests=r.total_requests,
            total_403s=r.total_403s,
            rate_403_pct=r.rate_403_pct,
            flagged_callers=[asdict(c) for c in r.flagged_callers],
        )

    def xǁAdminEndpointAuditUseCaseǁexecute__mutmut_6(self, command: AdminEndpointAuditCommand) -> AdminEndpointAuditResponse:
        req = AdminAuditRequest(
            endpoint_pattern=command.endpoint_pattern,
            flag_threshold=command.flag_threshold,
        )
        calls = self._port.fetch_failed_admin_calls(req)
        total = self._port.fetch_total_requests(req)
        r = AdminAuditResult.compute(request=req, calls=calls, total_requests=total)
        return AdminEndpointAuditResponse(
            endpoint_pattern=r.endpoint_pattern,
            total_requests=r.total_requests,
            total_403s=r.total_403s,
            rate_403_pct=r.rate_403_pct,
            flagged_callers=[asdict(c) for c in r.flagged_callers],
        )

    def xǁAdminEndpointAuditUseCaseǁexecute__mutmut_7(self, command: AdminEndpointAuditCommand) -> AdminEndpointAuditResponse:
        req = AdminAuditRequest(
            endpoint_pattern=command.endpoint_pattern,
            time_window_minutes=command.time_window_minutes,
            )
        calls = self._port.fetch_failed_admin_calls(req)
        total = self._port.fetch_total_requests(req)
        r = AdminAuditResult.compute(request=req, calls=calls, total_requests=total)
        return AdminEndpointAuditResponse(
            endpoint_pattern=r.endpoint_pattern,
            total_requests=r.total_requests,
            total_403s=r.total_403s,
            rate_403_pct=r.rate_403_pct,
            flagged_callers=[asdict(c) for c in r.flagged_callers],
        )

    def xǁAdminEndpointAuditUseCaseǁexecute__mutmut_8(self, command: AdminEndpointAuditCommand) -> AdminEndpointAuditResponse:
        req = AdminAuditRequest(
            endpoint_pattern=command.endpoint_pattern,
            time_window_minutes=command.time_window_minutes,
            flag_threshold=command.flag_threshold,
        )
        calls = None
        total = self._port.fetch_total_requests(req)
        r = AdminAuditResult.compute(request=req, calls=calls, total_requests=total)
        return AdminEndpointAuditResponse(
            endpoint_pattern=r.endpoint_pattern,
            total_requests=r.total_requests,
            total_403s=r.total_403s,
            rate_403_pct=r.rate_403_pct,
            flagged_callers=[asdict(c) for c in r.flagged_callers],
        )

    def xǁAdminEndpointAuditUseCaseǁexecute__mutmut_9(self, command: AdminEndpointAuditCommand) -> AdminEndpointAuditResponse:
        req = AdminAuditRequest(
            endpoint_pattern=command.endpoint_pattern,
            time_window_minutes=command.time_window_minutes,
            flag_threshold=command.flag_threshold,
        )
        calls = self._port.fetch_failed_admin_calls(None)
        total = self._port.fetch_total_requests(req)
        r = AdminAuditResult.compute(request=req, calls=calls, total_requests=total)
        return AdminEndpointAuditResponse(
            endpoint_pattern=r.endpoint_pattern,
            total_requests=r.total_requests,
            total_403s=r.total_403s,
            rate_403_pct=r.rate_403_pct,
            flagged_callers=[asdict(c) for c in r.flagged_callers],
        )

    def xǁAdminEndpointAuditUseCaseǁexecute__mutmut_10(self, command: AdminEndpointAuditCommand) -> AdminEndpointAuditResponse:
        req = AdminAuditRequest(
            endpoint_pattern=command.endpoint_pattern,
            time_window_minutes=command.time_window_minutes,
            flag_threshold=command.flag_threshold,
        )
        calls = self._port.fetch_failed_admin_calls(req)
        total = None
        r = AdminAuditResult.compute(request=req, calls=calls, total_requests=total)
        return AdminEndpointAuditResponse(
            endpoint_pattern=r.endpoint_pattern,
            total_requests=r.total_requests,
            total_403s=r.total_403s,
            rate_403_pct=r.rate_403_pct,
            flagged_callers=[asdict(c) for c in r.flagged_callers],
        )

    def xǁAdminEndpointAuditUseCaseǁexecute__mutmut_11(self, command: AdminEndpointAuditCommand) -> AdminEndpointAuditResponse:
        req = AdminAuditRequest(
            endpoint_pattern=command.endpoint_pattern,
            time_window_minutes=command.time_window_minutes,
            flag_threshold=command.flag_threshold,
        )
        calls = self._port.fetch_failed_admin_calls(req)
        total = self._port.fetch_total_requests(None)
        r = AdminAuditResult.compute(request=req, calls=calls, total_requests=total)
        return AdminEndpointAuditResponse(
            endpoint_pattern=r.endpoint_pattern,
            total_requests=r.total_requests,
            total_403s=r.total_403s,
            rate_403_pct=r.rate_403_pct,
            flagged_callers=[asdict(c) for c in r.flagged_callers],
        )

    def xǁAdminEndpointAuditUseCaseǁexecute__mutmut_12(self, command: AdminEndpointAuditCommand) -> AdminEndpointAuditResponse:
        req = AdminAuditRequest(
            endpoint_pattern=command.endpoint_pattern,
            time_window_minutes=command.time_window_minutes,
            flag_threshold=command.flag_threshold,
        )
        calls = self._port.fetch_failed_admin_calls(req)
        total = self._port.fetch_total_requests(req)
        r = None
        return AdminEndpointAuditResponse(
            endpoint_pattern=r.endpoint_pattern,
            total_requests=r.total_requests,
            total_403s=r.total_403s,
            rate_403_pct=r.rate_403_pct,
            flagged_callers=[asdict(c) for c in r.flagged_callers],
        )

    def xǁAdminEndpointAuditUseCaseǁexecute__mutmut_13(self, command: AdminEndpointAuditCommand) -> AdminEndpointAuditResponse:
        req = AdminAuditRequest(
            endpoint_pattern=command.endpoint_pattern,
            time_window_minutes=command.time_window_minutes,
            flag_threshold=command.flag_threshold,
        )
        calls = self._port.fetch_failed_admin_calls(req)
        total = self._port.fetch_total_requests(req)
        r = AdminAuditResult.compute(request=None, calls=calls, total_requests=total)
        return AdminEndpointAuditResponse(
            endpoint_pattern=r.endpoint_pattern,
            total_requests=r.total_requests,
            total_403s=r.total_403s,
            rate_403_pct=r.rate_403_pct,
            flagged_callers=[asdict(c) for c in r.flagged_callers],
        )

    def xǁAdminEndpointAuditUseCaseǁexecute__mutmut_14(self, command: AdminEndpointAuditCommand) -> AdminEndpointAuditResponse:
        req = AdminAuditRequest(
            endpoint_pattern=command.endpoint_pattern,
            time_window_minutes=command.time_window_minutes,
            flag_threshold=command.flag_threshold,
        )
        calls = self._port.fetch_failed_admin_calls(req)
        total = self._port.fetch_total_requests(req)
        r = AdminAuditResult.compute(request=req, calls=None, total_requests=total)
        return AdminEndpointAuditResponse(
            endpoint_pattern=r.endpoint_pattern,
            total_requests=r.total_requests,
            total_403s=r.total_403s,
            rate_403_pct=r.rate_403_pct,
            flagged_callers=[asdict(c) for c in r.flagged_callers],
        )

    def xǁAdminEndpointAuditUseCaseǁexecute__mutmut_15(self, command: AdminEndpointAuditCommand) -> AdminEndpointAuditResponse:
        req = AdminAuditRequest(
            endpoint_pattern=command.endpoint_pattern,
            time_window_minutes=command.time_window_minutes,
            flag_threshold=command.flag_threshold,
        )
        calls = self._port.fetch_failed_admin_calls(req)
        total = self._port.fetch_total_requests(req)
        r = AdminAuditResult.compute(request=req, calls=calls, total_requests=None)
        return AdminEndpointAuditResponse(
            endpoint_pattern=r.endpoint_pattern,
            total_requests=r.total_requests,
            total_403s=r.total_403s,
            rate_403_pct=r.rate_403_pct,
            flagged_callers=[asdict(c) for c in r.flagged_callers],
        )

    def xǁAdminEndpointAuditUseCaseǁexecute__mutmut_16(self, command: AdminEndpointAuditCommand) -> AdminEndpointAuditResponse:
        req = AdminAuditRequest(
            endpoint_pattern=command.endpoint_pattern,
            time_window_minutes=command.time_window_minutes,
            flag_threshold=command.flag_threshold,
        )
        calls = self._port.fetch_failed_admin_calls(req)
        total = self._port.fetch_total_requests(req)
        r = AdminAuditResult.compute(calls=calls, total_requests=total)
        return AdminEndpointAuditResponse(
            endpoint_pattern=r.endpoint_pattern,
            total_requests=r.total_requests,
            total_403s=r.total_403s,
            rate_403_pct=r.rate_403_pct,
            flagged_callers=[asdict(c) for c in r.flagged_callers],
        )

    def xǁAdminEndpointAuditUseCaseǁexecute__mutmut_17(self, command: AdminEndpointAuditCommand) -> AdminEndpointAuditResponse:
        req = AdminAuditRequest(
            endpoint_pattern=command.endpoint_pattern,
            time_window_minutes=command.time_window_minutes,
            flag_threshold=command.flag_threshold,
        )
        calls = self._port.fetch_failed_admin_calls(req)
        total = self._port.fetch_total_requests(req)
        r = AdminAuditResult.compute(request=req, total_requests=total)
        return AdminEndpointAuditResponse(
            endpoint_pattern=r.endpoint_pattern,
            total_requests=r.total_requests,
            total_403s=r.total_403s,
            rate_403_pct=r.rate_403_pct,
            flagged_callers=[asdict(c) for c in r.flagged_callers],
        )

    def xǁAdminEndpointAuditUseCaseǁexecute__mutmut_18(self, command: AdminEndpointAuditCommand) -> AdminEndpointAuditResponse:
        req = AdminAuditRequest(
            endpoint_pattern=command.endpoint_pattern,
            time_window_minutes=command.time_window_minutes,
            flag_threshold=command.flag_threshold,
        )
        calls = self._port.fetch_failed_admin_calls(req)
        total = self._port.fetch_total_requests(req)
        r = AdminAuditResult.compute(request=req, calls=calls, )
        return AdminEndpointAuditResponse(
            endpoint_pattern=r.endpoint_pattern,
            total_requests=r.total_requests,
            total_403s=r.total_403s,
            rate_403_pct=r.rate_403_pct,
            flagged_callers=[asdict(c) for c in r.flagged_callers],
        )

    def xǁAdminEndpointAuditUseCaseǁexecute__mutmut_19(self, command: AdminEndpointAuditCommand) -> AdminEndpointAuditResponse:
        req = AdminAuditRequest(
            endpoint_pattern=command.endpoint_pattern,
            time_window_minutes=command.time_window_minutes,
            flag_threshold=command.flag_threshold,
        )
        calls = self._port.fetch_failed_admin_calls(req)
        total = self._port.fetch_total_requests(req)
        r = AdminAuditResult.compute(request=req, calls=calls, total_requests=total)
        return AdminEndpointAuditResponse(
            endpoint_pattern=None,
            total_requests=r.total_requests,
            total_403s=r.total_403s,
            rate_403_pct=r.rate_403_pct,
            flagged_callers=[asdict(c) for c in r.flagged_callers],
        )

    def xǁAdminEndpointAuditUseCaseǁexecute__mutmut_20(self, command: AdminEndpointAuditCommand) -> AdminEndpointAuditResponse:
        req = AdminAuditRequest(
            endpoint_pattern=command.endpoint_pattern,
            time_window_minutes=command.time_window_minutes,
            flag_threshold=command.flag_threshold,
        )
        calls = self._port.fetch_failed_admin_calls(req)
        total = self._port.fetch_total_requests(req)
        r = AdminAuditResult.compute(request=req, calls=calls, total_requests=total)
        return AdminEndpointAuditResponse(
            endpoint_pattern=r.endpoint_pattern,
            total_requests=None,
            total_403s=r.total_403s,
            rate_403_pct=r.rate_403_pct,
            flagged_callers=[asdict(c) for c in r.flagged_callers],
        )

    def xǁAdminEndpointAuditUseCaseǁexecute__mutmut_21(self, command: AdminEndpointAuditCommand) -> AdminEndpointAuditResponse:
        req = AdminAuditRequest(
            endpoint_pattern=command.endpoint_pattern,
            time_window_minutes=command.time_window_minutes,
            flag_threshold=command.flag_threshold,
        )
        calls = self._port.fetch_failed_admin_calls(req)
        total = self._port.fetch_total_requests(req)
        r = AdminAuditResult.compute(request=req, calls=calls, total_requests=total)
        return AdminEndpointAuditResponse(
            endpoint_pattern=r.endpoint_pattern,
            total_requests=r.total_requests,
            total_403s=None,
            rate_403_pct=r.rate_403_pct,
            flagged_callers=[asdict(c) for c in r.flagged_callers],
        )

    def xǁAdminEndpointAuditUseCaseǁexecute__mutmut_22(self, command: AdminEndpointAuditCommand) -> AdminEndpointAuditResponse:
        req = AdminAuditRequest(
            endpoint_pattern=command.endpoint_pattern,
            time_window_minutes=command.time_window_minutes,
            flag_threshold=command.flag_threshold,
        )
        calls = self._port.fetch_failed_admin_calls(req)
        total = self._port.fetch_total_requests(req)
        r = AdminAuditResult.compute(request=req, calls=calls, total_requests=total)
        return AdminEndpointAuditResponse(
            endpoint_pattern=r.endpoint_pattern,
            total_requests=r.total_requests,
            total_403s=r.total_403s,
            rate_403_pct=None,
            flagged_callers=[asdict(c) for c in r.flagged_callers],
        )

    def xǁAdminEndpointAuditUseCaseǁexecute__mutmut_23(self, command: AdminEndpointAuditCommand) -> AdminEndpointAuditResponse:
        req = AdminAuditRequest(
            endpoint_pattern=command.endpoint_pattern,
            time_window_minutes=command.time_window_minutes,
            flag_threshold=command.flag_threshold,
        )
        calls = self._port.fetch_failed_admin_calls(req)
        total = self._port.fetch_total_requests(req)
        r = AdminAuditResult.compute(request=req, calls=calls, total_requests=total)
        return AdminEndpointAuditResponse(
            endpoint_pattern=r.endpoint_pattern,
            total_requests=r.total_requests,
            total_403s=r.total_403s,
            rate_403_pct=r.rate_403_pct,
            flagged_callers=None,
        )

    def xǁAdminEndpointAuditUseCaseǁexecute__mutmut_24(self, command: AdminEndpointAuditCommand) -> AdminEndpointAuditResponse:
        req = AdminAuditRequest(
            endpoint_pattern=command.endpoint_pattern,
            time_window_minutes=command.time_window_minutes,
            flag_threshold=command.flag_threshold,
        )
        calls = self._port.fetch_failed_admin_calls(req)
        total = self._port.fetch_total_requests(req)
        r = AdminAuditResult.compute(request=req, calls=calls, total_requests=total)
        return AdminEndpointAuditResponse(
            total_requests=r.total_requests,
            total_403s=r.total_403s,
            rate_403_pct=r.rate_403_pct,
            flagged_callers=[asdict(c) for c in r.flagged_callers],
        )

    def xǁAdminEndpointAuditUseCaseǁexecute__mutmut_25(self, command: AdminEndpointAuditCommand) -> AdminEndpointAuditResponse:
        req = AdminAuditRequest(
            endpoint_pattern=command.endpoint_pattern,
            time_window_minutes=command.time_window_minutes,
            flag_threshold=command.flag_threshold,
        )
        calls = self._port.fetch_failed_admin_calls(req)
        total = self._port.fetch_total_requests(req)
        r = AdminAuditResult.compute(request=req, calls=calls, total_requests=total)
        return AdminEndpointAuditResponse(
            endpoint_pattern=r.endpoint_pattern,
            total_403s=r.total_403s,
            rate_403_pct=r.rate_403_pct,
            flagged_callers=[asdict(c) for c in r.flagged_callers],
        )

    def xǁAdminEndpointAuditUseCaseǁexecute__mutmut_26(self, command: AdminEndpointAuditCommand) -> AdminEndpointAuditResponse:
        req = AdminAuditRequest(
            endpoint_pattern=command.endpoint_pattern,
            time_window_minutes=command.time_window_minutes,
            flag_threshold=command.flag_threshold,
        )
        calls = self._port.fetch_failed_admin_calls(req)
        total = self._port.fetch_total_requests(req)
        r = AdminAuditResult.compute(request=req, calls=calls, total_requests=total)
        return AdminEndpointAuditResponse(
            endpoint_pattern=r.endpoint_pattern,
            total_requests=r.total_requests,
            rate_403_pct=r.rate_403_pct,
            flagged_callers=[asdict(c) for c in r.flagged_callers],
        )

    def xǁAdminEndpointAuditUseCaseǁexecute__mutmut_27(self, command: AdminEndpointAuditCommand) -> AdminEndpointAuditResponse:
        req = AdminAuditRequest(
            endpoint_pattern=command.endpoint_pattern,
            time_window_minutes=command.time_window_minutes,
            flag_threshold=command.flag_threshold,
        )
        calls = self._port.fetch_failed_admin_calls(req)
        total = self._port.fetch_total_requests(req)
        r = AdminAuditResult.compute(request=req, calls=calls, total_requests=total)
        return AdminEndpointAuditResponse(
            endpoint_pattern=r.endpoint_pattern,
            total_requests=r.total_requests,
            total_403s=r.total_403s,
            flagged_callers=[asdict(c) for c in r.flagged_callers],
        )

    def xǁAdminEndpointAuditUseCaseǁexecute__mutmut_28(self, command: AdminEndpointAuditCommand) -> AdminEndpointAuditResponse:
        req = AdminAuditRequest(
            endpoint_pattern=command.endpoint_pattern,
            time_window_minutes=command.time_window_minutes,
            flag_threshold=command.flag_threshold,
        )
        calls = self._port.fetch_failed_admin_calls(req)
        total = self._port.fetch_total_requests(req)
        r = AdminAuditResult.compute(request=req, calls=calls, total_requests=total)
        return AdminEndpointAuditResponse(
            endpoint_pattern=r.endpoint_pattern,
            total_requests=r.total_requests,
            total_403s=r.total_403s,
            rate_403_pct=r.rate_403_pct,
            )

    def xǁAdminEndpointAuditUseCaseǁexecute__mutmut_29(self, command: AdminEndpointAuditCommand) -> AdminEndpointAuditResponse:
        req = AdminAuditRequest(
            endpoint_pattern=command.endpoint_pattern,
            time_window_minutes=command.time_window_minutes,
            flag_threshold=command.flag_threshold,
        )
        calls = self._port.fetch_failed_admin_calls(req)
        total = self._port.fetch_total_requests(req)
        r = AdminAuditResult.compute(request=req, calls=calls, total_requests=total)
        return AdminEndpointAuditResponse(
            endpoint_pattern=r.endpoint_pattern,
            total_requests=r.total_requests,
            total_403s=r.total_403s,
            rate_403_pct=r.rate_403_pct,
            flagged_callers=[asdict(None) for c in r.flagged_callers],
        )

mutants_xǁAdminEndpointAuditUseCaseǁ__init____mutmut['_mutmut_orig'] = AdminEndpointAuditUseCase.xǁAdminEndpointAuditUseCaseǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁAdminEndpointAuditUseCaseǁ__init____mutmut['xǁAdminEndpointAuditUseCaseǁ__init____mutmut_1'] = AdminEndpointAuditUseCase.xǁAdminEndpointAuditUseCaseǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁAdminEndpointAuditUseCaseǁexecute__mutmut['_mutmut_orig'] = AdminEndpointAuditUseCase.xǁAdminEndpointAuditUseCaseǁexecute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAdminEndpointAuditUseCaseǁexecute__mutmut['xǁAdminEndpointAuditUseCaseǁexecute__mutmut_1'] = AdminEndpointAuditUseCase.xǁAdminEndpointAuditUseCaseǁexecute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAdminEndpointAuditUseCaseǁexecute__mutmut['xǁAdminEndpointAuditUseCaseǁexecute__mutmut_2'] = AdminEndpointAuditUseCase.xǁAdminEndpointAuditUseCaseǁexecute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAdminEndpointAuditUseCaseǁexecute__mutmut['xǁAdminEndpointAuditUseCaseǁexecute__mutmut_3'] = AdminEndpointAuditUseCase.xǁAdminEndpointAuditUseCaseǁexecute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAdminEndpointAuditUseCaseǁexecute__mutmut['xǁAdminEndpointAuditUseCaseǁexecute__mutmut_4'] = AdminEndpointAuditUseCase.xǁAdminEndpointAuditUseCaseǁexecute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAdminEndpointAuditUseCaseǁexecute__mutmut['xǁAdminEndpointAuditUseCaseǁexecute__mutmut_5'] = AdminEndpointAuditUseCase.xǁAdminEndpointAuditUseCaseǁexecute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAdminEndpointAuditUseCaseǁexecute__mutmut['xǁAdminEndpointAuditUseCaseǁexecute__mutmut_6'] = AdminEndpointAuditUseCase.xǁAdminEndpointAuditUseCaseǁexecute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAdminEndpointAuditUseCaseǁexecute__mutmut['xǁAdminEndpointAuditUseCaseǁexecute__mutmut_7'] = AdminEndpointAuditUseCase.xǁAdminEndpointAuditUseCaseǁexecute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAdminEndpointAuditUseCaseǁexecute__mutmut['xǁAdminEndpointAuditUseCaseǁexecute__mutmut_8'] = AdminEndpointAuditUseCase.xǁAdminEndpointAuditUseCaseǁexecute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAdminEndpointAuditUseCaseǁexecute__mutmut['xǁAdminEndpointAuditUseCaseǁexecute__mutmut_9'] = AdminEndpointAuditUseCase.xǁAdminEndpointAuditUseCaseǁexecute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAdminEndpointAuditUseCaseǁexecute__mutmut['xǁAdminEndpointAuditUseCaseǁexecute__mutmut_10'] = AdminEndpointAuditUseCase.xǁAdminEndpointAuditUseCaseǁexecute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAdminEndpointAuditUseCaseǁexecute__mutmut['xǁAdminEndpointAuditUseCaseǁexecute__mutmut_11'] = AdminEndpointAuditUseCase.xǁAdminEndpointAuditUseCaseǁexecute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAdminEndpointAuditUseCaseǁexecute__mutmut['xǁAdminEndpointAuditUseCaseǁexecute__mutmut_12'] = AdminEndpointAuditUseCase.xǁAdminEndpointAuditUseCaseǁexecute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAdminEndpointAuditUseCaseǁexecute__mutmut['xǁAdminEndpointAuditUseCaseǁexecute__mutmut_13'] = AdminEndpointAuditUseCase.xǁAdminEndpointAuditUseCaseǁexecute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAdminEndpointAuditUseCaseǁexecute__mutmut['xǁAdminEndpointAuditUseCaseǁexecute__mutmut_14'] = AdminEndpointAuditUseCase.xǁAdminEndpointAuditUseCaseǁexecute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAdminEndpointAuditUseCaseǁexecute__mutmut['xǁAdminEndpointAuditUseCaseǁexecute__mutmut_15'] = AdminEndpointAuditUseCase.xǁAdminEndpointAuditUseCaseǁexecute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAdminEndpointAuditUseCaseǁexecute__mutmut['xǁAdminEndpointAuditUseCaseǁexecute__mutmut_16'] = AdminEndpointAuditUseCase.xǁAdminEndpointAuditUseCaseǁexecute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAdminEndpointAuditUseCaseǁexecute__mutmut['xǁAdminEndpointAuditUseCaseǁexecute__mutmut_17'] = AdminEndpointAuditUseCase.xǁAdminEndpointAuditUseCaseǁexecute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAdminEndpointAuditUseCaseǁexecute__mutmut['xǁAdminEndpointAuditUseCaseǁexecute__mutmut_18'] = AdminEndpointAuditUseCase.xǁAdminEndpointAuditUseCaseǁexecute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAdminEndpointAuditUseCaseǁexecute__mutmut['xǁAdminEndpointAuditUseCaseǁexecute__mutmut_19'] = AdminEndpointAuditUseCase.xǁAdminEndpointAuditUseCaseǁexecute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAdminEndpointAuditUseCaseǁexecute__mutmut['xǁAdminEndpointAuditUseCaseǁexecute__mutmut_20'] = AdminEndpointAuditUseCase.xǁAdminEndpointAuditUseCaseǁexecute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁAdminEndpointAuditUseCaseǁexecute__mutmut['xǁAdminEndpointAuditUseCaseǁexecute__mutmut_21'] = AdminEndpointAuditUseCase.xǁAdminEndpointAuditUseCaseǁexecute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁAdminEndpointAuditUseCaseǁexecute__mutmut['xǁAdminEndpointAuditUseCaseǁexecute__mutmut_22'] = AdminEndpointAuditUseCase.xǁAdminEndpointAuditUseCaseǁexecute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁAdminEndpointAuditUseCaseǁexecute__mutmut['xǁAdminEndpointAuditUseCaseǁexecute__mutmut_23'] = AdminEndpointAuditUseCase.xǁAdminEndpointAuditUseCaseǁexecute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁAdminEndpointAuditUseCaseǁexecute__mutmut['xǁAdminEndpointAuditUseCaseǁexecute__mutmut_24'] = AdminEndpointAuditUseCase.xǁAdminEndpointAuditUseCaseǁexecute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁAdminEndpointAuditUseCaseǁexecute__mutmut['xǁAdminEndpointAuditUseCaseǁexecute__mutmut_25'] = AdminEndpointAuditUseCase.xǁAdminEndpointAuditUseCaseǁexecute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁAdminEndpointAuditUseCaseǁexecute__mutmut['xǁAdminEndpointAuditUseCaseǁexecute__mutmut_26'] = AdminEndpointAuditUseCase.xǁAdminEndpointAuditUseCaseǁexecute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁAdminEndpointAuditUseCaseǁexecute__mutmut['xǁAdminEndpointAuditUseCaseǁexecute__mutmut_27'] = AdminEndpointAuditUseCase.xǁAdminEndpointAuditUseCaseǁexecute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁAdminEndpointAuditUseCaseǁexecute__mutmut['xǁAdminEndpointAuditUseCaseǁexecute__mutmut_28'] = AdminEndpointAuditUseCase.xǁAdminEndpointAuditUseCaseǁexecute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁAdminEndpointAuditUseCaseǁexecute__mutmut['xǁAdminEndpointAuditUseCaseǁexecute__mutmut_29'] = AdminEndpointAuditUseCase.xǁAdminEndpointAuditUseCaseǁexecute__mutmut_29 # type: ignore # mutmut generated
