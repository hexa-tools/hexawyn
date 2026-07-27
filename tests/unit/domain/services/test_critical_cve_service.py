from __future__ import annotations

from hexawyn.domain.services.critical_cve.critical_cve_service import (
    compute_critical_cve_report,
)


class TestComputeCriticalCveReport:
    def test_no_data_returns_warning(self) -> None:
        result = compute_critical_cve_report([], total_scanned=0, has_data=False, period="2026-07")
        assert result.has_data is False
        assert result.warning is not None
