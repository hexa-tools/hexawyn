from dataclasses import dataclass


@dataclass(frozen=True)
class ListOpenshiftSccsCommand:
    namespace: str | None = None
