from __future__ import annotations

from hexawyn.application.ports.driven.unauthorized_access_port import UnauthorizedAccessRaw


def _raw(count: int = 52, source: str = "external") -> UnauthorizedAccessRaw:
    return UnauthorizedAccessRaw(attempt_count=count, window_minutes=30, source_type=source)


class TestUnauthorizedAccessService:
    def test_fifty_two_external_is_high(self) -> None:
        from hexawyn.domain.services.unauthorized_access.unauthorized_access_service import (
            compute_unauthorized_access_report,
        )

        report = compute_unauthorized_access_report(
            _raw(52, "external"), has_data=True, period="30 min"
        )

        assert report.attempt_count == 52
        assert report.alert_level == "high"

    def test_internal_monitoring_is_low(self) -> None:
        from hexawyn.domain.services.unauthorized_access.unauthorized_access_service import (
            compute_unauthorized_access_report,
        )

        report = compute_unauthorized_access_report(
            _raw(52, "internal"), has_data=True, period="30 min"
        )

        assert report.alert_level == "medium"

    def test_zero_attempts_is_low(self) -> None:
        from hexawyn.domain.services.unauthorized_access.unauthorized_access_service import (
            compute_unauthorized_access_report,
        )

        report = compute_unauthorized_access_report(_raw(0), has_data=True, period="30 min")

        assert report.alert_level == "low"

    def test_no_data_warns(self) -> None:
        from hexawyn.domain.services.unauthorized_access.unauthorized_access_service import (
            compute_unauthorized_access_report,
        )

        report = compute_unauthorized_access_report(_raw(), has_data=False, period="30 min")

        assert report.has_data is False

    def test_external_small_is_medium(self) -> None:
        from hexawyn.domain.services.unauthorized_access.unauthorized_access_service import (
            compute_unauthorized_access_report,
        )

        report = compute_unauthorized_access_report(
            _raw(5, "external"), has_data=True, period="30 min"
        )

        assert report.alert_level == "medium"
