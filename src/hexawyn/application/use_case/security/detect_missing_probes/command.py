from dataclasses import dataclass


@dataclass(frozen=True)
class DetectMissingProbesCommand:
    namespace: str | None = None
