from __future__ import annotations

from hexawyn.domain.models.monthly_incident_report import (
    ImpactedService,
    MonthlyIncidentReport,
    SeverityBreakdown,
)


class MonthlyIncidentReportEngine:
    def compute(
        self,
        incidents: list[dict[str, object]],
        previous_incidents: list[dict[str, object]] | None = None,
    ) -> MonthlyIncidentReport:
        prev_incidents = previous_incidents or []
        curr_total, curr_downtime, curr_severity = _process_incidents(incidents)
        prev_total, prev_downtime, _ = _process_incidents(prev_incidents)
        decreasing = curr_total < prev_total

        return MonthlyIncidentReport(
            total_count=curr_total,
            total_downtime_minutes=curr_downtime,
            per_severity={
                sev: SeverityBreakdown(
                    severity=sev,
                    count=data["count"],
                    downtime_minutes=data["downtime"],
                )
                for sev, data in curr_severity.items()
            },
            most_impacted_services=_rank_impacted_services(incidents),
            previous_month_total_count=prev_total,
            previous_month_downtime_minutes=prev_downtime,
            incidents_decreasing=decreasing,
        )


def _process_incidents(
    incidents: list[dict[str, object]],
) -> tuple[int, int, dict[str, dict[str, int]]]:
    total_count = 0
    total_downtime = 0
    severity_map: dict[str, dict[str, int]] = {
        "P1": {"count": 0, "downtime": 0},
        "P2": {"count": 0, "downtime": 0},
        "P3": {"count": 0, "downtime": 0},
    }

    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue

        sev = str(inc.get("severity", "P3"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def _rank_impacted_services(
    incidents: list[dict[str, object]],
) -> list[ImpactedService]:
    svc_map: dict[str, dict[str, int]] = {}
    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue
        svc = str(inc.get("service_name", ""))
        downtime = _as_int(inc.get("downtime_minutes"))
        if svc not in svc_map:
            svc_map[svc] = {"total_downtime": 0, "incident_count": 0}
        svc_map[svc]["total_downtime"] += downtime
        svc_map[svc]["incident_count"] += 1

    result = [
        ImpactedService(
            service_name=svc,
            total_downtime=data["total_downtime"],
            incident_count=data["incident_count"],
        )
        for svc, data in svc_map.items()
    ]
    result.sort(key=lambda s: s.total_downtime, reverse=True)
    return result


def _as_int(value: object) -> int:
    if value is None:
        return 0
    try:
        return int(float(value))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0


def _as_bool(value: object) -> bool:
    if value is None:
        return False
    if isinstance(value, bool):
        return value
    return bool(value)
