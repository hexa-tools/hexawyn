from __future__ import annotations

from dataclasses import dataclass, field

from hexawyn.domain.models.calico import DataplaneMode


@dataclass
class CalicoDetectResponse:
    installed: bool = False
    status: str | None = None
    not_installed_marker: str | None = None
    version: str | None = None
    mode: DataplaneMode | None = None
    namespace: str | None = None
    tigera_operator: bool = False
    enterprise: bool = False
    agents: list[object] = field(default_factory=list)
    total_nodes: int = 0
    ready_agents: int = 0
    degraded_agents: int = 0
    degraded_summary: str | None = None
    error: str | None = None
