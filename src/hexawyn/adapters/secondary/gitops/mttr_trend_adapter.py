from __future__ import annotations

from hexawyn.application.ports.driven.mttr_trend_port import (
    IncidentResolutionData,
    MTTRTrendPort,
)


class MTTRTrendAdapter(MTTRTrendPort):
    def fetch_incidents_by_month(self, month: str) -> list[IncidentResolutionData]:
        return []
