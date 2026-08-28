from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class GetCalicoStatusResponse:
    installed: bool = False
    not_installed_marker: str | None = None
    status: str | None = None
    ready_agents: int = 0
    total_agents: int = 0
    degraded_summary: str | None = None
    agents: list[object] = field(default_factory=list)
    felix_errors_available: bool = False
    felix_errors: int | None = None
    connectivity_available: bool = False
    connectivity_status: str | None = None
    connectivity_detail: str | None = None
    error: str | None = None
