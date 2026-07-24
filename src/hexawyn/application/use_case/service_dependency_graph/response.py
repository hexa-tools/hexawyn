from dataclasses import dataclass, field


@dataclass
class ServiceDependencyGraphResponse:
    nodes: list[dict[str, object]] = field(default_factory=list)
    edges: list[dict[str, object]] = field(default_factory=list)
    error: str | None = None
