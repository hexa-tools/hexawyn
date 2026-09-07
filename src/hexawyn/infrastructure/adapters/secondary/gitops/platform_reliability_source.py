from __future__ import annotations

from hexawyn.application.ports.driven.platform_reliability_port import ReliabilityData

_MINUTES_IN_THIRTY_DAYS = 43200


class EmptyReliabilityDataSource:
    """Default reliability source used until the incident/MTTR roll-up is wired
    in. Reports a healthy 30-day period with no incidents and no pricing, so
    the report reads "Plateforme stable" rather than fabricating figures."""

    def fetch_reliability_data(self, period: str) -> ReliabilityData:
        return ReliabilityData(
            period_minutes=_MINUTES_IN_THIRTY_DAYS,
            incidents=[],
            previous_avg_resolution_minutes=None,
            cost_per_downtime_minute_eur=None,
        )
