from dataclasses import dataclass, field
from typing import TypedDict


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
    total_lines_watched: int = 0
    alert_count: int = 0
    alerts: list[WatchAlertDict] = field(default_factory=list)
    reconnections: int = 0
    timeout_occurred: bool = False
    summary: str = ""
    stop_reason: str = ""
    lines_observed: str = ""
    lines_sampled: str = ""
    lines_sampled: str = ""  # type: ignore
    reconnect_count: str = ""
    patterns: str = ""
    confidence: str = ""
    error: str | None = None
