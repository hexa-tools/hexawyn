from dataclasses import dataclass, field


@dataclass
class AnalyzeCriticalNamespaceEventsResponse:
    critical_events: list[dict[str, object]] = field(default_factory=list)
    error: str | None = None
