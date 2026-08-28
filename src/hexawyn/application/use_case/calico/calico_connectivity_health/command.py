from dataclasses import dataclass


@dataclass(frozen=True)
class CalicoConnectivityHealthCommand:
    """Empty command — Calico connectivity health is cluster-scoped."""

    pass
