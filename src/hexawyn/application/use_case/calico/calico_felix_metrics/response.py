from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class CalicoFelixMetricsResponse:
    installed: bool = False
    not_installed_marker: str | None = None
    metrics_available: bool = False
    metrics_message: str | None = None
    total_denies: int = 0
    total_allows: int = 0
    deny_policy_count: int = 0
    policies: list[object] = field(default_factory=list)
    error: str | None = None
