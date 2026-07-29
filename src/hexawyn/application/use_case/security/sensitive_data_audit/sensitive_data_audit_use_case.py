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


class SensitiveDataAuditUseCase:
    def __init__(self, port: ComplianceAuditPort) -> None:
        self._port = port

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
