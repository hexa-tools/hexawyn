from __future__ import annotations

from hexawyn.application.ports.driven.incident_cost_port import (
    BusinessConfigRaw,
    IncidentCostData,
)
from hexawyn.domain.models.incident_cost import CalculationBasis, IncidentCostReport

_MINUTES_PER_HOUR = 60
_FORMULA = "downtime_minutes x revenue_per_minute + support_cost + sla_penalty"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_compute_incident_cost__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compute_incident_cost__mutmut)
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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_orig(data: IncidentCostData) -> IncidentCostReport:
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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_1(data: IncidentCostData) -> IncidentCostReport:
    """Compute an incident's financial impact — deterministically.

    Revenue impact requires ``revenue_per_minute``; without it, no euro amount
    is produced and an explanation is returned instead (never a fabricated
    figure). Support cost and SLA penalty are added only when their respective
    parameters are configured, and the SLA penalty only when the SLA was
    breached. Every computed report carries a CalculationBasis for full
    traceability.
    """
    config = None
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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_2(data: IncidentCostData) -> IncidentCostReport:
    """Compute an incident's financial impact — deterministically.

    Revenue impact requires ``revenue_per_minute``; without it, no euro amount
    is produced and an explanation is returned instead (never a fabricated
    figure). Support cost and SLA penalty are added only when their respective
    parameters are configured, and the SLA penalty only when the SLA was
    breached. Every computed report carries a CalculationBasis for full
    traceability.
    """
    config = data["XXbusiness_configXX"]
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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_3(data: IncidentCostData) -> IncidentCostReport:
    """Compute an incident's financial impact — deterministically.

    Revenue impact requires ``revenue_per_minute``; without it, no euro amount
    is produced and an explanation is returned instead (never a fabricated
    figure). Support cost and SLA penalty are added only when their respective
    parameters are configured, and the SLA penalty only when the SLA was
    breached. Every computed report carries a CalculationBasis for full
    traceability.
    """
    config = data["BUSINESS_CONFIG"]
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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_4(data: IncidentCostData) -> IncidentCostReport:
    """Compute an incident's financial impact — deterministically.

    Revenue impact requires ``revenue_per_minute``; without it, no euro amount
    is produced and an explanation is returned instead (never a fabricated
    figure). Support cost and SLA penalty are added only when their respective
    parameters are configured, and the SLA penalty only when the SLA was
    breached. Every computed report carries a CalculationBasis for full
    traceability.
    """
    config = data["business_config"]
    downtime = None
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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_5(data: IncidentCostData) -> IncidentCostReport:
    """Compute an incident's financial impact — deterministically.

    Revenue impact requires ``revenue_per_minute``; without it, no euro amount
    is produced and an explanation is returned instead (never a fabricated
    figure). Support cost and SLA penalty are added only when their respective
    parameters are configured, and the SLA penalty only when the SLA was
    breached. Every computed report carries a CalculationBasis for full
    traceability.
    """
    config = data["business_config"]
    downtime = data["XXdowntime_minutesXX"]
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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_6(data: IncidentCostData) -> IncidentCostReport:
    """Compute an incident's financial impact — deterministically.

    Revenue impact requires ``revenue_per_minute``; without it, no euro amount
    is produced and an explanation is returned instead (never a fabricated
    figure). Support cost and SLA penalty are added only when their respective
    parameters are configured, and the SLA penalty only when the SLA was
    breached. Every computed report carries a CalculationBasis for full
    traceability.
    """
    config = data["business_config"]
    downtime = data["DOWNTIME_MINUTES"]
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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_7(data: IncidentCostData) -> IncidentCostReport:
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
    service = None

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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_8(data: IncidentCostData) -> IncidentCostReport:
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
    service = data["XXbusiness_service_nameXX"]

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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_9(data: IncidentCostData) -> IncidentCostReport:
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
    service = data["BUSINESS_SERVICE_NAME"]

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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_10(data: IncidentCostData) -> IncidentCostReport:
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

    if config["XXrevenue_per_minuteXX"] is None:
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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_11(data: IncidentCostData) -> IncidentCostReport:
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

    if config["REVENUE_PER_MINUTE"] is None:
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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_12(data: IncidentCostData) -> IncidentCostReport:
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

    if config["revenue_per_minute"] is not None:
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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_13(data: IncidentCostData) -> IncidentCostReport:
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
        return _unconfigured_report(None)

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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_14(data: IncidentCostData) -> IncidentCostReport:
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

    revenue_impact = None
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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_15(data: IncidentCostData) -> IncidentCostReport:
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

    revenue_impact = round(None, 2)
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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_16(data: IncidentCostData) -> IncidentCostReport:
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

    revenue_impact = round(downtime * config["revenue_per_minute"], None)
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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_17(data: IncidentCostData) -> IncidentCostReport:
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

    revenue_impact = round(2)
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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_18(data: IncidentCostData) -> IncidentCostReport:
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

    revenue_impact = round(downtime * config["revenue_per_minute"], )
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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_19(data: IncidentCostData) -> IncidentCostReport:
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

    revenue_impact = round(downtime / config["revenue_per_minute"], 2)
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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_20(data: IncidentCostData) -> IncidentCostReport:
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

    revenue_impact = round(downtime * config["XXrevenue_per_minuteXX"], 2)
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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_21(data: IncidentCostData) -> IncidentCostReport:
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

    revenue_impact = round(downtime * config["REVENUE_PER_MINUTE"], 2)
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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_22(data: IncidentCostData) -> IncidentCostReport:
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

    revenue_impact = round(downtime * config["revenue_per_minute"], 3)
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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_23(data: IncidentCostData) -> IncidentCostReport:
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
    support_cost = None
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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_24(data: IncidentCostData) -> IncidentCostReport:
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
    support_cost = _support_cost(None, config)
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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_25(data: IncidentCostData) -> IncidentCostReport:
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
    support_cost = _support_cost(downtime, None)
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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_26(data: IncidentCostData) -> IncidentCostReport:
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
    support_cost = _support_cost(config)
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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_27(data: IncidentCostData) -> IncidentCostReport:
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
    support_cost = _support_cost(downtime, )
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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_28(data: IncidentCostData) -> IncidentCostReport:
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
    sla_penalty = None
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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_29(data: IncidentCostData) -> IncidentCostReport:
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
    sla_penalty = _sla_penalty(None, config)
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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_30(data: IncidentCostData) -> IncidentCostReport:
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
    sla_penalty = _sla_penalty(data["sla_breached"], None)
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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_31(data: IncidentCostData) -> IncidentCostReport:
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
    sla_penalty = _sla_penalty(config)
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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_32(data: IncidentCostData) -> IncidentCostReport:
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
    sla_penalty = _sla_penalty(data["sla_breached"], )
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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_33(data: IncidentCostData) -> IncidentCostReport:
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
    sla_penalty = _sla_penalty(data["XXsla_breachedXX"], config)
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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_34(data: IncidentCostData) -> IncidentCostReport:
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
    sla_penalty = _sla_penalty(data["SLA_BREACHED"], config)
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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_35(data: IncidentCostData) -> IncidentCostReport:
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
    total = None

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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_36(data: IncidentCostData) -> IncidentCostReport:
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
    total = round(None, 2)

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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_37(data: IncidentCostData) -> IncidentCostReport:
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
    total = round(revenue_impact + support_cost + sla_penalty, None)

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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_38(data: IncidentCostData) -> IncidentCostReport:
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
    total = round(2)

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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_39(data: IncidentCostData) -> IncidentCostReport:
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
    total = round(revenue_impact + support_cost + sla_penalty, )

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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_40(data: IncidentCostData) -> IncidentCostReport:
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
    total = round(revenue_impact + support_cost - sla_penalty, 2)

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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_41(data: IncidentCostData) -> IncidentCostReport:
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
    total = round(revenue_impact - support_cost + sla_penalty, 2)

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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_42(data: IncidentCostData) -> IncidentCostReport:
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
    total = round(revenue_impact + support_cost + sla_penalty, 3)

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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_43(data: IncidentCostData) -> IncidentCostReport:
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
        business_service_name=None,
        downtime_minutes=downtime,
        revenue_impact_eur=revenue_impact,
        support_cost_eur=support_cost,
        sla_penalty_eur=sla_penalty,
        total_cost_eur=total,
        impacted_service_count=data["impacted_service_count"],
        resolved_at=data["resolved_at"],
        config_available=True,
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_44(data: IncidentCostData) -> IncidentCostReport:
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
        downtime_minutes=None,
        revenue_impact_eur=revenue_impact,
        support_cost_eur=support_cost,
        sla_penalty_eur=sla_penalty,
        total_cost_eur=total,
        impacted_service_count=data["impacted_service_count"],
        resolved_at=data["resolved_at"],
        config_available=True,
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_45(data: IncidentCostData) -> IncidentCostReport:
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
        revenue_impact_eur=None,
        support_cost_eur=support_cost,
        sla_penalty_eur=sla_penalty,
        total_cost_eur=total,
        impacted_service_count=data["impacted_service_count"],
        resolved_at=data["resolved_at"],
        config_available=True,
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_46(data: IncidentCostData) -> IncidentCostReport:
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
        support_cost_eur=None,
        sla_penalty_eur=sla_penalty,
        total_cost_eur=total,
        impacted_service_count=data["impacted_service_count"],
        resolved_at=data["resolved_at"],
        config_available=True,
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_47(data: IncidentCostData) -> IncidentCostReport:
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
        sla_penalty_eur=None,
        total_cost_eur=total,
        impacted_service_count=data["impacted_service_count"],
        resolved_at=data["resolved_at"],
        config_available=True,
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_48(data: IncidentCostData) -> IncidentCostReport:
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
        total_cost_eur=None,
        impacted_service_count=data["impacted_service_count"],
        resolved_at=data["resolved_at"],
        config_available=True,
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_49(data: IncidentCostData) -> IncidentCostReport:
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
        impacted_service_count=None,
        resolved_at=data["resolved_at"],
        config_available=True,
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_50(data: IncidentCostData) -> IncidentCostReport:
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
        resolved_at=None,
        config_available=True,
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_51(data: IncidentCostData) -> IncidentCostReport:
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
        config_available=None,
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_52(data: IncidentCostData) -> IncidentCostReport:
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
        calculation_basis=None,
    )


def x_compute_incident_cost__mutmut_53(data: IncidentCostData) -> IncidentCostReport:
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
        downtime_minutes=downtime,
        revenue_impact_eur=revenue_impact,
        support_cost_eur=support_cost,
        sla_penalty_eur=sla_penalty,
        total_cost_eur=total,
        impacted_service_count=data["impacted_service_count"],
        resolved_at=data["resolved_at"],
        config_available=True,
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_54(data: IncidentCostData) -> IncidentCostReport:
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
        revenue_impact_eur=revenue_impact,
        support_cost_eur=support_cost,
        sla_penalty_eur=sla_penalty,
        total_cost_eur=total,
        impacted_service_count=data["impacted_service_count"],
        resolved_at=data["resolved_at"],
        config_available=True,
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_55(data: IncidentCostData) -> IncidentCostReport:
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
        support_cost_eur=support_cost,
        sla_penalty_eur=sla_penalty,
        total_cost_eur=total,
        impacted_service_count=data["impacted_service_count"],
        resolved_at=data["resolved_at"],
        config_available=True,
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_56(data: IncidentCostData) -> IncidentCostReport:
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
        sla_penalty_eur=sla_penalty,
        total_cost_eur=total,
        impacted_service_count=data["impacted_service_count"],
        resolved_at=data["resolved_at"],
        config_available=True,
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_57(data: IncidentCostData) -> IncidentCostReport:
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
        total_cost_eur=total,
        impacted_service_count=data["impacted_service_count"],
        resolved_at=data["resolved_at"],
        config_available=True,
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_58(data: IncidentCostData) -> IncidentCostReport:
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
        impacted_service_count=data["impacted_service_count"],
        resolved_at=data["resolved_at"],
        config_available=True,
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_59(data: IncidentCostData) -> IncidentCostReport:
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
        resolved_at=data["resolved_at"],
        config_available=True,
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_60(data: IncidentCostData) -> IncidentCostReport:
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
        config_available=True,
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_61(data: IncidentCostData) -> IncidentCostReport:
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
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_62(data: IncidentCostData) -> IncidentCostReport:
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
        )


def x_compute_incident_cost__mutmut_63(data: IncidentCostData) -> IncidentCostReport:
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
        impacted_service_count=data["XXimpacted_service_countXX"],
        resolved_at=data["resolved_at"],
        config_available=True,
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_64(data: IncidentCostData) -> IncidentCostReport:
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
        impacted_service_count=data["IMPACTED_SERVICE_COUNT"],
        resolved_at=data["resolved_at"],
        config_available=True,
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_65(data: IncidentCostData) -> IncidentCostReport:
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
        resolved_at=data["XXresolved_atXX"],
        config_available=True,
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_66(data: IncidentCostData) -> IncidentCostReport:
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
        resolved_at=data["RESOLVED_AT"],
        config_available=True,
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_67(data: IncidentCostData) -> IncidentCostReport:
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
        config_available=False,
        calculation_basis=_build_basis(data, config),
    )


def x_compute_incident_cost__mutmut_68(data: IncidentCostData) -> IncidentCostReport:
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
        calculation_basis=_build_basis(None, config),
    )


def x_compute_incident_cost__mutmut_69(data: IncidentCostData) -> IncidentCostReport:
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
        calculation_basis=_build_basis(data, None),
    )


def x_compute_incident_cost__mutmut_70(data: IncidentCostData) -> IncidentCostReport:
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
        calculation_basis=_build_basis(config),
    )


def x_compute_incident_cost__mutmut_71(data: IncidentCostData) -> IncidentCostReport:
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
        calculation_basis=_build_basis(data, ),
    )

mutants_x_compute_incident_cost__mutmut['_mutmut_orig'] = x_compute_incident_cost__mutmut_orig # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_1'] = x_compute_incident_cost__mutmut_1 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_2'] = x_compute_incident_cost__mutmut_2 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_3'] = x_compute_incident_cost__mutmut_3 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_4'] = x_compute_incident_cost__mutmut_4 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_5'] = x_compute_incident_cost__mutmut_5 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_6'] = x_compute_incident_cost__mutmut_6 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_7'] = x_compute_incident_cost__mutmut_7 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_8'] = x_compute_incident_cost__mutmut_8 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_9'] = x_compute_incident_cost__mutmut_9 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_10'] = x_compute_incident_cost__mutmut_10 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_11'] = x_compute_incident_cost__mutmut_11 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_12'] = x_compute_incident_cost__mutmut_12 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_13'] = x_compute_incident_cost__mutmut_13 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_14'] = x_compute_incident_cost__mutmut_14 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_15'] = x_compute_incident_cost__mutmut_15 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_16'] = x_compute_incident_cost__mutmut_16 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_17'] = x_compute_incident_cost__mutmut_17 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_18'] = x_compute_incident_cost__mutmut_18 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_19'] = x_compute_incident_cost__mutmut_19 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_20'] = x_compute_incident_cost__mutmut_20 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_21'] = x_compute_incident_cost__mutmut_21 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_22'] = x_compute_incident_cost__mutmut_22 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_23'] = x_compute_incident_cost__mutmut_23 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_24'] = x_compute_incident_cost__mutmut_24 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_25'] = x_compute_incident_cost__mutmut_25 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_26'] = x_compute_incident_cost__mutmut_26 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_27'] = x_compute_incident_cost__mutmut_27 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_28'] = x_compute_incident_cost__mutmut_28 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_29'] = x_compute_incident_cost__mutmut_29 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_30'] = x_compute_incident_cost__mutmut_30 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_31'] = x_compute_incident_cost__mutmut_31 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_32'] = x_compute_incident_cost__mutmut_32 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_33'] = x_compute_incident_cost__mutmut_33 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_34'] = x_compute_incident_cost__mutmut_34 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_35'] = x_compute_incident_cost__mutmut_35 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_36'] = x_compute_incident_cost__mutmut_36 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_37'] = x_compute_incident_cost__mutmut_37 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_38'] = x_compute_incident_cost__mutmut_38 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_39'] = x_compute_incident_cost__mutmut_39 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_40'] = x_compute_incident_cost__mutmut_40 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_41'] = x_compute_incident_cost__mutmut_41 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_42'] = x_compute_incident_cost__mutmut_42 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_43'] = x_compute_incident_cost__mutmut_43 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_44'] = x_compute_incident_cost__mutmut_44 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_45'] = x_compute_incident_cost__mutmut_45 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_46'] = x_compute_incident_cost__mutmut_46 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_47'] = x_compute_incident_cost__mutmut_47 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_48'] = x_compute_incident_cost__mutmut_48 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_49'] = x_compute_incident_cost__mutmut_49 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_50'] = x_compute_incident_cost__mutmut_50 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_51'] = x_compute_incident_cost__mutmut_51 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_52'] = x_compute_incident_cost__mutmut_52 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_53'] = x_compute_incident_cost__mutmut_53 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_54'] = x_compute_incident_cost__mutmut_54 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_55'] = x_compute_incident_cost__mutmut_55 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_56'] = x_compute_incident_cost__mutmut_56 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_57'] = x_compute_incident_cost__mutmut_57 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_58'] = x_compute_incident_cost__mutmut_58 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_59'] = x_compute_incident_cost__mutmut_59 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_60'] = x_compute_incident_cost__mutmut_60 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_61'] = x_compute_incident_cost__mutmut_61 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_62'] = x_compute_incident_cost__mutmut_62 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_63'] = x_compute_incident_cost__mutmut_63 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_64'] = x_compute_incident_cost__mutmut_64 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_65'] = x_compute_incident_cost__mutmut_65 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_66'] = x_compute_incident_cost__mutmut_66 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_67'] = x_compute_incident_cost__mutmut_67 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_68'] = x_compute_incident_cost__mutmut_68 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_69'] = x_compute_incident_cost__mutmut_69 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_70'] = x_compute_incident_cost__mutmut_70 # type: ignore # mutmut generated
mutants_x_compute_incident_cost__mutmut['x_compute_incident_cost__mutmut_71'] = x_compute_incident_cost__mutmut_71 # type: ignore # mutmut generated
mutants_x__unconfigured_report__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__unconfigured_report__mutmut)
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


def x__unconfigured_report__mutmut_orig(data: IncidentCostData) -> IncidentCostReport:
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


def x__unconfigured_report__mutmut_1(data: IncidentCostData) -> IncidentCostReport:
    downtime = None
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


def x__unconfigured_report__mutmut_2(data: IncidentCostData) -> IncidentCostReport:
    downtime = data["XXdowntime_minutesXX"]
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


def x__unconfigured_report__mutmut_3(data: IncidentCostData) -> IncidentCostReport:
    downtime = data["DOWNTIME_MINUTES"]
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


def x__unconfigured_report__mutmut_4(data: IncidentCostData) -> IncidentCostReport:
    downtime = data["downtime_minutes"]
    explanation = None
    return IncidentCostReport(
        business_service_name=data["business_service_name"],
        downtime_minutes=downtime,
        impacted_service_count=data["impacted_service_count"],
        resolved_at=data["resolved_at"],
        config_available=False,
        explanation=explanation,
    )


def x__unconfigured_report__mutmut_5(data: IncidentCostData) -> IncidentCostReport:
    downtime = data["downtime_minutes"]
    explanation = (
        f"Le service {data['XXbusiness_service_nameXX']} est reste indisponible "
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


def x__unconfigured_report__mutmut_6(data: IncidentCostData) -> IncidentCostReport:
    downtime = data["downtime_minutes"]
    explanation = (
        f"Le service {data['BUSINESS_SERVICE_NAME']} est reste indisponible "
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


def x__unconfigured_report__mutmut_7(data: IncidentCostData) -> IncidentCostReport:
    downtime = data["downtime_minutes"]
    explanation = (
        f"Le service {data['business_service_name']} est reste indisponible "
        f"pendant {downtime} minutes. Configurez 'revenue_per_minute' dans la "
        f"section business pour obtenir l'estimation du chiffre d'affaires affecte."
    )
    return IncidentCostReport(
        business_service_name=None,
        downtime_minutes=downtime,
        impacted_service_count=data["impacted_service_count"],
        resolved_at=data["resolved_at"],
        config_available=False,
        explanation=explanation,
    )


def x__unconfigured_report__mutmut_8(data: IncidentCostData) -> IncidentCostReport:
    downtime = data["downtime_minutes"]
    explanation = (
        f"Le service {data['business_service_name']} est reste indisponible "
        f"pendant {downtime} minutes. Configurez 'revenue_per_minute' dans la "
        f"section business pour obtenir l'estimation du chiffre d'affaires affecte."
    )
    return IncidentCostReport(
        business_service_name=data["business_service_name"],
        downtime_minutes=None,
        impacted_service_count=data["impacted_service_count"],
        resolved_at=data["resolved_at"],
        config_available=False,
        explanation=explanation,
    )


def x__unconfigured_report__mutmut_9(data: IncidentCostData) -> IncidentCostReport:
    downtime = data["downtime_minutes"]
    explanation = (
        f"Le service {data['business_service_name']} est reste indisponible "
        f"pendant {downtime} minutes. Configurez 'revenue_per_minute' dans la "
        f"section business pour obtenir l'estimation du chiffre d'affaires affecte."
    )
    return IncidentCostReport(
        business_service_name=data["business_service_name"],
        downtime_minutes=downtime,
        impacted_service_count=None,
        resolved_at=data["resolved_at"],
        config_available=False,
        explanation=explanation,
    )


def x__unconfigured_report__mutmut_10(data: IncidentCostData) -> IncidentCostReport:
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
        resolved_at=None,
        config_available=False,
        explanation=explanation,
    )


def x__unconfigured_report__mutmut_11(data: IncidentCostData) -> IncidentCostReport:
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
        config_available=None,
        explanation=explanation,
    )


def x__unconfigured_report__mutmut_12(data: IncidentCostData) -> IncidentCostReport:
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
        explanation=None,
    )


def x__unconfigured_report__mutmut_13(data: IncidentCostData) -> IncidentCostReport:
    downtime = data["downtime_minutes"]
    explanation = (
        f"Le service {data['business_service_name']} est reste indisponible "
        f"pendant {downtime} minutes. Configurez 'revenue_per_minute' dans la "
        f"section business pour obtenir l'estimation du chiffre d'affaires affecte."
    )
    return IncidentCostReport(
        downtime_minutes=downtime,
        impacted_service_count=data["impacted_service_count"],
        resolved_at=data["resolved_at"],
        config_available=False,
        explanation=explanation,
    )


def x__unconfigured_report__mutmut_14(data: IncidentCostData) -> IncidentCostReport:
    downtime = data["downtime_minutes"]
    explanation = (
        f"Le service {data['business_service_name']} est reste indisponible "
        f"pendant {downtime} minutes. Configurez 'revenue_per_minute' dans la "
        f"section business pour obtenir l'estimation du chiffre d'affaires affecte."
    )
    return IncidentCostReport(
        business_service_name=data["business_service_name"],
        impacted_service_count=data["impacted_service_count"],
        resolved_at=data["resolved_at"],
        config_available=False,
        explanation=explanation,
    )


def x__unconfigured_report__mutmut_15(data: IncidentCostData) -> IncidentCostReport:
    downtime = data["downtime_minutes"]
    explanation = (
        f"Le service {data['business_service_name']} est reste indisponible "
        f"pendant {downtime} minutes. Configurez 'revenue_per_minute' dans la "
        f"section business pour obtenir l'estimation du chiffre d'affaires affecte."
    )
    return IncidentCostReport(
        business_service_name=data["business_service_name"],
        downtime_minutes=downtime,
        resolved_at=data["resolved_at"],
        config_available=False,
        explanation=explanation,
    )


def x__unconfigured_report__mutmut_16(data: IncidentCostData) -> IncidentCostReport:
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
        config_available=False,
        explanation=explanation,
    )


def x__unconfigured_report__mutmut_17(data: IncidentCostData) -> IncidentCostReport:
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
        explanation=explanation,
    )


def x__unconfigured_report__mutmut_18(data: IncidentCostData) -> IncidentCostReport:
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
        )


def x__unconfigured_report__mutmut_19(data: IncidentCostData) -> IncidentCostReport:
    downtime = data["downtime_minutes"]
    explanation = (
        f"Le service {data['business_service_name']} est reste indisponible "
        f"pendant {downtime} minutes. Configurez 'revenue_per_minute' dans la "
        f"section business pour obtenir l'estimation du chiffre d'affaires affecte."
    )
    return IncidentCostReport(
        business_service_name=data["XXbusiness_service_nameXX"],
        downtime_minutes=downtime,
        impacted_service_count=data["impacted_service_count"],
        resolved_at=data["resolved_at"],
        config_available=False,
        explanation=explanation,
    )


def x__unconfigured_report__mutmut_20(data: IncidentCostData) -> IncidentCostReport:
    downtime = data["downtime_minutes"]
    explanation = (
        f"Le service {data['business_service_name']} est reste indisponible "
        f"pendant {downtime} minutes. Configurez 'revenue_per_minute' dans la "
        f"section business pour obtenir l'estimation du chiffre d'affaires affecte."
    )
    return IncidentCostReport(
        business_service_name=data["BUSINESS_SERVICE_NAME"],
        downtime_minutes=downtime,
        impacted_service_count=data["impacted_service_count"],
        resolved_at=data["resolved_at"],
        config_available=False,
        explanation=explanation,
    )


def x__unconfigured_report__mutmut_21(data: IncidentCostData) -> IncidentCostReport:
    downtime = data["downtime_minutes"]
    explanation = (
        f"Le service {data['business_service_name']} est reste indisponible "
        f"pendant {downtime} minutes. Configurez 'revenue_per_minute' dans la "
        f"section business pour obtenir l'estimation du chiffre d'affaires affecte."
    )
    return IncidentCostReport(
        business_service_name=data["business_service_name"],
        downtime_minutes=downtime,
        impacted_service_count=data["XXimpacted_service_countXX"],
        resolved_at=data["resolved_at"],
        config_available=False,
        explanation=explanation,
    )


def x__unconfigured_report__mutmut_22(data: IncidentCostData) -> IncidentCostReport:
    downtime = data["downtime_minutes"]
    explanation = (
        f"Le service {data['business_service_name']} est reste indisponible "
        f"pendant {downtime} minutes. Configurez 'revenue_per_minute' dans la "
        f"section business pour obtenir l'estimation du chiffre d'affaires affecte."
    )
    return IncidentCostReport(
        business_service_name=data["business_service_name"],
        downtime_minutes=downtime,
        impacted_service_count=data["IMPACTED_SERVICE_COUNT"],
        resolved_at=data["resolved_at"],
        config_available=False,
        explanation=explanation,
    )


def x__unconfigured_report__mutmut_23(data: IncidentCostData) -> IncidentCostReport:
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
        resolved_at=data["XXresolved_atXX"],
        config_available=False,
        explanation=explanation,
    )


def x__unconfigured_report__mutmut_24(data: IncidentCostData) -> IncidentCostReport:
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
        resolved_at=data["RESOLVED_AT"],
        config_available=False,
        explanation=explanation,
    )


def x__unconfigured_report__mutmut_25(data: IncidentCostData) -> IncidentCostReport:
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
        config_available=True,
        explanation=explanation,
    )

mutants_x__unconfigured_report__mutmut['_mutmut_orig'] = x__unconfigured_report__mutmut_orig # type: ignore # mutmut generated
mutants_x__unconfigured_report__mutmut['x__unconfigured_report__mutmut_1'] = x__unconfigured_report__mutmut_1 # type: ignore # mutmut generated
mutants_x__unconfigured_report__mutmut['x__unconfigured_report__mutmut_2'] = x__unconfigured_report__mutmut_2 # type: ignore # mutmut generated
mutants_x__unconfigured_report__mutmut['x__unconfigured_report__mutmut_3'] = x__unconfigured_report__mutmut_3 # type: ignore # mutmut generated
mutants_x__unconfigured_report__mutmut['x__unconfigured_report__mutmut_4'] = x__unconfigured_report__mutmut_4 # type: ignore # mutmut generated
mutants_x__unconfigured_report__mutmut['x__unconfigured_report__mutmut_5'] = x__unconfigured_report__mutmut_5 # type: ignore # mutmut generated
mutants_x__unconfigured_report__mutmut['x__unconfigured_report__mutmut_6'] = x__unconfigured_report__mutmut_6 # type: ignore # mutmut generated
mutants_x__unconfigured_report__mutmut['x__unconfigured_report__mutmut_7'] = x__unconfigured_report__mutmut_7 # type: ignore # mutmut generated
mutants_x__unconfigured_report__mutmut['x__unconfigured_report__mutmut_8'] = x__unconfigured_report__mutmut_8 # type: ignore # mutmut generated
mutants_x__unconfigured_report__mutmut['x__unconfigured_report__mutmut_9'] = x__unconfigured_report__mutmut_9 # type: ignore # mutmut generated
mutants_x__unconfigured_report__mutmut['x__unconfigured_report__mutmut_10'] = x__unconfigured_report__mutmut_10 # type: ignore # mutmut generated
mutants_x__unconfigured_report__mutmut['x__unconfigured_report__mutmut_11'] = x__unconfigured_report__mutmut_11 # type: ignore # mutmut generated
mutants_x__unconfigured_report__mutmut['x__unconfigured_report__mutmut_12'] = x__unconfigured_report__mutmut_12 # type: ignore # mutmut generated
mutants_x__unconfigured_report__mutmut['x__unconfigured_report__mutmut_13'] = x__unconfigured_report__mutmut_13 # type: ignore # mutmut generated
mutants_x__unconfigured_report__mutmut['x__unconfigured_report__mutmut_14'] = x__unconfigured_report__mutmut_14 # type: ignore # mutmut generated
mutants_x__unconfigured_report__mutmut['x__unconfigured_report__mutmut_15'] = x__unconfigured_report__mutmut_15 # type: ignore # mutmut generated
mutants_x__unconfigured_report__mutmut['x__unconfigured_report__mutmut_16'] = x__unconfigured_report__mutmut_16 # type: ignore # mutmut generated
mutants_x__unconfigured_report__mutmut['x__unconfigured_report__mutmut_17'] = x__unconfigured_report__mutmut_17 # type: ignore # mutmut generated
mutants_x__unconfigured_report__mutmut['x__unconfigured_report__mutmut_18'] = x__unconfigured_report__mutmut_18 # type: ignore # mutmut generated
mutants_x__unconfigured_report__mutmut['x__unconfigured_report__mutmut_19'] = x__unconfigured_report__mutmut_19 # type: ignore # mutmut generated
mutants_x__unconfigured_report__mutmut['x__unconfigured_report__mutmut_20'] = x__unconfigured_report__mutmut_20 # type: ignore # mutmut generated
mutants_x__unconfigured_report__mutmut['x__unconfigured_report__mutmut_21'] = x__unconfigured_report__mutmut_21 # type: ignore # mutmut generated
mutants_x__unconfigured_report__mutmut['x__unconfigured_report__mutmut_22'] = x__unconfigured_report__mutmut_22 # type: ignore # mutmut generated
mutants_x__unconfigured_report__mutmut['x__unconfigured_report__mutmut_23'] = x__unconfigured_report__mutmut_23 # type: ignore # mutmut generated
mutants_x__unconfigured_report__mutmut['x__unconfigured_report__mutmut_24'] = x__unconfigured_report__mutmut_24 # type: ignore # mutmut generated
mutants_x__unconfigured_report__mutmut['x__unconfigured_report__mutmut_25'] = x__unconfigured_report__mutmut_25 # type: ignore # mutmut generated
mutants_x__support_cost__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__support_cost__mutmut)
def _support_cost(downtime_minutes: int, config: BusinessConfigRaw) -> float:
    if config["support_cost_per_hour"] is None:
        return 0.0
    return round(downtime_minutes / _MINUTES_PER_HOUR * config["support_cost_per_hour"], 2)


def x__support_cost__mutmut_orig(downtime_minutes: int, config: BusinessConfigRaw) -> float:
    if config["support_cost_per_hour"] is None:
        return 0.0
    return round(downtime_minutes / _MINUTES_PER_HOUR * config["support_cost_per_hour"], 2)


def x__support_cost__mutmut_1(downtime_minutes: int, config: BusinessConfigRaw) -> float:
    if config["XXsupport_cost_per_hourXX"] is None:
        return 0.0
    return round(downtime_minutes / _MINUTES_PER_HOUR * config["support_cost_per_hour"], 2)


def x__support_cost__mutmut_2(downtime_minutes: int, config: BusinessConfigRaw) -> float:
    if config["SUPPORT_COST_PER_HOUR"] is None:
        return 0.0
    return round(downtime_minutes / _MINUTES_PER_HOUR * config["support_cost_per_hour"], 2)


def x__support_cost__mutmut_3(downtime_minutes: int, config: BusinessConfigRaw) -> float:
    if config["support_cost_per_hour"] is not None:
        return 0.0
    return round(downtime_minutes / _MINUTES_PER_HOUR * config["support_cost_per_hour"], 2)


def x__support_cost__mutmut_4(downtime_minutes: int, config: BusinessConfigRaw) -> float:
    if config["support_cost_per_hour"] is None:
        return 1.0
    return round(downtime_minutes / _MINUTES_PER_HOUR * config["support_cost_per_hour"], 2)


def x__support_cost__mutmut_5(downtime_minutes: int, config: BusinessConfigRaw) -> float:
    if config["support_cost_per_hour"] is None:
        return 0.0
    return round(None, 2)


def x__support_cost__mutmut_6(downtime_minutes: int, config: BusinessConfigRaw) -> float:
    if config["support_cost_per_hour"] is None:
        return 0.0
    return round(downtime_minutes / _MINUTES_PER_HOUR * config["support_cost_per_hour"], None)


def x__support_cost__mutmut_7(downtime_minutes: int, config: BusinessConfigRaw) -> float:
    if config["support_cost_per_hour"] is None:
        return 0.0
    return round(2)


def x__support_cost__mutmut_8(downtime_minutes: int, config: BusinessConfigRaw) -> float:
    if config["support_cost_per_hour"] is None:
        return 0.0
    return round(downtime_minutes / _MINUTES_PER_HOUR * config["support_cost_per_hour"], )


def x__support_cost__mutmut_9(downtime_minutes: int, config: BusinessConfigRaw) -> float:
    if config["support_cost_per_hour"] is None:
        return 0.0
    return round(downtime_minutes / _MINUTES_PER_HOUR / config["support_cost_per_hour"], 2)


def x__support_cost__mutmut_10(downtime_minutes: int, config: BusinessConfigRaw) -> float:
    if config["support_cost_per_hour"] is None:
        return 0.0
    return round(downtime_minutes * _MINUTES_PER_HOUR * config["support_cost_per_hour"], 2)


def x__support_cost__mutmut_11(downtime_minutes: int, config: BusinessConfigRaw) -> float:
    if config["support_cost_per_hour"] is None:
        return 0.0
    return round(downtime_minutes / _MINUTES_PER_HOUR * config["XXsupport_cost_per_hourXX"], 2)


def x__support_cost__mutmut_12(downtime_minutes: int, config: BusinessConfigRaw) -> float:
    if config["support_cost_per_hour"] is None:
        return 0.0
    return round(downtime_minutes / _MINUTES_PER_HOUR * config["SUPPORT_COST_PER_HOUR"], 2)


def x__support_cost__mutmut_13(downtime_minutes: int, config: BusinessConfigRaw) -> float:
    if config["support_cost_per_hour"] is None:
        return 0.0
    return round(downtime_minutes / _MINUTES_PER_HOUR * config["support_cost_per_hour"], 3)

mutants_x__support_cost__mutmut['_mutmut_orig'] = x__support_cost__mutmut_orig # type: ignore # mutmut generated
mutants_x__support_cost__mutmut['x__support_cost__mutmut_1'] = x__support_cost__mutmut_1 # type: ignore # mutmut generated
mutants_x__support_cost__mutmut['x__support_cost__mutmut_2'] = x__support_cost__mutmut_2 # type: ignore # mutmut generated
mutants_x__support_cost__mutmut['x__support_cost__mutmut_3'] = x__support_cost__mutmut_3 # type: ignore # mutmut generated
mutants_x__support_cost__mutmut['x__support_cost__mutmut_4'] = x__support_cost__mutmut_4 # type: ignore # mutmut generated
mutants_x__support_cost__mutmut['x__support_cost__mutmut_5'] = x__support_cost__mutmut_5 # type: ignore # mutmut generated
mutants_x__support_cost__mutmut['x__support_cost__mutmut_6'] = x__support_cost__mutmut_6 # type: ignore # mutmut generated
mutants_x__support_cost__mutmut['x__support_cost__mutmut_7'] = x__support_cost__mutmut_7 # type: ignore # mutmut generated
mutants_x__support_cost__mutmut['x__support_cost__mutmut_8'] = x__support_cost__mutmut_8 # type: ignore # mutmut generated
mutants_x__support_cost__mutmut['x__support_cost__mutmut_9'] = x__support_cost__mutmut_9 # type: ignore # mutmut generated
mutants_x__support_cost__mutmut['x__support_cost__mutmut_10'] = x__support_cost__mutmut_10 # type: ignore # mutmut generated
mutants_x__support_cost__mutmut['x__support_cost__mutmut_11'] = x__support_cost__mutmut_11 # type: ignore # mutmut generated
mutants_x__support_cost__mutmut['x__support_cost__mutmut_12'] = x__support_cost__mutmut_12 # type: ignore # mutmut generated
mutants_x__support_cost__mutmut['x__support_cost__mutmut_13'] = x__support_cost__mutmut_13 # type: ignore # mutmut generated
mutants_x__sla_penalty__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__sla_penalty__mutmut)
def _sla_penalty(sla_breached: bool, config: BusinessConfigRaw) -> float:
    if not sla_breached or config["sla_penalty_per_hour"] is None:
        return 0.0
    return round(config["sla_penalty_per_hour"], 2)


def x__sla_penalty__mutmut_orig(sla_breached: bool, config: BusinessConfigRaw) -> float:
    if not sla_breached or config["sla_penalty_per_hour"] is None:
        return 0.0
    return round(config["sla_penalty_per_hour"], 2)


def x__sla_penalty__mutmut_1(sla_breached: bool, config: BusinessConfigRaw) -> float:
    if not sla_breached and config["sla_penalty_per_hour"] is None:
        return 0.0
    return round(config["sla_penalty_per_hour"], 2)


def x__sla_penalty__mutmut_2(sla_breached: bool, config: BusinessConfigRaw) -> float:
    if sla_breached or config["sla_penalty_per_hour"] is None:
        return 0.0
    return round(config["sla_penalty_per_hour"], 2)


def x__sla_penalty__mutmut_3(sla_breached: bool, config: BusinessConfigRaw) -> float:
    if not sla_breached or config["XXsla_penalty_per_hourXX"] is None:
        return 0.0
    return round(config["sla_penalty_per_hour"], 2)


def x__sla_penalty__mutmut_4(sla_breached: bool, config: BusinessConfigRaw) -> float:
    if not sla_breached or config["SLA_PENALTY_PER_HOUR"] is None:
        return 0.0
    return round(config["sla_penalty_per_hour"], 2)


def x__sla_penalty__mutmut_5(sla_breached: bool, config: BusinessConfigRaw) -> float:
    if not sla_breached or config["sla_penalty_per_hour"] is not None:
        return 0.0
    return round(config["sla_penalty_per_hour"], 2)


def x__sla_penalty__mutmut_6(sla_breached: bool, config: BusinessConfigRaw) -> float:
    if not sla_breached or config["sla_penalty_per_hour"] is None:
        return 1.0
    return round(config["sla_penalty_per_hour"], 2)


def x__sla_penalty__mutmut_7(sla_breached: bool, config: BusinessConfigRaw) -> float:
    if not sla_breached or config["sla_penalty_per_hour"] is None:
        return 0.0
    return round(None, 2)


def x__sla_penalty__mutmut_8(sla_breached: bool, config: BusinessConfigRaw) -> float:
    if not sla_breached or config["sla_penalty_per_hour"] is None:
        return 0.0
    return round(config["sla_penalty_per_hour"], None)


def x__sla_penalty__mutmut_9(sla_breached: bool, config: BusinessConfigRaw) -> float:
    if not sla_breached or config["sla_penalty_per_hour"] is None:
        return 0.0
    return round(2)


def x__sla_penalty__mutmut_10(sla_breached: bool, config: BusinessConfigRaw) -> float:
    if not sla_breached or config["sla_penalty_per_hour"] is None:
        return 0.0
    return round(config["sla_penalty_per_hour"], )


def x__sla_penalty__mutmut_11(sla_breached: bool, config: BusinessConfigRaw) -> float:
    if not sla_breached or config["sla_penalty_per_hour"] is None:
        return 0.0
    return round(config["XXsla_penalty_per_hourXX"], 2)


def x__sla_penalty__mutmut_12(sla_breached: bool, config: BusinessConfigRaw) -> float:
    if not sla_breached or config["sla_penalty_per_hour"] is None:
        return 0.0
    return round(config["SLA_PENALTY_PER_HOUR"], 2)


def x__sla_penalty__mutmut_13(sla_breached: bool, config: BusinessConfigRaw) -> float:
    if not sla_breached or config["sla_penalty_per_hour"] is None:
        return 0.0
    return round(config["sla_penalty_per_hour"], 3)

mutants_x__sla_penalty__mutmut['_mutmut_orig'] = x__sla_penalty__mutmut_orig # type: ignore # mutmut generated
mutants_x__sla_penalty__mutmut['x__sla_penalty__mutmut_1'] = x__sla_penalty__mutmut_1 # type: ignore # mutmut generated
mutants_x__sla_penalty__mutmut['x__sla_penalty__mutmut_2'] = x__sla_penalty__mutmut_2 # type: ignore # mutmut generated
mutants_x__sla_penalty__mutmut['x__sla_penalty__mutmut_3'] = x__sla_penalty__mutmut_3 # type: ignore # mutmut generated
mutants_x__sla_penalty__mutmut['x__sla_penalty__mutmut_4'] = x__sla_penalty__mutmut_4 # type: ignore # mutmut generated
mutants_x__sla_penalty__mutmut['x__sla_penalty__mutmut_5'] = x__sla_penalty__mutmut_5 # type: ignore # mutmut generated
mutants_x__sla_penalty__mutmut['x__sla_penalty__mutmut_6'] = x__sla_penalty__mutmut_6 # type: ignore # mutmut generated
mutants_x__sla_penalty__mutmut['x__sla_penalty__mutmut_7'] = x__sla_penalty__mutmut_7 # type: ignore # mutmut generated
mutants_x__sla_penalty__mutmut['x__sla_penalty__mutmut_8'] = x__sla_penalty__mutmut_8 # type: ignore # mutmut generated
mutants_x__sla_penalty__mutmut['x__sla_penalty__mutmut_9'] = x__sla_penalty__mutmut_9 # type: ignore # mutmut generated
mutants_x__sla_penalty__mutmut['x__sla_penalty__mutmut_10'] = x__sla_penalty__mutmut_10 # type: ignore # mutmut generated
mutants_x__sla_penalty__mutmut['x__sla_penalty__mutmut_11'] = x__sla_penalty__mutmut_11 # type: ignore # mutmut generated
mutants_x__sla_penalty__mutmut['x__sla_penalty__mutmut_12'] = x__sla_penalty__mutmut_12 # type: ignore # mutmut generated
mutants_x__sla_penalty__mutmut['x__sla_penalty__mutmut_13'] = x__sla_penalty__mutmut_13 # type: ignore # mutmut generated
mutants_x__build_basis__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__build_basis__mutmut)
def _build_basis(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
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


def x__build_basis__mutmut_orig(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
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


def x__build_basis__mutmut_1(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
    config_used: dict[str, str] = None
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


def x__build_basis__mutmut_2(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
    config_used: dict[str, str] = {"XXrevenue_per_minuteXX": str(config["revenue_per_minute"])}
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


def x__build_basis__mutmut_3(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
    config_used: dict[str, str] = {"REVENUE_PER_MINUTE": str(config["revenue_per_minute"])}
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


def x__build_basis__mutmut_4(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
    config_used: dict[str, str] = {"revenue_per_minute": str(None)}
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


def x__build_basis__mutmut_5(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
    config_used: dict[str, str] = {"revenue_per_minute": str(config["XXrevenue_per_minuteXX"])}
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


def x__build_basis__mutmut_6(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
    config_used: dict[str, str] = {"revenue_per_minute": str(config["REVENUE_PER_MINUTE"])}
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


def x__build_basis__mutmut_7(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
    config_used: dict[str, str] = {"revenue_per_minute": str(config["revenue_per_minute"])}
    if config["XXsupport_cost_per_hourXX"] is not None:
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


def x__build_basis__mutmut_8(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
    config_used: dict[str, str] = {"revenue_per_minute": str(config["revenue_per_minute"])}
    if config["SUPPORT_COST_PER_HOUR"] is not None:
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


def x__build_basis__mutmut_9(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
    config_used: dict[str, str] = {"revenue_per_minute": str(config["revenue_per_minute"])}
    if config["support_cost_per_hour"] is None:
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


def x__build_basis__mutmut_10(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
    config_used: dict[str, str] = {"revenue_per_minute": str(config["revenue_per_minute"])}
    if config["support_cost_per_hour"] is not None:
        config_used["support_cost_per_hour"] = None
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


def x__build_basis__mutmut_11(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
    config_used: dict[str, str] = {"revenue_per_minute": str(config["revenue_per_minute"])}
    if config["support_cost_per_hour"] is not None:
        config_used["XXsupport_cost_per_hourXX"] = str(config["support_cost_per_hour"])
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


def x__build_basis__mutmut_12(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
    config_used: dict[str, str] = {"revenue_per_minute": str(config["revenue_per_minute"])}
    if config["support_cost_per_hour"] is not None:
        config_used["SUPPORT_COST_PER_HOUR"] = str(config["support_cost_per_hour"])
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


def x__build_basis__mutmut_13(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
    config_used: dict[str, str] = {"revenue_per_minute": str(config["revenue_per_minute"])}
    if config["support_cost_per_hour"] is not None:
        config_used["support_cost_per_hour"] = str(None)
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


def x__build_basis__mutmut_14(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
    config_used: dict[str, str] = {"revenue_per_minute": str(config["revenue_per_minute"])}
    if config["support_cost_per_hour"] is not None:
        config_used["support_cost_per_hour"] = str(config["XXsupport_cost_per_hourXX"])
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


def x__build_basis__mutmut_15(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
    config_used: dict[str, str] = {"revenue_per_minute": str(config["revenue_per_minute"])}
    if config["support_cost_per_hour"] is not None:
        config_used["support_cost_per_hour"] = str(config["SUPPORT_COST_PER_HOUR"])
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


def x__build_basis__mutmut_16(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
    config_used: dict[str, str] = {"revenue_per_minute": str(config["revenue_per_minute"])}
    if config["support_cost_per_hour"] is not None:
        config_used["support_cost_per_hour"] = str(config["support_cost_per_hour"])
    if config["sla_penalty_per_hour"] is not None or data["sla_breached"]:
        config_used["sla_penalty_per_hour"] = str(config["sla_penalty_per_hour"])
    return CalculationBasis(
        formula=_FORMULA,
        config_values_used=config_used,
        source_metrics={
            "downtime_minutes": str(data["downtime_minutes"]),
            "sla_breached": str(data["sla_breached"]),
        },
    )


def x__build_basis__mutmut_17(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
    config_used: dict[str, str] = {"revenue_per_minute": str(config["revenue_per_minute"])}
    if config["support_cost_per_hour"] is not None:
        config_used["support_cost_per_hour"] = str(config["support_cost_per_hour"])
    if config["XXsla_penalty_per_hourXX"] is not None and data["sla_breached"]:
        config_used["sla_penalty_per_hour"] = str(config["sla_penalty_per_hour"])
    return CalculationBasis(
        formula=_FORMULA,
        config_values_used=config_used,
        source_metrics={
            "downtime_minutes": str(data["downtime_minutes"]),
            "sla_breached": str(data["sla_breached"]),
        },
    )


def x__build_basis__mutmut_18(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
    config_used: dict[str, str] = {"revenue_per_minute": str(config["revenue_per_minute"])}
    if config["support_cost_per_hour"] is not None:
        config_used["support_cost_per_hour"] = str(config["support_cost_per_hour"])
    if config["SLA_PENALTY_PER_HOUR"] is not None and data["sla_breached"]:
        config_used["sla_penalty_per_hour"] = str(config["sla_penalty_per_hour"])
    return CalculationBasis(
        formula=_FORMULA,
        config_values_used=config_used,
        source_metrics={
            "downtime_minutes": str(data["downtime_minutes"]),
            "sla_breached": str(data["sla_breached"]),
        },
    )


def x__build_basis__mutmut_19(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
    config_used: dict[str, str] = {"revenue_per_minute": str(config["revenue_per_minute"])}
    if config["support_cost_per_hour"] is not None:
        config_used["support_cost_per_hour"] = str(config["support_cost_per_hour"])
    if config["sla_penalty_per_hour"] is None and data["sla_breached"]:
        config_used["sla_penalty_per_hour"] = str(config["sla_penalty_per_hour"])
    return CalculationBasis(
        formula=_FORMULA,
        config_values_used=config_used,
        source_metrics={
            "downtime_minutes": str(data["downtime_minutes"]),
            "sla_breached": str(data["sla_breached"]),
        },
    )


def x__build_basis__mutmut_20(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
    config_used: dict[str, str] = {"revenue_per_minute": str(config["revenue_per_minute"])}
    if config["support_cost_per_hour"] is not None:
        config_used["support_cost_per_hour"] = str(config["support_cost_per_hour"])
    if config["sla_penalty_per_hour"] is not None and data["XXsla_breachedXX"]:
        config_used["sla_penalty_per_hour"] = str(config["sla_penalty_per_hour"])
    return CalculationBasis(
        formula=_FORMULA,
        config_values_used=config_used,
        source_metrics={
            "downtime_minutes": str(data["downtime_minutes"]),
            "sla_breached": str(data["sla_breached"]),
        },
    )


def x__build_basis__mutmut_21(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
    config_used: dict[str, str] = {"revenue_per_minute": str(config["revenue_per_minute"])}
    if config["support_cost_per_hour"] is not None:
        config_used["support_cost_per_hour"] = str(config["support_cost_per_hour"])
    if config["sla_penalty_per_hour"] is not None and data["SLA_BREACHED"]:
        config_used["sla_penalty_per_hour"] = str(config["sla_penalty_per_hour"])
    return CalculationBasis(
        formula=_FORMULA,
        config_values_used=config_used,
        source_metrics={
            "downtime_minutes": str(data["downtime_minutes"]),
            "sla_breached": str(data["sla_breached"]),
        },
    )


def x__build_basis__mutmut_22(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
    config_used: dict[str, str] = {"revenue_per_minute": str(config["revenue_per_minute"])}
    if config["support_cost_per_hour"] is not None:
        config_used["support_cost_per_hour"] = str(config["support_cost_per_hour"])
    if config["sla_penalty_per_hour"] is not None and data["sla_breached"]:
        config_used["sla_penalty_per_hour"] = None
    return CalculationBasis(
        formula=_FORMULA,
        config_values_used=config_used,
        source_metrics={
            "downtime_minutes": str(data["downtime_minutes"]),
            "sla_breached": str(data["sla_breached"]),
        },
    )


def x__build_basis__mutmut_23(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
    config_used: dict[str, str] = {"revenue_per_minute": str(config["revenue_per_minute"])}
    if config["support_cost_per_hour"] is not None:
        config_used["support_cost_per_hour"] = str(config["support_cost_per_hour"])
    if config["sla_penalty_per_hour"] is not None and data["sla_breached"]:
        config_used["XXsla_penalty_per_hourXX"] = str(config["sla_penalty_per_hour"])
    return CalculationBasis(
        formula=_FORMULA,
        config_values_used=config_used,
        source_metrics={
            "downtime_minutes": str(data["downtime_minutes"]),
            "sla_breached": str(data["sla_breached"]),
        },
    )


def x__build_basis__mutmut_24(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
    config_used: dict[str, str] = {"revenue_per_minute": str(config["revenue_per_minute"])}
    if config["support_cost_per_hour"] is not None:
        config_used["support_cost_per_hour"] = str(config["support_cost_per_hour"])
    if config["sla_penalty_per_hour"] is not None and data["sla_breached"]:
        config_used["SLA_PENALTY_PER_HOUR"] = str(config["sla_penalty_per_hour"])
    return CalculationBasis(
        formula=_FORMULA,
        config_values_used=config_used,
        source_metrics={
            "downtime_minutes": str(data["downtime_minutes"]),
            "sla_breached": str(data["sla_breached"]),
        },
    )


def x__build_basis__mutmut_25(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
    config_used: dict[str, str] = {"revenue_per_minute": str(config["revenue_per_minute"])}
    if config["support_cost_per_hour"] is not None:
        config_used["support_cost_per_hour"] = str(config["support_cost_per_hour"])
    if config["sla_penalty_per_hour"] is not None and data["sla_breached"]:
        config_used["sla_penalty_per_hour"] = str(None)
    return CalculationBasis(
        formula=_FORMULA,
        config_values_used=config_used,
        source_metrics={
            "downtime_minutes": str(data["downtime_minutes"]),
            "sla_breached": str(data["sla_breached"]),
        },
    )


def x__build_basis__mutmut_26(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
    config_used: dict[str, str] = {"revenue_per_minute": str(config["revenue_per_minute"])}
    if config["support_cost_per_hour"] is not None:
        config_used["support_cost_per_hour"] = str(config["support_cost_per_hour"])
    if config["sla_penalty_per_hour"] is not None and data["sla_breached"]:
        config_used["sla_penalty_per_hour"] = str(config["XXsla_penalty_per_hourXX"])
    return CalculationBasis(
        formula=_FORMULA,
        config_values_used=config_used,
        source_metrics={
            "downtime_minutes": str(data["downtime_minutes"]),
            "sla_breached": str(data["sla_breached"]),
        },
    )


def x__build_basis__mutmut_27(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
    config_used: dict[str, str] = {"revenue_per_minute": str(config["revenue_per_minute"])}
    if config["support_cost_per_hour"] is not None:
        config_used["support_cost_per_hour"] = str(config["support_cost_per_hour"])
    if config["sla_penalty_per_hour"] is not None and data["sla_breached"]:
        config_used["sla_penalty_per_hour"] = str(config["SLA_PENALTY_PER_HOUR"])
    return CalculationBasis(
        formula=_FORMULA,
        config_values_used=config_used,
        source_metrics={
            "downtime_minutes": str(data["downtime_minutes"]),
            "sla_breached": str(data["sla_breached"]),
        },
    )


def x__build_basis__mutmut_28(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
    config_used: dict[str, str] = {"revenue_per_minute": str(config["revenue_per_minute"])}
    if config["support_cost_per_hour"] is not None:
        config_used["support_cost_per_hour"] = str(config["support_cost_per_hour"])
    if config["sla_penalty_per_hour"] is not None and data["sla_breached"]:
        config_used["sla_penalty_per_hour"] = str(config["sla_penalty_per_hour"])
    return CalculationBasis(
        formula=None,
        config_values_used=config_used,
        source_metrics={
            "downtime_minutes": str(data["downtime_minutes"]),
            "sla_breached": str(data["sla_breached"]),
        },
    )


def x__build_basis__mutmut_29(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
    config_used: dict[str, str] = {"revenue_per_minute": str(config["revenue_per_minute"])}
    if config["support_cost_per_hour"] is not None:
        config_used["support_cost_per_hour"] = str(config["support_cost_per_hour"])
    if config["sla_penalty_per_hour"] is not None and data["sla_breached"]:
        config_used["sla_penalty_per_hour"] = str(config["sla_penalty_per_hour"])
    return CalculationBasis(
        formula=_FORMULA,
        config_values_used=None,
        source_metrics={
            "downtime_minutes": str(data["downtime_minutes"]),
            "sla_breached": str(data["sla_breached"]),
        },
    )


def x__build_basis__mutmut_30(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
    config_used: dict[str, str] = {"revenue_per_minute": str(config["revenue_per_minute"])}
    if config["support_cost_per_hour"] is not None:
        config_used["support_cost_per_hour"] = str(config["support_cost_per_hour"])
    if config["sla_penalty_per_hour"] is not None and data["sla_breached"]:
        config_used["sla_penalty_per_hour"] = str(config["sla_penalty_per_hour"])
    return CalculationBasis(
        formula=_FORMULA,
        config_values_used=config_used,
        source_metrics=None,
    )


def x__build_basis__mutmut_31(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
    config_used: dict[str, str] = {"revenue_per_minute": str(config["revenue_per_minute"])}
    if config["support_cost_per_hour"] is not None:
        config_used["support_cost_per_hour"] = str(config["support_cost_per_hour"])
    if config["sla_penalty_per_hour"] is not None and data["sla_breached"]:
        config_used["sla_penalty_per_hour"] = str(config["sla_penalty_per_hour"])
    return CalculationBasis(
        config_values_used=config_used,
        source_metrics={
            "downtime_minutes": str(data["downtime_minutes"]),
            "sla_breached": str(data["sla_breached"]),
        },
    )


def x__build_basis__mutmut_32(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
    config_used: dict[str, str] = {"revenue_per_minute": str(config["revenue_per_minute"])}
    if config["support_cost_per_hour"] is not None:
        config_used["support_cost_per_hour"] = str(config["support_cost_per_hour"])
    if config["sla_penalty_per_hour"] is not None and data["sla_breached"]:
        config_used["sla_penalty_per_hour"] = str(config["sla_penalty_per_hour"])
    return CalculationBasis(
        formula=_FORMULA,
        source_metrics={
            "downtime_minutes": str(data["downtime_minutes"]),
            "sla_breached": str(data["sla_breached"]),
        },
    )


def x__build_basis__mutmut_33(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
    config_used: dict[str, str] = {"revenue_per_minute": str(config["revenue_per_minute"])}
    if config["support_cost_per_hour"] is not None:
        config_used["support_cost_per_hour"] = str(config["support_cost_per_hour"])
    if config["sla_penalty_per_hour"] is not None and data["sla_breached"]:
        config_used["sla_penalty_per_hour"] = str(config["sla_penalty_per_hour"])
    return CalculationBasis(
        formula=_FORMULA,
        config_values_used=config_used,
        )


def x__build_basis__mutmut_34(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
    config_used: dict[str, str] = {"revenue_per_minute": str(config["revenue_per_minute"])}
    if config["support_cost_per_hour"] is not None:
        config_used["support_cost_per_hour"] = str(config["support_cost_per_hour"])
    if config["sla_penalty_per_hour"] is not None and data["sla_breached"]:
        config_used["sla_penalty_per_hour"] = str(config["sla_penalty_per_hour"])
    return CalculationBasis(
        formula=_FORMULA,
        config_values_used=config_used,
        source_metrics={
            "XXdowntime_minutesXX": str(data["downtime_minutes"]),
            "sla_breached": str(data["sla_breached"]),
        },
    )


def x__build_basis__mutmut_35(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
    config_used: dict[str, str] = {"revenue_per_minute": str(config["revenue_per_minute"])}
    if config["support_cost_per_hour"] is not None:
        config_used["support_cost_per_hour"] = str(config["support_cost_per_hour"])
    if config["sla_penalty_per_hour"] is not None and data["sla_breached"]:
        config_used["sla_penalty_per_hour"] = str(config["sla_penalty_per_hour"])
    return CalculationBasis(
        formula=_FORMULA,
        config_values_used=config_used,
        source_metrics={
            "DOWNTIME_MINUTES": str(data["downtime_minutes"]),
            "sla_breached": str(data["sla_breached"]),
        },
    )


def x__build_basis__mutmut_36(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
    config_used: dict[str, str] = {"revenue_per_minute": str(config["revenue_per_minute"])}
    if config["support_cost_per_hour"] is not None:
        config_used["support_cost_per_hour"] = str(config["support_cost_per_hour"])
    if config["sla_penalty_per_hour"] is not None and data["sla_breached"]:
        config_used["sla_penalty_per_hour"] = str(config["sla_penalty_per_hour"])
    return CalculationBasis(
        formula=_FORMULA,
        config_values_used=config_used,
        source_metrics={
            "downtime_minutes": str(None),
            "sla_breached": str(data["sla_breached"]),
        },
    )


def x__build_basis__mutmut_37(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
    config_used: dict[str, str] = {"revenue_per_minute": str(config["revenue_per_minute"])}
    if config["support_cost_per_hour"] is not None:
        config_used["support_cost_per_hour"] = str(config["support_cost_per_hour"])
    if config["sla_penalty_per_hour"] is not None and data["sla_breached"]:
        config_used["sla_penalty_per_hour"] = str(config["sla_penalty_per_hour"])
    return CalculationBasis(
        formula=_FORMULA,
        config_values_used=config_used,
        source_metrics={
            "downtime_minutes": str(data["XXdowntime_minutesXX"]),
            "sla_breached": str(data["sla_breached"]),
        },
    )


def x__build_basis__mutmut_38(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
    config_used: dict[str, str] = {"revenue_per_minute": str(config["revenue_per_minute"])}
    if config["support_cost_per_hour"] is not None:
        config_used["support_cost_per_hour"] = str(config["support_cost_per_hour"])
    if config["sla_penalty_per_hour"] is not None and data["sla_breached"]:
        config_used["sla_penalty_per_hour"] = str(config["sla_penalty_per_hour"])
    return CalculationBasis(
        formula=_FORMULA,
        config_values_used=config_used,
        source_metrics={
            "downtime_minutes": str(data["DOWNTIME_MINUTES"]),
            "sla_breached": str(data["sla_breached"]),
        },
    )


def x__build_basis__mutmut_39(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
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
            "XXsla_breachedXX": str(data["sla_breached"]),
        },
    )


def x__build_basis__mutmut_40(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
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
            "SLA_BREACHED": str(data["sla_breached"]),
        },
    )


def x__build_basis__mutmut_41(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
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
            "sla_breached": str(None),
        },
    )


def x__build_basis__mutmut_42(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
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
            "sla_breached": str(data["XXsla_breachedXX"]),
        },
    )


def x__build_basis__mutmut_43(data: IncidentCostData, config: BusinessConfigRaw) -> CalculationBasis:
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
            "sla_breached": str(data["SLA_BREACHED"]),
        },
    )

mutants_x__build_basis__mutmut['_mutmut_orig'] = x__build_basis__mutmut_orig # type: ignore # mutmut generated
mutants_x__build_basis__mutmut['x__build_basis__mutmut_1'] = x__build_basis__mutmut_1 # type: ignore # mutmut generated
mutants_x__build_basis__mutmut['x__build_basis__mutmut_2'] = x__build_basis__mutmut_2 # type: ignore # mutmut generated
mutants_x__build_basis__mutmut['x__build_basis__mutmut_3'] = x__build_basis__mutmut_3 # type: ignore # mutmut generated
mutants_x__build_basis__mutmut['x__build_basis__mutmut_4'] = x__build_basis__mutmut_4 # type: ignore # mutmut generated
mutants_x__build_basis__mutmut['x__build_basis__mutmut_5'] = x__build_basis__mutmut_5 # type: ignore # mutmut generated
mutants_x__build_basis__mutmut['x__build_basis__mutmut_6'] = x__build_basis__mutmut_6 # type: ignore # mutmut generated
mutants_x__build_basis__mutmut['x__build_basis__mutmut_7'] = x__build_basis__mutmut_7 # type: ignore # mutmut generated
mutants_x__build_basis__mutmut['x__build_basis__mutmut_8'] = x__build_basis__mutmut_8 # type: ignore # mutmut generated
mutants_x__build_basis__mutmut['x__build_basis__mutmut_9'] = x__build_basis__mutmut_9 # type: ignore # mutmut generated
mutants_x__build_basis__mutmut['x__build_basis__mutmut_10'] = x__build_basis__mutmut_10 # type: ignore # mutmut generated
mutants_x__build_basis__mutmut['x__build_basis__mutmut_11'] = x__build_basis__mutmut_11 # type: ignore # mutmut generated
mutants_x__build_basis__mutmut['x__build_basis__mutmut_12'] = x__build_basis__mutmut_12 # type: ignore # mutmut generated
mutants_x__build_basis__mutmut['x__build_basis__mutmut_13'] = x__build_basis__mutmut_13 # type: ignore # mutmut generated
mutants_x__build_basis__mutmut['x__build_basis__mutmut_14'] = x__build_basis__mutmut_14 # type: ignore # mutmut generated
mutants_x__build_basis__mutmut['x__build_basis__mutmut_15'] = x__build_basis__mutmut_15 # type: ignore # mutmut generated
mutants_x__build_basis__mutmut['x__build_basis__mutmut_16'] = x__build_basis__mutmut_16 # type: ignore # mutmut generated
mutants_x__build_basis__mutmut['x__build_basis__mutmut_17'] = x__build_basis__mutmut_17 # type: ignore # mutmut generated
mutants_x__build_basis__mutmut['x__build_basis__mutmut_18'] = x__build_basis__mutmut_18 # type: ignore # mutmut generated
mutants_x__build_basis__mutmut['x__build_basis__mutmut_19'] = x__build_basis__mutmut_19 # type: ignore # mutmut generated
mutants_x__build_basis__mutmut['x__build_basis__mutmut_20'] = x__build_basis__mutmut_20 # type: ignore # mutmut generated
mutants_x__build_basis__mutmut['x__build_basis__mutmut_21'] = x__build_basis__mutmut_21 # type: ignore # mutmut generated
mutants_x__build_basis__mutmut['x__build_basis__mutmut_22'] = x__build_basis__mutmut_22 # type: ignore # mutmut generated
mutants_x__build_basis__mutmut['x__build_basis__mutmut_23'] = x__build_basis__mutmut_23 # type: ignore # mutmut generated
mutants_x__build_basis__mutmut['x__build_basis__mutmut_24'] = x__build_basis__mutmut_24 # type: ignore # mutmut generated
mutants_x__build_basis__mutmut['x__build_basis__mutmut_25'] = x__build_basis__mutmut_25 # type: ignore # mutmut generated
mutants_x__build_basis__mutmut['x__build_basis__mutmut_26'] = x__build_basis__mutmut_26 # type: ignore # mutmut generated
mutants_x__build_basis__mutmut['x__build_basis__mutmut_27'] = x__build_basis__mutmut_27 # type: ignore # mutmut generated
mutants_x__build_basis__mutmut['x__build_basis__mutmut_28'] = x__build_basis__mutmut_28 # type: ignore # mutmut generated
mutants_x__build_basis__mutmut['x__build_basis__mutmut_29'] = x__build_basis__mutmut_29 # type: ignore # mutmut generated
mutants_x__build_basis__mutmut['x__build_basis__mutmut_30'] = x__build_basis__mutmut_30 # type: ignore # mutmut generated
mutants_x__build_basis__mutmut['x__build_basis__mutmut_31'] = x__build_basis__mutmut_31 # type: ignore # mutmut generated
mutants_x__build_basis__mutmut['x__build_basis__mutmut_32'] = x__build_basis__mutmut_32 # type: ignore # mutmut generated
mutants_x__build_basis__mutmut['x__build_basis__mutmut_33'] = x__build_basis__mutmut_33 # type: ignore # mutmut generated
mutants_x__build_basis__mutmut['x__build_basis__mutmut_34'] = x__build_basis__mutmut_34 # type: ignore # mutmut generated
mutants_x__build_basis__mutmut['x__build_basis__mutmut_35'] = x__build_basis__mutmut_35 # type: ignore # mutmut generated
mutants_x__build_basis__mutmut['x__build_basis__mutmut_36'] = x__build_basis__mutmut_36 # type: ignore # mutmut generated
mutants_x__build_basis__mutmut['x__build_basis__mutmut_37'] = x__build_basis__mutmut_37 # type: ignore # mutmut generated
mutants_x__build_basis__mutmut['x__build_basis__mutmut_38'] = x__build_basis__mutmut_38 # type: ignore # mutmut generated
mutants_x__build_basis__mutmut['x__build_basis__mutmut_39'] = x__build_basis__mutmut_39 # type: ignore # mutmut generated
mutants_x__build_basis__mutmut['x__build_basis__mutmut_40'] = x__build_basis__mutmut_40 # type: ignore # mutmut generated
mutants_x__build_basis__mutmut['x__build_basis__mutmut_41'] = x__build_basis__mutmut_41 # type: ignore # mutmut generated
mutants_x__build_basis__mutmut['x__build_basis__mutmut_42'] = x__build_basis__mutmut_42 # type: ignore # mutmut generated
mutants_x__build_basis__mutmut['x__build_basis__mutmut_43'] = x__build_basis__mutmut_43 # type: ignore # mutmut generated
