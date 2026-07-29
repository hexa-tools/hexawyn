from dataclasses import dataclass, field


@dataclass
class ServiceDependencyGraphResponse:
    time_window_minutes: int = 60
    nodes: list[str] = field(default_factory=list)
    edges: list[dict[str, object]] = field(default_factory=list)
