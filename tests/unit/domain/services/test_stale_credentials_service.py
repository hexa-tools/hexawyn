from __future__ import annotations

from hexawyn.domain.services.stale_credentials.stale_credentials_service import (
    compute_stale_credentials_report,
)


class TestComputeStaleCredentialsReport:
    def test_no_data_returns_warning(self) -> None:
        result = compute_stale_credentials_report([], has_data=False, period="2026-07")
        assert result.has_data is False
        assert result.warning is not None
