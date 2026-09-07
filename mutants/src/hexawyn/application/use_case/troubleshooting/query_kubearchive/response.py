from __future__ import annotations

from dataclasses import dataclass, field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class QueryKubearchiveResponse:
    total_resources: int = 0
    pods: list[dict[str, object]] = field(default_factory=list)
    queried_timestamp: str | None = None
    comparison: dict[str, object] | None = None
    error: str | None = None
