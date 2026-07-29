from __future__ import annotations

from datetime import UTC, datetime, timedelta


class TestWithinWindow:
    def test_happy_path_returns_true_for_recent_event(self) -> None:
        from hexawyn.domain.services.incident_triage.time_window import within_window

        recent = (datetime.now(UTC) - timedelta(minutes=5)).isoformat()

        assert within_window(recent, 30) is True

    def test_event_older_than_window_returns_false(self) -> None:
        from hexawyn.domain.services.incident_triage.time_window import within_window

        old = (datetime.now(UTC) - timedelta(minutes=120)).isoformat()

        assert within_window(old, 30) is False

    def test_none_start_time_returns_false(self) -> None:
        from hexawyn.domain.services.incident_triage.time_window import within_window

        assert within_window(None, 60) is False

    def test_empty_string_returns_false(self) -> None:
        from hexawyn.domain.services.incident_triage.time_window import within_window

        assert within_window("", 60) is False

    def test_malformed_timestamp_returns_false(self) -> None:
        from hexawyn.domain.services.incident_triage.time_window import within_window

        assert within_window("not-a-date", 60) is False

    def test_z_suffix_handled(self) -> None:
        from hexawyn.domain.services.incident_triage.time_window import within_window

        recent = (datetime.now(UTC) - timedelta(minutes=2)).strftime("%Y-%m-%dT%H:%M:%SZ")

        assert within_window(recent, 10) is True

    def test_exactly_at_boundary(self) -> None:
        from hexawyn.domain.services.incident_triage.time_window import within_window

        reference = datetime(2026, 1, 1, 12, 0, 0, tzinfo=UTC)
        exact_boundary = reference - timedelta(minutes=30)
        from unittest.mock import patch

        with patch("hexawyn.domain.services.incident_triage.time_window.datetime") as mock_dt:
            mock_dt.now.return_value = reference
            mock_dt.fromisoformat = datetime.fromisoformat
            mock_dt.UTC = UTC
            mock_dt.timedelta = timedelta

            assert within_window(exact_boundary.isoformat(), 30) is True

    def test_zero_window_returns_false_for_past_event(self) -> None:
        from hexawyn.domain.services.incident_triage.time_window import within_window

        past = (datetime.now(UTC) - timedelta(minutes=1)).isoformat()

        assert within_window(past, 0) is False

    def test_future_timestamp_returns_true(self) -> None:
        from hexawyn.domain.services.incident_triage.time_window import within_window

        future = (datetime.now(UTC) + timedelta(minutes=5)).isoformat()

        assert within_window(future, 60) is True

    def test_negative_window_treated_as_no_coverage(self) -> None:
        from hexawyn.domain.services.incident_triage.time_window import within_window

        recent = (datetime.now(UTC) - timedelta(minutes=10)).isoformat()

        assert within_window(recent, -60) is False

    def test_arbitrary_string_timestamp_value_error_returns_false(self) -> None:
        from hexawyn.domain.services.incident_triage.time_window import within_window

        assert within_window("garbage-text", 30) is False
