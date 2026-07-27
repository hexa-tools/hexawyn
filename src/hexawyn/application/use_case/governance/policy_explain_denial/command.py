from dataclasses import dataclass


@dataclass(frozen=True)
class PolicyExplainDenialCommand:
    name: str = ""
    namespace: str = ""
    resource_kind: str = ""
    resource_name: str = ""
    name: str  # type: ignore
    namespace: str  # type: ignore
