from __future__ import annotations

from dataclasses import dataclass


@dataclass
class KedaScaledObjectStatusResponse:
    name: str = ""
    namespace: str = ""
    phase: str = "unknown"
    current_replicas: int = 0
    hpa_target_replicas: int = 0
    last_scale_time: str | None = None
    cooldown_period_seconds: int = 0
    message: str | None = None
    error: str | None = None
