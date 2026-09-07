"""Unit tests for build_report — assembles the SecretRotationReport
aggregate and its human-readable summary."""

from __future__ import annotations

from hexawyn.domain.models.secret_rotation import ExcludedSecret, StaleSecretFinding


def _finding(name: str) -> StaleSecretFinding:
    return StaleSecretFinding(
        name=name,
        namespace="production",
        secret_type="Opaque",
        age_days=180,
        last_modified="2025-12-17",
        referenced_by=["payment-deploy"],
        risk_level="critical",
        urgency_score=95,
        note=None,
    )


class TestBuildReport:
    def test_no_findings_reports_none_found(self) -> None:
        from hexawyn.domain.services.secret_rotation.rotation_report_builder import build_report

        report = build_report(
            findings=[],
            excluded_secrets=[],
            total_secrets_checked=5,
            rotation_threshold_days=90,
        )

        assert report.findings == []
        assert report.total_secrets_checked == 5  # noqa: PLR2004
        assert report.rotation_threshold_days == 90  # noqa: PLR2004
        assert "No" in report.summary

    def test_tc5_eight_stale_secrets_summary(self) -> None:
        from hexawyn.domain.services.secret_rotation.rotation_report_builder import build_report

        findings = [_finding(f"secret-{i}") for i in range(8)]

        report = build_report(
            findings=findings,
            excluded_secrets=[],
            total_secrets_checked=10,
            rotation_threshold_days=90,
        )

        assert len(report.findings) == 8  # noqa: PLR2004
        assert "8" in report.summary

    def test_summary_mentions_excluded_secrets(self) -> None:
        from hexawyn.domain.services.secret_rotation.rotation_report_builder import build_report

        excluded = ExcludedSecret(
            name="tls-cert", namespace="production", reason="auto-rotated (cert-manager)"
        )

        report = build_report(
            findings=[],
            excluded_secrets=[excluded],
            total_secrets_checked=2,
            rotation_threshold_days=90,
        )

        assert "excluded" in report.summary.lower()
        assert report.excluded_secrets == [excluded]
