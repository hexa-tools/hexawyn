from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class RolloutsListResponse:
    rollouts: list[dict[str, object]] = field(default_factory=list)
    error: str | None = None
