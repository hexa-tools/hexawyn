"""Unit tests for EastWestNetworkSegmentationService (mocks NetworkPolicyAuditPort).

Covers the ticket's five Test Scenarios (TC1-TC5) and its five Edge Cases by
name in the test names.
"""

from __future__ import annotations

from unittest.mock import MagicMock

from hexawyn.application.ports.driving.detect_network_segmentation_gaps.detect_network_segmentation_gaps_command import (
    DetectNetworkSegmentationGapsCommand,
)
from hexawyn.application.service.east_west_network_segmentation_service import (
    EastWestNetworkSegmentationService,
)


def _namespace(name: str, pod_count: int = 8) -> dict:
    return {"name": name, "pod_count": pod_count}


def _policy(
    namespace: str,
    name: str = "policy",
    ingress_rule_count: int = 0,
    egress_rule_count: int = 0,
    has_empty_pod_selector: bool = False,
) -> dict:
    return {
        "name": name,
        "namespace": namespace,
        "ingress_rule_count": ingress_rule_count,
        "egress_rule_count": egress_rule_count,
        "has_empty_pod_selector": has_empty_pod_selector,
    }


def _make_service(
    namespaces: list[dict] | None = None,
    policies: list[dict] | None = None,
    has_calico: bool = False,
    has_istio_strict: bool = False,
) -> tuple[EastWestNetworkSegmentationService, MagicMock]:
    port = MagicMock()
    port.list_namespaces_with_pod_counts.return_value = namespaces or []
    port.list_network_policies.return_value = policies or []
    port.has_calico_global_network_policies.return_value = has_calico
    port.has_istio_strict_peer_authentication.return_value = has_istio_strict
    service = EastWestNetworkSegmentationService(network_policy_port=port)
    return service, port


class TestDevFullyOpen:
    def test_tc1_dev_namespace_zero_policies_is_fully_open_critical(self) -> None:
        service, _ = _make_service(namespaces=[_namespace("dev", pod_count=8)], policies=[])

        response = service.detect_segmentation_gaps(DetectNetworkSegmentationGapsCommand())

        finding = response.findings[0]
        assert finding["network_status"] == "open"
        assert finding["risk_level"] == "critical"


class TestProductionPartiallyRestricted:
    def test_tc2_ingress_only_is_partially_restricted(self) -> None:
        service, _ = _make_service(
            namespaces=[_namespace("production", pod_count=12)],
            policies=[_policy("production", ingress_rule_count=2, egress_rule_count=0)],
        )

        response = service.detect_segmentation_gaps(DetectNetworkSegmentationGapsCommand())

        finding = response.findings[0]
        assert finding["network_status"] == "partially_restricted"
        assert finding["risk_level"] == "medium"


class TestMonitoringRestrictedHealthy:
    def test_tc3_default_deny_with_allow_rules_is_restricted_healthy(self) -> None:
        service, _ = _make_service(
            namespaces=[_namespace("monitoring", pod_count=5)],
            policies=[
                _policy(
                    "monitoring",
                    name="default-deny",
                    ingress_rule_count=0,
                    egress_rule_count=0,
                    has_empty_pod_selector=True,
                ),
                _policy(
                    "monitoring", name="allow-scrape", ingress_rule_count=1, egress_rule_count=1
                ),
            ],
        )

        response = service.detect_segmentation_gaps(DetectNetworkSegmentationGapsCommand())

        finding = response.findings[0]
        assert finding["network_status"] == "restricted"
        assert finding["risk_level"] == "low"
        assert finding["recommendation"] is None


class TestFiveNamespacesThreeFullyOpen:
    def test_tc4_all_open_namespaces_listed_with_default_deny_recommendation(self) -> None:
        namespaces = [
            _namespace("dev"),
            _namespace("staging2"),
            _namespace("qa"),
            _namespace("production", pod_count=45),
            _namespace("monitoring"),
        ]
        policies = [
            _policy("production", ingress_rule_count=5, egress_rule_count=3),
            _policy("monitoring", ingress_rule_count=1, egress_rule_count=1),
        ]
        service, _ = _make_service(namespaces=namespaces, policies=policies)

        response = service.detect_segmentation_gaps(DetectNetworkSegmentationGapsCommand())

        assert len(response.findings) == 5
        open_findings = [f for f in response.findings if f["network_status"] == "open"]
        assert len(open_findings) == 3
        assert all(
            f["recommendation"] == "Apply default-deny NetworkPolicy for both ingress and egress"
            for f in open_findings
        )


class TestEmptyPodSelectorWithNoRulesIsSameAsNoPolicy:
    def test_tc5_empty_pod_selector_with_zero_rules_is_open(self) -> None:
        service, _ = _make_service(
            namespaces=[_namespace("dev", pod_count=8)],
            policies=[
                _policy(
                    "dev", ingress_rule_count=0, egress_rule_count=0, has_empty_pod_selector=True
                )
            ],
        )

        response = service.detect_segmentation_gaps(DetectNetworkSegmentationGapsCommand())

        finding = response.findings[0]
        assert finding["network_status"] == "open"


class TestCalicoGlobalNetworkPolicyDetected:
    def test_edge_case_calico_global_network_policy_is_noted(self) -> None:
        service, _ = _make_service(namespaces=[_namespace("dev")], policies=[], has_calico=True)

        response = service.detect_segmentation_gaps(DetectNetworkSegmentationGapsCommand())

        finding = response.findings[0]
        assert finding["note"] is not None
        assert "Calico" in finding["note"]
        assert finding["network_status"] == "open"


class TestIstioStrictMtlsDetected:
    def test_edge_case_istio_strict_mtls_is_noted(self) -> None:
        service, _ = _make_service(
            namespaces=[_namespace("dev")], policies=[], has_istio_strict=True
        )

        response = service.detect_segmentation_gaps(DetectNetworkSegmentationGapsCommand())

        finding = response.findings[0]
        assert finding["note"] is not None
        assert "Istio mTLS provides equivalent protection" in finding["note"]


class TestNamespaceWithNoPods:
    def test_edge_case_namespace_with_no_pods_is_low_impact(self) -> None:
        service, _ = _make_service(namespaces=[_namespace("empty-ns", pod_count=0)], policies=[])

        response = service.detect_segmentation_gaps(DetectNetworkSegmentationGapsCommand())

        finding = response.findings[0]
        assert finding["network_status"] == "open"
        assert finding["risk_level"] == "low"


class TestSystemNamespacesExcluded:
    def test_edge_case_system_namespaces_excluded_shown_separately(self) -> None:
        service, _ = _make_service(
            namespaces=[_namespace("kube-system", pod_count=10)], policies=[]
        )

        response = service.detect_segmentation_gaps(DetectNetworkSegmentationGapsCommand())

        assert response.findings == []
        assert response.excluded_namespaces == [
            {"namespace": "kube-system", "reason": "system namespace"}
        ]


class TestEmptyPodSelectorWithRulesNoted:
    def test_edge_case_empty_pod_selector_with_rules_is_noted(self) -> None:
        service, _ = _make_service(
            namespaces=[_namespace("production", pod_count=10)],
            policies=[
                _policy(
                    "production",
                    ingress_rule_count=2,
                    egress_rule_count=2,
                    has_empty_pod_selector=True,
                )
            ],
        )

        response = service.detect_segmentation_gaps(DetectNetworkSegmentationGapsCommand())

        finding = response.findings[0]
        assert finding["note"] is not None
        assert "empty podSelector" in finding["note"]


class TestNamespacesFilter:
    def test_namespaces_filter_narrows_to_requested_namespaces(self) -> None:
        service, _ = _make_service(
            namespaces=[_namespace("dev"), _namespace("staging2")], policies=[]
        )

        response = service.detect_segmentation_gaps(
            DetectNetworkSegmentationGapsCommand(namespaces=["dev"])
        )

        assert len(response.findings) == 1
        assert response.findings[0]["namespace"] == "dev"


class TestTotalNamespacesChecked:
    def test_total_namespaces_checked_reflects_all_non_excluded_namespaces(self) -> None:
        service, _ = _make_service(
            namespaces=[_namespace("dev"), _namespace("staging2")], policies=[]
        )

        response = service.detect_segmentation_gaps(DetectNetworkSegmentationGapsCommand())

        assert response.total_namespaces_checked == 2
