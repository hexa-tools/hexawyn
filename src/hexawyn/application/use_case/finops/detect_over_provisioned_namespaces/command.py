from dataclasses import dataclass


@dataclass(frozen=True)
class DetectOverProvisionedNamespacesCommand:
    analysis_window_days: int = 7
    top_n: int = 5
