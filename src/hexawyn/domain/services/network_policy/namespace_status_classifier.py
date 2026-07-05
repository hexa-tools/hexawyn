from __future__ import annotations

from hexawyn.domain.models.network_policy import NetworkStatus


def classify_network_status(ingress_policies: int, egress_policies: int) -> NetworkStatus:
    has_ingress = ingress_policies > 0
    has_egress = egress_policies > 0
    if not has_ingress and not has_egress:
        return "open"
    if has_ingress and has_egress:
        return "restricted"
    return "partially_restricted"
