from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ConfigurationDriftDetectionResponse:
    drifted_resources: list[dict[str, object]] = field(default_factory=list)
    drifted_by_namespace: dict[str, int] = field(default_factory=dict)
    in_sync_count: int = 0
    excluded_resources: int = 0
    total_checked: int = 0
    summary: str = ""
    error: str | None = None
