from dataclasses import dataclass


@dataclass
class AuditSecretRotationResponse:
    error: str | None = None
