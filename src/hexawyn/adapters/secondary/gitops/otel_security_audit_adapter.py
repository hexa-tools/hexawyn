from __future__ import annotations

from hexawyn.adapters.secondary.gitops.otel_http_client import search_jaeger_traces
from hexawyn.application.ports.driven.security_audit_port import SecurityAuditPort
from hexawyn.domain.models.admin_endpoint_audit import AdminAuditRequest, FailedAdminCall


class OTelSecurityAuditAdapter(SecurityAuditPort):
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

    def fetch_total_requests(self, request: AdminAuditRequest) -> int:
        traces = search_jaeger_traces(
            service="",
            limit=100,
        )
        return len(traces)
