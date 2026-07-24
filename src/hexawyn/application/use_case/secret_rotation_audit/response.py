from dataclasses import dataclass


@dataclass
class SecretRotationAuditResponse:
    error: str | None = None
