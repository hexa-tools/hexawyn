from dataclasses import dataclass


@dataclass(frozen=True)
class ETCDLogsCommand:
    time_window_minutes: int = 60
