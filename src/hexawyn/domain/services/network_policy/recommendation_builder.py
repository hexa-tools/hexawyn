from __future__ import annotations

from hexawyn.domain.models.network_policy import NetworkStatus


def build_recommendation(
    network_status: NetworkStatus, ingress_policies: int, egress_policies: int
) -> str | None:
    if network_status == "open":
        return "Apply default-deny NetworkPolicy for both ingress and egress"
    if network_status == "partially_restricted":
        if ingress_policies == 0:
            return "Add default-deny ingress NetworkPolicy"
        return "Add default-deny egress NetworkPolicy"
    return None
