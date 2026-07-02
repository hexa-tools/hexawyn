from __future__ import annotations

from hexawyn.application.ports.driving.sensitive_data_audit.sensitive_data_audit_command import (
    SensitiveDataAuditCommand,
)
from hexawyn.application.ports.driving.sensitive_data_audit.sensitive_data_audit_response import (
    SensitiveDataAuditResponse,
)
from hexawyn.application.ports.driving.sensitive_data_audit.sensitive_data_audit_service_port import (
    SensitiveDataAuditServicePort,
)


class SensitiveDataAuditUseCase:
    def __init__(self, service: SensitiveDataAuditServicePort) -> None:
        self._svc = service

    def execute(self, cmd: SensitiveDataAuditCommand) -> SensitiveDataAuditResponse:
        return self._svc.audit(cmd)
