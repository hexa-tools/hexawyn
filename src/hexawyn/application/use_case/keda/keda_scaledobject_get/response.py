from dataclasses import dataclass


@dataclass
class KedaScaledobjectGetResponse:
    name: str = ""
    namespace: str = ""
    phase: str = ""
    min_replicas: int = 0
    max_replicas: int = 0
    current_replicas: int = 0
    hpa_target_replicas: int = 0
    hpa_name: str = ""
    hpa_status: str = ""
    cooldown_period_seconds: int = 0
    last_scale_time: str | None = None
    idle_replicas: int = 0
    fallback_replicas: int = 0
    workload_kind: str = ""
    workload_name: str = ""
    ready: bool = False
    message: str = ""
    error: str | None = None
