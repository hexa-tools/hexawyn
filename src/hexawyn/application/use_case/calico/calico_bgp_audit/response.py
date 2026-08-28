from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class CalicoBgpAuditResponse:
    installed: bool = False
    not_installed_marker: str | None = None
    as_number: str | None = None
    node_to_node_mesh_enabled: bool | None = None
    service_cluster_ips: list[str] = field(default_factory=list)
    peer_count: int = 0
    peers: list[object] = field(default_factory=list)
    session_state: str = "unknown"
    session_note: str | None = None
    summary: str | None = None
    error: str | None = None
