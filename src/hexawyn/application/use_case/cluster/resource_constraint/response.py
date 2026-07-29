from dataclasses import dataclass


@dataclass
class ResourceConstraintResponse:
    namespace: str = ""
    total_pods: int = 0
    total_containers: int = 0
    critical_count: int = 0
    error: str | None = None
