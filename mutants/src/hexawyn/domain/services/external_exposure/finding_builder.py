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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_exclusion_reason__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_exclusion_reason__mutmut)
def exclusion_reason(service: ServiceRaw, allowlist: tuple[str, ...]) -> str | None:
    if is_allowlisted(service["name"], allowlist):
        return _cfg.allowlisted_reason
    if is_internal_load_balancer(service["annotations"], _cfg.internal_load_balancer_annotations):
        return _cfg.internal_lb_reason
    return None


def x_exclusion_reason__mutmut_orig(service: ServiceRaw, allowlist: tuple[str, ...]) -> str | None:
    if is_allowlisted(service["name"], allowlist):
        return _cfg.allowlisted_reason
    if is_internal_load_balancer(service["annotations"], _cfg.internal_load_balancer_annotations):
        return _cfg.internal_lb_reason
    return None


def x_exclusion_reason__mutmut_1(service: ServiceRaw, allowlist: tuple[str, ...]) -> str | None:
    if is_allowlisted(None, allowlist):
        return _cfg.allowlisted_reason
    if is_internal_load_balancer(service["annotations"], _cfg.internal_load_balancer_annotations):
        return _cfg.internal_lb_reason
    return None


def x_exclusion_reason__mutmut_2(service: ServiceRaw, allowlist: tuple[str, ...]) -> str | None:
    if is_allowlisted(service["name"], None):
        return _cfg.allowlisted_reason
    if is_internal_load_balancer(service["annotations"], _cfg.internal_load_balancer_annotations):
        return _cfg.internal_lb_reason
    return None


def x_exclusion_reason__mutmut_3(service: ServiceRaw, allowlist: tuple[str, ...]) -> str | None:
    if is_allowlisted(allowlist):
        return _cfg.allowlisted_reason
    if is_internal_load_balancer(service["annotations"], _cfg.internal_load_balancer_annotations):
        return _cfg.internal_lb_reason
    return None


def x_exclusion_reason__mutmut_4(service: ServiceRaw, allowlist: tuple[str, ...]) -> str | None:
    if is_allowlisted(service["name"], ):
        return _cfg.allowlisted_reason
    if is_internal_load_balancer(service["annotations"], _cfg.internal_load_balancer_annotations):
        return _cfg.internal_lb_reason
    return None


def x_exclusion_reason__mutmut_5(service: ServiceRaw, allowlist: tuple[str, ...]) -> str | None:
    if is_allowlisted(service["XXnameXX"], allowlist):
        return _cfg.allowlisted_reason
    if is_internal_load_balancer(service["annotations"], _cfg.internal_load_balancer_annotations):
        return _cfg.internal_lb_reason
    return None


def x_exclusion_reason__mutmut_6(service: ServiceRaw, allowlist: tuple[str, ...]) -> str | None:
    if is_allowlisted(service["NAME"], allowlist):
        return _cfg.allowlisted_reason
    if is_internal_load_balancer(service["annotations"], _cfg.internal_load_balancer_annotations):
        return _cfg.internal_lb_reason
    return None


def x_exclusion_reason__mutmut_7(service: ServiceRaw, allowlist: tuple[str, ...]) -> str | None:
    if is_allowlisted(service["name"], allowlist):
        return _cfg.allowlisted_reason
    if is_internal_load_balancer(None, _cfg.internal_load_balancer_annotations):
        return _cfg.internal_lb_reason
    return None


def x_exclusion_reason__mutmut_8(service: ServiceRaw, allowlist: tuple[str, ...]) -> str | None:
    if is_allowlisted(service["name"], allowlist):
        return _cfg.allowlisted_reason
    if is_internal_load_balancer(service["annotations"], None):
        return _cfg.internal_lb_reason
    return None


def x_exclusion_reason__mutmut_9(service: ServiceRaw, allowlist: tuple[str, ...]) -> str | None:
    if is_allowlisted(service["name"], allowlist):
        return _cfg.allowlisted_reason
    if is_internal_load_balancer(_cfg.internal_load_balancer_annotations):
        return _cfg.internal_lb_reason
    return None


def x_exclusion_reason__mutmut_10(service: ServiceRaw, allowlist: tuple[str, ...]) -> str | None:
    if is_allowlisted(service["name"], allowlist):
        return _cfg.allowlisted_reason
    if is_internal_load_balancer(service["annotations"], ):
        return _cfg.internal_lb_reason
    return None


def x_exclusion_reason__mutmut_11(service: ServiceRaw, allowlist: tuple[str, ...]) -> str | None:
    if is_allowlisted(service["name"], allowlist):
        return _cfg.allowlisted_reason
    if is_internal_load_balancer(service["XXannotationsXX"], _cfg.internal_load_balancer_annotations):
        return _cfg.internal_lb_reason
    return None


def x_exclusion_reason__mutmut_12(service: ServiceRaw, allowlist: tuple[str, ...]) -> str | None:
    if is_allowlisted(service["name"], allowlist):
        return _cfg.allowlisted_reason
    if is_internal_load_balancer(service["ANNOTATIONS"], _cfg.internal_load_balancer_annotations):
        return _cfg.internal_lb_reason
    return None

mutants_x_exclusion_reason__mutmut['_mutmut_orig'] = x_exclusion_reason__mutmut_orig # type: ignore # mutmut generated
mutants_x_exclusion_reason__mutmut['x_exclusion_reason__mutmut_1'] = x_exclusion_reason__mutmut_1 # type: ignore # mutmut generated
mutants_x_exclusion_reason__mutmut['x_exclusion_reason__mutmut_2'] = x_exclusion_reason__mutmut_2 # type: ignore # mutmut generated
mutants_x_exclusion_reason__mutmut['x_exclusion_reason__mutmut_3'] = x_exclusion_reason__mutmut_3 # type: ignore # mutmut generated
mutants_x_exclusion_reason__mutmut['x_exclusion_reason__mutmut_4'] = x_exclusion_reason__mutmut_4 # type: ignore # mutmut generated
mutants_x_exclusion_reason__mutmut['x_exclusion_reason__mutmut_5'] = x_exclusion_reason__mutmut_5 # type: ignore # mutmut generated
mutants_x_exclusion_reason__mutmut['x_exclusion_reason__mutmut_6'] = x_exclusion_reason__mutmut_6 # type: ignore # mutmut generated
mutants_x_exclusion_reason__mutmut['x_exclusion_reason__mutmut_7'] = x_exclusion_reason__mutmut_7 # type: ignore # mutmut generated
mutants_x_exclusion_reason__mutmut['x_exclusion_reason__mutmut_8'] = x_exclusion_reason__mutmut_8 # type: ignore # mutmut generated
mutants_x_exclusion_reason__mutmut['x_exclusion_reason__mutmut_9'] = x_exclusion_reason__mutmut_9 # type: ignore # mutmut generated
mutants_x_exclusion_reason__mutmut['x_exclusion_reason__mutmut_10'] = x_exclusion_reason__mutmut_10 # type: ignore # mutmut generated
mutants_x_exclusion_reason__mutmut['x_exclusion_reason__mutmut_11'] = x_exclusion_reason__mutmut_11 # type: ignore # mutmut generated
mutants_x_exclusion_reason__mutmut['x_exclusion_reason__mutmut_12'] = x_exclusion_reason__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_build_finding__mutmut)
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


def x_build_finding__mutmut_orig(service: ServiceRaw) -> ExternalExposureFinding:
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


def x_build_finding__mutmut_1(service: ServiceRaw) -> ExternalExposureFinding:
    base_severity = None
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


def x_build_finding__mutmut_2(service: ServiceRaw) -> ExternalExposureFinding:
    base_severity = classify_base_severity(None, _cfg.critical_ports, _cfg.medium_ports)
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


def x_build_finding__mutmut_3(service: ServiceRaw) -> ExternalExposureFinding:
    base_severity = classify_base_severity(service["ports"], None, _cfg.medium_ports)
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


def x_build_finding__mutmut_4(service: ServiceRaw) -> ExternalExposureFinding:
    base_severity = classify_base_severity(service["ports"], _cfg.critical_ports, None)
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


def x_build_finding__mutmut_5(service: ServiceRaw) -> ExternalExposureFinding:
    base_severity = classify_base_severity(_cfg.critical_ports, _cfg.medium_ports)
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


def x_build_finding__mutmut_6(service: ServiceRaw) -> ExternalExposureFinding:
    base_severity = classify_base_severity(service["ports"], _cfg.medium_ports)
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


def x_build_finding__mutmut_7(service: ServiceRaw) -> ExternalExposureFinding:
    base_severity = classify_base_severity(service["ports"], _cfg.critical_ports, )
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


def x_build_finding__mutmut_8(service: ServiceRaw) -> ExternalExposureFinding:
    base_severity = classify_base_severity(service["XXportsXX"], _cfg.critical_ports, _cfg.medium_ports)
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


def x_build_finding__mutmut_9(service: ServiceRaw) -> ExternalExposureFinding:
    base_severity = classify_base_severity(service["PORTS"], _cfg.critical_ports, _cfg.medium_ports)
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


def x_build_finding__mutmut_10(service: ServiceRaw) -> ExternalExposureFinding:
    base_severity = classify_base_severity(service["ports"], _cfg.critical_ports, _cfg.medium_ports)
    risk_level = None
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


def x_build_finding__mutmut_11(service: ServiceRaw) -> ExternalExposureFinding:
    base_severity = classify_base_severity(service["ports"], _cfg.critical_ports, _cfg.medium_ports)
    risk_level = classify_risk_level(
        base_severity=None,
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


def x_build_finding__mutmut_12(service: ServiceRaw) -> ExternalExposureFinding:
    base_severity = classify_base_severity(service["ports"], _cfg.critical_ports, _cfg.medium_ports)
    risk_level = classify_risk_level(
        base_severity=base_severity,
        service_type=None,  # type: ignore[arg-type]
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


def x_build_finding__mutmut_13(service: ServiceRaw) -> ExternalExposureFinding:
    base_severity = classify_base_severity(service["ports"], _cfg.critical_ports, _cfg.medium_ports)
    risk_level = classify_risk_level(
        base_severity=base_severity,
        service_type=service["service_type"],  # type: ignore[arg-type]
        namespace=None,
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


def x_build_finding__mutmut_14(service: ServiceRaw) -> ExternalExposureFinding:
    base_severity = classify_base_severity(service["ports"], _cfg.critical_ports, _cfg.medium_ports)
    risk_level = classify_risk_level(
        base_severity=base_severity,
        service_type=service["service_type"],  # type: ignore[arg-type]
        namespace=service["namespace"],
        production_namespace=None,
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


def x_build_finding__mutmut_15(service: ServiceRaw) -> ExternalExposureFinding:
    base_severity = classify_base_severity(service["ports"], _cfg.critical_ports, _cfg.medium_ports)
    risk_level = classify_risk_level(
        base_severity=base_severity,
        service_type=service["service_type"],  # type: ignore[arg-type]
        namespace=service["namespace"],
        production_namespace=_cfg.production_namespace,
        has_source_ranges=None,
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


def x_build_finding__mutmut_16(service: ServiceRaw) -> ExternalExposureFinding:
    base_severity = classify_base_severity(service["ports"], _cfg.critical_ports, _cfg.medium_ports)
    risk_level = classify_risk_level(
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


def x_build_finding__mutmut_17(service: ServiceRaw) -> ExternalExposureFinding:
    base_severity = classify_base_severity(service["ports"], _cfg.critical_ports, _cfg.medium_ports)
    risk_level = classify_risk_level(
        base_severity=base_severity,
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


def x_build_finding__mutmut_18(service: ServiceRaw) -> ExternalExposureFinding:
    base_severity = classify_base_severity(service["ports"], _cfg.critical_ports, _cfg.medium_ports)
    risk_level = classify_risk_level(
        base_severity=base_severity,
        service_type=service["service_type"],  # type: ignore[arg-type]
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


def x_build_finding__mutmut_19(service: ServiceRaw) -> ExternalExposureFinding:
    base_severity = classify_base_severity(service["ports"], _cfg.critical_ports, _cfg.medium_ports)
    risk_level = classify_risk_level(
        base_severity=base_severity,
        service_type=service["service_type"],  # type: ignore[arg-type]
        namespace=service["namespace"],
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


def x_build_finding__mutmut_20(service: ServiceRaw) -> ExternalExposureFinding:
    base_severity = classify_base_severity(service["ports"], _cfg.critical_ports, _cfg.medium_ports)
    risk_level = classify_risk_level(
        base_severity=base_severity,
        service_type=service["service_type"],  # type: ignore[arg-type]
        namespace=service["namespace"],
        production_namespace=_cfg.production_namespace,
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


def x_build_finding__mutmut_21(service: ServiceRaw) -> ExternalExposureFinding:
    base_severity = classify_base_severity(service["ports"], _cfg.critical_ports, _cfg.medium_ports)
    risk_level = classify_risk_level(
        base_severity=base_severity,
        service_type=service["XXservice_typeXX"],  # type: ignore[arg-type]
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


def x_build_finding__mutmut_22(service: ServiceRaw) -> ExternalExposureFinding:
    base_severity = classify_base_severity(service["ports"], _cfg.critical_ports, _cfg.medium_ports)
    risk_level = classify_risk_level(
        base_severity=base_severity,
        service_type=service["SERVICE_TYPE"],  # type: ignore[arg-type]
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


def x_build_finding__mutmut_23(service: ServiceRaw) -> ExternalExposureFinding:
    base_severity = classify_base_severity(service["ports"], _cfg.critical_ports, _cfg.medium_ports)
    risk_level = classify_risk_level(
        base_severity=base_severity,
        service_type=service["service_type"],  # type: ignore[arg-type]
        namespace=service["XXnamespaceXX"],
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


def x_build_finding__mutmut_24(service: ServiceRaw) -> ExternalExposureFinding:
    base_severity = classify_base_severity(service["ports"], _cfg.critical_ports, _cfg.medium_ports)
    risk_level = classify_risk_level(
        base_severity=base_severity,
        service_type=service["service_type"],  # type: ignore[arg-type]
        namespace=service["NAMESPACE"],
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


def x_build_finding__mutmut_25(service: ServiceRaw) -> ExternalExposureFinding:
    base_severity = classify_base_severity(service["ports"], _cfg.critical_ports, _cfg.medium_ports)
    risk_level = classify_risk_level(
        base_severity=base_severity,
        service_type=service["service_type"],  # type: ignore[arg-type]
        namespace=service["namespace"],
        production_namespace=_cfg.production_namespace,
        has_source_ranges=service["XXhas_source_rangesXX"],
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


def x_build_finding__mutmut_26(service: ServiceRaw) -> ExternalExposureFinding:
    base_severity = classify_base_severity(service["ports"], _cfg.critical_ports, _cfg.medium_ports)
    risk_level = classify_risk_level(
        base_severity=base_severity,
        service_type=service["service_type"],  # type: ignore[arg-type]
        namespace=service["namespace"],
        production_namespace=_cfg.production_namespace,
        has_source_ranges=service["HAS_SOURCE_RANGES"],
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


def x_build_finding__mutmut_27(service: ServiceRaw) -> ExternalExposureFinding:
    base_severity = classify_base_severity(service["ports"], _cfg.critical_ports, _cfg.medium_ports)
    risk_level = classify_risk_level(
        base_severity=base_severity,
        service_type=service["service_type"],  # type: ignore[arg-type]
        namespace=service["namespace"],
        production_namespace=_cfg.production_namespace,
        has_source_ranges=service["has_source_ranges"],
    )
    is_pending = None

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


def x_build_finding__mutmut_28(service: ServiceRaw) -> ExternalExposureFinding:
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
        and service["external_ip"] is None or service["external_hostname"] is None
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


def x_build_finding__mutmut_29(service: ServiceRaw) -> ExternalExposureFinding:
    base_severity = classify_base_severity(service["ports"], _cfg.critical_ports, _cfg.medium_ports)
    risk_level = classify_risk_level(
        base_severity=base_severity,
        service_type=service["service_type"],  # type: ignore[arg-type]
        namespace=service["namespace"],
        production_namespace=_cfg.production_namespace,
        has_source_ranges=service["has_source_ranges"],
    )
    is_pending = (
        service["service_type"] == "LoadBalancer" or service["external_ip"] is None
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


def x_build_finding__mutmut_30(service: ServiceRaw) -> ExternalExposureFinding:
    base_severity = classify_base_severity(service["ports"], _cfg.critical_ports, _cfg.medium_ports)
    risk_level = classify_risk_level(
        base_severity=base_severity,
        service_type=service["service_type"],  # type: ignore[arg-type]
        namespace=service["namespace"],
        production_namespace=_cfg.production_namespace,
        has_source_ranges=service["has_source_ranges"],
    )
    is_pending = (
        service["XXservice_typeXX"] == "LoadBalancer"
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


def x_build_finding__mutmut_31(service: ServiceRaw) -> ExternalExposureFinding:
    base_severity = classify_base_severity(service["ports"], _cfg.critical_ports, _cfg.medium_ports)
    risk_level = classify_risk_level(
        base_severity=base_severity,
        service_type=service["service_type"],  # type: ignore[arg-type]
        namespace=service["namespace"],
        production_namespace=_cfg.production_namespace,
        has_source_ranges=service["has_source_ranges"],
    )
    is_pending = (
        service["SERVICE_TYPE"] == "LoadBalancer"
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


def x_build_finding__mutmut_32(service: ServiceRaw) -> ExternalExposureFinding:
    base_severity = classify_base_severity(service["ports"], _cfg.critical_ports, _cfg.medium_ports)
    risk_level = classify_risk_level(
        base_severity=base_severity,
        service_type=service["service_type"],  # type: ignore[arg-type]
        namespace=service["namespace"],
        production_namespace=_cfg.production_namespace,
        has_source_ranges=service["has_source_ranges"],
    )
    is_pending = (
        service["service_type"] != "LoadBalancer"
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


def x_build_finding__mutmut_33(service: ServiceRaw) -> ExternalExposureFinding:
    base_severity = classify_base_severity(service["ports"], _cfg.critical_ports, _cfg.medium_ports)
    risk_level = classify_risk_level(
        base_severity=base_severity,
        service_type=service["service_type"],  # type: ignore[arg-type]
        namespace=service["namespace"],
        production_namespace=_cfg.production_namespace,
        has_source_ranges=service["has_source_ranges"],
    )
    is_pending = (
        service["service_type"] == "XXLoadBalancerXX"
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


def x_build_finding__mutmut_34(service: ServiceRaw) -> ExternalExposureFinding:
    base_severity = classify_base_severity(service["ports"], _cfg.critical_ports, _cfg.medium_ports)
    risk_level = classify_risk_level(
        base_severity=base_severity,
        service_type=service["service_type"],  # type: ignore[arg-type]
        namespace=service["namespace"],
        production_namespace=_cfg.production_namespace,
        has_source_ranges=service["has_source_ranges"],
    )
    is_pending = (
        service["service_type"] == "loadbalancer"
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


def x_build_finding__mutmut_35(service: ServiceRaw) -> ExternalExposureFinding:
    base_severity = classify_base_severity(service["ports"], _cfg.critical_ports, _cfg.medium_ports)
    risk_level = classify_risk_level(
        base_severity=base_severity,
        service_type=service["service_type"],  # type: ignore[arg-type]
        namespace=service["namespace"],
        production_namespace=_cfg.production_namespace,
        has_source_ranges=service["has_source_ranges"],
    )
    is_pending = (
        service["service_type"] == "LOADBALANCER"
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


def x_build_finding__mutmut_36(service: ServiceRaw) -> ExternalExposureFinding:
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
        and service["XXexternal_ipXX"] is None
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


def x_build_finding__mutmut_37(service: ServiceRaw) -> ExternalExposureFinding:
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
        and service["EXTERNAL_IP"] is None
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


def x_build_finding__mutmut_38(service: ServiceRaw) -> ExternalExposureFinding:
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
        and service["external_ip"] is not None
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


def x_build_finding__mutmut_39(service: ServiceRaw) -> ExternalExposureFinding:
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
        and service["XXexternal_hostnameXX"] is None
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


def x_build_finding__mutmut_40(service: ServiceRaw) -> ExternalExposureFinding:
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
        and service["EXTERNAL_HOSTNAME"] is None
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


def x_build_finding__mutmut_41(service: ServiceRaw) -> ExternalExposureFinding:
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
        and service["external_hostname"] is not None
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


def x_build_finding__mutmut_42(service: ServiceRaw) -> ExternalExposureFinding:
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
        name=None,
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


def x_build_finding__mutmut_43(service: ServiceRaw) -> ExternalExposureFinding:
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
        namespace=None,
        service_type=service["service_type"],  # type: ignore[arg-type]
        ports=service["ports"],
        external_ip=service["external_ip"],
        external_hostname=service["external_hostname"],
        node_port=service["node_port"],
        is_pending=is_pending,
        risk_level=risk_level,
        note=_cfg.source_ranges_note if service["has_source_ranges"] else None,
    )


def x_build_finding__mutmut_44(service: ServiceRaw) -> ExternalExposureFinding:
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
        service_type=None,  # type: ignore[arg-type]
        ports=service["ports"],
        external_ip=service["external_ip"],
        external_hostname=service["external_hostname"],
        node_port=service["node_port"],
        is_pending=is_pending,
        risk_level=risk_level,
        note=_cfg.source_ranges_note if service["has_source_ranges"] else None,
    )


def x_build_finding__mutmut_45(service: ServiceRaw) -> ExternalExposureFinding:
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
        ports=None,
        external_ip=service["external_ip"],
        external_hostname=service["external_hostname"],
        node_port=service["node_port"],
        is_pending=is_pending,
        risk_level=risk_level,
        note=_cfg.source_ranges_note if service["has_source_ranges"] else None,
    )


def x_build_finding__mutmut_46(service: ServiceRaw) -> ExternalExposureFinding:
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
        external_ip=None,
        external_hostname=service["external_hostname"],
        node_port=service["node_port"],
        is_pending=is_pending,
        risk_level=risk_level,
        note=_cfg.source_ranges_note if service["has_source_ranges"] else None,
    )


def x_build_finding__mutmut_47(service: ServiceRaw) -> ExternalExposureFinding:
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
        external_hostname=None,
        node_port=service["node_port"],
        is_pending=is_pending,
        risk_level=risk_level,
        note=_cfg.source_ranges_note if service["has_source_ranges"] else None,
    )


def x_build_finding__mutmut_48(service: ServiceRaw) -> ExternalExposureFinding:
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
        node_port=None,
        is_pending=is_pending,
        risk_level=risk_level,
        note=_cfg.source_ranges_note if service["has_source_ranges"] else None,
    )


def x_build_finding__mutmut_49(service: ServiceRaw) -> ExternalExposureFinding:
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
        is_pending=None,
        risk_level=risk_level,
        note=_cfg.source_ranges_note if service["has_source_ranges"] else None,
    )


def x_build_finding__mutmut_50(service: ServiceRaw) -> ExternalExposureFinding:
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
        risk_level=None,
        note=_cfg.source_ranges_note if service["has_source_ranges"] else None,
    )


def x_build_finding__mutmut_51(service: ServiceRaw) -> ExternalExposureFinding:
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
        note=None,
    )


def x_build_finding__mutmut_52(service: ServiceRaw) -> ExternalExposureFinding:
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


def x_build_finding__mutmut_53(service: ServiceRaw) -> ExternalExposureFinding:
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
        service_type=service["service_type"],  # type: ignore[arg-type]
        ports=service["ports"],
        external_ip=service["external_ip"],
        external_hostname=service["external_hostname"],
        node_port=service["node_port"],
        is_pending=is_pending,
        risk_level=risk_level,
        note=_cfg.source_ranges_note if service["has_source_ranges"] else None,
    )


def x_build_finding__mutmut_54(service: ServiceRaw) -> ExternalExposureFinding:
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
        ports=service["ports"],
        external_ip=service["external_ip"],
        external_hostname=service["external_hostname"],
        node_port=service["node_port"],
        is_pending=is_pending,
        risk_level=risk_level,
        note=_cfg.source_ranges_note if service["has_source_ranges"] else None,
    )


def x_build_finding__mutmut_55(service: ServiceRaw) -> ExternalExposureFinding:
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
        external_ip=service["external_ip"],
        external_hostname=service["external_hostname"],
        node_port=service["node_port"],
        is_pending=is_pending,
        risk_level=risk_level,
        note=_cfg.source_ranges_note if service["has_source_ranges"] else None,
    )


def x_build_finding__mutmut_56(service: ServiceRaw) -> ExternalExposureFinding:
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
        external_hostname=service["external_hostname"],
        node_port=service["node_port"],
        is_pending=is_pending,
        risk_level=risk_level,
        note=_cfg.source_ranges_note if service["has_source_ranges"] else None,
    )


def x_build_finding__mutmut_57(service: ServiceRaw) -> ExternalExposureFinding:
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
        node_port=service["node_port"],
        is_pending=is_pending,
        risk_level=risk_level,
        note=_cfg.source_ranges_note if service["has_source_ranges"] else None,
    )


def x_build_finding__mutmut_58(service: ServiceRaw) -> ExternalExposureFinding:
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
        is_pending=is_pending,
        risk_level=risk_level,
        note=_cfg.source_ranges_note if service["has_source_ranges"] else None,
    )


def x_build_finding__mutmut_59(service: ServiceRaw) -> ExternalExposureFinding:
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
        risk_level=risk_level,
        note=_cfg.source_ranges_note if service["has_source_ranges"] else None,
    )


def x_build_finding__mutmut_60(service: ServiceRaw) -> ExternalExposureFinding:
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
        note=_cfg.source_ranges_note if service["has_source_ranges"] else None,
    )


def x_build_finding__mutmut_61(service: ServiceRaw) -> ExternalExposureFinding:
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
        )


def x_build_finding__mutmut_62(service: ServiceRaw) -> ExternalExposureFinding:
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
        name=service["XXnameXX"],
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


def x_build_finding__mutmut_63(service: ServiceRaw) -> ExternalExposureFinding:
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
        name=service["NAME"],
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


def x_build_finding__mutmut_64(service: ServiceRaw) -> ExternalExposureFinding:
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
        namespace=service["XXnamespaceXX"],
        service_type=service["service_type"],  # type: ignore[arg-type]
        ports=service["ports"],
        external_ip=service["external_ip"],
        external_hostname=service["external_hostname"],
        node_port=service["node_port"],
        is_pending=is_pending,
        risk_level=risk_level,
        note=_cfg.source_ranges_note if service["has_source_ranges"] else None,
    )


def x_build_finding__mutmut_65(service: ServiceRaw) -> ExternalExposureFinding:
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
        namespace=service["NAMESPACE"],
        service_type=service["service_type"],  # type: ignore[arg-type]
        ports=service["ports"],
        external_ip=service["external_ip"],
        external_hostname=service["external_hostname"],
        node_port=service["node_port"],
        is_pending=is_pending,
        risk_level=risk_level,
        note=_cfg.source_ranges_note if service["has_source_ranges"] else None,
    )


def x_build_finding__mutmut_66(service: ServiceRaw) -> ExternalExposureFinding:
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
        service_type=service["XXservice_typeXX"],  # type: ignore[arg-type]
        ports=service["ports"],
        external_ip=service["external_ip"],
        external_hostname=service["external_hostname"],
        node_port=service["node_port"],
        is_pending=is_pending,
        risk_level=risk_level,
        note=_cfg.source_ranges_note if service["has_source_ranges"] else None,
    )


def x_build_finding__mutmut_67(service: ServiceRaw) -> ExternalExposureFinding:
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
        service_type=service["SERVICE_TYPE"],  # type: ignore[arg-type]
        ports=service["ports"],
        external_ip=service["external_ip"],
        external_hostname=service["external_hostname"],
        node_port=service["node_port"],
        is_pending=is_pending,
        risk_level=risk_level,
        note=_cfg.source_ranges_note if service["has_source_ranges"] else None,
    )


def x_build_finding__mutmut_68(service: ServiceRaw) -> ExternalExposureFinding:
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
        ports=service["XXportsXX"],
        external_ip=service["external_ip"],
        external_hostname=service["external_hostname"],
        node_port=service["node_port"],
        is_pending=is_pending,
        risk_level=risk_level,
        note=_cfg.source_ranges_note if service["has_source_ranges"] else None,
    )


def x_build_finding__mutmut_69(service: ServiceRaw) -> ExternalExposureFinding:
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
        ports=service["PORTS"],
        external_ip=service["external_ip"],
        external_hostname=service["external_hostname"],
        node_port=service["node_port"],
        is_pending=is_pending,
        risk_level=risk_level,
        note=_cfg.source_ranges_note if service["has_source_ranges"] else None,
    )


def x_build_finding__mutmut_70(service: ServiceRaw) -> ExternalExposureFinding:
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
        external_ip=service["XXexternal_ipXX"],
        external_hostname=service["external_hostname"],
        node_port=service["node_port"],
        is_pending=is_pending,
        risk_level=risk_level,
        note=_cfg.source_ranges_note if service["has_source_ranges"] else None,
    )


def x_build_finding__mutmut_71(service: ServiceRaw) -> ExternalExposureFinding:
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
        external_ip=service["EXTERNAL_IP"],
        external_hostname=service["external_hostname"],
        node_port=service["node_port"],
        is_pending=is_pending,
        risk_level=risk_level,
        note=_cfg.source_ranges_note if service["has_source_ranges"] else None,
    )


def x_build_finding__mutmut_72(service: ServiceRaw) -> ExternalExposureFinding:
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
        external_hostname=service["XXexternal_hostnameXX"],
        node_port=service["node_port"],
        is_pending=is_pending,
        risk_level=risk_level,
        note=_cfg.source_ranges_note if service["has_source_ranges"] else None,
    )


def x_build_finding__mutmut_73(service: ServiceRaw) -> ExternalExposureFinding:
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
        external_hostname=service["EXTERNAL_HOSTNAME"],
        node_port=service["node_port"],
        is_pending=is_pending,
        risk_level=risk_level,
        note=_cfg.source_ranges_note if service["has_source_ranges"] else None,
    )


def x_build_finding__mutmut_74(service: ServiceRaw) -> ExternalExposureFinding:
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
        node_port=service["XXnode_portXX"],
        is_pending=is_pending,
        risk_level=risk_level,
        note=_cfg.source_ranges_note if service["has_source_ranges"] else None,
    )


def x_build_finding__mutmut_75(service: ServiceRaw) -> ExternalExposureFinding:
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
        node_port=service["NODE_PORT"],
        is_pending=is_pending,
        risk_level=risk_level,
        note=_cfg.source_ranges_note if service["has_source_ranges"] else None,
    )


def x_build_finding__mutmut_76(service: ServiceRaw) -> ExternalExposureFinding:
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
        note=_cfg.source_ranges_note if service["XXhas_source_rangesXX"] else None,
    )


def x_build_finding__mutmut_77(service: ServiceRaw) -> ExternalExposureFinding:
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
        note=_cfg.source_ranges_note if service["HAS_SOURCE_RANGES"] else None,
    )

mutants_x_build_finding__mutmut['_mutmut_orig'] = x_build_finding__mutmut_orig # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_1'] = x_build_finding__mutmut_1 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_2'] = x_build_finding__mutmut_2 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_3'] = x_build_finding__mutmut_3 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_4'] = x_build_finding__mutmut_4 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_5'] = x_build_finding__mutmut_5 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_6'] = x_build_finding__mutmut_6 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_7'] = x_build_finding__mutmut_7 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_8'] = x_build_finding__mutmut_8 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_9'] = x_build_finding__mutmut_9 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_10'] = x_build_finding__mutmut_10 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_11'] = x_build_finding__mutmut_11 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_12'] = x_build_finding__mutmut_12 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_13'] = x_build_finding__mutmut_13 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_14'] = x_build_finding__mutmut_14 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_15'] = x_build_finding__mutmut_15 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_16'] = x_build_finding__mutmut_16 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_17'] = x_build_finding__mutmut_17 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_18'] = x_build_finding__mutmut_18 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_19'] = x_build_finding__mutmut_19 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_20'] = x_build_finding__mutmut_20 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_21'] = x_build_finding__mutmut_21 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_22'] = x_build_finding__mutmut_22 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_23'] = x_build_finding__mutmut_23 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_24'] = x_build_finding__mutmut_24 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_25'] = x_build_finding__mutmut_25 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_26'] = x_build_finding__mutmut_26 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_27'] = x_build_finding__mutmut_27 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_28'] = x_build_finding__mutmut_28 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_29'] = x_build_finding__mutmut_29 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_30'] = x_build_finding__mutmut_30 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_31'] = x_build_finding__mutmut_31 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_32'] = x_build_finding__mutmut_32 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_33'] = x_build_finding__mutmut_33 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_34'] = x_build_finding__mutmut_34 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_35'] = x_build_finding__mutmut_35 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_36'] = x_build_finding__mutmut_36 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_37'] = x_build_finding__mutmut_37 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_38'] = x_build_finding__mutmut_38 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_39'] = x_build_finding__mutmut_39 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_40'] = x_build_finding__mutmut_40 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_41'] = x_build_finding__mutmut_41 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_42'] = x_build_finding__mutmut_42 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_43'] = x_build_finding__mutmut_43 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_44'] = x_build_finding__mutmut_44 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_45'] = x_build_finding__mutmut_45 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_46'] = x_build_finding__mutmut_46 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_47'] = x_build_finding__mutmut_47 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_48'] = x_build_finding__mutmut_48 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_49'] = x_build_finding__mutmut_49 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_50'] = x_build_finding__mutmut_50 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_51'] = x_build_finding__mutmut_51 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_52'] = x_build_finding__mutmut_52 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_53'] = x_build_finding__mutmut_53 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_54'] = x_build_finding__mutmut_54 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_55'] = x_build_finding__mutmut_55 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_56'] = x_build_finding__mutmut_56 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_57'] = x_build_finding__mutmut_57 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_58'] = x_build_finding__mutmut_58 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_59'] = x_build_finding__mutmut_59 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_60'] = x_build_finding__mutmut_60 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_61'] = x_build_finding__mutmut_61 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_62'] = x_build_finding__mutmut_62 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_63'] = x_build_finding__mutmut_63 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_64'] = x_build_finding__mutmut_64 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_65'] = x_build_finding__mutmut_65 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_66'] = x_build_finding__mutmut_66 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_67'] = x_build_finding__mutmut_67 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_68'] = x_build_finding__mutmut_68 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_69'] = x_build_finding__mutmut_69 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_70'] = x_build_finding__mutmut_70 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_71'] = x_build_finding__mutmut_71 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_72'] = x_build_finding__mutmut_72 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_73'] = x_build_finding__mutmut_73 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_74'] = x_build_finding__mutmut_74 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_75'] = x_build_finding__mutmut_75 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_76'] = x_build_finding__mutmut_76 # type: ignore # mutmut generated
mutants_x_build_finding__mutmut['x_build_finding__mutmut_77'] = x_build_finding__mutmut_77 # type: ignore # mutmut generated
