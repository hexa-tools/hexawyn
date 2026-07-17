from __future__ import annotations

from hexawyn.application.ports.driven.sla_report_port import QuarterSlaData, SlaReportPort


class _FakeSource:
    def __init__(self, data: QuarterSlaData, previous: float | None) -> None:
        self._data = data
        self._previous = previous

    def fetch_quarter_sla_data(self, quarter: str) -> QuarterSlaData:
        return self._data

    def fetch_previous_quarter_avg_uptime(self, quarter: str) -> float | None:
        return self._previous


def _data() -> QuarterSlaData:
    return QuarterSlaData(
        has_data=True,
        services=[
            {
                "service_name": "payment",
                "sla_target_pct": 99.9,
                "uptime_pct": 99.95,
                "coverage_days": 90,
                "quarter_days": 90,
                "maintenance_minutes": 0,
            }
        ],
        breaches=[],
    )


class TestPortImplementation:
    def test_is_an_sla_report_port(self) -> None:
        from hexawyn.adapters.secondary.gitops.sla_report_adapter import SlaReportAdapter

        assert isinstance(SlaReportAdapter(source=_FakeSource(_data(), None)), SlaReportPort)


class TestDelegation:
    def test_get_quarter_sla_data_delegates(self) -> None:
        from hexawyn.adapters.secondary.gitops.sla_report_adapter import SlaReportAdapter

        adapter = SlaReportAdapter(source=_FakeSource(_data(), None))

        result = adapter.get_quarter_sla_data("2026-Q1")

        assert result["services"][0]["service_name"] == "payment"

    def test_get_previous_quarter_avg_uptime_delegates(self) -> None:
        from hexawyn.adapters.secondary.gitops.sla_report_adapter import SlaReportAdapter

        adapter = SlaReportAdapter(source=_FakeSource(_data(), 99.5))

        assert adapter.get_previous_quarter_avg_uptime("2026-Q1") == 99.5
