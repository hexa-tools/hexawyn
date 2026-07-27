from dataclasses import dataclass


@dataclass(frozen=True)
class KedaScaledobjectsListCommand:
    namespace: str | None = None
