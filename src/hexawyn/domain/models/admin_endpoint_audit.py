from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class CallerRisk(Enum):
    HIGH = "high"
    LOW = "low"


@dataclass(frozen=True)
class FailedAdminCall:
    timestamp: str
    caller_ip: str
    caller_service: str
    endpoint: str
    user_identity: str | None = None


@dataclass(frozen=True)
class CallerSummary:
    caller_ip: str
    caller_service: str
    attempts: int
    endpoints: list[str]
    flagged: bool
    risk: CallerRisk


@dataclass(frozen=True)
class AdminAuditRequest:
    endpoint_pattern: str = "/admin*"
    time_window_minutes: int = 30
    flag_threshold: int = 5


@dataclass(frozen=True)
class AdminAuditResult:
    endpoint_pattern: str
    total_requests: int
    total_403s: int
    rate_403_pct: float
    flagged_callers: list[CallerSummary]
    all_calls: list[FailedAdminCall]

    @staticmethod
    def compute(
        request: AdminAuditRequest,
        calls: list[FailedAdminCall],
        total_requests: int,
    ) -> AdminAuditResult:
        rate = (len(calls) / total_requests) * 100.0 if total_requests > 0 else 0.0

        grouped: dict[str, dict[str, object]] = {}
        for c in calls:
            key = c.caller_ip
            if key not in grouped:
                grouped[key] = {
                    "ip": c.caller_ip,
                    "service": c.caller_service,
                    "count": 0,
                    "endpoints": [],
                }
            entry = grouped[key]
            entry["count"] = int(str(entry["count"])) + 1
            eps: list[str] = entry["endpoints"]  # type: ignore[assignment]
            if c.endpoint not in eps:
                eps.append(c.endpoint)

        flagged: list[CallerSummary] = []
        for g in grouped.values():
            count = int(str(g["count"]))
            cs = CallerSummary(
                caller_ip=str(g["ip"]),
                caller_service=str(g["service"]),
                attempts=count,
                endpoints=g["endpoints"],  # type: ignore[arg-type]
                flagged=count >= request.flag_threshold,
                risk=CallerRisk.HIGH if count >= request.flag_threshold else CallerRisk.LOW,
            )
            if cs.flagged:
                flagged.append(cs)

        return AdminAuditResult(
            endpoint_pattern=request.endpoint_pattern,
            total_requests=total_requests,
            total_403s=len(calls),
            rate_403_pct=round(rate, 2),
            flagged_callers=flagged,
            all_calls=calls,
        )
