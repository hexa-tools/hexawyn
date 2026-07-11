from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class CalculationBasis:
    formula: str
    config_values_used: dict[str, str]
    source_metrics: dict[str, str]


@dataclass
class IncidentCostReport:
    business_service_name: str
    downtime_minutes: int
    revenue_impact_eur: float | None = None
    support_cost_eur: float | None = None
    sla_penalty_eur: float | None = None
    total_cost_eur: float | None = None
    impacted_service_count: int = 0
    resolved_at: str = ""
    config_available: bool = False
    explanation: str = ""
    calculation_basis: CalculationBasis | None = field(default=None)
