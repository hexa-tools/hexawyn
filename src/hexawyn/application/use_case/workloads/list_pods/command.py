from dataclasses import dataclass


@dataclass(frozen=True)
class ListPodsCommand:
    namespace: str
