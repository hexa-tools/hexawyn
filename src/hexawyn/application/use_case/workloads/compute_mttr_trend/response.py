from dataclasses import dataclass, field


@dataclass
class SeverityMTTR:
    count: int = 0
    downtime_total: int = 0
    mttr_minutes: float = 0.0


@dataclass
class SlowestIncident:
    incident_id: str = ""
    severity: str = ""
    downtime_minutes: int = 0
    service_name: str = ""


@dataclass
class MTTRTrendResult:
    trend: str = ""
    recommendation: str = ""
    per_month: dict[str, dict[str, SeverityMTTR]] = field(default_factory=dict)
    slowest_incidents: list[SlowestIncident] = field(default_factory=list)


@dataclass
class ComputeMTTRTrendResponse:
    result: MTTRTrendResult
    error: str | None = None
