"""Unit tests for build_report — assembles the RBACAuditReport aggregate and
its human-readable summary from the per-service-account results."""

from __future__ import annotations

from hexawyn.domain.models.rbac_audit import (
    PolicyRule,
    RBACFinding,
    SuggestedRole,
    UnusedServiceAccount,
)


def _finding(risk_level: str, name: str = "sa") -> RBACFinding:
    return RBACFinding(
        service_account=name,
        namespace="production",
        risk_level=risk_level,  # type: ignore[arg-type]
        reasons=[],
        current_permissions=[PolicyRule(verbs=["get"], resources=["pods"], api_groups=[""])],
        pods_using=[],
        misconfigured=False,
        recommendation="x",
        suggested_role=SuggestedRole(kind="Role", rules=[], basis="estimated"),
    )


class TestBuildReport:
    def test_no_findings_reports_none_found(self) -> None:
        from hexawyn.domain.services.rbac_audit.rbac_audit_report_builder import build_report

        report = build_report(
            findings=[],
            unused_service_accounts=[],
            excluded_system_service_accounts=[],
            total_service_accounts_checked=3,
        )

        assert report.findings == []
        assert report.total_service_accounts_checked == 3
        assert "No over-privileged" in report.summary

    def test_tc4_five_over_privileged_service_accounts_all_listed(self) -> None:
        from hexawyn.domain.services.rbac_audit.rbac_audit_report_builder import build_report

        findings = [_finding("critical", f"sa-{i}") for i in range(5)]

        report = build_report(
            findings=findings,
            unused_service_accounts=[],
            excluded_system_service_accounts=[],
            total_service_accounts_checked=10,
        )

        assert len(report.findings) == 5
        assert "5" in report.summary

    def test_summary_mentions_critical_count(self) -> None:
        from hexawyn.domain.services.rbac_audit.rbac_audit_report_builder import build_report

        findings = [_finding("critical", "sa-1"), _finding("medium", "sa-2")]

        report = build_report(
            findings=findings,
            unused_service_accounts=[],
            excluded_system_service_accounts=[],
            total_service_accounts_checked=5,
        )

        assert "critical" in report.summary.lower()

    def test_summary_mentions_unused_service_accounts(self) -> None:
        from hexawyn.domain.services.rbac_audit.rbac_audit_report_builder import build_report

        report = build_report(
            findings=[],
            unused_service_accounts=[UnusedServiceAccount(name="idle-sa", namespace="staging")],
            excluded_system_service_accounts=[],
            total_service_accounts_checked=2,
        )

        assert "unused" in report.summary.lower()
        assert report.unused_service_accounts == [
            UnusedServiceAccount(name="idle-sa", namespace="staging")
        ]

    def test_summary_mentions_excluded_system_service_accounts(self) -> None:
        from hexawyn.domain.services.rbac_audit.rbac_audit_report_builder import build_report

        report = build_report(
            findings=[],
            unused_service_accounts=[],
            excluded_system_service_accounts=["kube-system:default"],
            total_service_accounts_checked=4,
        )

        assert "system" in report.summary.lower()
        assert report.excluded_system_service_accounts == ["kube-system:default"]
