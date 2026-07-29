from dataclasses import dataclass


@dataclass(frozen=True)
class AuditRbacPermissionsCommand:
    window_days: int = 30
