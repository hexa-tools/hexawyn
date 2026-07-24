from __future__ import annotations

from collections import defaultdict

from hexawyn.application.ports.driven.monthly_incident_port import (
    IncidentSnapshotData,
    MonthlyIncidentPort,
)
from hexawyn.application.use_case.compute_monthly_incident_report.command import (
    ComputeMonthlyIncidentReportCommand,
)
from hexawyn.application.use_case.compute_monthly_incident_report.response import (
    ComputeMonthlyIncidentReportResponse,
    ImpactedService,
    MonthlyIncidentResult,
    SeverityBreakdown,
)

SEVERITY_ORDER = ["P1", "P2", "P3"]


def _default_month() -> str:
    from datetime import datetime

    now = datetime.now()
    return f"{now.year}-{now.month:02d}"


def _previous_month_name(month: str) -> str:
    year, mo = month.split("-")
    y = int(year)
    m = int(mo)
    if m == 1:
        return f"{y - 1}-12"
    return f"{y}-{m - 1:02d}"


def _aggregate(incidents: list[IncidentSnapshotData]) -> MonthlyIncidentResult:
    per_sev: dict[str, SeverityBreakdown] = defaultdict(lambda: SeverityBreakdown(0, 0))
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = inc.get("severity", "P3")
        dt = inc.get("downtime_minutes", 0)
        sb = per_sev[sev]
        sb.count += 1
        sb.downtime_minutes += dt
        total_downtime += dt
        svc = inc.get("service_name", "unknown")
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc, total_downtime=svc_downtime[svc], incident_count=svc_count[svc]
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    return MonthlyIncidentResult(
        month=incidents[0].get("timestamp", "")[:7] if incidents else "",
        total_count=len(incidents),
        total_downtime_minutes=total_downtime,
        per_severity=dict(per_sev),
        most_impacted_services=impacted,
    )


class ComputeMonthlyIncidentReportUseCase:
    def __init__(self, port: MonthlyIncidentPort) -> None:
        self._port = port

    def execute(
        self, command: ComputeMonthlyIncidentReportCommand
    ) -> ComputeMonthlyIncidentReportResponse:
        month = command.month or _default_month()
        prev_month = _previous_month_name(month)

        current = self._port.fetch_incidents(month)
        previous = self._port.fetch_incidents(prev_month)

        result = _aggregate(current)
        result.previous_month_total_count = len(previous)
        result.previous_month_downtime_minutes = sum(p.get("downtime_minutes", 0) for p in previous)
        result.incidents_decreasing = result.total_count < result.previous_month_total_count

        return ComputeMonthlyIncidentReportResponse(result=result)
