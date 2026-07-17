from __future__ import annotations

from hexawyn.application.ports.driven.platform_reliability_port import (
    PlatformReliabilityPort,
    ReliabilityData,
)


class _FakeSource:
    def __init__(self, data: ReliabilityData) -> None:
        self._data = data

    def fetch_reliability_data(self, period: str) -> ReliabilityData:
        return self._data


def _data() -> ReliabilityData:
    return ReliabilityData(
        period_minutes=43200,
        incidents=[],
        previous_avg_resolution_minutes=None,
        cost_per_downtime_minute_eur=None,
    )


class TestPortImplementation:
    def test_is_a_platform_reliability_port(self) -> None:
        from hexawyn.adapters.secondary.gitops.platform_reliability_adapter import (
            PlatformReliabilityAdapter,
        )

        assert isinstance(
            PlatformReliabilityAdapter(source=_FakeSource(_data())),
            PlatformReliabilityPort,
        )


class TestDelegation:
    def test_get_reliability_data_delegates(self) -> None:
        from hexawyn.adapters.secondary.gitops.platform_reliability_adapter import (
            PlatformReliabilityAdapter,
        )

        adapter = PlatformReliabilityAdapter(source=_FakeSource(_data()))

        result = adapter.get_reliability_data("2026-06")

        assert result["period_minutes"] == 43200
