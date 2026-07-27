from dataclasses import dataclass


@dataclass(frozen=True)
class KedaScaledobjectGetCommand:
    name: str
    namespace: str
