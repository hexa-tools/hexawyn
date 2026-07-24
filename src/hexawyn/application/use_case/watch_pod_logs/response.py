from dataclasses import dataclass


@dataclass
class WatchPodLogsResponse:
    error: str | None = None
