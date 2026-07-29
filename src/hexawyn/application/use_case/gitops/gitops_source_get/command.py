from dataclasses import dataclass


@dataclass(frozen=True)
class GitopsSourceGetCommand:
    name: str
    namespace: str
