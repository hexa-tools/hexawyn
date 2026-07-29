from dataclasses import dataclass


@dataclass(frozen=True)
class CompareClusterHealthCommand:
    cluster_a: str
    cluster_b: str
