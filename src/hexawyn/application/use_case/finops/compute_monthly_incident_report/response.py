from dataclasses import dataclass, field


@dataclass
class SeverityBreakdown:
    count: int = 0
    downtime_minutes: int = 0


@dataclass
class ImpactedService:
    service_name: str = ""
    total_downtime: int = 0
    incident_count: int = 0


@dataclass
class MonthlyIncidentResult:
    month: str = ""
    total_count: int = 0
    total_downtime_minutes: int = 0
    per_severity: dict[str, SeverityBreakdown] = field(default_factory=dict)
    most_impacted_services: list[ImpactedService] = field(default_factory=list)
    previous_month_total_count: int = 0
    previous_month_downtime_minutes: int = 0
    incidents_decreasing: bool = False


@dataclass
class ComputeMonthlyIncidentReportResponse:
    result: MonthlyIncidentResult
    error: str | None = None
