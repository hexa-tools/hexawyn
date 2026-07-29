from dataclasses import dataclass
from typing import TypedDict


class LogPatternDict(TypedDict):
    pattern: str
    count: int
    confidence: str


@dataclass
class AnalyzePodLogsResponse:
    pod_name: str = ""
    namespace: str = ""
    time_window_minutes: int = 0
    strategy_used: str = ""
    total_lines: int = 0
    error_count: int = 0
    warning_count: int = 0
    confidence: str = ""
    summary: str = ""
    restarts_detected: bool = False
    token_reduction_percentage: str = ""
    severity: str = ""
    sanitized_binary: str = ""
    runs: str = ""
    run_index: str = ""
    ranked_events: str = ""
    patterns: str = ""
    line_count: int = 0
    line: str = ""
    degraded: str = ""
    connection_timeouts: str = ""
    connection_refused: str = ""
    error: str | None = None


class ConnectionIssueDict(TypedDict):
    pod_name: str
    namespace: str
    reason: str


class PodRunSummaryDict(TypedDict):
    pod_name: str
    namespace: str
    status: str
    restart_count: int


class RankedEventDict(TypedDict):
    event_type: str
    reason: str
    count: int
