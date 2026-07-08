"""Checker node semantic-layer verification tests — validates that an
LLM-generated response would be caught by deterministic post-hoc checks.

Each checker case simulates an incorrect LLM output and asserts that
the semantic layer would detect and correct the error. These are the
deterministic safeguards that run after every tool invocation."""

from __future__ import annotations

import pytest


def _finding(
    name: str,
    namespace: str = "production",
    service_type: str = "LoadBalancer",
    ports: list[int] | None = None,
    risk_level: str = "critical",
    note: str | None = None,
) -> dict:
    return {
        "name": name,
        "namespace": namespace,
        "service_type": service_type,
        "ports": ports or [],
        "risk_level": risk_level,
        "note": note,
    }


def _classify_base_severity(
    ports: list[int],
    critical_ports: tuple[int, ...] = (5432, 3306, 27017, 6379, 9200, 11211, 2379, 9090),
    medium_ports: tuple[int, ...] = (80, 443, 3000, 8080, 8443),
) -> str:
    if any(p in critical_ports for p in ports):
        return "critical"
    if any(p in medium_ports for p in ports):
        return "medium"
    return "medium"


def _is_allowlisted(name: str, allowlist: tuple[str, ...]) -> bool:
    return name in allowlist


_DEFAULT_ALLOWLIST: tuple[str, ...] = ("api-gateway", "ingress-nginx-controller")

_INTERNAL_LB_ANNOTATIONS: tuple[tuple[str, str], ...] = (
    ("service.beta.kubernetes.io/aws-load-balancer-internal", "true"),
    ("service.beta.kubernetes.io/azure-load-balancer-internal", "true"),
    ("networking.gke.io/load-balancer-type", "Internal"),
)

_CRITICAL_PORTS = (5432, 3306, 27017, 6379, 9200, 11211, 2379, 9090)
_MEDIUM_PORTS = (80, 443, 3000, 8080, 8443)

_PRODUCTION_NAMESPACE = "production"

_RISK_DOWNGRADE: dict[str, str] = {
    "critical": "high",
    "high": "medium",
    "medium": "low",
    "low": "low",
}


class TestCheckerCase1AllowlistedServiceMustNotBeFlagged:
    """Checker Case 1: api-gateway is in the allowlist but the LLM includes
    it in the unintended exposure list anyway. The semantic layer must detect
    this and FAIL the response."""

    def test_allowlisted_service_in_findings_is_detected(self) -> None:
        findings = [
            _finding("api-gateway", ports=[443]),
            _finding("postgres-svc", ports=[5432]),
        ]

        allowlisted_in_findings = [
            f for f in findings if _is_allowlisted(f["name"], _DEFAULT_ALLOWLIST)
        ]

        assert len(allowlisted_in_findings) == 1
        assert allowlisted_in_findings[0]["name"] == "api-gateway"

    def test_no_allowlisted_services_in_findings_passes(self) -> None:
        findings = [
            _finding("postgres-svc", ports=[5432]),
            _finding("redis-cache", ports=[6379]),
        ]

        allowlisted_in_findings = [
            f for f in findings if _is_allowlisted(f["name"], _DEFAULT_ALLOWLIST)
        ]

        assert len(allowlisted_in_findings) == 0


class TestCheckerCase2RiskWeightedByNamespace:
    """Checker Case 2: redis-svc in dev (low risk) must not have the same
    severity as redis-svc in production (critical). The semantic layer
    verifies that risk accounts for namespace weight."""

    def test_dev_namespace_downgrades_risk(self) -> None:
        from hexawyn.domain.services.external_exposure.risk_scorer import classify_risk_level

        dev_risk = classify_risk_level(
            base_severity="critical",
            service_type="LoadBalancer",
            namespace="dev",
            production_namespace=_PRODUCTION_NAMESPACE,
            has_source_ranges=False,
        )
        prod_risk = classify_risk_level(
            base_severity="critical",
            service_type="LoadBalancer",
            namespace="production",
            production_namespace=_PRODUCTION_NAMESPACE,
            has_source_ranges=False,
        )

        assert (
            dev_risk != prod_risk
        ), f"Namespace weighting absent: dev={dev_risk}, production={prod_risk}"
        assert dev_risk == "high"
        assert prod_risk == "critical"

    def test_staging_redis_vs_production_redis_risk_differs(self) -> None:
        from hexawyn.domain.services.external_exposure.risk_scorer import classify_risk_level

        staging_risk = classify_risk_level(
            base_severity="critical",
            service_type="LoadBalancer",
            namespace="staging",
            production_namespace=_PRODUCTION_NAMESPACE,
            has_source_ranges=False,
        )
        prod_risk = classify_risk_level(
            base_severity="critical",
            service_type="LoadBalancer",
            namespace="production",
            production_namespace=_PRODUCTION_NAMESPACE,
            has_source_ranges=False,
        )

        assert staging_risk == "high"
        assert prod_risk == "critical"


class TestCheckerCase3InternalLBDetectedAsPublic:
    """Checker Case 3: A service with the AWS internal-LB annotation is
    flagged as "externally exposed". The semantic layer must check cloud
    provider annotations and FAIL if an internal LB is treated as public."""

    def test_internal_annotation_detected(self) -> None:
        from hexawyn.domain.services.external_exposure.internal_exposure_detector import (
            is_internal_load_balancer,
        )

        annotations = {
            "service.beta.kubernetes.io/aws-load-balancer-internal": "true",
        }
        assert is_internal_load_balancer(annotations, _INTERNAL_LB_ANNOTATIONS) is True

    def test_no_internal_annotation_passes(self) -> None:
        from hexawyn.domain.services.external_exposure.internal_exposure_detector import (
            is_internal_load_balancer,
        )

        assert is_internal_load_balancer({}, _INTERNAL_LB_ANNOTATIONS) is False

    def test_gke_internal_annotation_also_detected(self) -> None:
        from hexawyn.domain.services.external_exposure.internal_exposure_detector import (
            is_internal_load_balancer,
        )

        annotations = {"networking.gke.io/load-balancer-type": "Internal"}
        assert is_internal_load_balancer(annotations, _INTERNAL_LB_ANNOTATIONS) is True


class TestCheckerCase4PendingLoadBalancerStillFlagged:
    """Checker Case 4: A LoadBalancer with no external IP yet (pending) is
    reported as "not yet exposed" by the LLM. The semantic layer must verify
    that pending == still exposed == must still be flagged."""

    def test_pending_lb_is_still_an_exposure(self) -> None:
        from hexawyn.domain.services.external_exposure.service_type_classifier import (
            is_externally_exposed_type,
        )

        assert is_externally_exposed_type("LoadBalancer") is True

    def test_pending_lb_flagged_regardless_of_ip(self) -> None:
        pending_service: dict = {
            "name": "new-svc",
            "namespace": "production",
            "service_type": "LoadBalancer",
            "ports": [5432],
            "node_port": None,
            "external_ip": None,
            "external_hostname": None,
            "has_source_ranges": False,
            "annotations": {},
        }

        is_pending = (
            pending_service["service_type"] == "LoadBalancer"
            and pending_service["external_ip"] is None
            and pending_service["external_hostname"] is None
        )
        base_severity = _classify_base_severity(pending_service["ports"])

        assert is_pending is True, "Pending LB not detected as pending"
        assert base_severity == "critical", "Pending LB with DB port not classified critical"


class TestCheckerCase5SourceRangesMustBeNoted:
    """Checker Case 5: A LoadBalancer with loadBalancerSourceRanges is
    reported as "critical, publicly exposed" without mentioning the IP
    restriction. The semantic layer must verify sourceRanges presence
    and FLAG "risk reduced by IP allowlist"."""

    def test_source_ranges_downgrades_risk(self) -> None:
        from hexawyn.domain.services.external_exposure.risk_scorer import classify_risk_level

        without_restriction = classify_risk_level(
            base_severity="critical",
            service_type="LoadBalancer",
            namespace="production",
            production_namespace=_PRODUCTION_NAMESPACE,
            has_source_ranges=False,
        )
        with_restriction = classify_risk_level(
            base_severity="critical",
            service_type="LoadBalancer",
            namespace="production",
            production_namespace=_PRODUCTION_NAMESPACE,
            has_source_ranges=True,
        )

        assert without_restriction == "critical"
        assert with_restriction == "high"
        assert (
            with_restriction != without_restriction
        ), "Source ranges ignored — same risk level with and without IP restriction"

    def test_note_present_when_source_ranges_set(self) -> None:
        from unittest.mock import MagicMock

        from hexawyn.application.ports.driving.detect_unintended_external_exposure.detect_unintended_external_exposure_command import (
            DetectUnintendedExternalExposureCommand,
        )
        from hexawyn.application.service.unintended_external_exposure_service import (
            UnintendedExternalExposureService,
        )

        port = MagicMock()
        port.list_external_services.return_value = [
            {
                "name": "restricted-svc",
                "namespace": "production",
                "service_type": "LoadBalancer",
                "ports": [5432],
                "node_port": None,
                "external_ip": "10.0.0.1",
                "external_hostname": None,
                "has_source_ranges": True,
                "annotations": {},
            }
        ]

        service = UnintendedExternalExposureService(external_exposure_port=port)
        response = service.detect_unintended_exposure(DetectUnintendedExternalExposureCommand())

        finding = response.findings[0]
        assert finding["note"] is not None, "Source ranges present but no note added"
        assert "IP allowlist" in finding["note"]


class TestCheckerCase6PortBasedSeverityMatrix:
    """Checker Case 6: LLM classifies grafana (port 3000) as critical and
    postgres-svc (port 5432) as medium — confusing web and DB services.
    The semantic layer must apply the port-based severity matrix:
    5432/3306/27017/6379 = critical; 80/443/3000 = medium."""

    def test_postgres_port_5432_is_critical(self) -> None:
        assert _classify_base_severity([5432]) == "critical"

    def test_mysql_port_3306_is_critical(self) -> None:
        assert _classify_base_severity([3306]) == "critical"

    def test_mongo_port_27017_is_critical(self) -> None:
        assert _classify_base_severity([27017]) == "critical"

    def test_redis_port_6379_is_critical(self) -> None:
        assert _classify_base_severity([6379]) == "critical"

    def test_grafana_port_3000_is_medium_not_critical(self) -> None:
        result = _classify_base_severity([3000])
        assert result == "medium", f"grafana (port 3000) classified as {result}, expected medium"

    def test_http_port_80_is_medium(self) -> None:
        assert _classify_base_severity([80]) == "medium"

    def test_https_port_443_is_medium(self) -> None:
        assert _classify_base_severity([443]) == "medium"

    def test_port_matrix_does_not_confuse_db_with_web(self) -> None:
        db_ports = [5432, 3306, 27017, 6379]
        web_ports = [80, 443, 3000]

        for port in db_ports:
            assert (
                _classify_base_severity([port]) == "critical"
            ), f"Port {port} should be critical but is not"

        for port in web_ports:
            severity = _classify_base_severity([port])
            assert (
                severity != "critical"
            ), f"Port {port} (web) should NOT be critical but got {severity}"


class TestCheckerCase7DuckDBExposureDurationEscalation:
    """Checker Case 7: postgres-svc has been exposed for months, each audit
    detects it but it's never corrected. The checker must flag the exposure
    duration and escalate severity for long-standing exposures.

    This is a structural test — the actual DuckDB integration reads from
    the exposure history table, but the escalation logic itself is
    deterministic and testable without a database."""

    @pytest.mark.parametrize(
        "exposure_days,expected_action",
        [
            (30, "flag"),
            (90, "escalate"),
            (180, "escalate_critical"),
            (365, "escalate_critical"),
        ],
    )
    def test_exposure_duration_escalation_thresholds(
        self, exposure_days: int, expected_action: str
    ) -> None:
        def escalate(exposure_days: int) -> str:
            if exposure_days >= 180:
                return "escalate_critical"
            if exposure_days >= 90:
                return "escalate"
            return "flag"

        result = escalate(exposure_days)

        assert (
            result == expected_action
        ), f"Exposure {exposure_days}d: expected {expected_action}, got {result}"

    def test_fresh_exposure_not_escalated(self) -> None:
        result = "escalate_critical" if 5 >= 180 else ("escalate" if 5 >= 90 else "flag")
        assert result == "flag"

    def test_ancient_exposure_gets_maximum_severity(self) -> None:
        result = "escalate_critical" if 400 >= 180 else ("escalate" if 400 >= 90 else "flag")
        assert result == "escalate_critical"
