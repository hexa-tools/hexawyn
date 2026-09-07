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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut: MutantDict = {}  # type: ignore


class PlatformReliabilityService:
    """Domain service — turns raw incident data into a business-language CTO
    reliability report: availability, incident counts by severity, resolution
    time and trend, an honest financial impact, and a jargon-free summary."""

    @_mutmut_mutated(mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut)
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_orig(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_1(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
        incidents = None
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_2(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
        incidents = data["XXincidentsXX"]
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_3(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
        incidents = data["INCIDENTS"]
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_4(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
        incidents = data["incidents"]
        counted = None

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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_5(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
        incidents = data["incidents"]
        counted = [incident for incident in incidents if incident["planned_maintenance"]]

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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_6(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
        incidents = data["incidents"]
        counted = [incident for incident in incidents if not incident["XXplanned_maintenanceXX"]]

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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_7(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
        incidents = data["incidents"]
        counted = [incident for incident in incidents if not incident["PLANNED_MAINTENANCE"]]

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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_8(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
        incidents = data["incidents"]
        counted = [incident for incident in incidents if not incident["planned_maintenance"]]

        uptime = None
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_9(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
        incidents = data["incidents"]
        counted = [incident for incident in incidents if not incident["planned_maintenance"]]

        uptime = compute_uptime_pct(None, data["period_minutes"])
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_10(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
        incidents = data["incidents"]
        counted = [incident for incident in incidents if not incident["planned_maintenance"]]

        uptime = compute_uptime_pct(incidents, None)
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_11(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
        incidents = data["incidents"]
        counted = [incident for incident in incidents if not incident["planned_maintenance"]]

        uptime = compute_uptime_pct(data["period_minutes"])
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_12(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
        incidents = data["incidents"]
        counted = [incident for incident in incidents if not incident["planned_maintenance"]]

        uptime = compute_uptime_pct(incidents, )
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_13(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
        incidents = data["incidents"]
        counted = [incident for incident in incidents if not incident["planned_maintenance"]]

        uptime = compute_uptime_pct(incidents, data["XXperiod_minutesXX"])
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_14(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
        incidents = data["incidents"]
        counted = [incident for incident in incidents if not incident["planned_maintenance"]]

        uptime = compute_uptime_pct(incidents, data["PERIOD_MINUTES"])
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_15(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
        incidents = data["incidents"]
        counted = [incident for incident in incidents if not incident["planned_maintenance"]]

        uptime = compute_uptime_pct(incidents, data["period_minutes"])
        resolution = None
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_16(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
        incidents = data["incidents"]
        counted = [incident for incident in incidents if not incident["planned_maintenance"]]

        uptime = compute_uptime_pct(incidents, data["period_minutes"])
        resolution = compute_resolution(None, data["previous_avg_resolution_minutes"])
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_17(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
        incidents = data["incidents"]
        counted = [incident for incident in incidents if not incident["planned_maintenance"]]

        uptime = compute_uptime_pct(incidents, data["period_minutes"])
        resolution = compute_resolution(counted, None)
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_18(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
        incidents = data["incidents"]
        counted = [incident for incident in incidents if not incident["planned_maintenance"]]

        uptime = compute_uptime_pct(incidents, data["period_minutes"])
        resolution = compute_resolution(data["previous_avg_resolution_minutes"])
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_19(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
        incidents = data["incidents"]
        counted = [incident for incident in incidents if not incident["planned_maintenance"]]

        uptime = compute_uptime_pct(incidents, data["period_minutes"])
        resolution = compute_resolution(counted, )
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_20(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
        incidents = data["incidents"]
        counted = [incident for incident in incidents if not incident["planned_maintenance"]]

        uptime = compute_uptime_pct(incidents, data["period_minutes"])
        resolution = compute_resolution(counted, data["XXprevious_avg_resolution_minutesXX"])
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_21(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
        incidents = data["incidents"]
        counted = [incident for incident in incidents if not incident["planned_maintenance"]]

        uptime = compute_uptime_pct(incidents, data["period_minutes"])
        resolution = compute_resolution(counted, data["PREVIOUS_AVG_RESOLUTION_MINUTES"])
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_22(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
        incidents = data["incidents"]
        counted = [incident for incident in incidents if not incident["planned_maintenance"]]

        uptime = compute_uptime_pct(incidents, data["period_minutes"])
        resolution = compute_resolution(counted, data["previous_avg_resolution_minutes"])
        total_downtime = None
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_23(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
        incidents = data["incidents"]
        counted = [incident for incident in incidents if not incident["planned_maintenance"]]

        uptime = compute_uptime_pct(incidents, data["period_minutes"])
        resolution = compute_resolution(counted, data["previous_avg_resolution_minutes"])
        total_downtime = sum(None)
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_24(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
        incidents = data["incidents"]
        counted = [incident for incident in incidents if not incident["planned_maintenance"]]

        uptime = compute_uptime_pct(incidents, data["period_minutes"])
        resolution = compute_resolution(counted, data["previous_avg_resolution_minutes"])
        total_downtime = sum(incident["XXdowntime_minutesXX"] for incident in counted)
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_25(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
        incidents = data["incidents"]
        counted = [incident for incident in incidents if not incident["planned_maintenance"]]

        uptime = compute_uptime_pct(incidents, data["period_minutes"])
        resolution = compute_resolution(counted, data["previous_avg_resolution_minutes"])
        total_downtime = sum(incident["DOWNTIME_MINUTES"] for incident in counted)
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_26(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
        incidents = data["incidents"]
        counted = [incident for incident in incidents if not incident["planned_maintenance"]]

        uptime = compute_uptime_pct(incidents, data["period_minutes"])
        resolution = compute_resolution(counted, data["previous_avg_resolution_minutes"])
        total_downtime = sum(incident["downtime_minutes"] for incident in counted)
        financial_impact = None
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_27(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
        incidents = data["incidents"]
        counted = [incident for incident in incidents if not incident["planned_maintenance"]]

        uptime = compute_uptime_pct(incidents, data["period_minutes"])
        resolution = compute_resolution(counted, data["previous_avg_resolution_minutes"])
        total_downtime = sum(incident["downtime_minutes"] for incident in counted)
        financial_impact = compute_financial_impact(
            None, data["cost_per_downtime_minute_eur"]
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_28(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
        incidents = data["incidents"]
        counted = [incident for incident in incidents if not incident["planned_maintenance"]]

        uptime = compute_uptime_pct(incidents, data["period_minutes"])
        resolution = compute_resolution(counted, data["previous_avg_resolution_minutes"])
        total_downtime = sum(incident["downtime_minutes"] for incident in counted)
        financial_impact = compute_financial_impact(
            total_downtime, None
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_29(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
        incidents = data["incidents"]
        counted = [incident for incident in incidents if not incident["planned_maintenance"]]

        uptime = compute_uptime_pct(incidents, data["period_minutes"])
        resolution = compute_resolution(counted, data["previous_avg_resolution_minutes"])
        total_downtime = sum(incident["downtime_minutes"] for incident in counted)
        financial_impact = compute_financial_impact(
            data["cost_per_downtime_minute_eur"]
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_30(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
        incidents = data["incidents"]
        counted = [incident for incident in incidents if not incident["planned_maintenance"]]

        uptime = compute_uptime_pct(incidents, data["period_minutes"])
        resolution = compute_resolution(counted, data["previous_avg_resolution_minutes"])
        total_downtime = sum(incident["downtime_minutes"] for incident in counted)
        financial_impact = compute_financial_impact(
            total_downtime, )
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_31(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
        incidents = data["incidents"]
        counted = [incident for incident in incidents if not incident["planned_maintenance"]]

        uptime = compute_uptime_pct(incidents, data["period_minutes"])
        resolution = compute_resolution(counted, data["previous_avg_resolution_minutes"])
        total_downtime = sum(incident["downtime_minutes"] for incident in counted)
        financial_impact = compute_financial_impact(
            total_downtime, data["XXcost_per_downtime_minute_eurXX"]
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_32(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
        incidents = data["incidents"]
        counted = [incident for incident in incidents if not incident["planned_maintenance"]]

        uptime = compute_uptime_pct(incidents, data["period_minutes"])
        resolution = compute_resolution(counted, data["previous_avg_resolution_minutes"])
        total_downtime = sum(incident["downtime_minutes"] for incident in counted)
        financial_impact = compute_financial_impact(
            total_downtime, data["COST_PER_DOWNTIME_MINUTE_EUR"]
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_33(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
        incidents = data["incidents"]
        counted = [incident for incident in incidents if not incident["planned_maintenance"]]

        uptime = compute_uptime_pct(incidents, data["period_minutes"])
        resolution = compute_resolution(counted, data["previous_avg_resolution_minutes"])
        total_downtime = sum(incident["downtime_minutes"] for incident in counted)
        financial_impact = compute_financial_impact(
            total_downtime, data["cost_per_downtime_minute_eur"]
        )
        pricing_configured = None

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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_34(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
        incidents = data["incidents"]
        counted = [incident for incident in incidents if not incident["planned_maintenance"]]

        uptime = compute_uptime_pct(incidents, data["period_minutes"])
        resolution = compute_resolution(counted, data["previous_avg_resolution_minutes"])
        total_downtime = sum(incident["downtime_minutes"] for incident in counted)
        financial_impact = compute_financial_impact(
            total_downtime, data["cost_per_downtime_minute_eur"]
        )
        pricing_configured = data["XXcost_per_downtime_minute_eurXX"] is not None

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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_35(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
        incidents = data["incidents"]
        counted = [incident for incident in incidents if not incident["planned_maintenance"]]

        uptime = compute_uptime_pct(incidents, data["period_minutes"])
        resolution = compute_resolution(counted, data["previous_avg_resolution_minutes"])
        total_downtime = sum(incident["downtime_minutes"] for incident in counted)
        financial_impact = compute_financial_impact(
            total_downtime, data["cost_per_downtime_minute_eur"]
        )
        pricing_configured = data["COST_PER_DOWNTIME_MINUTE_EUR"] is not None

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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_36(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
        incidents = data["incidents"]
        counted = [incident for incident in incidents if not incident["planned_maintenance"]]

        uptime = compute_uptime_pct(incidents, data["period_minutes"])
        resolution = compute_resolution(counted, data["previous_avg_resolution_minutes"])
        total_downtime = sum(incident["downtime_minutes"] for incident in counted)
        financial_impact = compute_financial_impact(
            total_downtime, data["cost_per_downtime_minute_eur"]
        )
        pricing_configured = data["cost_per_downtime_minute_eur"] is None

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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_37(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
        incidents = data["incidents"]
        counted = [incident for incident in incidents if not incident["planned_maintenance"]]

        uptime = compute_uptime_pct(incidents, data["period_minutes"])
        resolution = compute_resolution(counted, data["previous_avg_resolution_minutes"])
        total_downtime = sum(incident["downtime_minutes"] for incident in counted)
        financial_impact = compute_financial_impact(
            total_downtime, data["cost_per_downtime_minute_eur"]
        )
        pricing_configured = data["cost_per_downtime_minute_eur"] is not None

        summaries = None
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_38(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
        incidents = data["incidents"]
        counted = [incident for incident in incidents if not incident["planned_maintenance"]]

        uptime = compute_uptime_pct(incidents, data["period_minutes"])
        resolution = compute_resolution(counted, data["previous_avg_resolution_minutes"])
        total_downtime = sum(incident["downtime_minutes"] for incident in counted)
        financial_impact = compute_financial_impact(
            total_downtime, data["cost_per_downtime_minute_eur"]
        )
        pricing_configured = data["cost_per_downtime_minute_eur"] is not None

        summaries = [_to_summary(None) for incident in counted]
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_39(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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
        major_count = None

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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_40(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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
        major_count = sum(None)

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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_41(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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
        major_count = sum(2 for incident in counted if incident["severity"] == _MAJOR)

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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_42(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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
        major_count = sum(1 for incident in counted if incident["XXseverityXX"] == _MAJOR)

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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_43(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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
        major_count = sum(1 for incident in counted if incident["SEVERITY"] == _MAJOR)

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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_44(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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
        major_count = sum(1 for incident in counted if incident["severity"] != _MAJOR)

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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_45(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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

        executive_summary = None

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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_46(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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
            uptime_pct=None,
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_47(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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
            incidents=None,
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_48(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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
            avg_resolution_minutes=None,
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_49(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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
            resolution_delta_pct=None,
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_50(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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
            resolution_trend=None,
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_51(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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
            financial_impact_eur=None,
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_52(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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
            pricing_configured=None,
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_53(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_54(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_55(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_56(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_57(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_58(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_59(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_60(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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
            period_label=None,
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_61(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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
            uptime_pct=None,
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_62(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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
            total_incidents=None,
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_63(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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
            major_count=None,
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_64(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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
            minor_count=None,
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_65(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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
            avg_resolution_minutes=None,
            resolution_trend=resolution.resolution_trend,
            resolution_delta_pct=resolution.resolution_delta_pct,
            previous_avg_resolution_minutes=data["previous_avg_resolution_minutes"],
            financial_impact_eur=financial_impact,
            pricing_configured=pricing_configured,
            incidents=summaries,
            has_major_incident=major_count > 0,
            executive_summary=executive_summary,
        )

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_66(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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
            resolution_trend=None,
            resolution_delta_pct=resolution.resolution_delta_pct,
            previous_avg_resolution_minutes=data["previous_avg_resolution_minutes"],
            financial_impact_eur=financial_impact,
            pricing_configured=pricing_configured,
            incidents=summaries,
            has_major_incident=major_count > 0,
            executive_summary=executive_summary,
        )

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_67(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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
            resolution_delta_pct=None,
            previous_avg_resolution_minutes=data["previous_avg_resolution_minutes"],
            financial_impact_eur=financial_impact,
            pricing_configured=pricing_configured,
            incidents=summaries,
            has_major_incident=major_count > 0,
            executive_summary=executive_summary,
        )

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_68(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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
            previous_avg_resolution_minutes=None,
            financial_impact_eur=financial_impact,
            pricing_configured=pricing_configured,
            incidents=summaries,
            has_major_incident=major_count > 0,
            executive_summary=executive_summary,
        )

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_69(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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
            financial_impact_eur=None,
            pricing_configured=pricing_configured,
            incidents=summaries,
            has_major_incident=major_count > 0,
            executive_summary=executive_summary,
        )

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_70(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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
            pricing_configured=None,
            incidents=summaries,
            has_major_incident=major_count > 0,
            executive_summary=executive_summary,
        )

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_71(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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
            incidents=None,
            has_major_incident=major_count > 0,
            executive_summary=executive_summary,
        )

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_72(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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
            has_major_incident=None,
            executive_summary=executive_summary,
        )

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_73(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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
            executive_summary=None,
        )

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_74(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_75(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_76(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_77(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_78(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_79(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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
            resolution_trend=resolution.resolution_trend,
            resolution_delta_pct=resolution.resolution_delta_pct,
            previous_avg_resolution_minutes=data["previous_avg_resolution_minutes"],
            financial_impact_eur=financial_impact,
            pricing_configured=pricing_configured,
            incidents=summaries,
            has_major_incident=major_count > 0,
            executive_summary=executive_summary,
        )

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_80(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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
            resolution_delta_pct=resolution.resolution_delta_pct,
            previous_avg_resolution_minutes=data["previous_avg_resolution_minutes"],
            financial_impact_eur=financial_impact,
            pricing_configured=pricing_configured,
            incidents=summaries,
            has_major_incident=major_count > 0,
            executive_summary=executive_summary,
        )

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_81(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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
            previous_avg_resolution_minutes=data["previous_avg_resolution_minutes"],
            financial_impact_eur=financial_impact,
            pricing_configured=pricing_configured,
            incidents=summaries,
            has_major_incident=major_count > 0,
            executive_summary=executive_summary,
        )

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_82(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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
            financial_impact_eur=financial_impact,
            pricing_configured=pricing_configured,
            incidents=summaries,
            has_major_incident=major_count > 0,
            executive_summary=executive_summary,
        )

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_83(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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
            pricing_configured=pricing_configured,
            incidents=summaries,
            has_major_incident=major_count > 0,
            executive_summary=executive_summary,
        )

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_84(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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
            incidents=summaries,
            has_major_incident=major_count > 0,
            executive_summary=executive_summary,
        )

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_85(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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
            has_major_incident=major_count > 0,
            executive_summary=executive_summary,
        )

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_86(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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
            executive_summary=executive_summary,
        )

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_87(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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
            )

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_88(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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
            minor_count=len(counted) + major_count,
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

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_89(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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
            previous_avg_resolution_minutes=data["XXprevious_avg_resolution_minutesXX"],
            financial_impact_eur=financial_impact,
            pricing_configured=pricing_configured,
            incidents=summaries,
            has_major_incident=major_count > 0,
            executive_summary=executive_summary,
        )

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_90(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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
            previous_avg_resolution_minutes=data["PREVIOUS_AVG_RESOLUTION_MINUTES"],
            financial_impact_eur=financial_impact,
            pricing_configured=pricing_configured,
            incidents=summaries,
            has_major_incident=major_count > 0,
            executive_summary=executive_summary,
        )

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_91(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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
            has_major_incident=major_count >= 0,
            executive_summary=executive_summary,
        )

    def xǁPlatformReliabilityServiceǁgenerate__mutmut_92(self, data: ReliabilityData, period: str) -> PlatformReliabilityReport:
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
            has_major_incident=major_count > 1,
            executive_summary=executive_summary,
        )

mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['_mutmut_orig'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_orig # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_1'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_1 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_2'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_2 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_3'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_3 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_4'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_4 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_5'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_5 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_6'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_6 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_7'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_7 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_8'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_8 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_9'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_9 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_10'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_10 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_11'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_11 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_12'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_12 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_13'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_13 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_14'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_14 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_15'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_15 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_16'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_16 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_17'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_17 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_18'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_18 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_19'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_19 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_20'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_20 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_21'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_21 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_22'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_22 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_23'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_23 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_24'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_24 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_25'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_25 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_26'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_26 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_27'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_27 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_28'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_28 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_29'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_29 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_30'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_30 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_31'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_31 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_32'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_32 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_33'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_33 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_34'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_34 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_35'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_35 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_36'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_36 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_37'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_37 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_38'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_38 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_39'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_39 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_40'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_40 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_41'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_41 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_42'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_42 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_43'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_43 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_44'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_44 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_45'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_45 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_46'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_46 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_47'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_47 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_48'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_48 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_49'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_49 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_50'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_50 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_51'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_51 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_52'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_52 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_53'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_53 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_54'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_54 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_55'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_55 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_56'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_56 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_57'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_57 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_58'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_58 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_59'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_59 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_60'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_60 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_61'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_61 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_62'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_62 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_63'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_63 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_64'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_64 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_65'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_65 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_66'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_66 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_67'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_67 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_68'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_68 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_69'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_69 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_70'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_70 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_71'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_71 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_72'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_72 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_73'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_73 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_74'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_74 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_75'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_75 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_76'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_76 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_77'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_77 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_78'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_78 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_79'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_79 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_80'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_80 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_81'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_81 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_82'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_82 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_83'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_83 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_84'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_84 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_85'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_85 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_86'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_86 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_87'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_87 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_88'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_88 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_89'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_89 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_90'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_90 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_91'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_91 # type: ignore # mutmut generated
mutants_xǁPlatformReliabilityServiceǁgenerate__mutmut['xǁPlatformReliabilityServiceǁgenerate__mutmut_92'] = PlatformReliabilityService.xǁPlatformReliabilityServiceǁgenerate__mutmut_92 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__to_summary__mutmut)
def _to_summary(incident: ReliabilityIncidentRaw) -> IncidentSummary:
    return IncidentSummary(
        date=incident["date"],
        severity=incident["severity"],
        downtime_minutes=incident["downtime_minutes"],
        root_cause=incident["root_cause"],
        resolved=incident["resolved"],
    )


def x__to_summary__mutmut_orig(incident: ReliabilityIncidentRaw) -> IncidentSummary:
    return IncidentSummary(
        date=incident["date"],
        severity=incident["severity"],
        downtime_minutes=incident["downtime_minutes"],
        root_cause=incident["root_cause"],
        resolved=incident["resolved"],
    )


def x__to_summary__mutmut_1(incident: ReliabilityIncidentRaw) -> IncidentSummary:
    return IncidentSummary(
        date=None,
        severity=incident["severity"],
        downtime_minutes=incident["downtime_minutes"],
        root_cause=incident["root_cause"],
        resolved=incident["resolved"],
    )


def x__to_summary__mutmut_2(incident: ReliabilityIncidentRaw) -> IncidentSummary:
    return IncidentSummary(
        date=incident["date"],
        severity=None,
        downtime_minutes=incident["downtime_minutes"],
        root_cause=incident["root_cause"],
        resolved=incident["resolved"],
    )


def x__to_summary__mutmut_3(incident: ReliabilityIncidentRaw) -> IncidentSummary:
    return IncidentSummary(
        date=incident["date"],
        severity=incident["severity"],
        downtime_minutes=None,
        root_cause=incident["root_cause"],
        resolved=incident["resolved"],
    )


def x__to_summary__mutmut_4(incident: ReliabilityIncidentRaw) -> IncidentSummary:
    return IncidentSummary(
        date=incident["date"],
        severity=incident["severity"],
        downtime_minutes=incident["downtime_minutes"],
        root_cause=None,
        resolved=incident["resolved"],
    )


def x__to_summary__mutmut_5(incident: ReliabilityIncidentRaw) -> IncidentSummary:
    return IncidentSummary(
        date=incident["date"],
        severity=incident["severity"],
        downtime_minutes=incident["downtime_minutes"],
        root_cause=incident["root_cause"],
        resolved=None,
    )


def x__to_summary__mutmut_6(incident: ReliabilityIncidentRaw) -> IncidentSummary:
    return IncidentSummary(
        severity=incident["severity"],
        downtime_minutes=incident["downtime_minutes"],
        root_cause=incident["root_cause"],
        resolved=incident["resolved"],
    )


def x__to_summary__mutmut_7(incident: ReliabilityIncidentRaw) -> IncidentSummary:
    return IncidentSummary(
        date=incident["date"],
        downtime_minutes=incident["downtime_minutes"],
        root_cause=incident["root_cause"],
        resolved=incident["resolved"],
    )


def x__to_summary__mutmut_8(incident: ReliabilityIncidentRaw) -> IncidentSummary:
    return IncidentSummary(
        date=incident["date"],
        severity=incident["severity"],
        root_cause=incident["root_cause"],
        resolved=incident["resolved"],
    )


def x__to_summary__mutmut_9(incident: ReliabilityIncidentRaw) -> IncidentSummary:
    return IncidentSummary(
        date=incident["date"],
        severity=incident["severity"],
        downtime_minutes=incident["downtime_minutes"],
        resolved=incident["resolved"],
    )


def x__to_summary__mutmut_10(incident: ReliabilityIncidentRaw) -> IncidentSummary:
    return IncidentSummary(
        date=incident["date"],
        severity=incident["severity"],
        downtime_minutes=incident["downtime_minutes"],
        root_cause=incident["root_cause"],
        )


def x__to_summary__mutmut_11(incident: ReliabilityIncidentRaw) -> IncidentSummary:
    return IncidentSummary(
        date=incident["XXdateXX"],
        severity=incident["severity"],
        downtime_minutes=incident["downtime_minutes"],
        root_cause=incident["root_cause"],
        resolved=incident["resolved"],
    )


def x__to_summary__mutmut_12(incident: ReliabilityIncidentRaw) -> IncidentSummary:
    return IncidentSummary(
        date=incident["DATE"],
        severity=incident["severity"],
        downtime_minutes=incident["downtime_minutes"],
        root_cause=incident["root_cause"],
        resolved=incident["resolved"],
    )


def x__to_summary__mutmut_13(incident: ReliabilityIncidentRaw) -> IncidentSummary:
    return IncidentSummary(
        date=incident["date"],
        severity=incident["XXseverityXX"],
        downtime_minutes=incident["downtime_minutes"],
        root_cause=incident["root_cause"],
        resolved=incident["resolved"],
    )


def x__to_summary__mutmut_14(incident: ReliabilityIncidentRaw) -> IncidentSummary:
    return IncidentSummary(
        date=incident["date"],
        severity=incident["SEVERITY"],
        downtime_minutes=incident["downtime_minutes"],
        root_cause=incident["root_cause"],
        resolved=incident["resolved"],
    )


def x__to_summary__mutmut_15(incident: ReliabilityIncidentRaw) -> IncidentSummary:
    return IncidentSummary(
        date=incident["date"],
        severity=incident["severity"],
        downtime_minutes=incident["XXdowntime_minutesXX"],
        root_cause=incident["root_cause"],
        resolved=incident["resolved"],
    )


def x__to_summary__mutmut_16(incident: ReliabilityIncidentRaw) -> IncidentSummary:
    return IncidentSummary(
        date=incident["date"],
        severity=incident["severity"],
        downtime_minutes=incident["DOWNTIME_MINUTES"],
        root_cause=incident["root_cause"],
        resolved=incident["resolved"],
    )


def x__to_summary__mutmut_17(incident: ReliabilityIncidentRaw) -> IncidentSummary:
    return IncidentSummary(
        date=incident["date"],
        severity=incident["severity"],
        downtime_minutes=incident["downtime_minutes"],
        root_cause=incident["XXroot_causeXX"],
        resolved=incident["resolved"],
    )


def x__to_summary__mutmut_18(incident: ReliabilityIncidentRaw) -> IncidentSummary:
    return IncidentSummary(
        date=incident["date"],
        severity=incident["severity"],
        downtime_minutes=incident["downtime_minutes"],
        root_cause=incident["ROOT_CAUSE"],
        resolved=incident["resolved"],
    )


def x__to_summary__mutmut_19(incident: ReliabilityIncidentRaw) -> IncidentSummary:
    return IncidentSummary(
        date=incident["date"],
        severity=incident["severity"],
        downtime_minutes=incident["downtime_minutes"],
        root_cause=incident["root_cause"],
        resolved=incident["XXresolvedXX"],
    )


def x__to_summary__mutmut_20(incident: ReliabilityIncidentRaw) -> IncidentSummary:
    return IncidentSummary(
        date=incident["date"],
        severity=incident["severity"],
        downtime_minutes=incident["downtime_minutes"],
        root_cause=incident["root_cause"],
        resolved=incident["RESOLVED"],
    )

mutants_x__to_summary__mutmut['_mutmut_orig'] = x__to_summary__mutmut_orig # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_1'] = x__to_summary__mutmut_1 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_2'] = x__to_summary__mutmut_2 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_3'] = x__to_summary__mutmut_3 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_4'] = x__to_summary__mutmut_4 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_5'] = x__to_summary__mutmut_5 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_6'] = x__to_summary__mutmut_6 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_7'] = x__to_summary__mutmut_7 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_8'] = x__to_summary__mutmut_8 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_9'] = x__to_summary__mutmut_9 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_10'] = x__to_summary__mutmut_10 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_11'] = x__to_summary__mutmut_11 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_12'] = x__to_summary__mutmut_12 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_13'] = x__to_summary__mutmut_13 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_14'] = x__to_summary__mutmut_14 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_15'] = x__to_summary__mutmut_15 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_16'] = x__to_summary__mutmut_16 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_17'] = x__to_summary__mutmut_17 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_18'] = x__to_summary__mutmut_18 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_19'] = x__to_summary__mutmut_19 # type: ignore # mutmut generated
mutants_x__to_summary__mutmut['x__to_summary__mutmut_20'] = x__to_summary__mutmut_20 # type: ignore # mutmut generated
