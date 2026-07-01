from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class CostProfilingResponse:
    time_window_minutes: int = 60
    ranked_endpoints: list[dict[str, object]] = field(default_factory=list)
    optimisation_candidates: list[dict[str, object]] = field(default_factory=list)
    error: str | None = None
