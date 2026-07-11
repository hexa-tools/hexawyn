from __future__ import annotations

from hexawyn.application.ports.driven.stale_credentials_port import StaleCredentialRaw


def _cred(name: str = "db-password", risk: str = "critical", days: int = 120) -> StaleCredentialRaw:
    return StaleCredentialRaw(name=name, risk_level=risk, days_unrotated=days)


class TestStaleCredentialsService:
    def test_eight_stale_three_critical(self) -> None:
        from hexawyn.domain.services.stale_credentials.stale_credentials_service import (
            compute_stale_credentials_report,
        )

        creds = [_cred("db", "critical"), _cred("tls", "critical"), _cred("api", "critical")]
        creds += [_cred(f"noncrit{i}", "medium") for i in range(5)]

        report = compute_stale_credentials_report(creds, has_data=True, period="Rotation")

        assert report.total_stale == 8
        assert report.critical_count == 3

    def test_below_ninety_days_filtered(self) -> None:
        from hexawyn.domain.services.stale_credentials.stale_credentials_service import (
            compute_stale_credentials_report,
        )

        report = compute_stale_credentials_report(
            [_cred("fresh", "critical", days=30)], has_data=True, period="Rotation"
        )

        assert report.total_stale == 0

    def test_no_data_warns(self) -> None:
        from hexawyn.domain.services.stale_credentials.stale_credentials_service import (
            compute_stale_credentials_report,
        )

        report = compute_stale_credentials_report([], has_data=False, period="Rotation")

        assert report.has_data is False
