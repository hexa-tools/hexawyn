from __future__ import annotations

from hexawyn.domain.models.external_exposure import RiskLevel


def classify_base_severity(
    ports: list[int], critical_ports: tuple[int, ...], medium_ports: tuple[int, ...]
) -> RiskLevel:
    if any(port in critical_ports for port in ports):
        return "critical"
    if any(port in medium_ports for port in ports):
        return "medium"
    return "medium"
