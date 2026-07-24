from dataclasses import dataclass


@dataclass(frozen=True)
class GitopsSourcesListCommand:
    namespace: str | None = None
