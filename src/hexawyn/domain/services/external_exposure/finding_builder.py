from __future__ import annotations

from hexawyn.application.ports.driven.external_exposure_audit_port import ServiceRaw
from hexawyn.domain.models.constants import ExternalExposureConstants
from hexawyn.domain.models.external_exposure import ExternalExposureFinding
from hexawyn.domain.services.external_exposure.allowlist_matcher import is_allowlisted
from hexawyn.domain.services.external_exposure.internal_exposure_detector import (
    is_internal_load_balancer,
)
from hexawyn.domain.services.external_exposure.port_severity_classifier import (
    classify_base_severity,
)
from hexawyn.domain.services.external_exposure.risk_scorer import classify_risk_level

_cfg = ExternalExposureConstants()


def exclusion_reason(service: ServiceRaw, allowlist: tuple[str, ...]) -> str | None:
    if is_allowlisted(service["name"], allowlist):
        return _cfg.allowlisted_reason
    if is_internal_load_balancer(service["annotations"], _cfg.internal_load_balancer_annotations):
        return _cfg.internal_lb_reason
    return None


def build_finding(service: ServiceRaw) -> ExternalExposureFinding:
    base_severity = classify_base_severity(service["ports"], _cfg.critical_ports, _cfg.medium_ports)
    risk_level = classify_risk_level(
        base_severity=base_severity,
        service_type=service["service_type"],  # type: ignore[arg-type]
        namespace=service["namespace"],
        production_namespace=_cfg.production_namespace,
        has_source_ranges=service["has_source_ranges"],
    )
    is_pending = (
        service["service_type"] == "LoadBalancer"
        and service["external_ip"] is None
        and service["external_hostname"] is None
    )

    return ExternalExposureFinding(
        name=service["name"],
        namespace=service["namespace"],
        service_type=service["service_type"],  # type: ignore[arg-type]
        ports=service["ports"],
        external_ip=service["external_ip"],
        external_hostname=service["external_hostname"],
        node_port=service["node_port"],
        is_pending=is_pending,
        risk_level=risk_level,
        note=_cfg.source_ranges_note if service["has_source_ranges"] else None,
    )
