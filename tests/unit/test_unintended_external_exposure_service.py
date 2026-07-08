"""Unit tests for UnintendedExternalExposureService (mocks ExternalExposureAuditPort).

Covers the ticket's five Test Scenarios (TC1-TC5) and its five Edge Cases by
name in the test names.
"""

from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driving.detect_unintended_external_exposure.detect_unintended_external_exposure_command import (
    DetectUnintendedExternalExposureCommand,
)
from hexawyn.application.service.unintended_external_exposure_service import (
    UnintendedExternalExposureService,
)


def _service(
    name: str,
    namespace: str = "production",
    service_type: str = "LoadBalancer",
    ports: list[int] | None = None,
    node_port: int | None = None,
    external_ip: str | None = None,
    external_hostname: str | None = None,
    has_source_ranges: bool = False,
    annotations: dict[str, str] | None = None,
) -> dict:
    return {
        "name": name,
        "namespace": namespace,
        "service_type": service_type,
        "ports": ports or [],
        "node_port": node_port,
        "external_ip": external_ip,
        "external_hostname": external_hostname,
        "has_source_ranges": has_source_ranges,
        "annotations": annotations or {},
    }


def _make_service(
    services: list[dict] | None = None,
) -> tuple[UnintendedExternalExposureService, MagicMock]:
    port = MagicMock()
    port.list_external_services.return_value = services or []
    service = UnintendedExternalExposureService(external_exposure_port=port)
    return service, port


class TestPostgresLoadBalancerCritical:
    def test_tc1_postgres_svc_loadbalancer_is_critical(self) -> None:
        service, _ = _make_service(
            services=[_service("postgres-svc", ports=[5432], external_ip="34.120.45.12")]
        )

        response = service.detect_unintended_exposure(DetectUnintendedExternalExposureCommand())

        finding = response.findings[0]
        assert finding["risk_level"] == "critical"
        assert finding["external_ip"] == "34.120.45.12"


class TestAllowlistedServiceIsHealthy:
    def test_tc2_allowlisted_service_is_excluded_not_flagged(self) -> None:
        service, _ = _make_service(
            services=[_service("api-gateway", ports=[443], external_ip="1.2.3.4")]
        )

        response = service.detect_unintended_exposure(
            DetectUnintendedExternalExposureCommand(allowlist=["api-gateway"])
        )

        assert response.findings == []
        assert response.excluded_exposures == [
            {"name": "api-gateway", "namespace": "production", "reason": "allowlisted"}
        ]


class TestRedisCacheNodePortHighRisk:
    def test_tc3_redis_cache_nodeport_is_high_risk(self) -> None:
        service, _ = _make_service(
            services=[
                _service("redis-cache", service_type="NodePort", ports=[6379], node_port=31234)
            ]
        )

        response = service.detect_unintended_exposure(DetectUnintendedExternalExposureCommand())

        finding = response.findings[0]
        assert finding["risk_level"] == "high"
        assert finding["node_port"] == 31234


class TestNoUnintendedServices:
    def test_tc4_all_external_services_expected_produces_no_findings(self) -> None:
        service, _ = _make_service(
            services=[_service("api-gateway", ports=[443], external_ip="1.2.3.4")]
        )

        response = service.detect_unintended_exposure(
            DetectUnintendedExternalExposureCommand(allowlist=["api-gateway"])
        )

        assert response.findings == []


class TestFiveUnexpectedlyExposedServices:
    def test_tc5_five_unexpectedly_exposed_services_all_listed(self) -> None:
        services = [_service(f"svc-{i}", ports=[5432]) for i in range(5)]
        service, _ = _make_service(services=services)

        response = service.detect_unintended_exposure(DetectUnintendedExternalExposureCommand())

        assert len(response.findings) == 5
        assert all(finding["risk_level"] == "critical" for finding in response.findings)


class TestSourceRangesLowersRisk:
    def test_edge_case_source_ranges_lowers_risk_and_is_noted(self) -> None:
        service, _ = _make_service(
            services=[_service("postgres-svc", ports=[5432], has_source_ranges=True)]
        )

        response = service.detect_unintended_exposure(DetectUnintendedExternalExposureCommand())

        finding = response.findings[0]
        assert finding["risk_level"] == "high"
        assert finding["note"] is not None


class TestIngressControllerAllowlisted:
    def test_edge_case_ingress_controller_in_allowlist_is_excluded(self) -> None:
        service, _ = _make_service(
            services=[_service("ingress-nginx-controller", ports=[443], external_ip="1.2.3.4")]
        )

        response = service.detect_unintended_exposure(
            DetectUnintendedExternalExposureCommand(allowlist=["ingress-nginx-controller"])
        )

        assert response.findings == []


class TestPendingLoadBalancerStillFlagged:
    def test_edge_case_pending_loadbalancer_is_still_flagged(self) -> None:
        service, _ = _make_service(
            services=[_service("new-svc", ports=[5432], external_ip=None, external_hostname=None)]
        )

        response = service.detect_unintended_exposure(DetectUnintendedExternalExposureCommand())

        finding = response.findings[0]
        assert finding["is_pending"] is True
        assert finding["risk_level"] == "critical"


class TestNamespaceWeighting:
    def test_edge_case_dev_namespace_is_lower_risk_than_production(self) -> None:
        service, _ = _make_service(
            services=[_service("db-svc", namespace="dev", ports=[5432], external_ip="1.2.3.4")]
        )

        response = service.detect_unintended_exposure(DetectUnintendedExternalExposureCommand())

        finding = response.findings[0]
        assert finding["risk_level"] == "high"

    def test_same_service_in_production_stays_critical(self) -> None:
        service, _ = _make_service(
            services=[
                _service("db-svc", namespace="production", ports=[5432], external_ip="1.2.3.4")
            ]
        )

        response = service.detect_unintended_exposure(DetectUnintendedExternalExposureCommand())

        finding = response.findings[0]
        assert finding["risk_level"] == "critical"


class TestInternalLoadBalancerExcluded:
    def test_edge_case_internal_loadbalancer_annotation_is_excluded(self) -> None:
        service, _ = _make_service(
            services=[
                _service(
                    "internal-svc",
                    ports=[5432],
                    annotations={"service.beta.kubernetes.io/aws-load-balancer-internal": "true"},
                )
            ]
        )

        response = service.detect_unintended_exposure(DetectUnintendedExternalExposureCommand())

        assert response.findings == []
        assert any(
            "internal" in excluded["reason"].lower() for excluded in response.excluded_exposures
        )


class TestClusterIpServicesIgnored:
    def test_cluster_ip_services_are_not_evaluated_at_all(self) -> None:
        service, _ = _make_service(
            services=[_service("internal-only", service_type="ClusterIP", ports=[5432])]
        )

        response = service.detect_unintended_exposure(DetectUnintendedExternalExposureCommand())

        assert response.findings == []
        assert response.excluded_exposures == []
        assert response.total_external_services_checked == 0


class TestNamespacesFilter:
    def test_namespaces_filter_narrows_to_requested_namespaces(self) -> None:
        service, _ = _make_service(
            services=[
                _service("a", namespace="production", ports=[5432]),
                _service("b", namespace="staging", ports=[5432]),
            ]
        )

        response = service.detect_unintended_exposure(
            DetectUnintendedExternalExposureCommand(namespaces=["production"])
        )

        assert len(response.findings) == 1
        assert response.findings[0]["name"] == "a"


class TestTotalExternalServicesChecked:
    def test_total_reflects_only_loadbalancer_and_nodeport_services(self) -> None:
        service, _ = _make_service(
            services=[
                _service("a", service_type="LoadBalancer", ports=[5432]),
                _service("b", service_type="NodePort", ports=[6379]),
                _service("c", service_type="ClusterIP", ports=[80]),
            ]
        )

        response = service.detect_unintended_exposure(DetectUnintendedExternalExposureCommand())

        assert response.total_external_services_checked == 2
