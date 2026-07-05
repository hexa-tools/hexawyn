from __future__ import annotations

from hexawyn.domain.models.network_policy import NetworkStatus, RiskLevel

_STATUS_RISK: dict[NetworkStatus, RiskLevel] = {
    "open": "critical",
    "partially_restricted": "medium",
    "restricted": "low",
}


def classify_risk_level(network_status: NetworkStatus, pod_count: int) -> RiskLevel:
    if pod_count == 0:
        return "low"
    return _STATUS_RISK[network_status]
