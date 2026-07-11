from __future__ import annotations

from dataclasses import dataclass

from hexawyn.application.ports.driven.sla_report_port import ServiceSlaRaw

_MINUTES_PER_DAY = 1440


@dataclass(frozen=True)
class ServiceUptimeResult:
    actual_uptime_pct: float
    met: bool
    exceeded: bool
    prorated: bool
    coverage_days: int


def evaluate_service(raw: ServiceSlaRaw) -> ServiceUptimeResult:
    """Evaluate a service's quarterly SLA.

    Planned-maintenance minutes are excluded from downtime, so scheduled
    windows do not count against the SLA. Coverage shorter than the full
    quarter (a mid-quarter onboarding) is flagged as prorated — the uptime is
    measured only over the days the service actually existed.
    """
    effective_uptime = _effective_uptime(raw)
    target = raw["sla_target_pct"]
    return ServiceUptimeResult(
        actual_uptime_pct=effective_uptime,
        met=effective_uptime >= target,
        exceeded=effective_uptime > target,
        prorated=raw["coverage_days"] < raw["quarter_days"],
        coverage_days=raw["coverage_days"],
    )


def _effective_uptime(raw: ServiceSlaRaw) -> float:
    covered_minutes = raw["coverage_days"] * _MINUTES_PER_DAY
    if covered_minutes <= 0:
        return round(raw["uptime_pct"], 3)

    raw_downtime = (100.0 - raw["uptime_pct"]) / 100.0 * covered_minutes
    effective_downtime = max(0.0, raw_downtime - raw["maintenance_minutes"])
    effective_uptime = 100.0 - effective_downtime / covered_minutes * 100.0
    return round(effective_uptime, 3)
