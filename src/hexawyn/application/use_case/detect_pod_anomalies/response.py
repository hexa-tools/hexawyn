from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class DetectPodAnomaliesResponse:
    namespace: str = ""
    total_pods: int = 0
    anomalies: list[dict[str, object]] = field(default_factory=list)
    excluded_pods: list[str] = field(default_factory=list)
    summary: str = ""
    error: str | None = None
