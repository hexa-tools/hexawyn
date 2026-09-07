"""Unit tests for touches_data / find_last_data_change_time. Checker case 2:
a label-only or metadata-only managedFields update must never be mistaken
for a rotation — only entries whose fields_v1 touches "f:data" count."""

from __future__ import annotations

from hexawyn.domain.models.secret_rotation import ManagedFieldsEntry


def _entry(time: str, fields_v1_raw: dict) -> ManagedFieldsEntry:
    return ManagedFieldsEntry(
        manager="kubectl-client-side-apply",
        operation="Update",
        time=time,
        fields_v1_raw=fields_v1_raw,
    )


class TestTouchesData:
    def test_entry_with_data_key_touches_data(self) -> None:
        from hexawyn.domain.services.secret_rotation.managed_fields_analyzer import touches_data

        assert touches_data({"f:data": {"f:PASSWORD": {}}}) is True

    def test_label_only_entry_does_not_touch_data(self) -> None:
        """Checker case 2: resourceVersion changed 5 days ago (label added)
        must never be read as a rotation."""
        from hexawyn.domain.services.secret_rotation.managed_fields_analyzer import touches_data

        assert touches_data({"f:metadata": {"f:labels": {"f:env": {}}}}) is False

    def test_empty_fields_does_not_touch_data(self) -> None:
        from hexawyn.domain.services.secret_rotation.managed_fields_analyzer import touches_data

        assert touches_data({}) is False


class TestFindLastDataChangeTime:
    def test_returns_latest_data_touching_entry(self) -> None:
        from hexawyn.domain.services.secret_rotation.managed_fields_analyzer import (
            find_last_data_change_time,
        )

        entries = [
            _entry("2025-01-01T00:00:00+00:00", {"f:data": {}}),
            _entry("2025-12-17T00:00:00+00:00", {"f:data": {}}),
        ]

        result = find_last_data_change_time(entries)

        assert result == "2025-12-17T00:00:00+00:00"

    def test_ignores_label_only_updates_more_recent_than_the_real_data_change(self) -> None:
        """The Checker's own scenario: a label was added 5 days ago (more
        recent than the last real data change) -- must not be picked."""
        from hexawyn.domain.services.secret_rotation.managed_fields_analyzer import (
            find_last_data_change_time,
        )

        entries = [
            _entry("2025-12-17T00:00:00+00:00", {"f:data": {}}),
            _entry("2026-06-11T00:00:00+00:00", {"f:metadata": {"f:labels": {}}}),
        ]

        result = find_last_data_change_time(entries)

        assert result == "2025-12-17T00:00:00+00:00"

    def test_no_data_touching_entry_returns_none(self) -> None:
        from hexawyn.domain.services.secret_rotation.managed_fields_analyzer import (
            find_last_data_change_time,
        )

        entries = [_entry("2026-01-01T00:00:00+00:00", {"f:metadata": {}})]

        assert find_last_data_change_time(entries) is None

    def test_empty_managed_fields_returns_none(self) -> None:
        from hexawyn.domain.services.secret_rotation.managed_fields_analyzer import (
            find_last_data_change_time,
        )

        assert find_last_data_change_time([]) is None
