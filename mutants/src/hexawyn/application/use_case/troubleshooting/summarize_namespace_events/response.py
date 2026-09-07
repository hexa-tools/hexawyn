from __future__ import annotations

from dataclasses import dataclass, field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class SummarizeNamespaceEventsResponse:
    namespace: str = ""
    total_events: int = 0
    severity_breakdown: dict[str, int] = field(default_factory=dict)
    top_affected_pods: list[dict[str, object]] = field(default_factory=list)
    error: str | None = None
