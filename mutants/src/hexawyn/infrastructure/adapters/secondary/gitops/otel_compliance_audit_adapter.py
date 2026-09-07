from __future__ import annotations

from hexawyn.application.ports.driven.compliance_audit_port import (
    ComplianceAuditPort,
)
from hexawyn.domain.models.sensitive_data_audit import AccessMatch, SensitiveAccessRequest
from hexawyn.infrastructure.adapters.secondary.gitops.otel_http_client import search_jaeger_traces


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut: MutantDict = {}  # type: ignore


class OTelComplianceAuditAdapter(ComplianceAuditPort):
    @_mutmut_mutated(mutants_xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut)
    def fetch_access_matches(self, request: SensitiveAccessRequest) -> list[AccessMatch]:
        if not request.pattern:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=20,
            with_errors=True,
        )
        result: list[AccessMatch] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    AccessMatch(
                        timestamp="",
                        caller_ip="",
                        caller_service="unknown",
                        method="",
                        url="",
                        status_code=0,
                        user_id=None,
                    )
                )
        return result
    def xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_orig(self, request: SensitiveAccessRequest) -> list[AccessMatch]:
        if not request.pattern:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=20,
            with_errors=True,
        )
        result: list[AccessMatch] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    AccessMatch(
                        timestamp="",
                        caller_ip="",
                        caller_service="unknown",
                        method="",
                        url="",
                        status_code=0,
                        user_id=None,
                    )
                )
        return result
    def xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_1(self, request: SensitiveAccessRequest) -> list[AccessMatch]:
        if request.pattern:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=20,
            with_errors=True,
        )
        result: list[AccessMatch] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    AccessMatch(
                        timestamp="",
                        caller_ip="",
                        caller_service="unknown",
                        method="",
                        url="",
                        status_code=0,
                        user_id=None,
                    )
                )
        return result
    def xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_2(self, request: SensitiveAccessRequest) -> list[AccessMatch]:
        if not request.pattern:
            return []

        traces = None
        result: list[AccessMatch] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    AccessMatch(
                        timestamp="",
                        caller_ip="",
                        caller_service="unknown",
                        method="",
                        url="",
                        status_code=0,
                        user_id=None,
                    )
                )
        return result
    def xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_3(self, request: SensitiveAccessRequest) -> list[AccessMatch]:
        if not request.pattern:
            return []

        traces = search_jaeger_traces(
            service=None,
            limit=20,
            with_errors=True,
        )
        result: list[AccessMatch] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    AccessMatch(
                        timestamp="",
                        caller_ip="",
                        caller_service="unknown",
                        method="",
                        url="",
                        status_code=0,
                        user_id=None,
                    )
                )
        return result
    def xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_4(self, request: SensitiveAccessRequest) -> list[AccessMatch]:
        if not request.pattern:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=None,
            with_errors=True,
        )
        result: list[AccessMatch] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    AccessMatch(
                        timestamp="",
                        caller_ip="",
                        caller_service="unknown",
                        method="",
                        url="",
                        status_code=0,
                        user_id=None,
                    )
                )
        return result
    def xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_5(self, request: SensitiveAccessRequest) -> list[AccessMatch]:
        if not request.pattern:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=20,
            with_errors=None,
        )
        result: list[AccessMatch] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    AccessMatch(
                        timestamp="",
                        caller_ip="",
                        caller_service="unknown",
                        method="",
                        url="",
                        status_code=0,
                        user_id=None,
                    )
                )
        return result
    def xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_6(self, request: SensitiveAccessRequest) -> list[AccessMatch]:
        if not request.pattern:
            return []

        traces = search_jaeger_traces(
            limit=20,
            with_errors=True,
        )
        result: list[AccessMatch] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    AccessMatch(
                        timestamp="",
                        caller_ip="",
                        caller_service="unknown",
                        method="",
                        url="",
                        status_code=0,
                        user_id=None,
                    )
                )
        return result
    def xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_7(self, request: SensitiveAccessRequest) -> list[AccessMatch]:
        if not request.pattern:
            return []

        traces = search_jaeger_traces(
            service="",
            with_errors=True,
        )
        result: list[AccessMatch] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    AccessMatch(
                        timestamp="",
                        caller_ip="",
                        caller_service="unknown",
                        method="",
                        url="",
                        status_code=0,
                        user_id=None,
                    )
                )
        return result
    def xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_8(self, request: SensitiveAccessRequest) -> list[AccessMatch]:
        if not request.pattern:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=20,
            )
        result: list[AccessMatch] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    AccessMatch(
                        timestamp="",
                        caller_ip="",
                        caller_service="unknown",
                        method="",
                        url="",
                        status_code=0,
                        user_id=None,
                    )
                )
        return result
    def xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_9(self, request: SensitiveAccessRequest) -> list[AccessMatch]:
        if not request.pattern:
            return []

        traces = search_jaeger_traces(
            service="XXXX",
            limit=20,
            with_errors=True,
        )
        result: list[AccessMatch] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    AccessMatch(
                        timestamp="",
                        caller_ip="",
                        caller_service="unknown",
                        method="",
                        url="",
                        status_code=0,
                        user_id=None,
                    )
                )
        return result
    def xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_10(self, request: SensitiveAccessRequest) -> list[AccessMatch]:
        if not request.pattern:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=21,
            with_errors=True,
        )
        result: list[AccessMatch] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    AccessMatch(
                        timestamp="",
                        caller_ip="",
                        caller_service="unknown",
                        method="",
                        url="",
                        status_code=0,
                        user_id=None,
                    )
                )
        return result
    def xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_11(self, request: SensitiveAccessRequest) -> list[AccessMatch]:
        if not request.pattern:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=20,
            with_errors=False,
        )
        result: list[AccessMatch] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    AccessMatch(
                        timestamp="",
                        caller_ip="",
                        caller_service="unknown",
                        method="",
                        url="",
                        status_code=0,
                        user_id=None,
                    )
                )
        return result
    def xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_12(self, request: SensitiveAccessRequest) -> list[AccessMatch]:
        if not request.pattern:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=20,
            with_errors=True,
        )
        result: list[AccessMatch] = None
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    AccessMatch(
                        timestamp="",
                        caller_ip="",
                        caller_service="unknown",
                        method="",
                        url="",
                        status_code=0,
                        user_id=None,
                    )
                )
        return result
    def xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_13(self, request: SensitiveAccessRequest) -> list[AccessMatch]:
        if not request.pattern:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=20,
            with_errors=True,
        )
        result: list[AccessMatch] = []
        for trace in traces:
            if trace.get(None):
                result.append(
                    AccessMatch(
                        timestamp="",
                        caller_ip="",
                        caller_service="unknown",
                        method="",
                        url="",
                        status_code=0,
                        user_id=None,
                    )
                )
        return result
    def xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_14(self, request: SensitiveAccessRequest) -> list[AccessMatch]:
        if not request.pattern:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=20,
            with_errors=True,
        )
        result: list[AccessMatch] = []
        for trace in traces:
            if trace.get("XXhasErrorsXX"):
                result.append(
                    AccessMatch(
                        timestamp="",
                        caller_ip="",
                        caller_service="unknown",
                        method="",
                        url="",
                        status_code=0,
                        user_id=None,
                    )
                )
        return result
    def xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_15(self, request: SensitiveAccessRequest) -> list[AccessMatch]:
        if not request.pattern:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=20,
            with_errors=True,
        )
        result: list[AccessMatch] = []
        for trace in traces:
            if trace.get("haserrors"):
                result.append(
                    AccessMatch(
                        timestamp="",
                        caller_ip="",
                        caller_service="unknown",
                        method="",
                        url="",
                        status_code=0,
                        user_id=None,
                    )
                )
        return result
    def xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_16(self, request: SensitiveAccessRequest) -> list[AccessMatch]:
        if not request.pattern:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=20,
            with_errors=True,
        )
        result: list[AccessMatch] = []
        for trace in traces:
            if trace.get("HASERRORS"):
                result.append(
                    AccessMatch(
                        timestamp="",
                        caller_ip="",
                        caller_service="unknown",
                        method="",
                        url="",
                        status_code=0,
                        user_id=None,
                    )
                )
        return result
    def xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_17(self, request: SensitiveAccessRequest) -> list[AccessMatch]:
        if not request.pattern:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=20,
            with_errors=True,
        )
        result: list[AccessMatch] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    None
                )
        return result
    def xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_18(self, request: SensitiveAccessRequest) -> list[AccessMatch]:
        if not request.pattern:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=20,
            with_errors=True,
        )
        result: list[AccessMatch] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    AccessMatch(
                        timestamp=None,
                        caller_ip="",
                        caller_service="unknown",
                        method="",
                        url="",
                        status_code=0,
                        user_id=None,
                    )
                )
        return result
    def xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_19(self, request: SensitiveAccessRequest) -> list[AccessMatch]:
        if not request.pattern:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=20,
            with_errors=True,
        )
        result: list[AccessMatch] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    AccessMatch(
                        timestamp="",
                        caller_ip=None,
                        caller_service="unknown",
                        method="",
                        url="",
                        status_code=0,
                        user_id=None,
                    )
                )
        return result
    def xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_20(self, request: SensitiveAccessRequest) -> list[AccessMatch]:
        if not request.pattern:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=20,
            with_errors=True,
        )
        result: list[AccessMatch] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    AccessMatch(
                        timestamp="",
                        caller_ip="",
                        caller_service=None,
                        method="",
                        url="",
                        status_code=0,
                        user_id=None,
                    )
                )
        return result
    def xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_21(self, request: SensitiveAccessRequest) -> list[AccessMatch]:
        if not request.pattern:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=20,
            with_errors=True,
        )
        result: list[AccessMatch] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    AccessMatch(
                        timestamp="",
                        caller_ip="",
                        caller_service="unknown",
                        method=None,
                        url="",
                        status_code=0,
                        user_id=None,
                    )
                )
        return result
    def xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_22(self, request: SensitiveAccessRequest) -> list[AccessMatch]:
        if not request.pattern:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=20,
            with_errors=True,
        )
        result: list[AccessMatch] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    AccessMatch(
                        timestamp="",
                        caller_ip="",
                        caller_service="unknown",
                        method="",
                        url=None,
                        status_code=0,
                        user_id=None,
                    )
                )
        return result
    def xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_23(self, request: SensitiveAccessRequest) -> list[AccessMatch]:
        if not request.pattern:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=20,
            with_errors=True,
        )
        result: list[AccessMatch] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    AccessMatch(
                        timestamp="",
                        caller_ip="",
                        caller_service="unknown",
                        method="",
                        url="",
                        status_code=None,
                        user_id=None,
                    )
                )
        return result
    def xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_24(self, request: SensitiveAccessRequest) -> list[AccessMatch]:
        if not request.pattern:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=20,
            with_errors=True,
        )
        result: list[AccessMatch] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    AccessMatch(
                        caller_ip="",
                        caller_service="unknown",
                        method="",
                        url="",
                        status_code=0,
                        user_id=None,
                    )
                )
        return result
    def xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_25(self, request: SensitiveAccessRequest) -> list[AccessMatch]:
        if not request.pattern:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=20,
            with_errors=True,
        )
        result: list[AccessMatch] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    AccessMatch(
                        timestamp="",
                        caller_service="unknown",
                        method="",
                        url="",
                        status_code=0,
                        user_id=None,
                    )
                )
        return result
    def xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_26(self, request: SensitiveAccessRequest) -> list[AccessMatch]:
        if not request.pattern:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=20,
            with_errors=True,
        )
        result: list[AccessMatch] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    AccessMatch(
                        timestamp="",
                        caller_ip="",
                        method="",
                        url="",
                        status_code=0,
                        user_id=None,
                    )
                )
        return result
    def xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_27(self, request: SensitiveAccessRequest) -> list[AccessMatch]:
        if not request.pattern:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=20,
            with_errors=True,
        )
        result: list[AccessMatch] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    AccessMatch(
                        timestamp="",
                        caller_ip="",
                        caller_service="unknown",
                        url="",
                        status_code=0,
                        user_id=None,
                    )
                )
        return result
    def xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_28(self, request: SensitiveAccessRequest) -> list[AccessMatch]:
        if not request.pattern:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=20,
            with_errors=True,
        )
        result: list[AccessMatch] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    AccessMatch(
                        timestamp="",
                        caller_ip="",
                        caller_service="unknown",
                        method="",
                        status_code=0,
                        user_id=None,
                    )
                )
        return result
    def xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_29(self, request: SensitiveAccessRequest) -> list[AccessMatch]:
        if not request.pattern:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=20,
            with_errors=True,
        )
        result: list[AccessMatch] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    AccessMatch(
                        timestamp="",
                        caller_ip="",
                        caller_service="unknown",
                        method="",
                        url="",
                        user_id=None,
                    )
                )
        return result
    def xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_30(self, request: SensitiveAccessRequest) -> list[AccessMatch]:
        if not request.pattern:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=20,
            with_errors=True,
        )
        result: list[AccessMatch] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    AccessMatch(
                        timestamp="",
                        caller_ip="",
                        caller_service="unknown",
                        method="",
                        url="",
                        status_code=0,
                        )
                )
        return result
    def xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_31(self, request: SensitiveAccessRequest) -> list[AccessMatch]:
        if not request.pattern:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=20,
            with_errors=True,
        )
        result: list[AccessMatch] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    AccessMatch(
                        timestamp="XXXX",
                        caller_ip="",
                        caller_service="unknown",
                        method="",
                        url="",
                        status_code=0,
                        user_id=None,
                    )
                )
        return result
    def xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_32(self, request: SensitiveAccessRequest) -> list[AccessMatch]:
        if not request.pattern:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=20,
            with_errors=True,
        )
        result: list[AccessMatch] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    AccessMatch(
                        timestamp="",
                        caller_ip="XXXX",
                        caller_service="unknown",
                        method="",
                        url="",
                        status_code=0,
                        user_id=None,
                    )
                )
        return result
    def xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_33(self, request: SensitiveAccessRequest) -> list[AccessMatch]:
        if not request.pattern:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=20,
            with_errors=True,
        )
        result: list[AccessMatch] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    AccessMatch(
                        timestamp="",
                        caller_ip="",
                        caller_service="XXunknownXX",
                        method="",
                        url="",
                        status_code=0,
                        user_id=None,
                    )
                )
        return result
    def xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_34(self, request: SensitiveAccessRequest) -> list[AccessMatch]:
        if not request.pattern:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=20,
            with_errors=True,
        )
        result: list[AccessMatch] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    AccessMatch(
                        timestamp="",
                        caller_ip="",
                        caller_service="UNKNOWN",
                        method="",
                        url="",
                        status_code=0,
                        user_id=None,
                    )
                )
        return result
    def xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_35(self, request: SensitiveAccessRequest) -> list[AccessMatch]:
        if not request.pattern:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=20,
            with_errors=True,
        )
        result: list[AccessMatch] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    AccessMatch(
                        timestamp="",
                        caller_ip="",
                        caller_service="unknown",
                        method="XXXX",
                        url="",
                        status_code=0,
                        user_id=None,
                    )
                )
        return result
    def xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_36(self, request: SensitiveAccessRequest) -> list[AccessMatch]:
        if not request.pattern:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=20,
            with_errors=True,
        )
        result: list[AccessMatch] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    AccessMatch(
                        timestamp="",
                        caller_ip="",
                        caller_service="unknown",
                        method="",
                        url="XXXX",
                        status_code=0,
                        user_id=None,
                    )
                )
        return result
    def xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_37(self, request: SensitiveAccessRequest) -> list[AccessMatch]:
        if not request.pattern:
            return []

        traces = search_jaeger_traces(
            service="",
            limit=20,
            with_errors=True,
        )
        result: list[AccessMatch] = []
        for trace in traces:
            if trace.get("hasErrors"):
                result.append(
                    AccessMatch(
                        timestamp="",
                        caller_ip="",
                        caller_service="unknown",
                        method="",
                        url="",
                        status_code=1,
                        user_id=None,
                    )
                )
        return result

mutants_xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut['_mutmut_orig'] = OTelComplianceAuditAdapter.xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut['xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_1'] = OTelComplianceAuditAdapter.xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut['xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_2'] = OTelComplianceAuditAdapter.xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut['xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_3'] = OTelComplianceAuditAdapter.xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut['xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_4'] = OTelComplianceAuditAdapter.xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut['xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_5'] = OTelComplianceAuditAdapter.xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut['xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_6'] = OTelComplianceAuditAdapter.xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_6 # type: ignore # mutmut generated
mutants_xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut['xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_7'] = OTelComplianceAuditAdapter.xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_7 # type: ignore # mutmut generated
mutants_xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut['xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_8'] = OTelComplianceAuditAdapter.xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_8 # type: ignore # mutmut generated
mutants_xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut['xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_9'] = OTelComplianceAuditAdapter.xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_9 # type: ignore # mutmut generated
mutants_xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut['xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_10'] = OTelComplianceAuditAdapter.xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_10 # type: ignore # mutmut generated
mutants_xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut['xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_11'] = OTelComplianceAuditAdapter.xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_11 # type: ignore # mutmut generated
mutants_xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut['xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_12'] = OTelComplianceAuditAdapter.xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_12 # type: ignore # mutmut generated
mutants_xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut['xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_13'] = OTelComplianceAuditAdapter.xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_13 # type: ignore # mutmut generated
mutants_xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut['xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_14'] = OTelComplianceAuditAdapter.xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_14 # type: ignore # mutmut generated
mutants_xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut['xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_15'] = OTelComplianceAuditAdapter.xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_15 # type: ignore # mutmut generated
mutants_xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut['xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_16'] = OTelComplianceAuditAdapter.xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_16 # type: ignore # mutmut generated
mutants_xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut['xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_17'] = OTelComplianceAuditAdapter.xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_17 # type: ignore # mutmut generated
mutants_xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut['xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_18'] = OTelComplianceAuditAdapter.xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_18 # type: ignore # mutmut generated
mutants_xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut['xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_19'] = OTelComplianceAuditAdapter.xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_19 # type: ignore # mutmut generated
mutants_xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut['xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_20'] = OTelComplianceAuditAdapter.xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_20 # type: ignore # mutmut generated
mutants_xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut['xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_21'] = OTelComplianceAuditAdapter.xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_21 # type: ignore # mutmut generated
mutants_xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut['xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_22'] = OTelComplianceAuditAdapter.xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_22 # type: ignore # mutmut generated
mutants_xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut['xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_23'] = OTelComplianceAuditAdapter.xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_23 # type: ignore # mutmut generated
mutants_xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut['xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_24'] = OTelComplianceAuditAdapter.xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_24 # type: ignore # mutmut generated
mutants_xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut['xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_25'] = OTelComplianceAuditAdapter.xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_25 # type: ignore # mutmut generated
mutants_xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut['xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_26'] = OTelComplianceAuditAdapter.xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_26 # type: ignore # mutmut generated
mutants_xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut['xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_27'] = OTelComplianceAuditAdapter.xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_27 # type: ignore # mutmut generated
mutants_xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut['xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_28'] = OTelComplianceAuditAdapter.xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_28 # type: ignore # mutmut generated
mutants_xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut['xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_29'] = OTelComplianceAuditAdapter.xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_29 # type: ignore # mutmut generated
mutants_xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut['xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_30'] = OTelComplianceAuditAdapter.xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_30 # type: ignore # mutmut generated
mutants_xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut['xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_31'] = OTelComplianceAuditAdapter.xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_31 # type: ignore # mutmut generated
mutants_xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut['xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_32'] = OTelComplianceAuditAdapter.xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_32 # type: ignore # mutmut generated
mutants_xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut['xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_33'] = OTelComplianceAuditAdapter.xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_33 # type: ignore # mutmut generated
mutants_xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut['xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_34'] = OTelComplianceAuditAdapter.xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_34 # type: ignore # mutmut generated
mutants_xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut['xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_35'] = OTelComplianceAuditAdapter.xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_35 # type: ignore # mutmut generated
mutants_xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut['xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_36'] = OTelComplianceAuditAdapter.xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_36 # type: ignore # mutmut generated
mutants_xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut['xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_37'] = OTelComplianceAuditAdapter.xǁOTelComplianceAuditAdapterǁfetch_access_matches__mutmut_37 # type: ignore # mutmut generated
