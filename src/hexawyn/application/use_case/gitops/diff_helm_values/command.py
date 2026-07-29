from dataclasses import dataclass


@dataclass(frozen=True)
class DiffHelmValuesCommand:
    release: str
    namespace: str
