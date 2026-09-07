from __future__ import annotations

from hexawyn.application.ports.driven.security_audit_port import SecurityAuditPort
from hexawyn.domain.models.admin_endpoint_audit import AdminAuditRequest, FailedAdminCall
from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_client import search_jaeger_traces


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut: MutantDict = {}  # type: ignore
mutants_xǁOTelSecurityAuditAdapterǁfetch_total_requests__mutmut: MutantDict = {}  # type: ignore


class OTelSecurityAuditAdapter(SecurityAuditPort):
    @_mutmut_mutated(mutants_xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut)
    def fetch_failed_admin_calls(self, request: AdminAuditRequest) -> list[FailedAdminCall]:
        if not request.time_window_minutes:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=50,
            with_errors=True,
        )
        result: list[FailedAdminCall] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    FailedAdminCall(
                        timestamp="",
                        caller_ip="",
                        caller_service="",
                        endpoint=f"trace:{trace['traceID'][:8]}",
                        user_identity=None,
                    )
                )
        return result
    def xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_orig(self, request: AdminAuditRequest) -> list[FailedAdminCall]:
        if not request.time_window_minutes:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=50,
            with_errors=True,
        )
        result: list[FailedAdminCall] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    FailedAdminCall(
                        timestamp="",
                        caller_ip="",
                        caller_service="",
                        endpoint=f"trace:{trace['traceID'][:8]}",
                        user_identity=None,
                    )
                )
        return result
    def xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_1(self, request: AdminAuditRequest) -> list[FailedAdminCall]:
        if request.time_window_minutes:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=50,
            with_errors=True,
        )
        result: list[FailedAdminCall] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    FailedAdminCall(
                        timestamp="",
                        caller_ip="",
                        caller_service="",
                        endpoint=f"trace:{trace['traceID'][:8]}",
                        user_identity=None,
                    )
                )
        return result
    def xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_2(self, request: AdminAuditRequest) -> list[FailedAdminCall]:
        if not request.time_window_minutes:
            return []

        traces = None
        result: list[FailedAdminCall] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    FailedAdminCall(
                        timestamp="",
                        caller_ip="",
                        caller_service="",
                        endpoint=f"trace:{trace['traceID'][:8]}",
                        user_identity=None,
                    )
                )
        return result
    def xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_3(self, request: AdminAuditRequest) -> list[FailedAdminCall]:
        if not request.time_window_minutes:
            return []

        traces = search_jaeger_traces(
            service=None,
            limit=50,
            with_errors=True,
        )
        result: list[FailedAdminCall] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    FailedAdminCall(
                        timestamp="",
                        caller_ip="",
                        caller_service="",
                        endpoint=f"trace:{trace['traceID'][:8]}",
                        user_identity=None,
                    )
                )
        return result
    def xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_4(self, request: AdminAuditRequest) -> list[FailedAdminCall]:
        if not request.time_window_minutes:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=None,
            with_errors=True,
        )
        result: list[FailedAdminCall] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    FailedAdminCall(
                        timestamp="",
                        caller_ip="",
                        caller_service="",
                        endpoint=f"trace:{trace['traceID'][:8]}",
                        user_identity=None,
                    )
                )
        return result
    def xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_5(self, request: AdminAuditRequest) -> list[FailedAdminCall]:
        if not request.time_window_minutes:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=50,
            with_errors=None,
        )
        result: list[FailedAdminCall] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    FailedAdminCall(
                        timestamp="",
                        caller_ip="",
                        caller_service="",
                        endpoint=f"trace:{trace['traceID'][:8]}",
                        user_identity=None,
                    )
                )
        return result
    def xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_6(self, request: AdminAuditRequest) -> list[FailedAdminCall]:
        if not request.time_window_minutes:
            return []

        traces = search_jaeger_traces(
            limit=50,
            with_errors=True,
        )
        result: list[FailedAdminCall] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    FailedAdminCall(
                        timestamp="",
                        caller_ip="",
                        caller_service="",
                        endpoint=f"trace:{trace['traceID'][:8]}",
                        user_identity=None,
                    )
                )
        return result
    def xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_7(self, request: AdminAuditRequest) -> list[FailedAdminCall]:
        if not request.time_window_minutes:
            return []

        traces = search_jaeger_traces(
            service="",
            with_errors=True,
        )
        result: list[FailedAdminCall] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    FailedAdminCall(
                        timestamp="",
                        caller_ip="",
                        caller_service="",
                        endpoint=f"trace:{trace['traceID'][:8]}",
                        user_identity=None,
                    )
                )
        return result
    def xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_8(self, request: AdminAuditRequest) -> list[FailedAdminCall]:
        if not request.time_window_minutes:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=50,
            )
        result: list[FailedAdminCall] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    FailedAdminCall(
                        timestamp="",
                        caller_ip="",
                        caller_service="",
                        endpoint=f"trace:{trace['traceID'][:8]}",
                        user_identity=None,
                    )
                )
        return result
    def xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_9(self, request: AdminAuditRequest) -> list[FailedAdminCall]:
        if not request.time_window_minutes:
            return []

        traces = search_jaeger_traces(
            service="XXXX",
            limit=50,
            with_errors=True,
        )
        result: list[FailedAdminCall] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    FailedAdminCall(
                        timestamp="",
                        caller_ip="",
                        caller_service="",
                        endpoint=f"trace:{trace['traceID'][:8]}",
                        user_identity=None,
                    )
                )
        return result
    def xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_10(self, request: AdminAuditRequest) -> list[FailedAdminCall]:
        if not request.time_window_minutes:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=51,
            with_errors=True,
        )
        result: list[FailedAdminCall] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    FailedAdminCall(
                        timestamp="",
                        caller_ip="",
                        caller_service="",
                        endpoint=f"trace:{trace['traceID'][:8]}",
                        user_identity=None,
                    )
                )
        return result
    def xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_11(self, request: AdminAuditRequest) -> list[FailedAdminCall]:
        if not request.time_window_minutes:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=50,
            with_errors=False,
        )
        result: list[FailedAdminCall] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    FailedAdminCall(
                        timestamp="",
                        caller_ip="",
                        caller_service="",
                        endpoint=f"trace:{trace['traceID'][:8]}",
                        user_identity=None,
                    )
                )
        return result
    def xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_12(self, request: AdminAuditRequest) -> list[FailedAdminCall]:
        if not request.time_window_minutes:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=50,
            with_errors=True,
        )
        result: list[FailedAdminCall] = None
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    FailedAdminCall(
                        timestamp="",
                        caller_ip="",
                        caller_service="",
                        endpoint=f"trace:{trace['traceID'][:8]}",
                        user_identity=None,
                    )
                )
        return result
    def xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_13(self, request: AdminAuditRequest) -> list[FailedAdminCall]:
        if not request.time_window_minutes:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=50,
            with_errors=True,
        )
        result: list[FailedAdminCall] = []
        for trace in traces:
            if trace.get(None):
                result.append(
                    FailedAdminCall(
                        timestamp="",
                        caller_ip="",
                        caller_service="",
                        endpoint=f"trace:{trace['traceID'][:8]}",
                        user_identity=None,
                    )
                )
        return result
    def xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_14(self, request: AdminAuditRequest) -> list[FailedAdminCall]:
        if not request.time_window_minutes:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=50,
            with_errors=True,
        )
        result: list[FailedAdminCall] = []
        for trace in traces:
            if trace.get("XXhasErrorsXX"):
                result.append(
                    FailedAdminCall(
                        timestamp="",
                        caller_ip="",
                        caller_service="",
                        endpoint=f"trace:{trace['traceID'][:8]}",
                        user_identity=None,
                    )
                )
        return result
    def xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_15(self, request: AdminAuditRequest) -> list[FailedAdminCall]:
        if not request.time_window_minutes:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=50,
            with_errors=True,
        )
        result: list[FailedAdminCall] = []
        for trace in traces:
            if trace.get("haserrors"):
                result.append(
                    FailedAdminCall(
                        timestamp="",
                        caller_ip="",
                        caller_service="",
                        endpoint=f"trace:{trace['traceID'][:8]}",
                        user_identity=None,
                    )
                )
        return result
    def xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_16(self, request: AdminAuditRequest) -> list[FailedAdminCall]:
        if not request.time_window_minutes:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=50,
            with_errors=True,
        )
        result: list[FailedAdminCall] = []
        for trace in traces:
            if trace.get("HASERRORS"):
                result.append(
                    FailedAdminCall(
                        timestamp="",
                        caller_ip="",
                        caller_service="",
                        endpoint=f"trace:{trace['traceID'][:8]}",
                        user_identity=None,
                    )
                )
        return result
    def xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_17(self, request: AdminAuditRequest) -> list[FailedAdminCall]:
        if not request.time_window_minutes:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=50,
            with_errors=True,
        )
        result: list[FailedAdminCall] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    None
                )
        return result
    def xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_18(self, request: AdminAuditRequest) -> list[FailedAdminCall]:
        if not request.time_window_minutes:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=50,
            with_errors=True,
        )
        result: list[FailedAdminCall] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    FailedAdminCall(
                        timestamp=None,
                        caller_ip="",
                        caller_service="",
                        endpoint=f"trace:{trace['traceID'][:8]}",
                        user_identity=None,
                    )
                )
        return result
    def xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_19(self, request: AdminAuditRequest) -> list[FailedAdminCall]:
        if not request.time_window_minutes:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=50,
            with_errors=True,
        )
        result: list[FailedAdminCall] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    FailedAdminCall(
                        timestamp="",
                        caller_ip=None,
                        caller_service="",
                        endpoint=f"trace:{trace['traceID'][:8]}",
                        user_identity=None,
                    )
                )
        return result
    def xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_20(self, request: AdminAuditRequest) -> list[FailedAdminCall]:
        if not request.time_window_minutes:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=50,
            with_errors=True,
        )
        result: list[FailedAdminCall] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    FailedAdminCall(
                        timestamp="",
                        caller_ip="",
                        caller_service=None,
                        endpoint=f"trace:{trace['traceID'][:8]}",
                        user_identity=None,
                    )
                )
        return result
    def xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_21(self, request: AdminAuditRequest) -> list[FailedAdminCall]:
        if not request.time_window_minutes:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=50,
            with_errors=True,
        )
        result: list[FailedAdminCall] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    FailedAdminCall(
                        timestamp="",
                        caller_ip="",
                        caller_service="",
                        endpoint=None,
                        user_identity=None,
                    )
                )
        return result
    def xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_22(self, request: AdminAuditRequest) -> list[FailedAdminCall]:
        if not request.time_window_minutes:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=50,
            with_errors=True,
        )
        result: list[FailedAdminCall] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    FailedAdminCall(
                        caller_ip="",
                        caller_service="",
                        endpoint=f"trace:{trace['traceID'][:8]}",
                        user_identity=None,
                    )
                )
        return result
    def xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_23(self, request: AdminAuditRequest) -> list[FailedAdminCall]:
        if not request.time_window_minutes:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=50,
            with_errors=True,
        )
        result: list[FailedAdminCall] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    FailedAdminCall(
                        timestamp="",
                        caller_service="",
                        endpoint=f"trace:{trace['traceID'][:8]}",
                        user_identity=None,
                    )
                )
        return result
    def xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_24(self, request: AdminAuditRequest) -> list[FailedAdminCall]:
        if not request.time_window_minutes:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=50,
            with_errors=True,
        )
        result: list[FailedAdminCall] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    FailedAdminCall(
                        timestamp="",
                        caller_ip="",
                        endpoint=f"trace:{trace['traceID'][:8]}",
                        user_identity=None,
                    )
                )
        return result
    def xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_25(self, request: AdminAuditRequest) -> list[FailedAdminCall]:
        if not request.time_window_minutes:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=50,
            with_errors=True,
        )
        result: list[FailedAdminCall] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    FailedAdminCall(
                        timestamp="",
                        caller_ip="",
                        caller_service="",
                        user_identity=None,
                    )
                )
        return result
    def xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_26(self, request: AdminAuditRequest) -> list[FailedAdminCall]:
        if not request.time_window_minutes:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=50,
            with_errors=True,
        )
        result: list[FailedAdminCall] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    FailedAdminCall(
                        timestamp="",
                        caller_ip="",
                        caller_service="",
                        endpoint=f"trace:{trace['traceID'][:8]}",
                        )
                )
        return result
    def xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_27(self, request: AdminAuditRequest) -> list[FailedAdminCall]:
        if not request.time_window_minutes:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=50,
            with_errors=True,
        )
        result: list[FailedAdminCall] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    FailedAdminCall(
                        timestamp="XXXX",
                        caller_ip="",
                        caller_service="",
                        endpoint=f"trace:{trace['traceID'][:8]}",
                        user_identity=None,
                    )
                )
        return result
    def xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_28(self, request: AdminAuditRequest) -> list[FailedAdminCall]:
        if not request.time_window_minutes:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=50,
            with_errors=True,
        )
        result: list[FailedAdminCall] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    FailedAdminCall(
                        timestamp="",
                        caller_ip="XXXX",
                        caller_service="",
                        endpoint=f"trace:{trace['traceID'][:8]}",
                        user_identity=None,
                    )
                )
        return result
    def xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_29(self, request: AdminAuditRequest) -> list[FailedAdminCall]:
        if not request.time_window_minutes:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=50,
            with_errors=True,
        )
        result: list[FailedAdminCall] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    FailedAdminCall(
                        timestamp="",
                        caller_ip="",
                        caller_service="XXXX",
                        endpoint=f"trace:{trace['traceID'][:8]}",
                        user_identity=None,
                    )
                )
        return result
    def xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_30(self, request: AdminAuditRequest) -> list[FailedAdminCall]:
        if not request.time_window_minutes:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=50,
            with_errors=True,
        )
        result: list[FailedAdminCall] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    FailedAdminCall(
                        timestamp="",
                        caller_ip="",
                        caller_service="",
                        endpoint=f"trace:{trace['XXtraceIDXX'][:8]}",
                        user_identity=None,
                    )
                )
        return result
    def xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_31(self, request: AdminAuditRequest) -> list[FailedAdminCall]:
        if not request.time_window_minutes:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=50,
            with_errors=True,
        )
        result: list[FailedAdminCall] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    FailedAdminCall(
                        timestamp="",
                        caller_ip="",
                        caller_service="",
                        endpoint=f"trace:{trace['traceid'][:8]}",
                        user_identity=None,
                    )
                )
        return result
    def xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_32(self, request: AdminAuditRequest) -> list[FailedAdminCall]:
        if not request.time_window_minutes:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=50,
            with_errors=True,
        )
        result: list[FailedAdminCall] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    FailedAdminCall(
                        timestamp="",
                        caller_ip="",
                        caller_service="",
                        endpoint=f"trace:{trace['TRACEID'][:8]}",
                        user_identity=None,
                    )
                )
        return result
    def xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_33(self, request: AdminAuditRequest) -> list[FailedAdminCall]:
        if not request.time_window_minutes:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=50,
            with_errors=True,
        )
        result: list[FailedAdminCall] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    FailedAdminCall(
                        timestamp="",
                        caller_ip="",
                        caller_service="",
                        endpoint=f"trace:{trace['traceID'][:9]}",
                        user_identity=None,
                    )
                )
        return result

    @_mutmut_mutated(mutants_xǁOTelSecurityAuditAdapterǁfetch_total_requests__mutmut)
    def fetch_total_requests(self, request: AdminAuditRequest) -> int:
        traces = search_jaeger_traces(
            service="",
            limit=100,
        )
        return len(traces)

    def xǁOTelSecurityAuditAdapterǁfetch_total_requests__mutmut_orig(self, request: AdminAuditRequest) -> int:
        traces = search_jaeger_traces(
            service="",
            limit=100,
        )
        return len(traces)

    def xǁOTelSecurityAuditAdapterǁfetch_total_requests__mutmut_1(self, request: AdminAuditRequest) -> int:
        traces = None
        return len(traces)

    def xǁOTelSecurityAuditAdapterǁfetch_total_requests__mutmut_2(self, request: AdminAuditRequest) -> int:
        traces = search_jaeger_traces(
            service=None,
            limit=100,
        )
        return len(traces)

    def xǁOTelSecurityAuditAdapterǁfetch_total_requests__mutmut_3(self, request: AdminAuditRequest) -> int:
        traces = search_jaeger_traces(
            service="",
            limit=None,
        )
        return len(traces)

    def xǁOTelSecurityAuditAdapterǁfetch_total_requests__mutmut_4(self, request: AdminAuditRequest) -> int:
        traces = search_jaeger_traces(
            limit=100,
        )
        return len(traces)

    def xǁOTelSecurityAuditAdapterǁfetch_total_requests__mutmut_5(self, request: AdminAuditRequest) -> int:
        traces = search_jaeger_traces(
            service="",
            )
        return len(traces)

    def xǁOTelSecurityAuditAdapterǁfetch_total_requests__mutmut_6(self, request: AdminAuditRequest) -> int:
        traces = search_jaeger_traces(
            service="XXXX",
            limit=100,
        )
        return len(traces)

    def xǁOTelSecurityAuditAdapterǁfetch_total_requests__mutmut_7(self, request: AdminAuditRequest) -> int:
        traces = search_jaeger_traces(
            service="",
            limit=101,
        )
        return len(traces)

mutants_xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut['_mutmut_orig'] = OTelSecurityAuditAdapter.xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut['xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_1'] = OTelSecurityAuditAdapter.xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut['xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_2'] = OTelSecurityAuditAdapter.xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut['xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_3'] = OTelSecurityAuditAdapter.xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut['xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_4'] = OTelSecurityAuditAdapter.xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut['xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_5'] = OTelSecurityAuditAdapter.xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut['xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_6'] = OTelSecurityAuditAdapter.xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_6 # type: ignore # mutmut generated
mutants_xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut['xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_7'] = OTelSecurityAuditAdapter.xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_7 # type: ignore # mutmut generated
mutants_xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut['xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_8'] = OTelSecurityAuditAdapter.xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_8 # type: ignore # mutmut generated
mutants_xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut['xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_9'] = OTelSecurityAuditAdapter.xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_9 # type: ignore # mutmut generated
mutants_xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut['xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_10'] = OTelSecurityAuditAdapter.xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_10 # type: ignore # mutmut generated
mutants_xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut['xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_11'] = OTelSecurityAuditAdapter.xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_11 # type: ignore # mutmut generated
mutants_xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut['xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_12'] = OTelSecurityAuditAdapter.xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_12 # type: ignore # mutmut generated
mutants_xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut['xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_13'] = OTelSecurityAuditAdapter.xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_13 # type: ignore # mutmut generated
mutants_xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut['xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_14'] = OTelSecurityAuditAdapter.xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_14 # type: ignore # mutmut generated
mutants_xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut['xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_15'] = OTelSecurityAuditAdapter.xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_15 # type: ignore # mutmut generated
mutants_xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut['xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_16'] = OTelSecurityAuditAdapter.xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_16 # type: ignore # mutmut generated
mutants_xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut['xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_17'] = OTelSecurityAuditAdapter.xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_17 # type: ignore # mutmut generated
mutants_xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut['xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_18'] = OTelSecurityAuditAdapter.xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_18 # type: ignore # mutmut generated
mutants_xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut['xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_19'] = OTelSecurityAuditAdapter.xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_19 # type: ignore # mutmut generated
mutants_xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut['xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_20'] = OTelSecurityAuditAdapter.xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_20 # type: ignore # mutmut generated
mutants_xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut['xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_21'] = OTelSecurityAuditAdapter.xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_21 # type: ignore # mutmut generated
mutants_xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut['xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_22'] = OTelSecurityAuditAdapter.xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_22 # type: ignore # mutmut generated
mutants_xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut['xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_23'] = OTelSecurityAuditAdapter.xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_23 # type: ignore # mutmut generated
mutants_xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut['xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_24'] = OTelSecurityAuditAdapter.xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_24 # type: ignore # mutmut generated
mutants_xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut['xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_25'] = OTelSecurityAuditAdapter.xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_25 # type: ignore # mutmut generated
mutants_xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut['xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_26'] = OTelSecurityAuditAdapter.xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_26 # type: ignore # mutmut generated
mutants_xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut['xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_27'] = OTelSecurityAuditAdapter.xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_27 # type: ignore # mutmut generated
mutants_xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut['xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_28'] = OTelSecurityAuditAdapter.xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_28 # type: ignore # mutmut generated
mutants_xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut['xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_29'] = OTelSecurityAuditAdapter.xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_29 # type: ignore # mutmut generated
mutants_xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut['xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_30'] = OTelSecurityAuditAdapter.xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_30 # type: ignore # mutmut generated
mutants_xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut['xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_31'] = OTelSecurityAuditAdapter.xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_31 # type: ignore # mutmut generated
mutants_xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut['xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_32'] = OTelSecurityAuditAdapter.xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_32 # type: ignore # mutmut generated
mutants_xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut['xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_33'] = OTelSecurityAuditAdapter.xǁOTelSecurityAuditAdapterǁfetch_failed_admin_calls__mutmut_33 # type: ignore # mutmut generated

mutants_xǁOTelSecurityAuditAdapterǁfetch_total_requests__mutmut['_mutmut_orig'] = OTelSecurityAuditAdapter.xǁOTelSecurityAuditAdapterǁfetch_total_requests__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOTelSecurityAuditAdapterǁfetch_total_requests__mutmut['xǁOTelSecurityAuditAdapterǁfetch_total_requests__mutmut_1'] = OTelSecurityAuditAdapter.xǁOTelSecurityAuditAdapterǁfetch_total_requests__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOTelSecurityAuditAdapterǁfetch_total_requests__mutmut['xǁOTelSecurityAuditAdapterǁfetch_total_requests__mutmut_2'] = OTelSecurityAuditAdapter.xǁOTelSecurityAuditAdapterǁfetch_total_requests__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOTelSecurityAuditAdapterǁfetch_total_requests__mutmut['xǁOTelSecurityAuditAdapterǁfetch_total_requests__mutmut_3'] = OTelSecurityAuditAdapter.xǁOTelSecurityAuditAdapterǁfetch_total_requests__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOTelSecurityAuditAdapterǁfetch_total_requests__mutmut['xǁOTelSecurityAuditAdapterǁfetch_total_requests__mutmut_4'] = OTelSecurityAuditAdapter.xǁOTelSecurityAuditAdapterǁfetch_total_requests__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOTelSecurityAuditAdapterǁfetch_total_requests__mutmut['xǁOTelSecurityAuditAdapterǁfetch_total_requests__mutmut_5'] = OTelSecurityAuditAdapter.xǁOTelSecurityAuditAdapterǁfetch_total_requests__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOTelSecurityAuditAdapterǁfetch_total_requests__mutmut['xǁOTelSecurityAuditAdapterǁfetch_total_requests__mutmut_6'] = OTelSecurityAuditAdapter.xǁOTelSecurityAuditAdapterǁfetch_total_requests__mutmut_6 # type: ignore # mutmut generated
mutants_xǁOTelSecurityAuditAdapterǁfetch_total_requests__mutmut['xǁOTelSecurityAuditAdapterǁfetch_total_requests__mutmut_7'] = OTelSecurityAuditAdapter.xǁOTelSecurityAuditAdapterǁfetch_total_requests__mutmut_7 # type: ignore # mutmut generated
