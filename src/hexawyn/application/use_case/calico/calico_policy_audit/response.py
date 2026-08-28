from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class CalicoPolicyAuditResponse:
    installed: bool = False
    not_installed_marker: str | None = None
    degraded_to_vanilla: bool = False
    total_namespaces_checked: int = 0
    gap_count: int = 0
    findings: list[object] = field(default_factory=list)
    summary: str | None = None
    error: str | None = None
