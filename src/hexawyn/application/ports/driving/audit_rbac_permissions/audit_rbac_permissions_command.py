from __future__ import annotations

from dataclasses import dataclass

from hexawyn.domain.models.constants import RBACAuditConstants

_cfg = RBACAuditConstants()


@dataclass(frozen=True)
class AuditRBACPermissionsCommand:
    window_days: int = _cfg.default_audit_window_days
