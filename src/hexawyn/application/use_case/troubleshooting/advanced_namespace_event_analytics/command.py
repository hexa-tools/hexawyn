from dataclasses import dataclass


@dataclass(frozen=True)
class AdvancedNamespaceEventAnalyticsCommand:
    namespace: str
    time_window_minutes: int = 15
