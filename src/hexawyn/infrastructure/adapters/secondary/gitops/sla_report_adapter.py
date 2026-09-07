from __future__ import annotations

from typing import Protocol

from hexawyn.application.ports.driven.sla_report_port import QuarterSlaData, SlaReportPort


class QuarterSlaSource(Protocol):
    """Assembles quarter-level SLA data from the weekly reliability / SLO
    sources into the uniform QuarterSlaData contract."""

    def fetch_quarter_sla_data(self, quarter: str) -> QuarterSlaData: ...

    def fetch_previous_quarter_avg_uptime(self, quarter: str) -> float | None: ...


class SlaReportAdapter(SlaReportPort):
    """Facade over the reliability/SLO sources for quarterly SLA reporting.

    Delegates to an injected source that rolls up weekly reliability data into
    quarter-level records, keeping the domain free of those sources.
    """

    def __init__(self, source: QuarterSlaSource) -> None:
        self._source = source

    def get_quarter_sla_data(self, quarter: str) -> QuarterSlaData:
        return self._source.fetch_quarter_sla_data(quarter)

    def get_previous_quarter_avg_uptime(self, quarter: str) -> float | None:
        return self._source.fetch_previous_quarter_avg_uptime(quarter)
