from dataclasses import dataclass


@dataclass(frozen=True)
class DetectZombiesCommand:
    analysis_window_hours: int = 24
