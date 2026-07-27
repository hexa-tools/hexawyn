from dataclasses import dataclass


@dataclass(frozen=True)
class GitopsAppGetCommand:
    name: str
    namespace: str
