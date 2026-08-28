from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class CalicoSegmentationAuditResponse:
    installed: bool = False
    not_installed_marker: str | None = None
    view: str = "vanilla"
    tiers: list[str] = field(default_factory=list)
    edges: list[object] = field(default_factory=list)
    gap_count: int = 0
    total_paths: int = 0
    summary: str | None = None
    error: str | None = None
