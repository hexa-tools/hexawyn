from dataclasses import dataclass


@dataclass(frozen=True)
class SlowestTracesCommand:
    pod_name: str = ""
    time_window_minutes: str = ""
    top_n: str = ""
