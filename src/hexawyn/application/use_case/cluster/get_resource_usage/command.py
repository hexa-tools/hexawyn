from dataclasses import dataclass


@dataclass(frozen=True)
class GetResourceUsageCommand:
    namespace: str | None = None
    resource: str = "both"
