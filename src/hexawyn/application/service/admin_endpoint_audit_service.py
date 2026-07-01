from __future__ import annotations

from dataclasses import asdict

from hexawyn.application.ports.driven.security_audit_port import SecurityAuditPort
from hexawyn.application.ports.driving.admin_endpoint_audit.admin_endpoint_audit_command import (
    AdminEndpointAuditCommand,
)
from hexawyn.application.ports.driving.admin_endpoint_audit.admin_endpoint_audit_response import (
    AdminEndpointAuditResponse,
)
from hexawyn.application.ports.driving.admin_endpoint_audit.admin_endpoint_audit_service_port import (
    AdminEndpointAuditServicePort,
)
from hexawyn.domain.models.admin_endpoint_audit import AdminAuditRequest, AdminAuditResult


class AdminEndpointAuditService(AdminEndpointAuditServicePort):
    def __init__(self, port: SecurityAuditPort) -> None:
        self._port = port

    def audit(self, command: AdminEndpointAuditCommand) -> AdminEndpointAuditResponse:
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
