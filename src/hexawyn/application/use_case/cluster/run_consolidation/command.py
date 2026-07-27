from dataclasses import dataclass


@dataclass(frozen=True)
class RunConsolidationCommand:
    cluster_name: str = "unknown"
