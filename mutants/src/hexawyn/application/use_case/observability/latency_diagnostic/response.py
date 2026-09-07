from __future__ import annotations

from dataclasses import dataclass, field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


@dataclass
class LatencyDiagnosticResponse:
    service_name: str = ""
    slow_trace_count: int = 0
    total_traces: int = 0
    bottlenecks: list[dict[str, object]] = field(default_factory=list)
    slowest_span: dict[str, object] | None = None
    error: str | None = None
