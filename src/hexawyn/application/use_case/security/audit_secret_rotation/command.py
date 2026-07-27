from dataclasses import dataclass


@dataclass(frozen=True)
class AuditSecretRotationCommand:
    rotation_threshold_days: int = 90
