from dataclasses import dataclass


@dataclass(frozen=True)
class AnalyzePodLogsCommand:
    pod_name: str = ""
    namespace: str = ""
    time_window_minutes: int = 15
