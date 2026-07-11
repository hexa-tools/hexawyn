from __future__ import annotations

from hexawyn.application.ports.driven.platform_reliability_port import (
    ReliabilityData,
    ReliabilityIncidentRaw,
)
from hexawyn.domain.models.platform_reliability import (
    IncidentSummary,
    PlatformReliabilityReport,
)
from hexawyn.domain.services.platform_reliability.executive_summary_builder import (
    build_summary,
)
from hexawyn.domain.services.platform_reliability.financial_impact import (
    compute_financial_impact,
)
from hexawyn.domain.services.platform_reliability.resolution_trend import (
    compute_resolution,
)
from hexawyn.domain.services.platform_reliability.uptime_calculator import (
    compute_uptime_pct,
)

_MAJOR = "major"


class PlatformReliabilityService:
    """Domain service — turns raw incident data into a business-language CTO
    reliability report: availability, incident counts by severity, resolution
    time and trend, an honest financial impact, and a jargon-free summary."""

    def generate(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
        incidents = data["incidents"]
        counted = [incident for incident in incidents if not incident["planned_maintenance"]]

        uptime = compute_uptime_pct(incidents, data["period_minutes"])
        resolution = compute_resolution(counted, data["previous_avg_resolution_minutes"])
        total_downtime = sum(incident["downtime_minutes"] for incident in counted)
        financial_impact = compute_financial_impact(
            total_downtime, data["cost_per_downtime_minute_eur"]
        )
        pricing_configured = data["cost_per_downtime_minute_eur"] is not None

        summaries = [_to_summary(incident) for incident in counted]
        major_count = sum(1 for incident in counted if incident["severity"] == _MAJOR)

        executive_summary = build_summary(
            uptime_pct=uptime,
            incidents=summaries,
            avg_resolution_minutes=resolution.avg_resolution_minutes,
            resolution_delta_pct=resolution.resolution_delta_pct,
            resolution_trend=resolution.resolution_trend,
            financial_impact_eur=financial_impact,
            pricing_configured=pricing_configured,
        )

        return PlatformReliabilityReport(
            period_label=period,
            uptime_pct=uptime,
            total_incidents=len(counted),
            major_count=major_count,
            minor_count=len(counted) - major_count,
            avg_resolution_minutes=resolution.avg_resolution_minutes,
            resolution_trend=resolution.resolution_trend,
            resolution_delta_pct=resolution.resolution_delta_pct,
            previous_avg_resolution_minutes=data["previous_avg_resolution_minutes"],
            financial_impact_eur=financial_impact,
            pricing_configured=pricing_configured,
            incidents=summaries,
            has_major_incident=major_count > 0,
            executive_summary=executive_summary,
        )


def _to_summary(incident: ReliabilityIncidentRaw) -> IncidentSummary:
    return IncidentSummary(
        date=incident["date"],
        severity=incident["severity"],
        downtime_minutes=incident["downtime_minutes"],
        root_cause=incident["root_cause"],
        resolved=incident["resolved"],
    )
