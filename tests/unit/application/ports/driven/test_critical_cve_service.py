from __future__ import annotations

from hexawyn.application.ports.driven.critical_cve_port import CveRaw


def _cve(
    service: str = "payment-service",
    severity: str = "critical",
    count: int = 2,
    oldest: int = 12,
) -> CveRaw:
    return CveRaw(
        business_service_name=service,
        severity=severity,
        count=count,
        oldest_unresolved_days=oldest,
    )


class TestCriticalCveReport:
    def test_three_critical_on_two_services(self) -> None:
        from hexawyn.domain.services.critical_cve.critical_cve_service import (
            compute_critical_cve_report,
        )

        cves = [_cve("payment-service", count=2), _cve("auth-service", count=1)]

        report = compute_critical_cve_report(
            cves, total_scanned=10, has_data=True, period="Dernier scan"
        )

        assert report.total_critical_cves == 3
        assert report.affected_service_count == 2
        assert report.oldest_unresolved_days == 12

    def test_zero_critical_is_green(self) -> None:
        from hexawyn.domain.services.critical_cve.critical_cve_service import (
            compute_critical_cve_report,
        )

        report = compute_critical_cve_report(
            [], total_scanned=10, has_data=True, period="Dernier scan"
        )

        assert report.total_critical_cves == 0

    def test_non_critical_filtered_out(self) -> None:
        from hexawyn.domain.services.critical_cve.critical_cve_service import (
            compute_critical_cve_report,
        )

        report = compute_critical_cve_report(
            [_cve(severity="high", count=5)], total_scanned=10, has_data=True, period="Dernier scan"
        )

        assert report.total_critical_cves == 0

    def test_no_data_warns(self) -> None:
        from hexawyn.domain.services.critical_cve.critical_cve_service import (
            compute_critical_cve_report,
        )

        report = compute_critical_cve_report(
            [], total_scanned=0, has_data=False, period="Dernier scan"
        )

        assert report.has_data is False
        assert report.warning != ""
