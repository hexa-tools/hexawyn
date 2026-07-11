from __future__ import annotations

from dataclasses import dataclass

from hexawyn.domain.models.security_posture import SecurityPostureReport


@dataclass
class ComputeSecurityPostureResponse:
    result: SecurityPostureReport
