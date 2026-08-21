from dataclasses import dataclass


@dataclass(frozen=True)
class ListIngressesCommand:
    namespace: str | None = None
