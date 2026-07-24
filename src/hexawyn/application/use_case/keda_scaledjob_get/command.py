from dataclasses import dataclass


@dataclass(frozen=True)
class KedaScaledjobGetCommand:
    name: str
    namespace: str
