from dataclasses import dataclass


@dataclass(frozen=True)
class WatchPodLogsCommand:
    pod_name: str = ""
    namespace: str = ""
    timeout_seconds: int = 300
    max_reconnect_attempts: int = 3
    sample_rate: int = 1
