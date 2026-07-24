from dataclasses import dataclass


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
    error: str | None = None
