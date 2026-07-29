from dataclasses import dataclass


@dataclass(frozen=True)
class GitopsAppsListCommand:
    namespace: str | None = None
