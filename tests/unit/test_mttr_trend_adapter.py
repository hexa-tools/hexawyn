"""RED → GREEN — MTTRTrendAdapter unit tests."""

from hexawyn.adapters.secondary.gitops.mttr_trend_adapter import MTTRTrendAdapter
from hexawyn.application.ports.driven.mttr_trend_port import MTTRTrendPort


class TestMTTRTrendAdapter:
    def test_implements_port(self) -> None:
        adapter = MTTRTrendAdapter()
        assert isinstance(adapter, MTTRTrendPort)

    def test_fetch_incidents_by_month_returns_empty(self) -> None:
        adapter = MTTRTrendAdapter()
        result = adapter.fetch_incidents_by_month("2026-07")
        assert result == []
