from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class SummarizeNamespaceEventsResponse:
    namespace: str = ""
    total_events: int = 0
    severity_breakdown: dict[str, int] = field(default_factory=dict)
    top_affected_pods: list[dict[str, object]] = field(default_factory=list)
    error: str | None = None
