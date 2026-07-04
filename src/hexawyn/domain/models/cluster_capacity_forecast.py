from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

ResourceType = Literal["cpu", "memory"]
CriticalResource = Literal["CPU", "Memory", "None"]
Confidence = Literal["low", "medium", "high"]


@dataclass(frozen=True)
class ClusterCapacityRawData:
    """Fusion of ECA-31's Prometheus usage series and CapacityForecastPort's
    K8s allocatable/autoscaler data — assembled by the service, consumed by
    the pure domain composer. Deliberately not tied to either port's own
    TypedDict shape, so the domain layer stays decoupled from both."""

    cpu_daily_usage_cores: list[float] = field(default_factory=list)
    memory_daily_usage_gb: list[float] = field(default_factory=list)
    total_allocatable_cpu_cores: float = 0.0
    total_allocatable_memory_gb: float = 0.0
    autoscaler_enabled: bool = False


@dataclass(frozen=True)
class ResourceForecast:
    resource_type: ResourceType
    current_value: float
    ceiling: float
    current_utilization_percent: float
    growth_rate_per_day: float
    days_to_saturation: int | None
    saturation_date: str | None
    capacity_jump_detected: bool
    spike_caveat: bool
    capped_horizon: bool


@dataclass(frozen=True)
class ClusterCapacityForecastRequest:
    window_days: int = 14


@dataclass(frozen=True)
class ClusterCapacityForecastReport:
    cpu: ResourceForecast
    memory: ResourceForecast
    critical_resource: CriticalResource
    autoscaler_enabled: bool
    recommendation: str
    confidence: Confidence
    window_days_used: int
