from dataclasses import dataclass


@dataclass(frozen=True)
class ListOpenshiftRoutesCommand:
    namespace: str | None = None
