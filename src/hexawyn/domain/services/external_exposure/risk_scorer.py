from __future__ import annotations

from hexawyn.domain.models.external_exposure import RiskLevel, ServiceType

_DOWNGRADE: dict[RiskLevel, RiskLevel] = {
    "critical": "high",
    "high": "medium",
    "medium": "low",
    "low": "low",
}


def classify_risk_level(
    base_severity: RiskLevel,
    service_type: ServiceType,
    namespace: str,
    production_namespace: str,
    has_source_ranges: bool,
) -> RiskLevel:
    level = base_severity
    if service_type == "NodePort":
        level = _DOWNGRADE[level]
    elif namespace != production_namespace:
        level = _DOWNGRADE[level]

    if has_source_ranges:
        level = _DOWNGRADE[level]

    return level
