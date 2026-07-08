from __future__ import annotations

from hexawyn.domain.models.weekly_reliability_report import (
    ServiceReliability,
    TopIncident,
    WeeklyReliabilityReport,
)

_MAX_TOP_INCIDENTS = 3


class WeeklyReliabilityReportEngine:
    """Pure domain service — no infra deps, no try/catch."""

    def compute(
        self,
        services_raw: list[dict[str, object]],
        incidents_raw: list[dict[str, object]],
    ) -> WeeklyReliabilityReport:
        services = [_build_service_reliability(s) for s in services_raw]
        ranked_incidents = _rank_incidents(incidents_raw)

        slo_pass = sum(1 for s in services if s.slo_status == "pass")
        slo_fail = len(services) - slo_pass
        health_score = round((slo_pass / len(services)) * 100.0, 1) if len(services) > 0 else 0.0

        return WeeklyReliabilityReport(
            report_period_start="",
            report_period_end="",
            services=services,
            top_incidents=ranked_incidents,
            total_incident_count=len(incidents_raw),
            health_score=health_score,
            slo_pass_count=slo_pass,
            slo_fail_count=slo_fail,
            total_services=len(services),
        )


def _build_service_reliability(raw: dict[str, object]) -> ServiceReliability:
    uptime = _as_float(raw.get("uptime_pct"))
    slo_target = _as_float(raw.get("slo_target"))
    slo_status = "pass" if uptime >= slo_target else "fail"

    return ServiceReliability(
        service_name=str(raw.get("service_name", "")),
        uptime_pct=uptime,
        error_rate=_as_float(raw.get("error_rate")),
        p99_latency_ms=_as_float(raw.get("p99_latency_ms")),
        slo_target=slo_target,
        slo_status=slo_status,
        downtime_minutes=_as_int(raw.get("downtime_minutes")),
        data_gap_minutes=_as_int(raw.get("data_gap_minutes")),
        created_mid_week=_as_bool(raw.get("created_mid_week")),
    )


def _rank_incidents(
    incidents_raw: list[dict[str, object]],
) -> list[TopIncident]:
    scored: list[TopIncident] = []
    for inc in incidents_raw:
        duration = _as_int(inc.get("duration_minutes"))
        error_rate = _as_float(inc.get("error_rate"))
        impact = round(duration * error_rate, 2)

        scored.append(
            TopIncident(
                service_name=str(inc.get("service_name", "")),
                timestamp=str(inc.get("timestamp", "")),
                duration_minutes=duration,
                error_rate=error_rate,
                impact_score=impact,
                description=str(inc.get("description", "")),
            )
        )

    scored.sort(key=lambda x: x.impact_score, reverse=True)
    return scored[:_MAX_TOP_INCIDENTS]


def _as_float(value: object) -> float:
    if value is None:
        return 0.0
    try:
        return float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0.0


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
