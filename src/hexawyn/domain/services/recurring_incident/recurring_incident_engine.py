from __future__ import annotations

from hexawyn.domain.models.recurring_incident import (
    RecurringIncidentReport,
    ServiceIncidentSummary,
)

_TOP_N = 10
_RECURRENCE_THRESHOLD = 3


class RecurringIncidentEngine:
    def compute(
        self,
        incidents: list[dict[str, object]],
    ) -> RecurringIncidentReport:
        svc_counts: dict[str, int] = {}
        svc_durations: dict[str, list[float]] = {}
        svc_causes: dict[str, dict[str, int]] = {}

        for inc in incidents:
            svc = str(inc.get("service_name", ""))
            cause = str(inc.get("root_cause", ""))
            if not cause:
                cause = "uncategorized"
            duration = _as_float(inc.get("duration_minutes"))

            svc_counts[svc] = svc_counts.get(svc, 0) + 1
            if svc not in svc_durations:
                svc_durations[svc] = []
            svc_durations[svc].append(duration)

            if svc not in svc_causes:
                svc_causes[svc] = {}
            svc_causes[svc][cause] = svc_causes[svc].get(cause, 0) + 1

        summaries: list[ServiceIncidentSummary] = []
        for svc in svc_counts:
            count = svc_counts[svc]
            durations = svc_durations.get(svc, [])
            avg = round(sum(durations) / len(durations), 1) if durations else 0.0
            causes = svc_causes.get(svc, {})
            most_common = max(causes, key=lambda k: causes[k]) if causes else "uncategorized"
            rec_count = causes.get(most_common, 0)
            is_recurring = rec_count > _RECURRENCE_THRESHOLD
            recommendation = _recommend(count, is_recurring, rec_count)

            summaries.append(
                ServiceIncidentSummary(
                    service_name=svc,
                    incident_count=count,
                    avg_duration_minutes=avg,
                    most_common_cause=most_common,
                    recurrence_count=rec_count,
                    is_recurring=is_recurring,
                    recommendation=recommendation,
                )
            )

        summaries.sort(key=lambda s: s.incident_count, reverse=True)
        return RecurringIncidentReport(services=summaries[:_TOP_N])


def _recommend(count: int, recurring: bool, recurrence_count: int) -> str:
    if recurring and recurrence_count > _RECURRENCE_THRESHOLD:
        return "Recurring pattern detected — invest in code quality and root cause fix"
    if count >= 5:  # noqa: PLR2004
        return "High incident frequency — prioritize reliability improvements and auto-scaling"
    if count >= 3:  # noqa: PLR2004
        return "Moderate incident frequency — review capacity limits and resource allocation"
    return "Low incident frequency — monitor and address root cause individually"


def _as_float(value: object) -> float:
    if value is None:
        return 0.0
    try:
        return float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0.0
