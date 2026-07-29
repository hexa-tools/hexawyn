from dataclasses import dataclass


@dataclass(frozen=True)
class GetPodEventsCommand:
    namespace: str | None = None
    pod_name: str | None = None
    time_window_minutes: int = 15
