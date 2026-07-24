from dataclasses import dataclass


@dataclass(frozen=True)
class GitopsAppStatusCommand:
    name: str
    namespace: str
