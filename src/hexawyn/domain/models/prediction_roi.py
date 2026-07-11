from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class PreventedIncident:
    incident_ref: str
    business_service_name: str
    detected_at: str
    avoided_downtime_minutes: int
    confidence_pct: float
    avoided_cost_eur: float


@dataclass
class PredictionRoiReport:
    period_label: str
    detected_count: int = 0
    prevented_incident_count: int = 0
    avoided_downtime_minutes: int = 0
    total_avoided_cost_eur: float | None = None
    infrastructure_cost_eur: float = 0.0
    roi_eur: float | None = None
    prevented_incidents: list[PreventedIncident] = field(default_factory=list)
    config_available: bool = False
    explanation: str = ""
