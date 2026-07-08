"""Unit tests for build_report — aggregates classified drifts into a
ContainerImageDriftReport."""

from __future__ import annotations

from hexawyn.domain.models.image_drift import ContainerImageDrift
from hexawyn.domain.services.image_drift.image_drift_report_builder import build_report


def _drift(deployment: str = "payment-service") -> ContainerImageDrift:
    return ContainerImageDrift(
        deployment=deployment,
        namespace="production",
        container="app",
        running_image="payment:v1.3-hotfix",
        declared_image="payment:v1.2",
        source_of_truth="helm-release:payment-chart",
        drift_type="tag_mismatch",
        severity="critical",
    )


class TestBuildReport:
    def test_no_drifts_produces_empty_out_of_sync(self) -> None:
        report = build_report([], in_sync_count=38, excluded_count=0)

        assert report.out_of_sync == []
        assert report.in_sync_count == 38
        assert report.excluded_count == 0
        assert report.total_checked == 38
        assert "in sync" in report.summary.lower()

    def test_drifts_reflected_and_total_checked_sums_correctly(self) -> None:
        drifts = [_drift("payment-service"), _drift("analytics-worker")]

        report = build_report(drifts, in_sync_count=38, excluded_count=1)

        assert report.out_of_sync == drifts
        assert report.in_sync_count == 38
        assert report.excluded_count == 1
        assert report.total_checked == 40
        assert "2" in report.summary

    def test_excluded_count_noted_in_summary(self) -> None:
        report = build_report([], in_sync_count=10, excluded_count=3)

        assert "3" in report.summary
        assert "excluded" in report.summary.lower()
