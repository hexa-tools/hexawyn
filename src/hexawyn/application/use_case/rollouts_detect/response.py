from dataclasses import dataclass


@dataclass
class RolloutsDetectResponse:
    installed: bool = False
    version: str | None = None
    namespace: str | None = None
    error: str | None = None
