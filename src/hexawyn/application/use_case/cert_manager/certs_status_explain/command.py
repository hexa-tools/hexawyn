from dataclasses import dataclass


@dataclass(frozen=True)
class CertsStatusExplainCommand:
    name: str
    namespace: str
