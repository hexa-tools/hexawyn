from __future__ import annotations

from dataclasses import dataclass, field

SlaTrend = str


@dataclass(frozen=True)
class SlaBreach:
    service_name: str
    date: str
    duration_minutes: int
    impacted_users: int
    root_cause_ref: str


@dataclass(frozen=True)
class ServiceSla:
    service_name: str
    sla_target_pct: float
    actual_uptime_pct: float
    met: bool
    exceeded: bool
    breaches: list[SlaBreach]
    breach_count: int
    prorated: bool
    coverage_days: int


@dataclass
class SlaReport:
    quarter_label: str
    services: list[ServiceSla] = field(default_factory=list)
    overall_met_count: int = 0
    overall_breached_count: int = 0
    trend: str = "stable"
    previous_avg_uptime_pct: float | None = None
    current_avg_uptime_pct: float = 0.0
    has_data: bool = True
    warning: str = ""
