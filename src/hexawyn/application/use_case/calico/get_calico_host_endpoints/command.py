from dataclasses import dataclass


@dataclass(frozen=True)
class GetCalicoHostEndpointsCommand:
    """Empty command — Calico HostEndpoints are cluster-scoped."""

    pass
