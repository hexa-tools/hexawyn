from dataclasses import dataclass


@dataclass(frozen=True)
class CertsGetCommand:
    name: str
    namespace: str
