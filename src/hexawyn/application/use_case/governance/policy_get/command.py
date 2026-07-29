from dataclasses import dataclass


@dataclass(frozen=True)
class PolicyGetCommand:
    name: str
    namespace: str
