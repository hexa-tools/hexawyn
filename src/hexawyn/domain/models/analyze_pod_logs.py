from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

from hexawyn.domain.models.log import RankedEvent

ConnectionIssueCategory = Literal["connection_timeout", "connection_refused"]


@dataclass(frozen=True)
class PodLogLine:
    timestamp: str
    level: str
    message: str
    run_index: int
    is_json: bool

    @property
    def is_error(self) -> bool:
        return self.level.upper() in ("ERROR", "FATAL")

    @property
    def is_warning(self) -> bool:
        return self.level.upper() in ("WARN", "WARNING")


@dataclass(frozen=True)
class ConnectionIssue:
    category: ConnectionIssueCategory
    message_sample: str
    count: int
    confidence: float


@dataclass(frozen=True)
class LogPatternMatch:
    pattern: str
    count: int
    confidence: float


@dataclass(frozen=True)
class PodRunSummary:
    run_index: int
    line_count: int
    error_count: int
    warning_count: int


@dataclass(frozen=True)
class AnalyzePodLogsRequest:
    pod_name: str
    namespace: str
    time_window_minutes: int = 30


@dataclass(frozen=True)
class AnalyzePodLogsResult:
    pod_name: str
    namespace: str
    time_window_minutes: int
    strategy_used: str
    total_lines: int
    error_count: int
    warning_count: int
    patterns: list[LogPatternMatch] = field(default_factory=list)
    connection_timeouts: list[ConnectionIssue] = field(default_factory=list)
    connection_refused: list[ConnectionIssue] = field(default_factory=list)
    confidence: float = 0.0
    summary: str = ""
    restarts_detected: bool = False
    runs: list[PodRunSummary] = field(default_factory=list)
    sanitized_binary: bool = False
    token_reduction_percentage: float = 0.0
    degraded: bool = False
    ranked_events: list[RankedEvent] = field(default_factory=list)
