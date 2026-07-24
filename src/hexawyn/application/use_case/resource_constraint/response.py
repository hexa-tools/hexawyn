from dataclasses import dataclass


@dataclass
class ResourceConstraintResponse:
    error: str | None = None
