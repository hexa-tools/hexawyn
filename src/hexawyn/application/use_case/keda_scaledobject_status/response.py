from dataclasses import dataclass


@dataclass
class KedaScaledobjectStatusResponse:
    name: str = ""
    namespace: str | None = None
    phase: str = ""
    current_replicas: int = 0
    hpa_target_replicas: int | None = None
    last_scale_time: str | None = None
    cooldown_period_seconds: int = 0
    message: str | None = None
    error: str | None = None
