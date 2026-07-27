from dataclasses import dataclass


@dataclass(frozen=True)
class KedaScaledobjectStatusCommand:
    name: str
    namespace: str
