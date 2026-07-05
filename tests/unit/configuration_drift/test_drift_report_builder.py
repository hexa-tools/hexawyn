"""Unit tests for build_drift_report — pure report assembly, grouping, and
summary composition."""

from __future__ import annotations

from hexawyn.domain.models.configuration_drift import DriftedField, DriftResult
from hexawyn.domain.services.configuration_drift.drift_report_builder import build_drift_report


def _in_sync(name: str, namespace: str = "production") -> DriftResult:
    return DriftResult(
        kind="Deployment",
        name=name,
        namespace=namespace,
        managed_by="helm",
        release_or_source="chart",
        drifted_fields=[],
        has_critical_drift=False,
        is_orphaned=False,
    )


def _drifted(name: str, namespace: str, critical: bool = False) -> DriftResult:
    field = DriftedField(
        field_path="image",
        desired_value="a",
        live_value="b",
        severity="critical" if critical else "warning",
    )
    return DriftResult(
        kind="Deployment",
        name=name,
        namespace=namespace,
        managed_by="helm",
        release_or_source="chart",
        drifted_fields=[field],
        has_critical_drift=critical,
        is_orphaned=False,
    )


def _orphaned(name: str, namespace: str = "production") -> DriftResult:
    return DriftResult(
        kind="Deployment",
        name=name,
        namespace=namespace,
        managed_by="helm",
        release_or_source="deleted-release",
        drifted_fields=[],
        has_critical_drift=False,
        is_orphaned=True,
    )


class TestNoDrift:
    def test_tc3_no_drift_found_summary(self) -> None:
        """TC3: no drift found → all resources in sync with desired state."""
        results = [_in_sync("a"), _in_sync("b"), _in_sync("c")]

        report = build_drift_report(results, excluded=[])

        assert report.drifted_resources == []
        assert report.in_sync_count == 3
        assert report.total_checked == 3
        assert "in sync" in report.summary.lower()


class TestGroupedByNamespace:
    def test_tc5_five_drifted_across_three_namespaces(self) -> None:
        """TC5: 5 drifted resources across 3 namespaces → grouped by namespace."""
        results = [
            _drifted("a", "production"),
            _drifted("b", "production"),
            _drifted("c", "staging"),
            _drifted("d", "staging"),
            _drifted("e", "dev"),
        ]

        report = build_drift_report(results, excluded=[])

        assert len(report.drifted_resources) == 5
        assert set(report.drifted_by_namespace) == {"production", "staging", "dev"}
        assert len(report.drifted_by_namespace["production"]) == 2
        assert len(report.drifted_by_namespace["staging"]) == 2
        assert len(report.drifted_by_namespace["dev"]) == 1


class TestOrphanNeverInSync:
    def test_orphaned_resource_counted_as_drifted_not_in_sync(self) -> None:
        results = [_in_sync("a"), _orphaned("b")]

        report = build_drift_report(results, excluded=[])

        assert report.in_sync_count == 1
        assert len(report.drifted_resources) == 1
        assert report.drifted_resources[0].is_orphaned is True


class TestExcludedResources:
    def test_excluded_resources_noted_in_summary(self) -> None:
        results = [_in_sync("a")]

        report = build_drift_report(results, excluded=["Service/unmanaged-svc in production"])

        assert report.excluded_resources == ["Service/unmanaged-svc in production"]
        assert "excluded" in report.summary.lower()


class TestCriticalCountInSummary:
    def test_summary_mentions_critical_count(self) -> None:
        results = [_drifted("a", "production", critical=True), _drifted("b", "production")]

        report = build_drift_report(results, excluded=[])

        assert "1 critical" in report.summary
