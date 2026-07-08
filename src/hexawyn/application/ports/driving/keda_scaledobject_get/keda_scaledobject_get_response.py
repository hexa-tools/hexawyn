from __future__ import annotations

from dataclasses import dataclass


@dataclass
class KedaScaledObjectGetResponse:
    name: str = ""
    namespace: str = ""
    phase: str = "unknown"
    min_replicas: int = 0
    max_replicas: int = 0
    current_replicas: int = 0
    hpa_target_replicas: int = 0
    hpa_name: str | None = None
    hpa_status: str = "unknown"
    cooldown_period_seconds: int = 0
    last_scale_time: str | None = None
    idle_replicas: int = 0
    fallback_replicas: int | None = None
    workload_kind: str = ""
    workload_name: str = ""
    ready: bool = False
    message: str | None = None
    error: str | None = None
