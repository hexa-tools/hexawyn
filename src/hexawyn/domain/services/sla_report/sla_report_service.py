from __future__ import annotations

from hexawyn.application.ports.driven.sla_report_port import (
    QuarterSlaData,
    ServiceSlaRaw,
    SlaBreachRaw,
)
from hexawyn.domain.models.sla_report import ServiceSla, SlaBreach, SlaReport
from hexawyn.domain.services.sla_report.sla_trend import classify_trend
from hexawyn.domain.services.sla_report.uptime_calculator import evaluate_service

_NO_DATA_WARNING = (
    "No incident or reliability data available for this quarter — SLA figures "
    "cannot be computed. Verify the observability data source."
)


class SlaReportService:
    """Domain service — builds an executive quarterly SLA report: per-service
    uptime vs target, breaches (excluding planned maintenance), mid-quarter
    proration, and the quarter-over-quarter reliability trend."""

    def generate(
        self,
        data: QuarterSlaData,
        quarter: str,
        previous_avg: float | None,
    ) -> SlaReport:
        if not data["has_data"]:
            return SlaReport(quarter_label=quarter, has_data=False, warning=_NO_DATA_WARNING)

        breaches_by_service = _group_breaches(data["breaches"])
        services = [
            _build_service_sla(raw, breaches_by_service.get(raw["service_name"], []))
            for raw in data["services"]
        ]

        current_avg = _average_uptime(services)
        return SlaReport(
            quarter_label=quarter,
            services=services,
            overall_met_count=sum(1 for service in services if service.met),
            overall_breached_count=sum(1 for service in services if not service.met),
            trend=classify_trend(current_avg, previous_avg),
            previous_avg_uptime_pct=previous_avg,
            current_avg_uptime_pct=current_avg,
            has_data=True,
        )


def _group_breaches(breaches: list[SlaBreachRaw]) -> dict[str, list[SlaBreach]]:
    grouped: dict[str, list[SlaBreach]] = {}
    for raw in breaches:
        if raw["planned_maintenance"]:
            continue
        grouped.setdefault(raw["service_name"], []).append(
            SlaBreach(
                service_name=raw["service_name"],
                date=raw["date"],
                duration_minutes=raw["duration_minutes"],
                impacted_users=raw["impacted_users"],
                root_cause_ref=raw["root_cause_ref"],
            )
        )
    return grouped


def _build_service_sla(raw: ServiceSlaRaw, breaches: list[SlaBreach]) -> ServiceSla:
    evaluation = evaluate_service(raw)
    return ServiceSla(
        service_name=raw["service_name"],
        sla_target_pct=raw["sla_target_pct"],
        actual_uptime_pct=evaluation.actual_uptime_pct,
        met=evaluation.met,
        exceeded=evaluation.exceeded,
        breaches=breaches,
        breach_count=len(breaches),
        prorated=evaluation.prorated,
        coverage_days=evaluation.coverage_days,
    )


def _average_uptime(services: list[ServiceSla]) -> float:
    if not services:
        return 0.0
    return round(sum(service.actual_uptime_pct for service in services) / len(services), 3)
