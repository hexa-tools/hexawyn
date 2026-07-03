from __future__ import annotations

from dataclasses import dataclass, field
from typing import TypedDict

from hexawyn.application.ports.driving.analyze_pod_logs.analyze_pod_logs_response import (
    LogPatternDict,
)


class WatchAlertDict(TypedDict):
    category: str
    pattern: str
    log_line: str
    timestamp: str
    pod_name: str


@dataclass
class WatchPodLogsResponse:
    pod_name: str = ""
    namespace: str = ""
    stop_reason: str = ""
    lines_observed: int = 0
    lines_sampled: int = 0
    reconnect_count: int = 0
    confidence: float = 0.0
    summary: str = ""
    alerts: list[WatchAlertDict] = field(default_factory=list)
    patterns: list[LogPatternDict] = field(default_factory=list)
    error: str | None = None
