from dataclasses import dataclass


@dataclass(frozen=True)
class AdaptiveNamespaceInvestigationCommand:
    namespace: str = ""
    depth: int = 3
