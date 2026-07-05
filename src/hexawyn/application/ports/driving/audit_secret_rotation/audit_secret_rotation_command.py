from __future__ import annotations

from dataclasses import dataclass

from hexawyn.domain.models.constants import SecretRotationConstants

_cfg = SecretRotationConstants()


@dataclass(frozen=True)
class AuditSecretRotationCommand:
    rotation_threshold_days: int = _cfg.default_rotation_threshold_days
