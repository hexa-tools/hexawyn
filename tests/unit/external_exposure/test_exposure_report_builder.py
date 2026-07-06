"""Unit tests for build_report — assembles the ExternalExposureReport
aggregate. Only unintended (non-excluded) findings appear in `findings`;
allowlisted/internal services live in the separate `excluded_exposures`
bucket, never mixed in."""

from __future__ import annotations

from hexawyn.domain.models.external_exposure import ExcludedExposure, ExternalExposureFinding


def _finding(name: str, risk_level: str = "critical") -> ExternalExposureFinding:
    return ExternalExposureFinding(
        name=name,
        namespace="production",
        service_type="LoadBalancer",
        ports=[5432],
        external_ip="1.2.3.4",
        external_hostname=None,
        node_port=None,
        is_pending=False,
        risk_level=risk_level,  # type: ignore[arg-type]
        note=None,
    )


class TestBuildReport:
    def test_tc4_no_findings_reports_none_found(self) -> None:
        from hexawyn.domain.services.external_exposure.exposure_report_builder import (
            build_report,
        )

        report = build_report(findings=[], excluded_exposures=[], total_external_services_checked=3)

        assert report.findings == []
        assert report.total_external_services_checked == 3
        assert "No unintended" in report.summary

    def test_tc5_five_unexpectedly_exposed_services(self) -> None:
        from hexawyn.domain.services.external_exposure.exposure_report_builder import (
            build_report,
        )

        findings = [_finding(f"svc-{i}") for i in range(5)]

        report = build_report(
            findings=findings, excluded_exposures=[], total_external_services_checked=8
        )

        assert len(report.findings) == 5
        assert "5" in report.summary

    def test_summary_mentions_excluded_exposures(self) -> None:
        from hexawyn.domain.services.external_exposure.exposure_report_builder import (
            build_report,
        )

        excluded = ExcludedExposure(
            name="api-gateway", namespace="production", reason="allowlisted"
        )

        report = build_report(
            findings=[], excluded_exposures=[excluded], total_external_services_checked=1
        )

        assert "excluded" in report.summary.lower()
        assert report.excluded_exposures == [excluded]
