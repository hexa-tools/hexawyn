from __future__ import annotations

from datetime import UTC, datetime

from hexawyn.application.ports.driven.mttr_trend_port import MTTRTrendPort
from hexawyn.application.ports.driving.compute_mttr_trend.compute_mttr_trend_command import (
    ComputeMTTRTrendCommand,
)
from hexawyn.application.ports.driving.compute_mttr_trend.compute_mttr_trend_response import (
    ComputeMTTRTrendResponse,
)
from hexawyn.application.ports.driving.compute_mttr_trend.compute_mttr_trend_service_port import (
    ComputeMTTRTrendServicePort,
)
from hexawyn.domain.services.mttr_trend.mttr_trend_engine import MTTRTrendEngine


class ComputeMTTRTrendService(ComputeMTTRTrendServicePort):
    def __init__(self, mttr_port: MTTRTrendPort) -> None:
        self._port = mttr_port
        self._engine = MTTRTrendEngine()

    def compute(self, command: ComputeMTTRTrendCommand) -> ComputeMTTRTrendResponse:
        now = datetime.now(UTC)
        if command.months:
            months = command.months
        else:
            months = _last_3_months(now.year, now.month)

        months_data: dict[str, list[dict[str, object]]] = {}
        for month in months:
            raw = self._port.fetch_incidents_by_month(month)
            months_data[month] = [dict(i) for i in raw]

        result = self._engine.compute(months_data)
        return ComputeMTTRTrendResponse(result=result)


def _last_3_months(year: int, month: int) -> list[str]:
    result = []
    y, m = year, month
    for _ in range(3):
        result.append(f"{y}-{m:02d}")
        if m == 1:
            m = 12
            y -= 1
        else:
            m -= 1
    result.reverse()
    return result
