from dataclasses import dataclass


@dataclass(frozen=True)
class QueryKubearchiveCommand:
    namespace: str
    resource_type: str = "pods"
    timestamp: str = ""
    compare_with_current: bool = False
