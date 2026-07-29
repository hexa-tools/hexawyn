from dataclasses import dataclass, field


@dataclass
class MemorySaturationResponse:
    prediction_window_minutes: int = 30
    critical_pods: list[dict[str, object]] = field(default_factory=list)
    safe_pod_count: int = 0
