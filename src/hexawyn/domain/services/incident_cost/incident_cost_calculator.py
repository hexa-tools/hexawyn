from __future__ import annotations

from hexawyn.application.ports.driven.incident_cost_port import (
    BusinessConfigRaw,
    IncidentCostData,
)
from hexawyn.domain.models.incident_cost import CalculationBasis, IncidentCostReport

_MINUTES_PER_HOUR = 60
_FORMULA = "downtime_minutes x revenue_per_minute + support_cost + sla_penalty"


def compute_incident_cost(data: IncidentCostData) -> IncidentCostReport:
    """Compute an incident's financial impact — deterministically.

    Revenue impact requires ``revenue_per_minute``; without it, no euro amount
    is produced and an explanation is returned instead (never a fabricated
    figure). Support cost and SLA penalty are added only when their respective
    parameters are configured, and the SLA penalty only when the SLA was
    breached. Every computed report carries a CalculationBasis for full
    traceability.
    """
    config = data["business_config"]
    downtime = data["downtime_minutes"]
    service = data["business_service_name"]

    if config["revenue_per_minute"] is None:
        return _unconfigured_report(data)

    revenue_impact = round(downtime * config["revenue_per_minute"], 2)
    support_cost = _support_cost(downtime, config)
    sla_penalty = _sla_penalty(data["sla_breached"], config)
    total = round(revenue_impact + support_cost + sla_penalty, 2)

    return IncidentCostReport(
        business_service_name=service,
        downtime_minutes=downtime,
        revenue_impact_eur=revenue_impact,
        support_cost_eur=support_cost,
        sla_penalty_eur=sla_penalty,
        total_cost_eur=total,
        impacted_service_count=data["impacted_service_count"],
        resolved_at=data["resolved_at"],
        config_available=True,
        calculation_basis=_build_basis(data, config, support_cost, sla_penalty),
    )


def _unconfigured_report(data: IncidentCostData) -> IncidentCostReport:
    downtime = data["downtime_minutes"]
    explanation = (
        f"Le service {data['business_service_name']} est reste indisponible "
        f"pendant {downtime} minutes. Configurez 'revenue_per_minute' dans la "
        f"section business pour obtenir l'estimation du chiffre d'affaires affecte."
    )
    return IncidentCostReport(
        business_service_name=data["business_service_name"],
        downtime_minutes=downtime,
        impacted_service_count=data["impacted_service_count"],
        resolved_at=data["resolved_at"],
        config_available=False,
        explanation=explanation,
    )


def _support_cost(downtime_minutes: int, config: BusinessConfigRaw) -> float:
    if config["support_cost_per_hour"] is None:
        return 0.0
    return round(downtime_minutes / _MINUTES_PER_HOUR * config["support_cost_per_hour"], 2)


def _sla_penalty(sla_breached: bool, config: BusinessConfigRaw) -> float:
    if not sla_breached or config["sla_penalty_per_hour"] is None:
        return 0.0
    return round(config["sla_penalty_per_hour"], 2)


def _build_basis(
    data: IncidentCostData,
    config: BusinessConfigRaw,
    support_cost: float,
    sla_penalty: float,
) -> CalculationBasis:
    config_used: dict[str, str] = {"revenue_per_minute": str(config["revenue_per_minute"])}
    if config["support_cost_per_hour"] is not None:
        config_used["support_cost_per_hour"] = str(config["support_cost_per_hour"])
    if config["sla_penalty_per_hour"] is not None and data["sla_breached"]:
        config_used["sla_penalty_per_hour"] = str(config["sla_penalty_per_hour"])
    return CalculationBasis(
        formula=_FORMULA,
        config_values_used=config_used,
        source_metrics={
            "downtime_minutes": str(data["downtime_minutes"]),
            "sla_breached": str(data["sla_breached"]),
        },
    )
