from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class RedundantCallsResponse:
    flow: str = ""
    patterns: list[dict[str, object]] = field(default_factory=list)
    total_redundant_calls: int = 0
    calculated_waste_ms: float = 0.0
    error: str | None = None
