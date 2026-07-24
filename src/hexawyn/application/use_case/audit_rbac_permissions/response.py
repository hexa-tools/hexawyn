from dataclasses import dataclass


@dataclass
class AuditRbacPermissionsResponse:
    error: str | None = None
