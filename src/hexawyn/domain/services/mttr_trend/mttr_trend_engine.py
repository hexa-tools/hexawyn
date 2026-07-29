from __future__ import annotations

from hexawyn.domain.models.mttr_trend import (
    MTTRPerSeverity,
    MTTRTrendReport,
    SlowestIncident,
)

_BENCHMARKS = {"P1": 30, "P2": 120}
_SIGNIFICANT_TREND_PCT = 10


class MTTRTrendEngine:
    def compute(
        self,
        months: dict[str, list[dict[str, object]]],
    ) -> MTTRTrendReport:
        per_month: dict[str, dict[str, MTTRPerSeverity]] = {}
        all_slowest: list[dict[str, object]] = []

        for month, incidents in months.items():
            per_month[month] = {}
            sev_data: dict[str, dict[str, float | int]] = {}

            for inc in incidents:
                all_slowest.append(inc)
                if not _as_bool(inc.get("resolved")):
                    continue

                sev = str(inc.get("severity", "P1"))
                mins = _as_int(inc.get("resolution_minutes"))

                if sev not in sev_data:
                    sev_data[sev] = {"total": 0.0, "count": 0}
                sev_data[sev]["total"] += mins
                sev_data[sev]["count"] += 1

            for sev in _BENCHMARKS:
                if sev in sev_data and sev_data[sev]["count"] > 0:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS.get(sev, 0)
                    per_month[month][sev] = MTTRPerSeverity(
                        severity=sev,
                        mttr_minutes=mttr,
                        incident_count=int(sev_data[sev]["count"]),
                        meets_benchmark=meets,
                    )
                else:
                    per_month[month][sev] = MTTRPerSeverity(
                        severity=sev,
                        mttr_minutes=None,
                        incident_count=0,
                        meets_benchmark=False,
                    )

        sorted_months = sorted(months.keys())
        trend, recommendation = _compute_trend(per_month, sorted_months)

        slowest = _rank_slowest(all_slowest)

        report = MTTRTrendReport(
            per_month=per_month,
            slowest_incidents=slowest,
            trend=trend,
            recommendation=recommendation,
        )
        return report


def _compute_trend(
    per_month: dict[str, dict[str, MTTRPerSeverity]],
    sorted_months: list[str],
) -> tuple[str, str]:
    p1_values: list[float] = []
    for m in sorted_months:
        p1 = per_month.get(m, {}).get("P1")
        if p1 and p1.mttr_minutes is not None:
            p1_values.append(p1.mttr_minutes)

    if len(p1_values) < 2:  # noqa: PLR2004
        return "insufficient_data", "Need at least 2 months of P1 data for trend analysis"

    first = p1_values[0]
    last = p1_values[-1]
    if first == 0:
        return "stable", "No change in MTTR"

    delta = round(((last - first) / first) * 100.0, 1)

    if abs(delta) < _SIGNIFICANT_TREND_PCT:
        return "stable", "MTTR is stable across the period"
    if delta < 0:
        return "improving", f"MTTR improved by {abs(delta):.0f}% — response processes are effective"
    return (
        "degrading",
        f"MTTR degraded by {delta:.0f}% — review on-call runbooks and escalation paths",
    )


def _rank_slowest(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("resolution_minutes")), reverse=True)
    top = ranked[:3]
    return [
        SlowestIncident(
            incident_id=str(inc.get("incident_id", "")),
            service_name=str(inc.get("service_name", "")),
            severity=str(inc.get("severity", "P1")),
            resolution_minutes=_as_int(inc.get("resolution_minutes")),
            root_cause=str(inc.get("root_cause", "")),
            month="",
        )
        for inc in top
    ]


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
