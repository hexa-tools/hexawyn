from dataclasses import dataclass, field


@dataclass
class AdvancedNamespaceEventAnalyticsResponse:
    namespace: str = ""
    events: list[dict[str, object]] = field(default_factory=list)
    error: str | None = None
