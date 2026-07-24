from dataclasses import dataclass


@dataclass(frozen=True)
class KedaScaledobjectTriggersCommand:
    name: str
    namespace: str
