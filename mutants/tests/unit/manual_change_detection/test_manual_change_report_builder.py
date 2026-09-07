"""Unit tests for build_report — aggregates classified changes into a
ManualChangeOutsideGitOpsReport, noting degraded-data conditions."""

from __future__ import annotations

from hexawyn.domain.models.manual_change import ManualChange


def _change(name: str = "app-config") -> ManualChange:
    return ManualChange(
        kind="ConfigMap",
        name=name,
        namespace="production",
        timestamp="2026-06-14T14:23:00Z",
        actor="user:john.doe@company.com",
        actor_type="human",
        changed_fields=["data.DATABASE_URL"],
        severity="warning",
        is_limited_actor_info=False,
    )


class TestBasicAggregation:
    def test_no_changes_produces_empty_report_with_no_notes(self) -> None:
        from hexawyn.domain.services.manual_change_detection.manual_change_report_builder import (
            build_report,
        )

        report = build_report([], excluded_count=0, used_fallback=False, partial_window=False)

        assert report.manual_changes == []
        assert report.total_manual_changes == 0
        assert report.excluded_gitops_change_count == 0
        assert report.notes == []

    def test_changes_and_excluded_count_reflected(self) -> None:
        from hexawyn.domain.services.manual_change_detection.manual_change_report_builder import (
            build_report,
        )

        changes = [_change("app-config"), _change("other-config")]
        report = build_report(changes, excluded_count=3, used_fallback=False, partial_window=False)

        assert report.total_manual_changes == 2  # noqa: PLR2004
        assert report.excluded_gitops_change_count == 3  # noqa: PLR2004
        assert report.manual_changes == changes


class TestFallbackNote:
    def test_used_fallback_adds_limited_actor_info_note(self) -> None:
        from hexawyn.domain.services.manual_change_detection.manual_change_report_builder import (
            build_report,
        )

        report = build_report(
            [_change()], excluded_count=0, used_fallback=True, partial_window=False
        )

        assert report.used_managed_fields_fallback is True
        assert any("managedFields" in note for note in report.notes)

    def test_no_fallback_omits_the_note(self) -> None:
        from hexawyn.domain.services.manual_change_detection.manual_change_report_builder import (
            build_report,
        )

        report = build_report(
            [_change()], excluded_count=0, used_fallback=False, partial_window=False
        )

        assert report.used_managed_fields_fallback is False
        assert not any("managedFields" in note for note in report.notes)


class TestPartialWindowNote:
    def test_partial_window_adds_pruned_note(self) -> None:
        from hexawyn.domain.services.manual_change_detection.manual_change_report_builder import (
            build_report,
        )

        report = build_report(
            [_change()], excluded_count=0, used_fallback=False, partial_window=True
        )

        assert report.partial_window is True
        assert any("prune" in note.lower() or "partial" in note.lower() for note in report.notes)

    def test_both_fallback_and_partial_window_notes_present(self) -> None:
        from hexawyn.domain.services.manual_change_detection.manual_change_report_builder import (
            build_report,
        )

        report = build_report(
            [_change()], excluded_count=0, used_fallback=True, partial_window=True
        )

        assert len(report.notes) == 2  # noqa: PLR2004
