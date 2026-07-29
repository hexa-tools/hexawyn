from dataclasses import dataclass, field


@dataclass
class RedundantCallsResponse:
    calls: list[dict[str, object]] = field(default_factory=list)
    total_redundant_calls: int = 0
    patterns: str = ""
    flow: str = ""
    calculated_waste_ms: str = ""
    error: str | None = None
