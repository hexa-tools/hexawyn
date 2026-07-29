from dataclasses import dataclass


@dataclass(frozen=True)
class ListOpenshiftProjectsCommand:
    namespace: str | None = None
