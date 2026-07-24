from dataclasses import dataclass


@dataclass(frozen=True)
class AdminEndpointAuditCommand:
    namespace: str | None = None
