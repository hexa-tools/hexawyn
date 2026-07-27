from dataclasses import dataclass


@dataclass
class KedaScaledobjectStatusResponse:
    name: str = ""
    namespace: str = ""
    phase: str = ""
    current_replicas: int = 0
    hpa_target_replicas: int = 0
    last_scale_time: str | None = None
    cooldown_period_seconds: int = 0
    message: str = ""
    error: str | None = None
