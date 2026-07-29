from dataclasses import dataclass


@dataclass(frozen=True)
class ListOpenshiftImagestreamsCommand:
    namespace: str | None = None
