from dataclasses import dataclass


@dataclass(frozen=True)
class ResourceYamlCommand:
    kind: str
    name: str
    namespace: str
