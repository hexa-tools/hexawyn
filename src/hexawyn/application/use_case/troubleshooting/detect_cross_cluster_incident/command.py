from dataclasses import dataclass


@dataclass(frozen=True)
class DetectCrossClusterIncidentCommand:
    window_minutes: int = 30
