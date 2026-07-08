from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class OutdatedHelmRelease:
    release_name: str
    namespace: str
    chart_name: str
    current_version: str
    latest_version: str
    delta_type: str
    breaking_changes: str
    is_pinned: bool
    repo_error: str


@dataclass
class OutdatedHelmReport:
    total_releases: int = 0
    outdated_count: int = 0
    up_to_date_count: int = 0
    error_count: int = 0
    releases: list[OutdatedHelmRelease] = field(default_factory=list)
