from __future__ import annotations

from hexawyn.domain.models.constants import SecretRotationConstants
from hexawyn.domain.models.secret_rotation import RiskLevel

_cfg = SecretRotationConstants()


def classify_risk_level(secret_type: str, data_keys: list[str]) -> RiskLevel:
    if secret_type in _cfg.critical_secret_types:
        return "critical"

    upper_keys = [key.upper() for key in data_keys]
    if any(fragment in key for key in upper_keys for fragment in _cfg.critical_key_fragments):
        return "critical"
    if any(fragment in key for key in upper_keys for fragment in _cfg.medium_key_fragments):
        return "medium"
    return "low"
