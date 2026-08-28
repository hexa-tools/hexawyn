from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class CalicoConnectivityHealthResponse:
    installed: bool = False
    not_installed_marker: str | None = None
    verdict: str = "unknown"
    ready_agents: int = 0
    total_agents: int = 0
    dataplane_mode: str | None = None
    tunnel_summary: str = "UNKNOWN"
    bgp_summary: str = "UNKNOWN"
    connectivity_probe: str | None = None
    nodes: list[object] = field(default_factory=list)
    degraded_nodes: list[str] = field(default_factory=list)
    summary: str | None = None
    error: str | None = None
