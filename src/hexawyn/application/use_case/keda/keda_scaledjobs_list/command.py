from dataclasses import dataclass


@dataclass(frozen=True)
class KedaScaledjobsListCommand:
    namespace: str | None = None
