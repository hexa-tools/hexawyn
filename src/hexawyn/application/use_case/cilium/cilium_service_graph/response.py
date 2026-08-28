from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class CiliumServiceGraphResponse:
    time_window_minutes: int = 60
    nodes: list[str] = field(default_factory=list)
    edges: list[dict[str, object]] = field(default_factory=list)
    note: str | None = None
    error: str | None = None
