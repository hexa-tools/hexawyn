"""Unit tests for the audit-event window/exclusion helpers."""

from __future__ import annotations

from datetime import UTC, datetime


class TestIsWithinWindow:
    def test_timestamp_three_days_ago_is_within_seven_day_window(self) -> None:
        from hexawyn.domain.services.manual_change_detection.audit_event_filter import (
            is_within_window,
        )

        now = datetime(2026, 6, 15, tzinfo=UTC)
        assert is_within_window("2026-06-12T09:11:00Z", 7, now) is True

    def test_timestamp_ten_days_ago_is_outside_seven_day_window(self) -> None:
        from hexawyn.domain.services.manual_change_detection.audit_event_filter import (
            is_within_window,
        )

        now = datetime(2026, 6, 15, tzinfo=UTC)
        assert is_within_window("2026-06-05T09:11:00Z", 7, now) is False

    def test_timestamp_exactly_at_window_start_is_within(self) -> None:
        from hexawyn.domain.services.manual_change_detection.audit_event_filter import (
            is_within_window,
        )

        now = datetime(2026, 6, 15, tzinfo=UTC)
        assert is_within_window("2026-06-08T00:00:00Z", 7, now) is True


class TestIsManualChange:
    def test_human_is_manual(self) -> None:
        from hexawyn.domain.services.manual_change_detection.audit_event_filter import (
            is_manual_change,
        )

        assert is_manual_change("human") is True

    def test_service_account_is_manual(self) -> None:
        from hexawyn.domain.services.manual_change_detection.audit_event_filter import (
            is_manual_change,
        )

        assert is_manual_change("service_account") is True

    def test_gitops_controller_is_not_manual(self) -> None:
        from hexawyn.domain.services.manual_change_detection.audit_event_filter import (
            is_manual_change,
        )

        assert is_manual_change("gitops_controller") is False


class TestIsPartialWindow:
    def test_earliest_timestamp_newer_than_window_start_is_partial(self) -> None:
        from hexawyn.domain.services.manual_change_detection.audit_event_filter import (
            is_partial_window,
        )

        now = datetime(2026, 6, 15, tzinfo=UTC)
        assert is_partial_window("2026-06-12T00:00:00Z", 7, now) is True

    def test_earliest_timestamp_covering_full_window_is_not_partial(self) -> None:
        from hexawyn.domain.services.manual_change_detection.audit_event_filter import (
            is_partial_window,
        )

        now = datetime(2026, 6, 15, tzinfo=UTC)
        assert is_partial_window("2026-06-01T00:00:00Z", 7, now) is False

    def test_no_earliest_timestamp_is_not_partial(self) -> None:
        from hexawyn.domain.services.manual_change_detection.audit_event_filter import (
            is_partial_window,
        )

        now = datetime(2026, 6, 15, tzinfo=UTC)
        assert is_partial_window(None, 7, now) is False
