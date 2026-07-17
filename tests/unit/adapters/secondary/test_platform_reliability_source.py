from __future__ import annotations


class TestEmptyReliabilityDataSource:
    def test_returns_healthy_period_by_default(self) -> None:
        from hexawyn.adapters.secondary.gitops.platform_reliability_source import (
            EmptyReliabilityDataSource,
        )

        data = EmptyReliabilityDataSource().fetch_reliability_data("2026-06")

        assert data["incidents"] == []
        assert data["cost_per_downtime_minute_eur"] is None
        assert data["previous_avg_resolution_minutes"] is None
        assert data["period_minutes"] > 0
