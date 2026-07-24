from dataclasses import dataclass


@dataclass(frozen=True)
class AdvancedNamespaceEventAnalyticsCommand:
    namespace: str
