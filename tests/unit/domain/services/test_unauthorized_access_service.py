from __future__ import annotations

from hexawyn.domain.services.unauthorized_access.unauthorized_access_service import (
    _alert_level,
    compute_unauthorized_access_report,
)


class TestComputeUnauthorizedAccessReport:
    def test_no_data(self) -> None:
        raw = {"attempt_count": 0, "window_minutes": 60, "source_type": "external"}
        report = compute_unauthorized_access_report(raw, False, "2026-07")
        assert not report.has_data
        assert report.warning is not None

    def test_has_data_external_low(self) -> None:
        raw = {"attempt_count": 5, "window_minutes": 60, "source_type": "external"}
        report = compute_unauthorized_access_report(raw, True, "2026-07")
        assert report.has_data
        assert report.attempt_count == 5  # noqa: PLR2004
        assert report.alert_level == "medium"

    def test_external_zero_attempts(self) -> None:
        raw = {"attempt_count": 0, "window_minutes": 60, "source_type": "external"}
        report = compute_unauthorized_access_report(raw, True, "2026-07")
        assert report.alert_level == "low"

    def test_external_high(self) -> None:
        raw = {"attempt_count": 100, "window_minutes": 60, "source_type": "external"}
        report = compute_unauthorized_access_report(raw, True, "2026-07")
        assert report.alert_level == "high"

    def test_internal_high(self) -> None:
        raw = {"attempt_count": 100, "window_minutes": 60, "source_type": "internal"}
        report = compute_unauthorized_access_report(raw, True, "2026-07")
        assert report.alert_level == "medium"  # internal treats >50 as medium

    def test_internal_low(self) -> None:
        raw = {"attempt_count": 5, "window_minutes": 60, "source_type": "internal"}
        report = compute_unauthorized_access_report(raw, True, "2026-07")
        assert report.alert_level == "low"


class TestAlertLevel:
    def test_internal_boundary_50(self) -> None:
        assert _alert_level(50, "internal") == "low"
        assert _alert_level(51, "internal") == "medium"

    def test_external_boundary_20(self) -> None:
        assert _alert_level(20, "external") == "medium"
        assert _alert_level(21, "external") == "high"

    def test_external_zero(self) -> None:
        assert _alert_level(0, "internal") == "low"
        assert _alert_level(0, "external") == "low"
