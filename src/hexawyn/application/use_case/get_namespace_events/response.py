from dataclasses import dataclass, field


@dataclass
class GetNamespaceEventsResponse:
    events: list[dict[str, object]] = field(default_factory=list)
    error: str | None = None
