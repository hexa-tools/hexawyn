from dataclasses import dataclass, field


@dataclass
class SlowestTracesResponse:
    traces: list[dict[str, object]] = field(default_factory=list)
    error: str | None = None
