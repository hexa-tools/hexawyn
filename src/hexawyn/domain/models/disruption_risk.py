from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class RiskEvent:
    business_service_name: str
    risk_type: str
    predicted_date: str
    days_from_now: int
    detail: str


@dataclass
class DisruptionRiskReport:
    period_label: str
    risks: list[RiskEvent] = field(default_factory=list)
    has_risks: bool = False
    has_data: bool = True
    warning: str = ""
