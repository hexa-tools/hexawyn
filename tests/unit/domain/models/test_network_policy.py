"""Unit tests for the East-West Network Segmentation domain models."""

from __future__ import annotations

import dataclasses

import pytest


class TestNamespaceNetworkFinding:
    def test_creates_finding_with_expected_fields(self) -> None:
        from hexawyn.domain.models.network_policy import NamespaceNetworkFinding

        finding = NamespaceNetworkFinding(
            namespace="dev",
            ingress_policies=0,
            egress_policies=0,
            pod_count=8,
            network_status="open",
            risk_level="critical",
            recommendation="Apply default-deny NetworkPolicy for both ingress and egress",
            note=None,
        )

        assert finding.namespace == "dev"
        assert finding.ingress_policies == 0
        assert finding.egress_policies == 0
        assert finding.pod_count == 8
        assert finding.network_status == "open"
        assert finding.risk_level == "critical"
        assert (
            finding.recommendation == "Apply default-deny NetworkPolicy for both ingress and egress"
        )
        assert finding.note is None

    def test_restricted_namespace_has_no_recommendation(self) -> None:
        from hexawyn.domain.models.network_policy import NamespaceNetworkFinding

        finding = NamespaceNetworkFinding(
            namespace="production",
            ingress_policies=5,
            egress_policies=3,
            pod_count=45,
            network_status="restricted",
            risk_level="low",
            recommendation=None,
            note=None,
        )

        assert finding.recommendation is None

    def test_is_frozen(self) -> None:
        from hexawyn.domain.models.network_policy import NamespaceNetworkFinding

        finding = NamespaceNetworkFinding(
            namespace="n",
            ingress_policies=0,
            egress_policies=0,
            pod_count=0,
            network_status="open",
            risk_level="low",
            recommendation=None,
            note=None,
        )

        with pytest.raises(dataclasses.FrozenInstanceError):
            finding.risk_level = "critical"  # type: ignore[misc]


class TestExcludedNamespace:
    def test_creates_excluded_namespace_with_expected_fields(self) -> None:
        from hexawyn.domain.models.network_policy import ExcludedNamespace

        excluded = ExcludedNamespace(namespace="kube-system", reason="system namespace")

        assert excluded.namespace == "kube-system"
        assert excluded.reason == "system namespace"


class TestNetworkSegmentationReport:
    def test_creates_report_with_expected_fields(self) -> None:
        from hexawyn.domain.models.network_policy import (
            ExcludedNamespace,
            NamespaceNetworkFinding,
            NetworkSegmentationReport,
        )

        finding = NamespaceNetworkFinding(
            namespace="dev",
            ingress_policies=0,
            egress_policies=0,
            pod_count=8,
            network_status="open",
            risk_level="critical",
            recommendation="Apply default-deny NetworkPolicy for both ingress and egress",
            note=None,
        )
        excluded = ExcludedNamespace(namespace="kube-system", reason="system namespace")
        report = NetworkSegmentationReport(
            findings=[finding],
            excluded_namespaces=[excluded],
            total_namespaces_checked=8,
            fully_open_count=2,
            partially_restricted_count=3,
            restricted_count=3,
            summary="2 namespace(s) fully open out of 8 checked.",
        )

        assert report.findings == [finding]
        assert report.excluded_namespaces == [excluded]
        assert report.total_namespaces_checked == 8
        assert report.fully_open_count == 2
        assert report.partially_restricted_count == 3
        assert report.restricted_count == 3
        assert "fully open" in report.summary
