from dataclasses import dataclass


@dataclass(frozen=True)
class ListNamespacesCommand:
    cluster_name: str | None = None
