from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class SeverityBreakdown:
    severity: str
    count: int
    downtime_minutes: int


@dataclass(frozen=True)
class ImpactedService:
    service_name: str
    total_downtime: int
    incident_count: int


@dataclass
class MonthlyIncidentReport:
    month: str = ""
    total_count: int = 0
    total_downtime_minutes: int = 0
    per_severity: dict[str, SeverityBreakdown] = field(default_factory=dict)
    most_impacted_services: list[ImpactedService] = field(default_factory=list)
    previous_month_total_count: int = 0
    previous_month_downtime_minutes: int = 0
    incidents_decreasing: bool = False
