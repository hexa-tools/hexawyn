from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ListCalicoNetworkPoliciesResponse:
    installed: bool = False
    not_installed_marker: str | None = None
    policies: list[object] = field(default_factory=list)
    total: int = 0
    global_count: int = 0
    namespaced_count: int = 0
    error: str | None = None
