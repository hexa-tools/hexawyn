from dataclasses import dataclass


@dataclass(frozen=True)
class GitopsAppSyncCommand:
    name: str
    namespace: str
