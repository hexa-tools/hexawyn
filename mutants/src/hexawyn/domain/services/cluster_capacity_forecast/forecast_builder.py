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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_build_cluster_capacity_forecast__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_cluster_capacity_forecast__mutmut)
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


def x_build_cluster_capacity_forecast__mutmut_orig(
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


def x_build_cluster_capacity_forecast__mutmut_1(
    request: ClusterCapacityForecastRequest,
    raw_data: ClusterCapacityRawData,
    observed_at: date,
) -> ClusterCapacityForecastReport:
    cpu = None
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


def x_build_cluster_capacity_forecast__mutmut_2(
    request: ClusterCapacityForecastRequest,
    raw_data: ClusterCapacityRawData,
    observed_at: date,
) -> ClusterCapacityForecastReport:
    cpu = _build_resource_forecast(
        None, raw_data.cpu_daily_usage_cores, raw_data.total_allocatable_cpu_cores, observed_at
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


def x_build_cluster_capacity_forecast__mutmut_3(
    request: ClusterCapacityForecastRequest,
    raw_data: ClusterCapacityRawData,
    observed_at: date,
) -> ClusterCapacityForecastReport:
    cpu = _build_resource_forecast(
        "cpu", None, raw_data.total_allocatable_cpu_cores, observed_at
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


def x_build_cluster_capacity_forecast__mutmut_4(
    request: ClusterCapacityForecastRequest,
    raw_data: ClusterCapacityRawData,
    observed_at: date,
) -> ClusterCapacityForecastReport:
    cpu = _build_resource_forecast(
        "cpu", raw_data.cpu_daily_usage_cores, None, observed_at
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


def x_build_cluster_capacity_forecast__mutmut_5(
    request: ClusterCapacityForecastRequest,
    raw_data: ClusterCapacityRawData,
    observed_at: date,
) -> ClusterCapacityForecastReport:
    cpu = _build_resource_forecast(
        "cpu", raw_data.cpu_daily_usage_cores, raw_data.total_allocatable_cpu_cores, None
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


def x_build_cluster_capacity_forecast__mutmut_6(
    request: ClusterCapacityForecastRequest,
    raw_data: ClusterCapacityRawData,
    observed_at: date,
) -> ClusterCapacityForecastReport:
    cpu = _build_resource_forecast(
        raw_data.cpu_daily_usage_cores, raw_data.total_allocatable_cpu_cores, observed_at
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


def x_build_cluster_capacity_forecast__mutmut_7(
    request: ClusterCapacityForecastRequest,
    raw_data: ClusterCapacityRawData,
    observed_at: date,
) -> ClusterCapacityForecastReport:
    cpu = _build_resource_forecast(
        "cpu", raw_data.total_allocatable_cpu_cores, observed_at
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


def x_build_cluster_capacity_forecast__mutmut_8(
    request: ClusterCapacityForecastRequest,
    raw_data: ClusterCapacityRawData,
    observed_at: date,
) -> ClusterCapacityForecastReport:
    cpu = _build_resource_forecast(
        "cpu", raw_data.cpu_daily_usage_cores, observed_at
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


def x_build_cluster_capacity_forecast__mutmut_9(
    request: ClusterCapacityForecastRequest,
    raw_data: ClusterCapacityRawData,
    observed_at: date,
) -> ClusterCapacityForecastReport:
    cpu = _build_resource_forecast(
        "cpu", raw_data.cpu_daily_usage_cores, raw_data.total_allocatable_cpu_cores, )
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


def x_build_cluster_capacity_forecast__mutmut_10(
    request: ClusterCapacityForecastRequest,
    raw_data: ClusterCapacityRawData,
    observed_at: date,
) -> ClusterCapacityForecastReport:
    cpu = _build_resource_forecast(
        "XXcpuXX", raw_data.cpu_daily_usage_cores, raw_data.total_allocatable_cpu_cores, observed_at
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


def x_build_cluster_capacity_forecast__mutmut_11(
    request: ClusterCapacityForecastRequest,
    raw_data: ClusterCapacityRawData,
    observed_at: date,
) -> ClusterCapacityForecastReport:
    cpu = _build_resource_forecast(
        "CPU", raw_data.cpu_daily_usage_cores, raw_data.total_allocatable_cpu_cores, observed_at
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


def x_build_cluster_capacity_forecast__mutmut_12(
    request: ClusterCapacityForecastRequest,
    raw_data: ClusterCapacityRawData,
    observed_at: date,
) -> ClusterCapacityForecastReport:
    cpu = _build_resource_forecast(
        "cpu", raw_data.cpu_daily_usage_cores, raw_data.total_allocatable_cpu_cores, observed_at
    )
    memory = None

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


def x_build_cluster_capacity_forecast__mutmut_13(
    request: ClusterCapacityForecastRequest,
    raw_data: ClusterCapacityRawData,
    observed_at: date,
) -> ClusterCapacityForecastReport:
    cpu = _build_resource_forecast(
        "cpu", raw_data.cpu_daily_usage_cores, raw_data.total_allocatable_cpu_cores, observed_at
    )
    memory = _build_resource_forecast(
        None,
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


def x_build_cluster_capacity_forecast__mutmut_14(
    request: ClusterCapacityForecastRequest,
    raw_data: ClusterCapacityRawData,
    observed_at: date,
) -> ClusterCapacityForecastReport:
    cpu = _build_resource_forecast(
        "cpu", raw_data.cpu_daily_usage_cores, raw_data.total_allocatable_cpu_cores, observed_at
    )
    memory = _build_resource_forecast(
        "memory",
        None,
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


def x_build_cluster_capacity_forecast__mutmut_15(
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
        None,
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


def x_build_cluster_capacity_forecast__mutmut_16(
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
        None,
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


def x_build_cluster_capacity_forecast__mutmut_17(
    request: ClusterCapacityForecastRequest,
    raw_data: ClusterCapacityRawData,
    observed_at: date,
) -> ClusterCapacityForecastReport:
    cpu = _build_resource_forecast(
        "cpu", raw_data.cpu_daily_usage_cores, raw_data.total_allocatable_cpu_cores, observed_at
    )
    memory = _build_resource_forecast(
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


def x_build_cluster_capacity_forecast__mutmut_18(
    request: ClusterCapacityForecastRequest,
    raw_data: ClusterCapacityRawData,
    observed_at: date,
) -> ClusterCapacityForecastReport:
    cpu = _build_resource_forecast(
        "cpu", raw_data.cpu_daily_usage_cores, raw_data.total_allocatable_cpu_cores, observed_at
    )
    memory = _build_resource_forecast(
        "memory",
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


def x_build_cluster_capacity_forecast__mutmut_19(
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


def x_build_cluster_capacity_forecast__mutmut_20(
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


def x_build_cluster_capacity_forecast__mutmut_21(
    request: ClusterCapacityForecastRequest,
    raw_data: ClusterCapacityRawData,
    observed_at: date,
) -> ClusterCapacityForecastReport:
    cpu = _build_resource_forecast(
        "cpu", raw_data.cpu_daily_usage_cores, raw_data.total_allocatable_cpu_cores, observed_at
    )
    memory = _build_resource_forecast(
        "XXmemoryXX",
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


def x_build_cluster_capacity_forecast__mutmut_22(
    request: ClusterCapacityForecastRequest,
    raw_data: ClusterCapacityRawData,
    observed_at: date,
) -> ClusterCapacityForecastReport:
    cpu = _build_resource_forecast(
        "cpu", raw_data.cpu_daily_usage_cores, raw_data.total_allocatable_cpu_cores, observed_at
    )
    memory = _build_resource_forecast(
        "MEMORY",
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


def x_build_cluster_capacity_forecast__mutmut_23(
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

    critical_resource = None
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


def x_build_cluster_capacity_forecast__mutmut_24(
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

    critical_resource = _pick_critical_resource(None, memory)
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


def x_build_cluster_capacity_forecast__mutmut_25(
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

    critical_resource = _pick_critical_resource(cpu, None)
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


def x_build_cluster_capacity_forecast__mutmut_26(
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

    critical_resource = _pick_critical_resource(memory)
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


def x_build_cluster_capacity_forecast__mutmut_27(
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

    critical_resource = _pick_critical_resource(cpu, )
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


def x_build_cluster_capacity_forecast__mutmut_28(
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
    window_days_used = None

    return ClusterCapacityForecastReport(
        cpu=cpu,
        memory=memory,
        critical_resource=critical_resource,
        autoscaler_enabled=raw_data.autoscaler_enabled,
        recommendation=_build_recommendation(critical_resource, cpu, memory),
        confidence=_compute_confidence(window_days_used),
        window_days_used=window_days_used,
    )


def x_build_cluster_capacity_forecast__mutmut_29(
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
        None,
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


def x_build_cluster_capacity_forecast__mutmut_30(
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
        None,
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


def x_build_cluster_capacity_forecast__mutmut_31(
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


def x_build_cluster_capacity_forecast__mutmut_32(
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


def x_build_cluster_capacity_forecast__mutmut_33(
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
        len(raw_data.cpu_daily_usage_cores) and request.window_days,
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


def x_build_cluster_capacity_forecast__mutmut_34(
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
        len(raw_data.memory_daily_usage_gb) and request.window_days,
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


def x_build_cluster_capacity_forecast__mutmut_35(
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
        cpu=None,
        memory=memory,
        critical_resource=critical_resource,
        autoscaler_enabled=raw_data.autoscaler_enabled,
        recommendation=_build_recommendation(critical_resource, cpu, memory),
        confidence=_compute_confidence(window_days_used),
        window_days_used=window_days_used,
    )


def x_build_cluster_capacity_forecast__mutmut_36(
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
        memory=None,
        critical_resource=critical_resource,
        autoscaler_enabled=raw_data.autoscaler_enabled,
        recommendation=_build_recommendation(critical_resource, cpu, memory),
        confidence=_compute_confidence(window_days_used),
        window_days_used=window_days_used,
    )


def x_build_cluster_capacity_forecast__mutmut_37(
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
        critical_resource=None,
        autoscaler_enabled=raw_data.autoscaler_enabled,
        recommendation=_build_recommendation(critical_resource, cpu, memory),
        confidence=_compute_confidence(window_days_used),
        window_days_used=window_days_used,
    )


def x_build_cluster_capacity_forecast__mutmut_38(
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
        autoscaler_enabled=None,
        recommendation=_build_recommendation(critical_resource, cpu, memory),
        confidence=_compute_confidence(window_days_used),
        window_days_used=window_days_used,
    )


def x_build_cluster_capacity_forecast__mutmut_39(
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
        recommendation=None,
        confidence=_compute_confidence(window_days_used),
        window_days_used=window_days_used,
    )


def x_build_cluster_capacity_forecast__mutmut_40(
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
        confidence=None,
        window_days_used=window_days_used,
    )


def x_build_cluster_capacity_forecast__mutmut_41(
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
        window_days_used=None,
    )


def x_build_cluster_capacity_forecast__mutmut_42(
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
        memory=memory,
        critical_resource=critical_resource,
        autoscaler_enabled=raw_data.autoscaler_enabled,
        recommendation=_build_recommendation(critical_resource, cpu, memory),
        confidence=_compute_confidence(window_days_used),
        window_days_used=window_days_used,
    )


def x_build_cluster_capacity_forecast__mutmut_43(
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
        critical_resource=critical_resource,
        autoscaler_enabled=raw_data.autoscaler_enabled,
        recommendation=_build_recommendation(critical_resource, cpu, memory),
        confidence=_compute_confidence(window_days_used),
        window_days_used=window_days_used,
    )


def x_build_cluster_capacity_forecast__mutmut_44(
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
        autoscaler_enabled=raw_data.autoscaler_enabled,
        recommendation=_build_recommendation(critical_resource, cpu, memory),
        confidence=_compute_confidence(window_days_used),
        window_days_used=window_days_used,
    )


def x_build_cluster_capacity_forecast__mutmut_45(
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
        recommendation=_build_recommendation(critical_resource, cpu, memory),
        confidence=_compute_confidence(window_days_used),
        window_days_used=window_days_used,
    )


def x_build_cluster_capacity_forecast__mutmut_46(
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
        confidence=_compute_confidence(window_days_used),
        window_days_used=window_days_used,
    )


def x_build_cluster_capacity_forecast__mutmut_47(
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
        window_days_used=window_days_used,
    )


def x_build_cluster_capacity_forecast__mutmut_48(
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
        )


def x_build_cluster_capacity_forecast__mutmut_49(
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
        recommendation=_build_recommendation(None, cpu, memory),
        confidence=_compute_confidence(window_days_used),
        window_days_used=window_days_used,
    )


def x_build_cluster_capacity_forecast__mutmut_50(
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
        recommendation=_build_recommendation(critical_resource, None, memory),
        confidence=_compute_confidence(window_days_used),
        window_days_used=window_days_used,
    )


def x_build_cluster_capacity_forecast__mutmut_51(
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
        recommendation=_build_recommendation(critical_resource, cpu, None),
        confidence=_compute_confidence(window_days_used),
        window_days_used=window_days_used,
    )


def x_build_cluster_capacity_forecast__mutmut_52(
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
        recommendation=_build_recommendation(cpu, memory),
        confidence=_compute_confidence(window_days_used),
        window_days_used=window_days_used,
    )


def x_build_cluster_capacity_forecast__mutmut_53(
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
        recommendation=_build_recommendation(critical_resource, memory),
        confidence=_compute_confidence(window_days_used),
        window_days_used=window_days_used,
    )


def x_build_cluster_capacity_forecast__mutmut_54(
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
        recommendation=_build_recommendation(critical_resource, cpu, ),
        confidence=_compute_confidence(window_days_used),
        window_days_used=window_days_used,
    )


def x_build_cluster_capacity_forecast__mutmut_55(
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
        confidence=_compute_confidence(None),
        window_days_used=window_days_used,
    )

mutants_x_build_cluster_capacity_forecast__mutmut['_mutmut_orig'] = x_build_cluster_capacity_forecast__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_1'] = x_build_cluster_capacity_forecast__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_2'] = x_build_cluster_capacity_forecast__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_3'] = x_build_cluster_capacity_forecast__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_4'] = x_build_cluster_capacity_forecast__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_5'] = x_build_cluster_capacity_forecast__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_6'] = x_build_cluster_capacity_forecast__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_7'] = x_build_cluster_capacity_forecast__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_8'] = x_build_cluster_capacity_forecast__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_9'] = x_build_cluster_capacity_forecast__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_10'] = x_build_cluster_capacity_forecast__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_11'] = x_build_cluster_capacity_forecast__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_12'] = x_build_cluster_capacity_forecast__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_13'] = x_build_cluster_capacity_forecast__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_14'] = x_build_cluster_capacity_forecast__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_15'] = x_build_cluster_capacity_forecast__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_16'] = x_build_cluster_capacity_forecast__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_17'] = x_build_cluster_capacity_forecast__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_18'] = x_build_cluster_capacity_forecast__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_19'] = x_build_cluster_capacity_forecast__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_20'] = x_build_cluster_capacity_forecast__mutmut_20 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_21'] = x_build_cluster_capacity_forecast__mutmut_21 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_22'] = x_build_cluster_capacity_forecast__mutmut_22 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_23'] = x_build_cluster_capacity_forecast__mutmut_23 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_24'] = x_build_cluster_capacity_forecast__mutmut_24 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_25'] = x_build_cluster_capacity_forecast__mutmut_25 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_26'] = x_build_cluster_capacity_forecast__mutmut_26 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_27'] = x_build_cluster_capacity_forecast__mutmut_27 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_28'] = x_build_cluster_capacity_forecast__mutmut_28 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_29'] = x_build_cluster_capacity_forecast__mutmut_29 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_30'] = x_build_cluster_capacity_forecast__mutmut_30 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_31'] = x_build_cluster_capacity_forecast__mutmut_31 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_32'] = x_build_cluster_capacity_forecast__mutmut_32 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_33'] = x_build_cluster_capacity_forecast__mutmut_33 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_34'] = x_build_cluster_capacity_forecast__mutmut_34 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_35'] = x_build_cluster_capacity_forecast__mutmut_35 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_36'] = x_build_cluster_capacity_forecast__mutmut_36 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_37'] = x_build_cluster_capacity_forecast__mutmut_37 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_38'] = x_build_cluster_capacity_forecast__mutmut_38 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_39'] = x_build_cluster_capacity_forecast__mutmut_39 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_40'] = x_build_cluster_capacity_forecast__mutmut_40 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_41'] = x_build_cluster_capacity_forecast__mutmut_41 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_42'] = x_build_cluster_capacity_forecast__mutmut_42 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_43'] = x_build_cluster_capacity_forecast__mutmut_43 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_44'] = x_build_cluster_capacity_forecast__mutmut_44 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_45'] = x_build_cluster_capacity_forecast__mutmut_45 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_46'] = x_build_cluster_capacity_forecast__mutmut_46 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_47'] = x_build_cluster_capacity_forecast__mutmut_47 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_48'] = x_build_cluster_capacity_forecast__mutmut_48 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_49'] = x_build_cluster_capacity_forecast__mutmut_49 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_50'] = x_build_cluster_capacity_forecast__mutmut_50 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_51'] = x_build_cluster_capacity_forecast__mutmut_51 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_52'] = x_build_cluster_capacity_forecast__mutmut_52 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_53'] = x_build_cluster_capacity_forecast__mutmut_53 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_54'] = x_build_cluster_capacity_forecast__mutmut_54 # type: ignore # mutmut generated
mutants_x_build_cluster_capacity_forecast__mutmut['x_build_cluster_capacity_forecast__mutmut_55'] = x_build_cluster_capacity_forecast__mutmut_55 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__build_resource_forecast__mutmut)
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


def x__build_resource_forecast__mutmut_orig(
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


def x__build_resource_forecast__mutmut_1(
    resource_type: ResourceType, daily_values: list[float], ceiling: float, observed_at: date
) -> ResourceForecast:
    growth = None
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


def x__build_resource_forecast__mutmut_2(
    resource_type: ResourceType, daily_values: list[float], ceiling: float, observed_at: date
) -> ResourceForecast:
    growth = compute_growth_rate(None)
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


def x__build_resource_forecast__mutmut_3(
    resource_type: ResourceType, daily_values: list[float], ceiling: float, observed_at: date
) -> ResourceForecast:
    growth = compute_growth_rate(daily_values)
    current = None
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


def x__build_resource_forecast__mutmut_4(
    resource_type: ResourceType, daily_values: list[float], ceiling: float, observed_at: date
) -> ResourceForecast:
    growth = compute_growth_rate(daily_values)
    current = daily_values[+1] if daily_values else 0.0
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


def x__build_resource_forecast__mutmut_5(
    resource_type: ResourceType, daily_values: list[float], ceiling: float, observed_at: date
) -> ResourceForecast:
    growth = compute_growth_rate(daily_values)
    current = daily_values[-2] if daily_values else 0.0
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


def x__build_resource_forecast__mutmut_6(
    resource_type: ResourceType, daily_values: list[float], ceiling: float, observed_at: date
) -> ResourceForecast:
    growth = compute_growth_rate(daily_values)
    current = daily_values[-1] if daily_values else 1.0
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


def x__build_resource_forecast__mutmut_7(
    resource_type: ResourceType, daily_values: list[float], ceiling: float, observed_at: date
) -> ResourceForecast:
    growth = compute_growth_rate(daily_values)
    current = daily_values[-1] if daily_values else 0.0
    utilization_percent = None
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


def x__build_resource_forecast__mutmut_8(
    resource_type: ResourceType, daily_values: list[float], ceiling: float, observed_at: date
) -> ResourceForecast:
    growth = compute_growth_rate(daily_values)
    current = daily_values[-1] if daily_values else 0.0
    utilization_percent = round(None, 2) if ceiling > 0 else 0.0
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


def x__build_resource_forecast__mutmut_9(
    resource_type: ResourceType, daily_values: list[float], ceiling: float, observed_at: date
) -> ResourceForecast:
    growth = compute_growth_rate(daily_values)
    current = daily_values[-1] if daily_values else 0.0
    utilization_percent = round(current / ceiling * 100, None) if ceiling > 0 else 0.0
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


def x__build_resource_forecast__mutmut_10(
    resource_type: ResourceType, daily_values: list[float], ceiling: float, observed_at: date
) -> ResourceForecast:
    growth = compute_growth_rate(daily_values)
    current = daily_values[-1] if daily_values else 0.0
    utilization_percent = round(2) if ceiling > 0 else 0.0
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


def x__build_resource_forecast__mutmut_11(
    resource_type: ResourceType, daily_values: list[float], ceiling: float, observed_at: date
) -> ResourceForecast:
    growth = compute_growth_rate(daily_values)
    current = daily_values[-1] if daily_values else 0.0
    utilization_percent = round(current / ceiling * 100, ) if ceiling > 0 else 0.0
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


def x__build_resource_forecast__mutmut_12(
    resource_type: ResourceType, daily_values: list[float], ceiling: float, observed_at: date
) -> ResourceForecast:
    growth = compute_growth_rate(daily_values)
    current = daily_values[-1] if daily_values else 0.0
    utilization_percent = round(current / ceiling / 100, 2) if ceiling > 0 else 0.0
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


def x__build_resource_forecast__mutmut_13(
    resource_type: ResourceType, daily_values: list[float], ceiling: float, observed_at: date
) -> ResourceForecast:
    growth = compute_growth_rate(daily_values)
    current = daily_values[-1] if daily_values else 0.0
    utilization_percent = round(current * ceiling * 100, 2) if ceiling > 0 else 0.0
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


def x__build_resource_forecast__mutmut_14(
    resource_type: ResourceType, daily_values: list[float], ceiling: float, observed_at: date
) -> ResourceForecast:
    growth = compute_growth_rate(daily_values)
    current = daily_values[-1] if daily_values else 0.0
    utilization_percent = round(current / ceiling * 101, 2) if ceiling > 0 else 0.0
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


def x__build_resource_forecast__mutmut_15(
    resource_type: ResourceType, daily_values: list[float], ceiling: float, observed_at: date
) -> ResourceForecast:
    growth = compute_growth_rate(daily_values)
    current = daily_values[-1] if daily_values else 0.0
    utilization_percent = round(current / ceiling * 100, 3) if ceiling > 0 else 0.0
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


def x__build_resource_forecast__mutmut_16(
    resource_type: ResourceType, daily_values: list[float], ceiling: float, observed_at: date
) -> ResourceForecast:
    growth = compute_growth_rate(daily_values)
    current = daily_values[-1] if daily_values else 0.0
    utilization_percent = round(current / ceiling * 100, 2) if ceiling >= 0 else 0.0
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


def x__build_resource_forecast__mutmut_17(
    resource_type: ResourceType, daily_values: list[float], ceiling: float, observed_at: date
) -> ResourceForecast:
    growth = compute_growth_rate(daily_values)
    current = daily_values[-1] if daily_values else 0.0
    utilization_percent = round(current / ceiling * 100, 2) if ceiling > 1 else 0.0
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


def x__build_resource_forecast__mutmut_18(
    resource_type: ResourceType, daily_values: list[float], ceiling: float, observed_at: date
) -> ResourceForecast:
    growth = compute_growth_rate(daily_values)
    current = daily_values[-1] if daily_values else 0.0
    utilization_percent = round(current / ceiling * 100, 2) if ceiling > 0 else 1.0
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


def x__build_resource_forecast__mutmut_19(
    resource_type: ResourceType, daily_values: list[float], ceiling: float, observed_at: date
) -> ResourceForecast:
    growth = compute_growth_rate(daily_values)
    current = daily_values[-1] if daily_values else 0.0
    utilization_percent = round(current / ceiling * 100, 2) if ceiling > 0 else 0.0
    saturation = None

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


def x__build_resource_forecast__mutmut_20(
    resource_type: ResourceType, daily_values: list[float], ceiling: float, observed_at: date
) -> ResourceForecast:
    growth = compute_growth_rate(daily_values)
    current = daily_values[-1] if daily_values else 0.0
    utilization_percent = round(current / ceiling * 100, 2) if ceiling > 0 else 0.0
    saturation = predict_saturation(
        current=None,
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


def x__build_resource_forecast__mutmut_21(
    resource_type: ResourceType, daily_values: list[float], ceiling: float, observed_at: date
) -> ResourceForecast:
    growth = compute_growth_rate(daily_values)
    current = daily_values[-1] if daily_values else 0.0
    utilization_percent = round(current / ceiling * 100, 2) if ceiling > 0 else 0.0
    saturation = predict_saturation(
        current=current,
        ceiling=None,
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


def x__build_resource_forecast__mutmut_22(
    resource_type: ResourceType, daily_values: list[float], ceiling: float, observed_at: date
) -> ResourceForecast:
    growth = compute_growth_rate(daily_values)
    current = daily_values[-1] if daily_values else 0.0
    utilization_percent = round(current / ceiling * 100, 2) if ceiling > 0 else 0.0
    saturation = predict_saturation(
        current=current,
        ceiling=ceiling,
        growth_rate_per_day=None,
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


def x__build_resource_forecast__mutmut_23(
    resource_type: ResourceType, daily_values: list[float], ceiling: float, observed_at: date
) -> ResourceForecast:
    growth = compute_growth_rate(daily_values)
    current = daily_values[-1] if daily_values else 0.0
    utilization_percent = round(current / ceiling * 100, 2) if ceiling > 0 else 0.0
    saturation = predict_saturation(
        current=current,
        ceiling=ceiling,
        growth_rate_per_day=growth.slope_per_day,
        observed_at=None,
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


def x__build_resource_forecast__mutmut_24(
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
        max_horizon_days=None,
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


def x__build_resource_forecast__mutmut_25(
    resource_type: ResourceType, daily_values: list[float], ceiling: float, observed_at: date
) -> ResourceForecast:
    growth = compute_growth_rate(daily_values)
    current = daily_values[-1] if daily_values else 0.0
    utilization_percent = round(current / ceiling * 100, 2) if ceiling > 0 else 0.0
    saturation = predict_saturation(
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


def x__build_resource_forecast__mutmut_26(
    resource_type: ResourceType, daily_values: list[float], ceiling: float, observed_at: date
) -> ResourceForecast:
    growth = compute_growth_rate(daily_values)
    current = daily_values[-1] if daily_values else 0.0
    utilization_percent = round(current / ceiling * 100, 2) if ceiling > 0 else 0.0
    saturation = predict_saturation(
        current=current,
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


def x__build_resource_forecast__mutmut_27(
    resource_type: ResourceType, daily_values: list[float], ceiling: float, observed_at: date
) -> ResourceForecast:
    growth = compute_growth_rate(daily_values)
    current = daily_values[-1] if daily_values else 0.0
    utilization_percent = round(current / ceiling * 100, 2) if ceiling > 0 else 0.0
    saturation = predict_saturation(
        current=current,
        ceiling=ceiling,
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


def x__build_resource_forecast__mutmut_28(
    resource_type: ResourceType, daily_values: list[float], ceiling: float, observed_at: date
) -> ResourceForecast:
    growth = compute_growth_rate(daily_values)
    current = daily_values[-1] if daily_values else 0.0
    utilization_percent = round(current / ceiling * 100, 2) if ceiling > 0 else 0.0
    saturation = predict_saturation(
        current=current,
        ceiling=ceiling,
        growth_rate_per_day=growth.slope_per_day,
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


def x__build_resource_forecast__mutmut_29(
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


def x__build_resource_forecast__mutmut_30(
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
        resource_type=None,
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


def x__build_resource_forecast__mutmut_31(
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
        current_value=None,
        ceiling=ceiling,
        current_utilization_percent=utilization_percent,
        growth_rate_per_day=growth.slope_per_day,
        days_to_saturation=saturation.days_to_saturation,
        saturation_date=saturation.saturation_date,
        capacity_jump_detected=growth.capacity_jump_detected,
        spike_caveat=growth.spike_caveat,
        capped_horizon=saturation.capped_horizon,
    )


def x__build_resource_forecast__mutmut_32(
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
        ceiling=None,
        current_utilization_percent=utilization_percent,
        growth_rate_per_day=growth.slope_per_day,
        days_to_saturation=saturation.days_to_saturation,
        saturation_date=saturation.saturation_date,
        capacity_jump_detected=growth.capacity_jump_detected,
        spike_caveat=growth.spike_caveat,
        capped_horizon=saturation.capped_horizon,
    )


def x__build_resource_forecast__mutmut_33(
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
        current_utilization_percent=None,
        growth_rate_per_day=growth.slope_per_day,
        days_to_saturation=saturation.days_to_saturation,
        saturation_date=saturation.saturation_date,
        capacity_jump_detected=growth.capacity_jump_detected,
        spike_caveat=growth.spike_caveat,
        capped_horizon=saturation.capped_horizon,
    )


def x__build_resource_forecast__mutmut_34(
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
        growth_rate_per_day=None,
        days_to_saturation=saturation.days_to_saturation,
        saturation_date=saturation.saturation_date,
        capacity_jump_detected=growth.capacity_jump_detected,
        spike_caveat=growth.spike_caveat,
        capped_horizon=saturation.capped_horizon,
    )


def x__build_resource_forecast__mutmut_35(
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
        days_to_saturation=None,
        saturation_date=saturation.saturation_date,
        capacity_jump_detected=growth.capacity_jump_detected,
        spike_caveat=growth.spike_caveat,
        capped_horizon=saturation.capped_horizon,
    )


def x__build_resource_forecast__mutmut_36(
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
        saturation_date=None,
        capacity_jump_detected=growth.capacity_jump_detected,
        spike_caveat=growth.spike_caveat,
        capped_horizon=saturation.capped_horizon,
    )


def x__build_resource_forecast__mutmut_37(
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
        capacity_jump_detected=None,
        spike_caveat=growth.spike_caveat,
        capped_horizon=saturation.capped_horizon,
    )


def x__build_resource_forecast__mutmut_38(
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
        spike_caveat=None,
        capped_horizon=saturation.capped_horizon,
    )


def x__build_resource_forecast__mutmut_39(
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
        capped_horizon=None,
    )


def x__build_resource_forecast__mutmut_40(
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


def x__build_resource_forecast__mutmut_41(
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
        ceiling=ceiling,
        current_utilization_percent=utilization_percent,
        growth_rate_per_day=growth.slope_per_day,
        days_to_saturation=saturation.days_to_saturation,
        saturation_date=saturation.saturation_date,
        capacity_jump_detected=growth.capacity_jump_detected,
        spike_caveat=growth.spike_caveat,
        capped_horizon=saturation.capped_horizon,
    )


def x__build_resource_forecast__mutmut_42(
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
        current_utilization_percent=utilization_percent,
        growth_rate_per_day=growth.slope_per_day,
        days_to_saturation=saturation.days_to_saturation,
        saturation_date=saturation.saturation_date,
        capacity_jump_detected=growth.capacity_jump_detected,
        spike_caveat=growth.spike_caveat,
        capped_horizon=saturation.capped_horizon,
    )


def x__build_resource_forecast__mutmut_43(
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
        growth_rate_per_day=growth.slope_per_day,
        days_to_saturation=saturation.days_to_saturation,
        saturation_date=saturation.saturation_date,
        capacity_jump_detected=growth.capacity_jump_detected,
        spike_caveat=growth.spike_caveat,
        capped_horizon=saturation.capped_horizon,
    )


def x__build_resource_forecast__mutmut_44(
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
        days_to_saturation=saturation.days_to_saturation,
        saturation_date=saturation.saturation_date,
        capacity_jump_detected=growth.capacity_jump_detected,
        spike_caveat=growth.spike_caveat,
        capped_horizon=saturation.capped_horizon,
    )


def x__build_resource_forecast__mutmut_45(
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
        saturation_date=saturation.saturation_date,
        capacity_jump_detected=growth.capacity_jump_detected,
        spike_caveat=growth.spike_caveat,
        capped_horizon=saturation.capped_horizon,
    )


def x__build_resource_forecast__mutmut_46(
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
        capacity_jump_detected=growth.capacity_jump_detected,
        spike_caveat=growth.spike_caveat,
        capped_horizon=saturation.capped_horizon,
    )


def x__build_resource_forecast__mutmut_47(
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
        spike_caveat=growth.spike_caveat,
        capped_horizon=saturation.capped_horizon,
    )


def x__build_resource_forecast__mutmut_48(
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
        capped_horizon=saturation.capped_horizon,
    )


def x__build_resource_forecast__mutmut_49(
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
        )

mutants_x__build_resource_forecast__mutmut['_mutmut_orig'] = x__build_resource_forecast__mutmut_orig # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_1'] = x__build_resource_forecast__mutmut_1 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_2'] = x__build_resource_forecast__mutmut_2 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_3'] = x__build_resource_forecast__mutmut_3 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_4'] = x__build_resource_forecast__mutmut_4 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_5'] = x__build_resource_forecast__mutmut_5 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_6'] = x__build_resource_forecast__mutmut_6 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_7'] = x__build_resource_forecast__mutmut_7 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_8'] = x__build_resource_forecast__mutmut_8 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_9'] = x__build_resource_forecast__mutmut_9 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_10'] = x__build_resource_forecast__mutmut_10 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_11'] = x__build_resource_forecast__mutmut_11 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_12'] = x__build_resource_forecast__mutmut_12 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_13'] = x__build_resource_forecast__mutmut_13 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_14'] = x__build_resource_forecast__mutmut_14 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_15'] = x__build_resource_forecast__mutmut_15 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_16'] = x__build_resource_forecast__mutmut_16 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_17'] = x__build_resource_forecast__mutmut_17 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_18'] = x__build_resource_forecast__mutmut_18 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_19'] = x__build_resource_forecast__mutmut_19 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_20'] = x__build_resource_forecast__mutmut_20 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_21'] = x__build_resource_forecast__mutmut_21 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_22'] = x__build_resource_forecast__mutmut_22 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_23'] = x__build_resource_forecast__mutmut_23 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_24'] = x__build_resource_forecast__mutmut_24 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_25'] = x__build_resource_forecast__mutmut_25 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_26'] = x__build_resource_forecast__mutmut_26 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_27'] = x__build_resource_forecast__mutmut_27 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_28'] = x__build_resource_forecast__mutmut_28 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_29'] = x__build_resource_forecast__mutmut_29 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_30'] = x__build_resource_forecast__mutmut_30 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_31'] = x__build_resource_forecast__mutmut_31 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_32'] = x__build_resource_forecast__mutmut_32 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_33'] = x__build_resource_forecast__mutmut_33 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_34'] = x__build_resource_forecast__mutmut_34 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_35'] = x__build_resource_forecast__mutmut_35 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_36'] = x__build_resource_forecast__mutmut_36 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_37'] = x__build_resource_forecast__mutmut_37 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_38'] = x__build_resource_forecast__mutmut_38 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_39'] = x__build_resource_forecast__mutmut_39 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_40'] = x__build_resource_forecast__mutmut_40 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_41'] = x__build_resource_forecast__mutmut_41 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_42'] = x__build_resource_forecast__mutmut_42 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_43'] = x__build_resource_forecast__mutmut_43 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_44'] = x__build_resource_forecast__mutmut_44 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_45'] = x__build_resource_forecast__mutmut_45 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_46'] = x__build_resource_forecast__mutmut_46 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_47'] = x__build_resource_forecast__mutmut_47 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_48'] = x__build_resource_forecast__mutmut_48 # type: ignore # mutmut generated
mutants_x__build_resource_forecast__mutmut['x__build_resource_forecast__mutmut_49'] = x__build_resource_forecast__mutmut_49 # type: ignore # mutmut generated
mutants_x__pick_critical_resource__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__pick_critical_resource__mutmut)
def _pick_critical_resource(cpu: ResourceForecast, memory: ResourceForecast) -> CriticalResource:
    if cpu.days_to_saturation is None and memory.days_to_saturation is None:
        return "None"
    if cpu.days_to_saturation is None:
        return "Memory"
    if memory.days_to_saturation is None:
        return "CPU"
    return "CPU" if cpu.days_to_saturation <= memory.days_to_saturation else "Memory"


def x__pick_critical_resource__mutmut_orig(cpu: ResourceForecast, memory: ResourceForecast) -> CriticalResource:
    if cpu.days_to_saturation is None and memory.days_to_saturation is None:
        return "None"
    if cpu.days_to_saturation is None:
        return "Memory"
    if memory.days_to_saturation is None:
        return "CPU"
    return "CPU" if cpu.days_to_saturation <= memory.days_to_saturation else "Memory"


def x__pick_critical_resource__mutmut_1(cpu: ResourceForecast, memory: ResourceForecast) -> CriticalResource:
    if cpu.days_to_saturation is None or memory.days_to_saturation is None:
        return "None"
    if cpu.days_to_saturation is None:
        return "Memory"
    if memory.days_to_saturation is None:
        return "CPU"
    return "CPU" if cpu.days_to_saturation <= memory.days_to_saturation else "Memory"


def x__pick_critical_resource__mutmut_2(cpu: ResourceForecast, memory: ResourceForecast) -> CriticalResource:
    if cpu.days_to_saturation is not None and memory.days_to_saturation is None:
        return "None"
    if cpu.days_to_saturation is None:
        return "Memory"
    if memory.days_to_saturation is None:
        return "CPU"
    return "CPU" if cpu.days_to_saturation <= memory.days_to_saturation else "Memory"


def x__pick_critical_resource__mutmut_3(cpu: ResourceForecast, memory: ResourceForecast) -> CriticalResource:
    if cpu.days_to_saturation is None and memory.days_to_saturation is not None:
        return "None"
    if cpu.days_to_saturation is None:
        return "Memory"
    if memory.days_to_saturation is None:
        return "CPU"
    return "CPU" if cpu.days_to_saturation <= memory.days_to_saturation else "Memory"


def x__pick_critical_resource__mutmut_4(cpu: ResourceForecast, memory: ResourceForecast) -> CriticalResource:
    if cpu.days_to_saturation is None and memory.days_to_saturation is None:
        return "XXNoneXX"
    if cpu.days_to_saturation is None:
        return "Memory"
    if memory.days_to_saturation is None:
        return "CPU"
    return "CPU" if cpu.days_to_saturation <= memory.days_to_saturation else "Memory"


def x__pick_critical_resource__mutmut_5(cpu: ResourceForecast, memory: ResourceForecast) -> CriticalResource:
    if cpu.days_to_saturation is None and memory.days_to_saturation is None:
        return "none"
    if cpu.days_to_saturation is None:
        return "Memory"
    if memory.days_to_saturation is None:
        return "CPU"
    return "CPU" if cpu.days_to_saturation <= memory.days_to_saturation else "Memory"


def x__pick_critical_resource__mutmut_6(cpu: ResourceForecast, memory: ResourceForecast) -> CriticalResource:
    if cpu.days_to_saturation is None and memory.days_to_saturation is None:
        return "NONE"
    if cpu.days_to_saturation is None:
        return "Memory"
    if memory.days_to_saturation is None:
        return "CPU"
    return "CPU" if cpu.days_to_saturation <= memory.days_to_saturation else "Memory"


def x__pick_critical_resource__mutmut_7(cpu: ResourceForecast, memory: ResourceForecast) -> CriticalResource:
    if cpu.days_to_saturation is None and memory.days_to_saturation is None:
        return "None"
    if cpu.days_to_saturation is not None:
        return "Memory"
    if memory.days_to_saturation is None:
        return "CPU"
    return "CPU" if cpu.days_to_saturation <= memory.days_to_saturation else "Memory"


def x__pick_critical_resource__mutmut_8(cpu: ResourceForecast, memory: ResourceForecast) -> CriticalResource:
    if cpu.days_to_saturation is None and memory.days_to_saturation is None:
        return "None"
    if cpu.days_to_saturation is None:
        return "XXMemoryXX"
    if memory.days_to_saturation is None:
        return "CPU"
    return "CPU" if cpu.days_to_saturation <= memory.days_to_saturation else "Memory"


def x__pick_critical_resource__mutmut_9(cpu: ResourceForecast, memory: ResourceForecast) -> CriticalResource:
    if cpu.days_to_saturation is None and memory.days_to_saturation is None:
        return "None"
    if cpu.days_to_saturation is None:
        return "memory"
    if memory.days_to_saturation is None:
        return "CPU"
    return "CPU" if cpu.days_to_saturation <= memory.days_to_saturation else "Memory"


def x__pick_critical_resource__mutmut_10(cpu: ResourceForecast, memory: ResourceForecast) -> CriticalResource:
    if cpu.days_to_saturation is None and memory.days_to_saturation is None:
        return "None"
    if cpu.days_to_saturation is None:
        return "MEMORY"
    if memory.days_to_saturation is None:
        return "CPU"
    return "CPU" if cpu.days_to_saturation <= memory.days_to_saturation else "Memory"


def x__pick_critical_resource__mutmut_11(cpu: ResourceForecast, memory: ResourceForecast) -> CriticalResource:
    if cpu.days_to_saturation is None and memory.days_to_saturation is None:
        return "None"
    if cpu.days_to_saturation is None:
        return "Memory"
    if memory.days_to_saturation is not None:
        return "CPU"
    return "CPU" if cpu.days_to_saturation <= memory.days_to_saturation else "Memory"


def x__pick_critical_resource__mutmut_12(cpu: ResourceForecast, memory: ResourceForecast) -> CriticalResource:
    if cpu.days_to_saturation is None and memory.days_to_saturation is None:
        return "None"
    if cpu.days_to_saturation is None:
        return "Memory"
    if memory.days_to_saturation is None:
        return "XXCPUXX"
    return "CPU" if cpu.days_to_saturation <= memory.days_to_saturation else "Memory"


def x__pick_critical_resource__mutmut_13(cpu: ResourceForecast, memory: ResourceForecast) -> CriticalResource:
    if cpu.days_to_saturation is None and memory.days_to_saturation is None:
        return "None"
    if cpu.days_to_saturation is None:
        return "Memory"
    if memory.days_to_saturation is None:
        return "cpu"
    return "CPU" if cpu.days_to_saturation <= memory.days_to_saturation else "Memory"


def x__pick_critical_resource__mutmut_14(cpu: ResourceForecast, memory: ResourceForecast) -> CriticalResource:
    if cpu.days_to_saturation is None and memory.days_to_saturation is None:
        return "None"
    if cpu.days_to_saturation is None:
        return "Memory"
    if memory.days_to_saturation is None:
        return "CPU"
    return "XXCPUXX" if cpu.days_to_saturation <= memory.days_to_saturation else "Memory"


def x__pick_critical_resource__mutmut_15(cpu: ResourceForecast, memory: ResourceForecast) -> CriticalResource:
    if cpu.days_to_saturation is None and memory.days_to_saturation is None:
        return "None"
    if cpu.days_to_saturation is None:
        return "Memory"
    if memory.days_to_saturation is None:
        return "CPU"
    return "cpu" if cpu.days_to_saturation <= memory.days_to_saturation else "Memory"


def x__pick_critical_resource__mutmut_16(cpu: ResourceForecast, memory: ResourceForecast) -> CriticalResource:
    if cpu.days_to_saturation is None and memory.days_to_saturation is None:
        return "None"
    if cpu.days_to_saturation is None:
        return "Memory"
    if memory.days_to_saturation is None:
        return "CPU"
    return "CPU" if cpu.days_to_saturation < memory.days_to_saturation else "Memory"


def x__pick_critical_resource__mutmut_17(cpu: ResourceForecast, memory: ResourceForecast) -> CriticalResource:
    if cpu.days_to_saturation is None and memory.days_to_saturation is None:
        return "None"
    if cpu.days_to_saturation is None:
        return "Memory"
    if memory.days_to_saturation is None:
        return "CPU"
    return "CPU" if cpu.days_to_saturation <= memory.days_to_saturation else "XXMemoryXX"


def x__pick_critical_resource__mutmut_18(cpu: ResourceForecast, memory: ResourceForecast) -> CriticalResource:
    if cpu.days_to_saturation is None and memory.days_to_saturation is None:
        return "None"
    if cpu.days_to_saturation is None:
        return "Memory"
    if memory.days_to_saturation is None:
        return "CPU"
    return "CPU" if cpu.days_to_saturation <= memory.days_to_saturation else "memory"


def x__pick_critical_resource__mutmut_19(cpu: ResourceForecast, memory: ResourceForecast) -> CriticalResource:
    if cpu.days_to_saturation is None and memory.days_to_saturation is None:
        return "None"
    if cpu.days_to_saturation is None:
        return "Memory"
    if memory.days_to_saturation is None:
        return "CPU"
    return "CPU" if cpu.days_to_saturation <= memory.days_to_saturation else "MEMORY"

mutants_x__pick_critical_resource__mutmut['_mutmut_orig'] = x__pick_critical_resource__mutmut_orig # type: ignore # mutmut generated
mutants_x__pick_critical_resource__mutmut['x__pick_critical_resource__mutmut_1'] = x__pick_critical_resource__mutmut_1 # type: ignore # mutmut generated
mutants_x__pick_critical_resource__mutmut['x__pick_critical_resource__mutmut_2'] = x__pick_critical_resource__mutmut_2 # type: ignore # mutmut generated
mutants_x__pick_critical_resource__mutmut['x__pick_critical_resource__mutmut_3'] = x__pick_critical_resource__mutmut_3 # type: ignore # mutmut generated
mutants_x__pick_critical_resource__mutmut['x__pick_critical_resource__mutmut_4'] = x__pick_critical_resource__mutmut_4 # type: ignore # mutmut generated
mutants_x__pick_critical_resource__mutmut['x__pick_critical_resource__mutmut_5'] = x__pick_critical_resource__mutmut_5 # type: ignore # mutmut generated
mutants_x__pick_critical_resource__mutmut['x__pick_critical_resource__mutmut_6'] = x__pick_critical_resource__mutmut_6 # type: ignore # mutmut generated
mutants_x__pick_critical_resource__mutmut['x__pick_critical_resource__mutmut_7'] = x__pick_critical_resource__mutmut_7 # type: ignore # mutmut generated
mutants_x__pick_critical_resource__mutmut['x__pick_critical_resource__mutmut_8'] = x__pick_critical_resource__mutmut_8 # type: ignore # mutmut generated
mutants_x__pick_critical_resource__mutmut['x__pick_critical_resource__mutmut_9'] = x__pick_critical_resource__mutmut_9 # type: ignore # mutmut generated
mutants_x__pick_critical_resource__mutmut['x__pick_critical_resource__mutmut_10'] = x__pick_critical_resource__mutmut_10 # type: ignore # mutmut generated
mutants_x__pick_critical_resource__mutmut['x__pick_critical_resource__mutmut_11'] = x__pick_critical_resource__mutmut_11 # type: ignore # mutmut generated
mutants_x__pick_critical_resource__mutmut['x__pick_critical_resource__mutmut_12'] = x__pick_critical_resource__mutmut_12 # type: ignore # mutmut generated
mutants_x__pick_critical_resource__mutmut['x__pick_critical_resource__mutmut_13'] = x__pick_critical_resource__mutmut_13 # type: ignore # mutmut generated
mutants_x__pick_critical_resource__mutmut['x__pick_critical_resource__mutmut_14'] = x__pick_critical_resource__mutmut_14 # type: ignore # mutmut generated
mutants_x__pick_critical_resource__mutmut['x__pick_critical_resource__mutmut_15'] = x__pick_critical_resource__mutmut_15 # type: ignore # mutmut generated
mutants_x__pick_critical_resource__mutmut['x__pick_critical_resource__mutmut_16'] = x__pick_critical_resource__mutmut_16 # type: ignore # mutmut generated
mutants_x__pick_critical_resource__mutmut['x__pick_critical_resource__mutmut_17'] = x__pick_critical_resource__mutmut_17 # type: ignore # mutmut generated
mutants_x__pick_critical_resource__mutmut['x__pick_critical_resource__mutmut_18'] = x__pick_critical_resource__mutmut_18 # type: ignore # mutmut generated
mutants_x__pick_critical_resource__mutmut['x__pick_critical_resource__mutmut_19'] = x__pick_critical_resource__mutmut_19 # type: ignore # mutmut generated
mutants_x__compute_confidence__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__compute_confidence__mutmut)
def _compute_confidence(window_days_used: int) -> Confidence:
    if window_days_used >= _cfg.default_window_days:
        return "high"
    if window_days_used >= _cfg.min_medium_confidence_days:
        return "medium"
    return "low"


def x__compute_confidence__mutmut_orig(window_days_used: int) -> Confidence:
    if window_days_used >= _cfg.default_window_days:
        return "high"
    if window_days_used >= _cfg.min_medium_confidence_days:
        return "medium"
    return "low"


def x__compute_confidence__mutmut_1(window_days_used: int) -> Confidence:
    if window_days_used > _cfg.default_window_days:
        return "high"
    if window_days_used >= _cfg.min_medium_confidence_days:
        return "medium"
    return "low"


def x__compute_confidence__mutmut_2(window_days_used: int) -> Confidence:
    if window_days_used >= _cfg.default_window_days:
        return "XXhighXX"
    if window_days_used >= _cfg.min_medium_confidence_days:
        return "medium"
    return "low"


def x__compute_confidence__mutmut_3(window_days_used: int) -> Confidence:
    if window_days_used >= _cfg.default_window_days:
        return "HIGH"
    if window_days_used >= _cfg.min_medium_confidence_days:
        return "medium"
    return "low"


def x__compute_confidence__mutmut_4(window_days_used: int) -> Confidence:
    if window_days_used >= _cfg.default_window_days:
        return "high"
    if window_days_used > _cfg.min_medium_confidence_days:
        return "medium"
    return "low"


def x__compute_confidence__mutmut_5(window_days_used: int) -> Confidence:
    if window_days_used >= _cfg.default_window_days:
        return "high"
    if window_days_used >= _cfg.min_medium_confidence_days:
        return "XXmediumXX"
    return "low"


def x__compute_confidence__mutmut_6(window_days_used: int) -> Confidence:
    if window_days_used >= _cfg.default_window_days:
        return "high"
    if window_days_used >= _cfg.min_medium_confidence_days:
        return "MEDIUM"
    return "low"


def x__compute_confidence__mutmut_7(window_days_used: int) -> Confidence:
    if window_days_used >= _cfg.default_window_days:
        return "high"
    if window_days_used >= _cfg.min_medium_confidence_days:
        return "medium"
    return "XXlowXX"


def x__compute_confidence__mutmut_8(window_days_used: int) -> Confidence:
    if window_days_used >= _cfg.default_window_days:
        return "high"
    if window_days_used >= _cfg.min_medium_confidence_days:
        return "medium"
    return "LOW"

mutants_x__compute_confidence__mutmut['_mutmut_orig'] = x__compute_confidence__mutmut_orig # type: ignore # mutmut generated
mutants_x__compute_confidence__mutmut['x__compute_confidence__mutmut_1'] = x__compute_confidence__mutmut_1 # type: ignore # mutmut generated
mutants_x__compute_confidence__mutmut['x__compute_confidence__mutmut_2'] = x__compute_confidence__mutmut_2 # type: ignore # mutmut generated
mutants_x__compute_confidence__mutmut['x__compute_confidence__mutmut_3'] = x__compute_confidence__mutmut_3 # type: ignore # mutmut generated
mutants_x__compute_confidence__mutmut['x__compute_confidence__mutmut_4'] = x__compute_confidence__mutmut_4 # type: ignore # mutmut generated
mutants_x__compute_confidence__mutmut['x__compute_confidence__mutmut_5'] = x__compute_confidence__mutmut_5 # type: ignore # mutmut generated
mutants_x__compute_confidence__mutmut['x__compute_confidence__mutmut_6'] = x__compute_confidence__mutmut_6 # type: ignore # mutmut generated
mutants_x__compute_confidence__mutmut['x__compute_confidence__mutmut_7'] = x__compute_confidence__mutmut_7 # type: ignore # mutmut generated
mutants_x__compute_confidence__mutmut['x__compute_confidence__mutmut_8'] = x__compute_confidence__mutmut_8 # type: ignore # mutmut generated
mutants_x__build_recommendation__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__build_recommendation__mutmut)
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


def x__build_recommendation__mutmut_orig(
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


def x__build_recommendation__mutmut_1(
    critical_resource: CriticalResource, cpu: ResourceForecast, memory: ResourceForecast
) -> str:
    if critical_resource != "None":
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


def x__build_recommendation__mutmut_2(
    critical_resource: CriticalResource, cpu: ResourceForecast, memory: ResourceForecast
) -> str:
    if critical_resource == "XXNoneXX":
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


def x__build_recommendation__mutmut_3(
    critical_resource: CriticalResource, cpu: ResourceForecast, memory: ResourceForecast
) -> str:
    if critical_resource == "none":
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


def x__build_recommendation__mutmut_4(
    critical_resource: CriticalResource, cpu: ResourceForecast, memory: ResourceForecast
) -> str:
    if critical_resource == "NONE":
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


def x__build_recommendation__mutmut_5(
    critical_resource: CriticalResource, cpu: ResourceForecast, memory: ResourceForecast
) -> str:
    if critical_resource == "None":
        return "XXNo saturation risk in the foreseeable future — cluster capacity is stable.XX"

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


def x__build_recommendation__mutmut_6(
    critical_resource: CriticalResource, cpu: ResourceForecast, memory: ResourceForecast
) -> str:
    if critical_resource == "None":
        return "no saturation risk in the foreseeable future — cluster capacity is stable."

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


def x__build_recommendation__mutmut_7(
    critical_resource: CriticalResource, cpu: ResourceForecast, memory: ResourceForecast
) -> str:
    if critical_resource == "None":
        return "NO SATURATION RISK IN THE FORESEEABLE FUTURE — CLUSTER CAPACITY IS STABLE."

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


def x__build_recommendation__mutmut_8(
    critical_resource: CriticalResource, cpu: ResourceForecast, memory: ResourceForecast
) -> str:
    if critical_resource == "None":
        return "No saturation risk in the foreseeable future — cluster capacity is stable."

    resource = None
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


def x__build_recommendation__mutmut_9(
    critical_resource: CriticalResource, cpu: ResourceForecast, memory: ResourceForecast
) -> str:
    if critical_resource == "None":
        return "No saturation risk in the foreseeable future — cluster capacity is stable."

    resource = cpu if critical_resource != "CPU" else memory
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


def x__build_recommendation__mutmut_10(
    critical_resource: CriticalResource, cpu: ResourceForecast, memory: ResourceForecast
) -> str:
    if critical_resource == "None":
        return "No saturation risk in the foreseeable future — cluster capacity is stable."

    resource = cpu if critical_resource == "XXCPUXX" else memory
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


def x__build_recommendation__mutmut_11(
    critical_resource: CriticalResource, cpu: ResourceForecast, memory: ResourceForecast
) -> str:
    if critical_resource == "None":
        return "No saturation risk in the foreseeable future — cluster capacity is stable."

    resource = cpu if critical_resource == "cpu" else memory
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


def x__build_recommendation__mutmut_12(
    critical_resource: CriticalResource, cpu: ResourceForecast, memory: ResourceForecast
) -> str:
    if critical_resource == "None":
        return "No saturation risk in the foreseeable future — cluster capacity is stable."

    resource = cpu if critical_resource == "CPU" else memory
    if (
        resource.days_to_saturation is not None or resource.days_to_saturation <= _NEAR_TERM_HORIZON_DAYS
    ):
        return (
            f"{critical_resource} projected to saturate in {resource.days_to_saturation} "
            f"days (around {resource.saturation_date}) — plan capacity expansion soon."
        )
    return (
        f"{critical_resource} is the limiting resource, projected to saturate around "
        f"{resource.saturation_date} — monitor and plan ahead."
    )


def x__build_recommendation__mutmut_13(
    critical_resource: CriticalResource, cpu: ResourceForecast, memory: ResourceForecast
) -> str:
    if critical_resource == "None":
        return "No saturation risk in the foreseeable future — cluster capacity is stable."

    resource = cpu if critical_resource == "CPU" else memory
    if (
        resource.days_to_saturation is None
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


def x__build_recommendation__mutmut_14(
    critical_resource: CriticalResource, cpu: ResourceForecast, memory: ResourceForecast
) -> str:
    if critical_resource == "None":
        return "No saturation risk in the foreseeable future — cluster capacity is stable."

    resource = cpu if critical_resource == "CPU" else memory
    if (
        resource.days_to_saturation is not None
        and resource.days_to_saturation < _NEAR_TERM_HORIZON_DAYS
    ):
        return (
            f"{critical_resource} projected to saturate in {resource.days_to_saturation} "
            f"days (around {resource.saturation_date}) — plan capacity expansion soon."
        )
    return (
        f"{critical_resource} is the limiting resource, projected to saturate around "
        f"{resource.saturation_date} — monitor and plan ahead."
    )

mutants_x__build_recommendation__mutmut['_mutmut_orig'] = x__build_recommendation__mutmut_orig # type: ignore # mutmut generated
mutants_x__build_recommendation__mutmut['x__build_recommendation__mutmut_1'] = x__build_recommendation__mutmut_1 # type: ignore # mutmut generated
mutants_x__build_recommendation__mutmut['x__build_recommendation__mutmut_2'] = x__build_recommendation__mutmut_2 # type: ignore # mutmut generated
mutants_x__build_recommendation__mutmut['x__build_recommendation__mutmut_3'] = x__build_recommendation__mutmut_3 # type: ignore # mutmut generated
mutants_x__build_recommendation__mutmut['x__build_recommendation__mutmut_4'] = x__build_recommendation__mutmut_4 # type: ignore # mutmut generated
mutants_x__build_recommendation__mutmut['x__build_recommendation__mutmut_5'] = x__build_recommendation__mutmut_5 # type: ignore # mutmut generated
mutants_x__build_recommendation__mutmut['x__build_recommendation__mutmut_6'] = x__build_recommendation__mutmut_6 # type: ignore # mutmut generated
mutants_x__build_recommendation__mutmut['x__build_recommendation__mutmut_7'] = x__build_recommendation__mutmut_7 # type: ignore # mutmut generated
mutants_x__build_recommendation__mutmut['x__build_recommendation__mutmut_8'] = x__build_recommendation__mutmut_8 # type: ignore # mutmut generated
mutants_x__build_recommendation__mutmut['x__build_recommendation__mutmut_9'] = x__build_recommendation__mutmut_9 # type: ignore # mutmut generated
mutants_x__build_recommendation__mutmut['x__build_recommendation__mutmut_10'] = x__build_recommendation__mutmut_10 # type: ignore # mutmut generated
mutants_x__build_recommendation__mutmut['x__build_recommendation__mutmut_11'] = x__build_recommendation__mutmut_11 # type: ignore # mutmut generated
mutants_x__build_recommendation__mutmut['x__build_recommendation__mutmut_12'] = x__build_recommendation__mutmut_12 # type: ignore # mutmut generated
mutants_x__build_recommendation__mutmut['x__build_recommendation__mutmut_13'] = x__build_recommendation__mutmut_13 # type: ignore # mutmut generated
mutants_x__build_recommendation__mutmut['x__build_recommendation__mutmut_14'] = x__build_recommendation__mutmut_14 # type: ignore # mutmut generated
