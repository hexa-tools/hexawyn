from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class AlertLevel(Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    NONE = "none"


@dataclass(frozen=True)
class AccessMatch:
    timestamp: str
    caller_ip: str
    caller_service: str
    method: str
    url: str
    status_code: int
    user_id: str | None = None


@dataclass(frozen=True)
class SensitiveAccessRequest:
    pattern: str
    time_window_minutes: int = 10
    allowlist: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class SensitiveAuditResult:
    pattern: str
    time_window_minutes: int
    total_matches: int
    flagged: list[AccessMatch]
    unflagged: list[AccessMatch]
    alert_level: AlertLevel

    @staticmethod
    def compute(
        request: SensitiveAccessRequest,
        matches: list[AccessMatch],
    ) -> SensitiveAuditResult:
        allow = set(request.allowlist)
        flagged: list[AccessMatch] = []
        unflagged: list[AccessMatch] = []

        for m in matches:
            if m.caller_service in allow:
                unflagged.append(m)
            else:
                flagged.append(m)

        if len(flagged) > 5:
            level = AlertLevel.HIGH
        elif len(flagged) > 0:
            level = AlertLevel.MEDIUM
        else:
            level = AlertLevel.NONE

        return SensitiveAuditResult(
            pattern=request.pattern,
            time_window_minutes=request.time_window_minutes,
            total_matches=len(matches),
            flagged=flagged,
            unflagged=unflagged,
            alert_level=level,
        )
