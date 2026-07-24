from hexawyn.application.ports.driven.secret_rotation_audit_port import SecretRotationAuditPort
from hexawyn.application.use_case.audit_secret_rotation.command import AuditSecretRotationCommand
from hexawyn.application.use_case.audit_secret_rotation.response import AuditSecretRotationResponse


class AuditSecretRotationUseCase:
    def __init__(self, port: SecretRotationAuditPort) -> None:
        self._port = port

    def execute(self, command: AuditSecretRotationCommand) -> AuditSecretRotationResponse:
        return AuditSecretRotationResponse()
