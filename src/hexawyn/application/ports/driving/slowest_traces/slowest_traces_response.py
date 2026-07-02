from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class SlowestTracesResponse:
    pod_name: str = ""
    slowest_traces: list[dict[str, object]] = field(default_factory=list)
    total_traces_found: int = 0
    note: str = ""
    error: str | None = None
