from dataclasses import dataclass


@dataclass
class KedaScaledjobGetResponse:
    name: str = ""
    namespace: str | None = None
    phase: str = ""
    error: str | None = None
