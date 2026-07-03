"""Unit tests for format_report_as_markdown — Confluence/Notion-shareable export."""

from __future__ import annotations

from dataclasses import replace

from hexawyn.domain.models.incident_triage import (
    ImpactAssessment,
    IncidentCauseCategory,
    IncidentTriageReport,
    RootCauseCandidate,
    TimelineEntry,
)
from hexawyn.domain.services.incident_triage.markdown_formatter import format_report_as_markdown


def _report() -> IncidentTriageReport:
    return IncidentTriageReport(
        namespace="payment",
        time_window_minutes=120,
        timeline=[
            TimelineEntry(
                timestamp="2024-06-01T14:15:00Z",
                source="event",
                namespace="payment",
                object="payment-db",
                reason="FailedConnect",
                message="connection pool exhausted for postgres",
                severity="Warning",
            )
        ],
        root_causes=[
            RootCauseCandidate(
                description="database issue on payment-db",
                category=IncidentCauseCategory.DATABASE,
                confidence=0.85,
                evidence=[
                    "2024-06-01T14:15:00Z payment-db: FailedConnect — connection pool exhausted"
                ],
                involved_objects=["payment-db"],
            )
        ],
        impact=ImpactAssessment(
            affected_services=["payment-db", "checkout-service"],
            estimated_user_impact="High — 2 service(s) affected (cascade risk: medium)",
            duration_minutes=87,
            ongoing=False,
        ),
        remediation_steps=["Restore database connectivity — check the connection pool."],
        resolved=True,
        resolution_time="2024-06-01T15:42:00Z",
        mttr_minutes=87,
    )


class TestFormatReportAsMarkdown:
    def test_includes_required_sections(self) -> None:
        markdown = format_report_as_markdown(_report())

        assert "# Incident Report" in markdown
        assert "payment" in markdown
        assert "## Timeline" in markdown
        assert "## Impact Assessment" in markdown
        assert "## Root Cause" in markdown
        assert "## Remediation Steps" in markdown

    def test_timeline_rendered_as_table(self) -> None:
        markdown = format_report_as_markdown(_report())

        assert "| Timestamp | Source | Object | Reason | Message |" in markdown
        assert "payment-db" in markdown
        assert "FailedConnect" in markdown

    def test_includes_mttr_and_resolution_time_when_resolved(self) -> None:
        markdown = format_report_as_markdown(_report())

        assert "87" in markdown
        assert "2024-06-01T15:42:00Z" in markdown

    def test_empty_report_does_not_crash(self) -> None:
        empty = IncidentTriageReport(
            namespace="payment", time_window_minutes=120, insufficient_data=True
        )

        markdown = format_report_as_markdown(empty)

        assert "# Incident Report" in markdown
        assert "insufficient" in markdown.lower()

    def test_includes_ntp_drift_warning_when_detected(self) -> None:
        report = replace(
            _report(),
            ntp_drift_detected=True,
            ntp_drift_note="Log and event timestamps for checkout-service-abc differ by 300s",
        )

        markdown = format_report_as_markdown(report)

        assert "Clock drift warning" in markdown
        assert "checkout-service-abc" in markdown

    def test_includes_cross_namespace_correlation_when_present(self) -> None:
        report = replace(
            _report(), cross_namespace_correlation=["billing: billing-db (FailedConnect)"]
        )

        markdown = format_report_as_markdown(report)

        assert "Cross-namespace correlation" in markdown
        assert "billing: billing-db (FailedConnect)" in markdown
