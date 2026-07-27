from dataclasses import dataclass


@dataclass(frozen=True)
class RolloutStatusCommand:
    name: str
    namespace: str
