"""Unit tests for domain/models/version_info.py — VersionCheckResult."""

from __future__ import annotations

from hexawyn.domain.models.version_info import VersionCheckResult


class TestVersionCheckResult:
    def test_fields_are_accessible(self) -> None:
        result = VersionCheckResult(
            current_version="0.1.0b3",
            latest_version="0.1.0b4",
            status="update_available",
        )

        assert result.current_version == "0.1.0b3"
        assert result.latest_version == "0.1.0b4"
        assert result.status == "update_available"
        assert result.error is None

    def test_error_defaults_to_none(self) -> None:
        result = VersionCheckResult(
            current_version="0.1.0b4",
            latest_version="",
            status="unknown",
        )

        assert result.error is None

    def test_error_can_be_set(self) -> None:
        result = VersionCheckResult(
            current_version="0.1.0b4",
            latest_version="",
            status="unknown",
            error="network unavailable",
        )

        assert result.error == "network unavailable"
