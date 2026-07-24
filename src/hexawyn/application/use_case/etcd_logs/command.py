from dataclasses import dataclass


@dataclass(frozen=True)
class EtcdLogsCommand:
    time_window_minutes: int = 60
