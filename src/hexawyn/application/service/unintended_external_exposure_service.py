from __future__ import annotations

from hexawyn.application.ports.driven.external_exposure_audit_port import (
    ExternalExposureAuditPort,
    ServiceRaw,
)
from hexawyn.application.ports.driving.detect_unintended_external_exposure.detect_unintended_external_exposure_service_port import (
    DetectUnintendedExternalExposureServicePort,
)
from hexawyn.application.use_case.detect_unintended_external_exposure.command import (
    DetectUnintendedExternalExposureCommand,
)
from hexawyn.application.use_case.detect_unintended_external_exposure.response import (
    DetectUnintendedExternalExposureResponse,
    ExcludedExposureDict,
    ExternalExposureFindingDict,
)
from hexawyn.domain.models.constants import ExternalExposureConstants
from hexawyn.domain.models.external_exposure import (
    ExcludedExposure,
    ExternalExposureFinding,
    ExternalExposureReport,
)
from hexawyn.domain.services.external_exposure.allowlist_matcher import is_allowlisted
from hexawyn.domain.services.external_exposure.exposure_report_builder import build_report
from hexawyn.domain.services.external_exposure.internal_exposure_detector import (
    is_internal_load_balancer,
)
from hexawyn.domain.services.external_exposure.port_severity_classifier import (
    classify_base_severity,
)
from hexawyn.domain.services.external_exposure.risk_scorer import classify_risk_level
from hexawyn.domain.services.external_exposure.service_type_classifier import (
    is_externally_exposed_type,
)

_cfg = ExternalExposureConstants()
_SOURCE_RANGES_NOTE = "risk reduced by IP allowlist (loadBalancerSourceRanges)"
_ALLOWLISTED_REASON = "allowlisted"
_INTERNAL_LB_REASON = "internal LoadBalancer (not public)"


class UnintendedExternalExposureService(DetectUnintendedExternalExposureServicePort):
    def __init__(self, external_exposure_port: ExternalExposureAuditPort) -> None:
        self._external_exposure_port = external_exposure_port

    def detect_unintended_exposure(
        self, command: DetectUnintendedExternalExposureCommand
    ) -> DetectUnintendedExternalExposureResponse:
        services_raw = self._external_exposure_port.list_external_services()
        if command.namespaces is not None:
            allowed_namespaces = set(command.namespaces)
            services_raw = [s for s in services_raw if s["namespace"] in allowed_namespaces]

        allowlist = tuple(command.allowlist or [])
        externally_exposed = [
            service
            for service in services_raw
            if is_externally_exposed_type(service["service_type"])
        ]

        findings: list[ExternalExposureFinding] = []
        excluded: list[ExcludedExposure] = []

        for service in externally_exposed:
            exclusion_reason = _exclusion_reason(service, allowlist)
            if exclusion_reason is not None:
                excluded.append(
                    ExcludedExposure(
                        name=service["name"],
                        namespace=service["namespace"],
                        reason=exclusion_reason,
                    )
                )
                continue

            findings.append(_build_finding(service))

        report = build_report(
            findings=findings,
            excluded_exposures=excluded,
            total_external_services_checked=len(externally_exposed),
        )
        return _to_response(report)


def _exclusion_reason(service: ServiceRaw, allowlist: tuple[str, ...]) -> str | None:
    if is_allowlisted(service["name"], allowlist):
        return _ALLOWLISTED_REASON
    if is_internal_load_balancer(service["annotations"], _cfg.internal_load_balancer_annotations):
        return _INTERNAL_LB_REASON
    return None


def _build_finding(service: ServiceRaw) -> ExternalExposureFinding:
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
        note=_SOURCE_RANGES_NOTE if service["has_source_ranges"] else None,
    )


def _to_response(report: ExternalExposureReport) -> DetectUnintendedExternalExposureResponse:
    return DetectUnintendedExternalExposureResponse(
        findings=[_to_finding_dict(finding) for finding in report.findings],
        excluded_exposures=[_to_excluded_dict(excluded) for excluded in report.excluded_exposures],
        total_external_services_checked=report.total_external_services_checked,
        summary=report.summary,
        error=None,
    )


def _to_finding_dict(finding: ExternalExposureFinding) -> ExternalExposureFindingDict:
    return ExternalExposureFindingDict(
        name=finding.name,
        namespace=finding.namespace,
        service_type=finding.service_type,
        ports=finding.ports,
        external_ip=finding.external_ip,
        external_hostname=finding.external_hostname,
        node_port=finding.node_port,
        is_pending=finding.is_pending,
        risk_level=finding.risk_level,
        note=finding.note,
    )


def _to_excluded_dict(excluded: ExcludedExposure) -> ExcludedExposureDict:
    return ExcludedExposureDict(
        name=excluded.name, namespace=excluded.namespace, reason=excluded.reason
    )
