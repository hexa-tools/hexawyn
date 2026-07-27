from dataclasses import dataclass


@dataclass(frozen=True)
class KedaTriggerauthGetCommand:
    name: str
    namespace: str
