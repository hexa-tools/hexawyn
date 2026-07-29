from dataclasses import dataclass
from typing import TypedDict


class ResourceForecastDict(TypedDict):
    resource_type: str
    current_value: float
    ceiling: float
    current_utilization_percent: float
    growth_rate_per_day: float
    days_to_saturation: int | None
    saturation_date: str | None
    capacity_jump_detected: bool
    spike_caveat: bool
    capped_horizon: bool


@dataclass
class ClusterCapacityCeilingForecastResponse:
    cpu: ResourceForecastDict | None = None
    memory: ResourceForecastDict | None = None
    critical_resource: str = ""
    autoscaler_enabled: bool = False
    recommendation: str = ""
    confidence: str = ""
    window_days_used: int = 0
    error: str | None = None
