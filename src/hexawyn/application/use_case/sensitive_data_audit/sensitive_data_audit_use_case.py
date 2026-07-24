from dataclasses import asdict

from hexawyn.application.ports.driven.compliance_audit_port import ComplianceAuditPort
from hexawyn.application.use_case.sensitive_data_audit.command import SensitiveDataAuditCommand
from hexawyn.application.use_case.sensitive_data_audit.response import SensitiveDataAuditResponse


class SensitiveDataAuditUseCase:
    def __init__(self, port: ComplianceAuditPort) -> None:
        self._port = port

    def execute(self, command: SensitiveDataAuditCommand) -> SensitiveDataAuditResponse:
        findings = self._port.audit_sensitive_data(namespace=command.namespace)
        return SensitiveDataAuditResponse(findings=[asdict(f) for f in findings])
