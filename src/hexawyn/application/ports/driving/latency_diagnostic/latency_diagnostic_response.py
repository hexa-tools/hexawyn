from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class LatencyDiagnosticResponse:
    service_name: str = ""
    slow_trace_count: int = 0
    total_traces: int = 0
    bottlenecks: list[dict[str, object]] = field(default_factory=list)
    slowest_span: dict[str, object] | None = None
    error: str | None = None
