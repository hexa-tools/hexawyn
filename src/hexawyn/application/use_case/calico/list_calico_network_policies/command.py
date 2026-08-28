from dataclasses import dataclass


@dataclass(frozen=True)
class ListCalicoNetworkPoliciesCommand:
    """Optional namespace filter for Calico NetworkPolicies."""

    namespace: str | None = None
