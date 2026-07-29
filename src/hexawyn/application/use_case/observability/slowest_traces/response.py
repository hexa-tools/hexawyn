from dataclasses import dataclass, field


@dataclass
class SlowestTracesResponse:
    traces: list[dict[str, object]] = field(default_factory=list)
    total_traces_found: int = 0
    slowest_traces: str = ""
    pod_name: str = ""
    note: str = ""
    error: str | None = None
