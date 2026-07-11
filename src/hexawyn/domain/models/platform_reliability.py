from __future__ import annotations

from dataclasses import dataclass, field

IncidentSeverity = str
ResolutionTrend = str


@dataclass(frozen=True)
class IncidentSummary:
    date: str
    severity: str
    downtime_minutes: int
    root_cause: str
    resolved: bool


@dataclass
class PlatformReliabilityReport:
    period_label: str
    uptime_pct: float
    total_incidents: int = 0
    major_count: int = 0
    minor_count: int = 0
    avg_resolution_minutes: int = 0
    resolution_trend: str = "stable"
    resolution_delta_pct: float = 0.0
    previous_avg_resolution_minutes: int | None = None
    financial_impact_eur: float | None = None
    pricing_configured: bool = False
    incidents: list[IncidentSummary] = field(default_factory=list)
    has_major_incident: bool = False
    executive_summary: str = ""
