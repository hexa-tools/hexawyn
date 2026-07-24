from dataclasses import dataclass


@dataclass(frozen=True)
class PolicyExplainDenialCommand:
    name: str
    namespace: str
