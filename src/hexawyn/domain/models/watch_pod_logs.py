from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

from hexawyn.domain.models.analyze_pod_logs import LogPatternMatch

CriticalPatternCategory = Literal["oom", "db_connection_error", "panic"]
WatchStopReason = Literal["timeout", "pod_deleted", "session_ended"]


@dataclass(frozen=True)
class CriticalMatch:
    category: CriticalPatternCategory
    pattern: str
    log_line: str
    timestamp: str
    pod_name: str


@dataclass(frozen=True)
class WatchPodLogsRequest:
    pod_name: str
    namespace: str
    timeout_seconds: int = 300
    max_reconnect_attempts: int = 3
    sample_rate: int = 100


@dataclass(frozen=True)
class WatchPodLogsResult:
    pod_name: str
    namespace: str
    stop_reason: WatchStopReason
    lines_observed: int
    lines_sampled: int
    reconnect_count: int
    alerts: list[CriticalMatch] = field(default_factory=list)
    patterns: list[LogPatternMatch] = field(default_factory=list)
    confidence: float = 0.0
    summary: str = ""
