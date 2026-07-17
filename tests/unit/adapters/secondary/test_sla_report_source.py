from __future__ import annotations


class TestEmptyQuarterSlaSource:
    def test_returns_no_data_by_default(self) -> None:
        from hexawyn.adapters.secondary.gitops.sla_report_source import (
            EmptyQuarterSlaSource,
        )

        data = EmptyQuarterSlaSource().fetch_quarter_sla_data("2026-Q1")

        assert data["has_data"] is False
        assert data["services"] == []
        assert data["breaches"] == []

    def test_previous_avg_is_none(self) -> None:
        from hexawyn.adapters.secondary.gitops.sla_report_source import (
            EmptyQuarterSlaSource,
        )

        assert EmptyQuarterSlaSource().fetch_previous_quarter_avg_uptime("2026-Q1") is None
