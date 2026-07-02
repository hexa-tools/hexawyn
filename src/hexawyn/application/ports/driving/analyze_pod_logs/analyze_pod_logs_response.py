from __future__ import annotations

from dataclasses import dataclass, field
from typing import TypedDict


class LogPatternDict(TypedDict):
    pattern: str
    count: int
    confidence: float


class ConnectionIssueDict(TypedDict):
    category: str
    message_sample: str
    count: int
    confidence: float


class PodRunSummaryDict(TypedDict):
    run_index: int
    line_count: int
    error_count: int
    warning_count: int


@dataclass
class AnalyzePodLogsResponse:
    pod_name: str = ""
    namespace: str = ""
    time_window_minutes: int = 30
    strategy_used: str = ""
    total_lines: int = 0
    error_count: int = 0
    warning_count: int = 0
    confidence: float = 0.0
    summary: str = ""
    restarts_detected: bool = False
    sanitized_binary: bool = False
    patterns: list[LogPatternDict] = field(default_factory=list)
    connection_timeouts: list[ConnectionIssueDict] = field(default_factory=list)
    connection_refused: list[ConnectionIssueDict] = field(default_factory=list)
    runs: list[PodRunSummaryDict] = field(default_factory=list)
    error: str | None = None
