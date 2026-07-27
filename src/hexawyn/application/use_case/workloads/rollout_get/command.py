from dataclasses import dataclass


@dataclass(frozen=True)
class RolloutGetCommand:
    name: str
    namespace: str
