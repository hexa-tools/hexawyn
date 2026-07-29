from dataclasses import dataclass


@dataclass(frozen=True)
class ConservativeNamespaceOverviewCommand:
    namespace: str = ""
    max_tokens: int = 2000
