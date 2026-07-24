from dataclasses import dataclass


@dataclass
class DetectMissingProbesResponse:
    error: str | None = None
