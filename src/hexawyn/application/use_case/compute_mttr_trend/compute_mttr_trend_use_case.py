from __future__ import annotations

from collections import defaultdict
from datetime import datetime

from hexawyn.application.ports.driven.mttr_trend_port import IncidentResolutionData, MTTRTrendPort
from hexawyn.application.use_case.compute_mttr_trend.command import ComputeMttrTrendCommand
from hexawyn.application.use_case.compute_mttr_trend.response import (
    ComputeMttrTrendResponse,
    MTTRTrendResult,
    SeverityMTTR,
    SlowestIncident,
)

BENCHMARKS: dict[str, float] = {"P1": 60, "P2": 240, "P3": 1440}


def _default_months() -> list[str]:
    now = datetime.now()
    months: list[str] = []
    for offset in (2, 1, 0):
        y = now.year
        m = now.month - offset
        if m <= 0:
            m += 12
            y -= 1
        months.append(f"{y}-{m:02d}")
    return months


def _compute_mttr(incidents: list[IncidentResolutionData]) -> dict[str, SeverityMTTR]:
    by_sev: dict[str, tuple[int, int]] = defaultdict(lambda: (0, 0))
    for inc in incidents:
        if not inc.get("resolved", True):
            continue
        sev = inc.get("severity", "P3")
        total, count = by_sev[sev]
        by_sev[sev] = (total + inc.get("resolution_minutes", 0), count + 1)
    return {
        sev: SeverityMTTR(
            mttr_minutes=round(total / count, 1) if count > 0 else 0.0,
            incident_count=count,
            meets_benchmark=(total / count <= BENCHMARKS.get(sev, 1440)) if count > 0 else True,
        )
        for sev, (total, count) in by_sev.items()
    }


class ComputeMttrTrendUseCase:
    def __init__(self, port: MTTRTrendPort) -> None:
        self._port = port

    def execute(self, command: ComputeMttrTrendCommand) -> ComputeMttrTrendResponse:
        months = command.months if command.months else _default_months()
        per_month: dict[str, dict[str, SeverityMTTR]] = {}
        all_incidents: list[IncidentResolutionData] = []

        for month in months:
            incidents = self._port.fetch_incidents_by_month(month)
            all_incidents.extend(incidents)
            per_month[month] = _compute_mttr(incidents)

        slowest = sorted(all_incidents, key=lambda i: i.get("resolution_minutes", 0), reverse=True)[
            :3
        ]
        slowest_entries = [
            SlowestIncident(
                incident_id=i.get("incident_id", ""),
                service_name=i.get("service_name", ""),
                severity=i.get("severity", ""),
                resolution_minutes=i.get("resolution_minutes", 0),
                root_cause=i.get("root_cause", ""),
            )
            for i in slowest
        ]

        if len(months) >= 2:
            first = months[0]
            last = months[-1]
            p1_first = per_month.get(first, {}).get("P1", SeverityMTTR()).mttr_minutes
            p1_last = per_month.get(last, {}).get("P1", SeverityMTTR()).mttr_minutes
            if p1_last < p1_first * 0.9:
                trend = "improving"
                rec = "MTTR is trending down — good incident response"
            elif p1_last > p1_first * 1.1:
                trend = "degrading"
                rec = "MTTR is increasing — review incident response process"
            else:
                trend = "stable"
                rec = "MTTR is stable — continue current practices"
        else:
            trend = "stable"
            rec = ""

        result = MTTRTrendResult(
            trend=trend, recommendation=rec, per_month=per_month, slowest_incidents=slowest_entries
        )
        return ComputeMttrTrendResponse(result=result)
