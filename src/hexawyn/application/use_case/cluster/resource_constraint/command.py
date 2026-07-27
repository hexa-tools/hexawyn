from dataclasses import dataclass


@dataclass(frozen=True)
class ResourceConstraintCommand:
    namespace: str | None = None
