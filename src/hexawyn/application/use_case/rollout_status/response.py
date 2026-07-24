from dataclasses import dataclass


@dataclass
class RolloutStatusResponse:
    name: str = ""
    namespace: str | None = None
    phase: str = ""
    strategy: str = ""
    message: str | None = None
    error: str | None = None
