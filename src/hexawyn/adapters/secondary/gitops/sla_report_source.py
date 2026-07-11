from __future__ import annotations

from hexawyn.application.ports.driven.sla_report_port import QuarterSlaData


class EmptyQuarterSlaSource:
    """Default quarterly SLA source used until a persistent reliability roll-up
    is wired in. Reports no data, so the domain warns about missing data rather
    than presenting a misleading 100% uptime."""

    def fetch_quarter_sla_data(self, quarter: str) -> QuarterSlaData:
        return QuarterSlaData(has_data=False, services=[], breaches=[])

    def fetch_previous_quarter_avg_uptime(self, quarter: str) -> float | None:
        return None
