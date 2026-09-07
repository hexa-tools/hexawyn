"""Unit tests for AlertDeduplicator — suppresses repeated alerts within a time window."""

from __future__ import annotations

from hexawyn.domain.services.log_analysis.alert_deduplicator import AlertDeduplicator


class TestAlertDeduplicator:
    def test_first_alert_for_category_is_allowed(self) -> None:
        dedup = AlertDeduplicator()
        assert dedup.should_alert("oom", now=0.0) is True

    def test_same_category_within_window_is_suppressed(self) -> None:
        dedup = AlertDeduplicator()
        dedup.should_alert("oom", now=0.0)
        assert dedup.should_alert("oom", now=1.0) is False

    def test_same_category_after_window_is_allowed(self) -> None:
        dedup = AlertDeduplicator(window_seconds=5.0)
        dedup.should_alert("oom", now=0.0)
        assert dedup.should_alert("oom", now=6.0) is True

    def test_different_category_is_independent(self) -> None:
        dedup = AlertDeduplicator()
        dedup.should_alert("oom", now=0.0)
        assert dedup.should_alert("db_connection_error", now=0.1) is True

    def test_multiple_alerts_in_one_second_deduplicated(self) -> None:
        """Edge case: multiple critical errors in 1 second -> deduplicated, not flooded."""
        dedup = AlertDeduplicator()
        results = [dedup.should_alert("oom", now=t) for t in (0.0, 0.2, 0.4, 0.6, 0.8)]
        assert results == [True, False, False, False, False]

    def test_default_window_is_5_seconds(self) -> None:
        dedup = AlertDeduplicator()
        assert dedup.window_seconds == 5.0  # noqa: PLR2004
