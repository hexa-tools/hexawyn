"""Unit tests for build_report — assembles the PodSecurityAuditReport
aggregate and its human-readable summary from per-pod findings."""

from __future__ import annotations

from hexawyn.domain.models.pod_security import PodSecurityFinding, SecurityViolation


def _finding(namespace: str, severity: str = "critical", name: str = "pod") -> PodSecurityFinding:
    violation = SecurityViolation(
        violation_type="privileged",
        severity=severity,  # type: ignore[arg-type]
        pss_level="Baseline",
        container_name="app",
        recommendation="x",
    )
    return PodSecurityFinding(
        pod_name=name,
        namespace=namespace,
        violations=[violation],
        note=None,
        namespace_psa_enforce_level=None,
    )


class TestBuildReport:
    def test_no_findings_reports_none_found(self) -> None:
        from hexawyn.domain.services.pod_security.pod_security_report_builder import build_report

        report = build_report(findings=[], compliant_pod_count=5, total_pods_checked=5)

        assert report.findings == []
        assert report.total_pods_checked == 5  # noqa: PLR2004
        assert "No" in report.summary

    def test_tc4_all_pods_compliant_produces_empty_findings(self) -> None:
        from hexawyn.domain.services.pod_security.pod_security_report_builder import build_report

        report = build_report(findings=[], compliant_pod_count=12, total_pods_checked=12)

        assert report.findings == []
        assert report.compliant_pod_count == 12  # noqa: PLR2004

    def test_tc5_ten_violating_pods_across_three_namespaces_are_all_listed(self) -> None:
        from hexawyn.domain.services.pod_security.pod_security_report_builder import build_report

        findings = (
            [_finding("production", name=f"pod-{i}") for i in range(4)]
            + [_finding("staging", name=f"pod-{i}") for i in range(4, 7)]
            + [_finding("monitoring", name=f"pod-{i}") for i in range(7, 10)]
        )

        report = build_report(findings=findings, compliant_pod_count=2, total_pods_checked=12)

        assert len(report.findings) == 10  # noqa: PLR2004
        assert "10" in report.summary
        assert "3" in report.summary

    def test_summary_mentions_critical_count(self) -> None:
        from hexawyn.domain.services.pod_security.pod_security_report_builder import build_report

        findings = [_finding("production", "critical", "a"), _finding("production", "medium", "b")]

        report = build_report(findings=findings, compliant_pod_count=0, total_pods_checked=2)

        assert "critical" in report.summary.lower()
