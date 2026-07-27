"""Unit tests for build_report — assembles the NetworkSegmentationReport
aggregate. Every checked namespace appears in findings (open, partially
restricted, or restricted) — the ticket's own summary counts only add up
(2 + 3 + 3 = 8) if every namespace is listed, not just the open ones."""

from __future__ import annotations

from hexawyn.domain.models.network_policy import (
    ExcludedNamespace,
    NamespaceNetworkFinding,
)


def _finding(
    namespace: str, network_status: str, risk_level: str = "critical"
) -> NamespaceNetworkFinding:
    return NamespaceNetworkFinding(
        namespace=namespace,
        ingress_policies=0,
        egress_policies=0,
        pod_count=8,
        network_status=network_status,  # type: ignore[arg-type]
        risk_level=risk_level,  # type: ignore[arg-type]
        recommendation=None,
        note=None,
    )


class TestBuildReport:
    def test_tc4_five_namespaces_three_fully_open_counts(self) -> None:
        """Test Scenario 4: 5 namespaces, 3 fully open."""
        from hexawyn.domain.services.network_policy.network_segmentation_report_builder import (
            build_report,
        )

        findings = [
            _finding("dev", "open"),
            _finding("staging", "open"),
            _finding("qa", "open"),
            _finding("production", "restricted"),
            _finding("monitoring", "partially_restricted"),
        ]

        report = build_report(findings=findings, excluded_namespaces=[], total_namespaces_checked=5)

        assert len(report.findings) == 5  # noqa: PLR2004
        assert report.fully_open_count == 3  # noqa: PLR2004
        assert report.partially_restricted_count == 1
        assert report.restricted_count == 1
        assert "3" in report.summary

    def test_ticket_summary_arithmetic_matches_total(self) -> None:
        """Test Data summary: total=8, fully_open=2, partially_restricted=3, restricted=3."""
        from hexawyn.domain.services.network_policy.network_segmentation_report_builder import (
            build_report,
        )

        findings = (
            [_finding(f"open-{i}", "open") for i in range(2)]
            + [_finding(f"partial-{i}", "partially_restricted") for i in range(3)]
            + [_finding(f"restricted-{i}", "restricted") for i in range(3)]
        )

        report = build_report(findings=findings, excluded_namespaces=[], total_namespaces_checked=8)

        assert report.fully_open_count == 2  # noqa: PLR2004
        assert report.partially_restricted_count == 3  # noqa: PLR2004
        assert report.restricted_count == 3  # noqa: PLR2004
        assert (
            report.fully_open_count + report.partially_restricted_count + report.restricted_count
            == report.total_namespaces_checked
        )

    def test_no_findings_reports_none_open(self) -> None:
        from hexawyn.domain.services.network_policy.network_segmentation_report_builder import (
            build_report,
        )

        report = build_report(findings=[], excluded_namespaces=[], total_namespaces_checked=0)

        assert report.fully_open_count == 0
        assert "No" in report.summary

    def test_excluded_namespaces_in_summary(self) -> None:
        from hexawyn.domain.services.network_policy.network_segmentation_report_builder import (
            build_report,
        )

        findings = [_finding("open-1", "open")]
        excluded = [ExcludedNamespace(namespace="kube-system", reason="system namespace")]
        report = build_report(
            findings=findings, excluded_namespaces=excluded, total_namespaces_checked=1
        )

        assert report.fully_open_count == 1
        assert "system namespace" in report.summary

    def test_excluded_namespaces_with_no_open_namespaces(self) -> None:
        from hexawyn.domain.services.network_policy.network_segmentation_report_builder import (
            build_report,
        )

        findings = [_finding("ns-1", "restricted")]
        excluded = [ExcludedNamespace(namespace="kube-system", reason="system")]
        report = build_report(
            findings=findings, excluded_namespaces=excluded, total_namespaces_checked=1
        )

        assert "No namespaces fully open" in report.summary
        assert "system namespace" in report.summary
