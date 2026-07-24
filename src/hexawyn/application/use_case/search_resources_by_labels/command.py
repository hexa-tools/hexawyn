from dataclasses import dataclass


@dataclass(frozen=True)
class SearchResourcesByLabelsCommand:
    namespace: str | None = None
