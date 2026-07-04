from __future__ import annotations

from datetime import date

from hexawyn.domain.models.cluster_capacity_forecast import (
    ClusterCapacityForecastReport,
    ClusterCapacityForecastRequest,
    ClusterCapacityRawData,
    Confidence,
    CriticalResource,
    ResourceForecast,
    ResourceType,
)
from hexawyn.domain.models.constants import ClusterCapacityForecastConstants
from hexawyn.domain.services.cluster_capacity_forecast.growth_rate import compute_growth_rate
from hexawyn.domain.services.cluster_capacity_forecast.saturation_prediction import (
    predict_saturation,
)

_cfg = ClusterCapacityForecastConstants()
_NEAR_TERM_HORIZON_DAYS = 30


def build_cluster_capacity_forecast(
    request: ClusterCapacityForecastRequest,
    raw_data: ClusterCapacityRawData,
    observed_at: date,
) -> ClusterCapacityForecastReport:
    cpu = _build_resource_forecast(
        "cpu", raw_data.cpu_daily_usage_cores, raw_data.total_allocatable_cpu_cores, observed_at
    )
    memory = _build_resource_forecast(
        "memory",
        raw_data.memory_daily_usage_gb,
        raw_data.total_allocatable_memory_gb,
        observed_at,
    )

    critical_resource = _pick_critical_resource(cpu, memory)
    window_days_used = min(
        len(raw_data.cpu_daily_usage_cores) or request.window_days,
        len(raw_data.memory_daily_usage_gb) or request.window_days,
    )

    return ClusterCapacityForecastReport(
        cpu=cpu,
        memory=memory,
        critical_resource=critical_resource,
        autoscaler_enabled=raw_data.autoscaler_enabled,
        recommendation=_build_recommendation(critical_resource, cpu, memory),
        confidence=_compute_confidence(window_days_used),
        window_days_used=window_days_used,
    )


def _build_resource_forecast(
    resource_type: ResourceType, daily_values: list[float], ceiling: float, observed_at: date
) -> ResourceForecast:
    growth = compute_growth_rate(daily_values)
    current = daily_values[-1] if daily_values else 0.0
    utilization_percent = round(current / ceiling * 100, 2) if ceiling > 0 else 0.0
    saturation = predict_saturation(
        current=current,
        ceiling=ceiling,
        growth_rate_per_day=growth.slope_per_day,
        observed_at=observed_at,
        max_horizon_days=_cfg.max_forecast_horizon_days,
    )

    return ResourceForecast(
        resource_type=resource_type,
        current_value=current,
        ceiling=ceiling,
        current_utilization_percent=utilization_percent,
        growth_rate_per_day=growth.slope_per_day,
        days_to_saturation=saturation.days_to_saturation,
        saturation_date=saturation.saturation_date,
        capacity_jump_detected=growth.capacity_jump_detected,
        spike_caveat=growth.spike_caveat,
        capped_horizon=saturation.capped_horizon,
    )


def _pick_critical_resource(cpu: ResourceForecast, memory: ResourceForecast) -> CriticalResource:
    if cpu.days_to_saturation is None and memory.days_to_saturation is None:
        return "None"
    if cpu.days_to_saturation is None:
        return "Memory"
    if memory.days_to_saturation is None:
        return "CPU"
    return "CPU" if cpu.days_to_saturation <= memory.days_to_saturation else "Memory"


def _compute_confidence(window_days_used: int) -> Confidence:
    if window_days_used >= _cfg.default_window_days:
        return "high"
    if window_days_used >= _cfg.min_medium_confidence_days:
        return "medium"
    return "low"


def _build_recommendation(
    critical_resource: CriticalResource, cpu: ResourceForecast, memory: ResourceForecast
) -> str:
    if critical_resource == "None":
        return "No saturation risk in the foreseeable future — cluster capacity is stable."

    resource = cpu if critical_resource == "CPU" else memory
    if (
        resource.days_to_saturation is not None
        and resource.days_to_saturation <= _NEAR_TERM_HORIZON_DAYS
    ):
        return (
            f"{critical_resource} projected to saturate in {resource.days_to_saturation} "
            f"days (around {resource.saturation_date}) — plan capacity expansion soon."
        )
    return (
        f"{critical_resource} is the limiting resource, projected to saturate around "
        f"{resource.saturation_date} — monitor and plan ahead."
    )
