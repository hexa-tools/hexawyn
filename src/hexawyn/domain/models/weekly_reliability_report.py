from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class ServiceReliability:
    service_name: str
    uptime_pct: float
    error_rate: float
    p99_latency_ms: float
    slo_target: float
    slo_status: str
    downtime_minutes: int
    data_gap_minutes: int
    created_mid_week: bool


@dataclass(frozen=True)
class TopIncident:
    service_name: str
    timestamp: str
    duration_minutes: int
    error_rate: float
    impact_score: float
    description: str


@dataclass
class WeeklyReliabilityReport:
    report_period_start: str = ""
    report_period_end: str = ""
    services: list[ServiceReliability] = field(default_factory=list)
    top_incidents: list[TopIncident] = field(default_factory=list)
    total_incident_count: int = 0
    health_score: float = 0.0
    slo_pass_count: int = 0
    slo_fail_count: int = 0
    total_services: int = 0
