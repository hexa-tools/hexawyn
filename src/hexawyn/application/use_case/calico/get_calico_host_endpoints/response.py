from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class GetCalicoHostEndpointsResponse:
    installed: bool = False
    not_installed_marker: str | None = None
    total: int = 0
    endpoints: list[object] = field(default_factory=list)
    error: str | None = None
