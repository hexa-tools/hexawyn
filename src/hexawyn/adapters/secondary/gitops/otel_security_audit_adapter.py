from __future__ import annotations

from hexawyn.application.ports.driven.security_audit_port import SecurityAuditPort
from hexawyn.domain.models.admin_endpoint_audit import AdminAuditRequest, FailedAdminCall


class OTelSecurityAuditAdapter(SecurityAuditPort):
    def fetch_failed_admin_calls(self, request: AdminAuditRequest) -> list[FailedAdminCall]:
        return []

    def fetch_total_requests(self, request: AdminAuditRequest) -> int:
        return 0
