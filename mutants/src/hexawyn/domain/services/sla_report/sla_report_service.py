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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁSlaReportServiceǁgenerate__mutmut: MutantDict = {}  # type: ignore


class SlaReportService:
    """Domain service — builds an executive quarterly SLA report: per-service
    uptime vs target, breaches (excluding planned maintenance), mid-quarter
    proration, and the quarter-over-quarter reliability trend."""

    @_mutmut_mutated(mutants_xǁSlaReportServiceǁgenerate__mutmut)
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

    def xǁSlaReportServiceǁgenerate__mutmut_orig(
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

    def xǁSlaReportServiceǁgenerate__mutmut_1(
        self,
        data: QuarterSlaData,
        quarter: str,
        previous_avg: float | None,
    ) -> SlaReport:
        if data["has_data"]:
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

    def xǁSlaReportServiceǁgenerate__mutmut_2(
        self,
        data: QuarterSlaData,
        quarter: str,
        previous_avg: float | None,
    ) -> SlaReport:
        if not data["XXhas_dataXX"]:
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

    def xǁSlaReportServiceǁgenerate__mutmut_3(
        self,
        data: QuarterSlaData,
        quarter: str,
        previous_avg: float | None,
    ) -> SlaReport:
        if not data["HAS_DATA"]:
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

    def xǁSlaReportServiceǁgenerate__mutmut_4(
        self,
        data: QuarterSlaData,
        quarter: str,
        previous_avg: float | None,
    ) -> SlaReport:
        if not data["has_data"]:
            return SlaReport(quarter_label=None, has_data=False, warning=_NO_DATA_WARNING)

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

    def xǁSlaReportServiceǁgenerate__mutmut_5(
        self,
        data: QuarterSlaData,
        quarter: str,
        previous_avg: float | None,
    ) -> SlaReport:
        if not data["has_data"]:
            return SlaReport(quarter_label=quarter, has_data=None, warning=_NO_DATA_WARNING)

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

    def xǁSlaReportServiceǁgenerate__mutmut_6(
        self,
        data: QuarterSlaData,
        quarter: str,
        previous_avg: float | None,
    ) -> SlaReport:
        if not data["has_data"]:
            return SlaReport(quarter_label=quarter, has_data=False, warning=None)

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

    def xǁSlaReportServiceǁgenerate__mutmut_7(
        self,
        data: QuarterSlaData,
        quarter: str,
        previous_avg: float | None,
    ) -> SlaReport:
        if not data["has_data"]:
            return SlaReport(has_data=False, warning=_NO_DATA_WARNING)

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

    def xǁSlaReportServiceǁgenerate__mutmut_8(
        self,
        data: QuarterSlaData,
        quarter: str,
        previous_avg: float | None,
    ) -> SlaReport:
        if not data["has_data"]:
            return SlaReport(quarter_label=quarter, warning=_NO_DATA_WARNING)

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

    def xǁSlaReportServiceǁgenerate__mutmut_9(
        self,
        data: QuarterSlaData,
        quarter: str,
        previous_avg: float | None,
    ) -> SlaReport:
        if not data["has_data"]:
            return SlaReport(quarter_label=quarter, has_data=False, )

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

    def xǁSlaReportServiceǁgenerate__mutmut_10(
        self,
        data: QuarterSlaData,
        quarter: str,
        previous_avg: float | None,
    ) -> SlaReport:
        if not data["has_data"]:
            return SlaReport(quarter_label=quarter, has_data=True, warning=_NO_DATA_WARNING)

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

    def xǁSlaReportServiceǁgenerate__mutmut_11(
        self,
        data: QuarterSlaData,
        quarter: str,
        previous_avg: float | None,
    ) -> SlaReport:
        if not data["has_data"]:
            return SlaReport(quarter_label=quarter, has_data=False, warning=_NO_DATA_WARNING)

        breaches_by_service = None
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

    def xǁSlaReportServiceǁgenerate__mutmut_12(
        self,
        data: QuarterSlaData,
        quarter: str,
        previous_avg: float | None,
    ) -> SlaReport:
        if not data["has_data"]:
            return SlaReport(quarter_label=quarter, has_data=False, warning=_NO_DATA_WARNING)

        breaches_by_service = _group_breaches(None)
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

    def xǁSlaReportServiceǁgenerate__mutmut_13(
        self,
        data: QuarterSlaData,
        quarter: str,
        previous_avg: float | None,
    ) -> SlaReport:
        if not data["has_data"]:
            return SlaReport(quarter_label=quarter, has_data=False, warning=_NO_DATA_WARNING)

        breaches_by_service = _group_breaches(data["XXbreachesXX"])
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

    def xǁSlaReportServiceǁgenerate__mutmut_14(
        self,
        data: QuarterSlaData,
        quarter: str,
        previous_avg: float | None,
    ) -> SlaReport:
        if not data["has_data"]:
            return SlaReport(quarter_label=quarter, has_data=False, warning=_NO_DATA_WARNING)

        breaches_by_service = _group_breaches(data["BREACHES"])
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

    def xǁSlaReportServiceǁgenerate__mutmut_15(
        self,
        data: QuarterSlaData,
        quarter: str,
        previous_avg: float | None,
    ) -> SlaReport:
        if not data["has_data"]:
            return SlaReport(quarter_label=quarter, has_data=False, warning=_NO_DATA_WARNING)

        breaches_by_service = _group_breaches(data["breaches"])
        services = None

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

    def xǁSlaReportServiceǁgenerate__mutmut_16(
        self,
        data: QuarterSlaData,
        quarter: str,
        previous_avg: float | None,
    ) -> SlaReport:
        if not data["has_data"]:
            return SlaReport(quarter_label=quarter, has_data=False, warning=_NO_DATA_WARNING)

        breaches_by_service = _group_breaches(data["breaches"])
        services = [
            _build_service_sla(None, breaches_by_service.get(raw["service_name"], []))
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

    def xǁSlaReportServiceǁgenerate__mutmut_17(
        self,
        data: QuarterSlaData,
        quarter: str,
        previous_avg: float | None,
    ) -> SlaReport:
        if not data["has_data"]:
            return SlaReport(quarter_label=quarter, has_data=False, warning=_NO_DATA_WARNING)

        breaches_by_service = _group_breaches(data["breaches"])
        services = [
            _build_service_sla(raw, None)
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

    def xǁSlaReportServiceǁgenerate__mutmut_18(
        self,
        data: QuarterSlaData,
        quarter: str,
        previous_avg: float | None,
    ) -> SlaReport:
        if not data["has_data"]:
            return SlaReport(quarter_label=quarter, has_data=False, warning=_NO_DATA_WARNING)

        breaches_by_service = _group_breaches(data["breaches"])
        services = [
            _build_service_sla(breaches_by_service.get(raw["service_name"], []))
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

    def xǁSlaReportServiceǁgenerate__mutmut_19(
        self,
        data: QuarterSlaData,
        quarter: str,
        previous_avg: float | None,
    ) -> SlaReport:
        if not data["has_data"]:
            return SlaReport(quarter_label=quarter, has_data=False, warning=_NO_DATA_WARNING)

        breaches_by_service = _group_breaches(data["breaches"])
        services = [
            _build_service_sla(raw, )
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

    def xǁSlaReportServiceǁgenerate__mutmut_20(
        self,
        data: QuarterSlaData,
        quarter: str,
        previous_avg: float | None,
    ) -> SlaReport:
        if not data["has_data"]:
            return SlaReport(quarter_label=quarter, has_data=False, warning=_NO_DATA_WARNING)

        breaches_by_service = _group_breaches(data["breaches"])
        services = [
            _build_service_sla(raw, breaches_by_service.get(None, []))
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

    def xǁSlaReportServiceǁgenerate__mutmut_21(
        self,
        data: QuarterSlaData,
        quarter: str,
        previous_avg: float | None,
    ) -> SlaReport:
        if not data["has_data"]:
            return SlaReport(quarter_label=quarter, has_data=False, warning=_NO_DATA_WARNING)

        breaches_by_service = _group_breaches(data["breaches"])
        services = [
            _build_service_sla(raw, breaches_by_service.get(raw["service_name"], None))
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

    def xǁSlaReportServiceǁgenerate__mutmut_22(
        self,
        data: QuarterSlaData,
        quarter: str,
        previous_avg: float | None,
    ) -> SlaReport:
        if not data["has_data"]:
            return SlaReport(quarter_label=quarter, has_data=False, warning=_NO_DATA_WARNING)

        breaches_by_service = _group_breaches(data["breaches"])
        services = [
            _build_service_sla(raw, breaches_by_service.get([]))
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

    def xǁSlaReportServiceǁgenerate__mutmut_23(
        self,
        data: QuarterSlaData,
        quarter: str,
        previous_avg: float | None,
    ) -> SlaReport:
        if not data["has_data"]:
            return SlaReport(quarter_label=quarter, has_data=False, warning=_NO_DATA_WARNING)

        breaches_by_service = _group_breaches(data["breaches"])
        services = [
            _build_service_sla(raw, breaches_by_service.get(raw["service_name"], ))
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

    def xǁSlaReportServiceǁgenerate__mutmut_24(
        self,
        data: QuarterSlaData,
        quarter: str,
        previous_avg: float | None,
    ) -> SlaReport:
        if not data["has_data"]:
            return SlaReport(quarter_label=quarter, has_data=False, warning=_NO_DATA_WARNING)

        breaches_by_service = _group_breaches(data["breaches"])
        services = [
            _build_service_sla(raw, breaches_by_service.get(raw["XXservice_nameXX"], []))
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

    def xǁSlaReportServiceǁgenerate__mutmut_25(
        self,
        data: QuarterSlaData,
        quarter: str,
        previous_avg: float | None,
    ) -> SlaReport:
        if not data["has_data"]:
            return SlaReport(quarter_label=quarter, has_data=False, warning=_NO_DATA_WARNING)

        breaches_by_service = _group_breaches(data["breaches"])
        services = [
            _build_service_sla(raw, breaches_by_service.get(raw["SERVICE_NAME"], []))
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

    def xǁSlaReportServiceǁgenerate__mutmut_26(
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
            for raw in data["XXservicesXX"]
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

    def xǁSlaReportServiceǁgenerate__mutmut_27(
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
            for raw in data["SERVICES"]
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

    def xǁSlaReportServiceǁgenerate__mutmut_28(
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

        current_avg = None
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

    def xǁSlaReportServiceǁgenerate__mutmut_29(
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

        current_avg = _average_uptime(None)
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

    def xǁSlaReportServiceǁgenerate__mutmut_30(
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
            quarter_label=None,
            services=services,
            overall_met_count=sum(1 for service in services if service.met),
            overall_breached_count=sum(1 for service in services if not service.met),
            trend=classify_trend(current_avg, previous_avg),
            previous_avg_uptime_pct=previous_avg,
            current_avg_uptime_pct=current_avg,
            has_data=True,
        )

    def xǁSlaReportServiceǁgenerate__mutmut_31(
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
            services=None,
            overall_met_count=sum(1 for service in services if service.met),
            overall_breached_count=sum(1 for service in services if not service.met),
            trend=classify_trend(current_avg, previous_avg),
            previous_avg_uptime_pct=previous_avg,
            current_avg_uptime_pct=current_avg,
            has_data=True,
        )

    def xǁSlaReportServiceǁgenerate__mutmut_32(
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
            overall_met_count=None,
            overall_breached_count=sum(1 for service in services if not service.met),
            trend=classify_trend(current_avg, previous_avg),
            previous_avg_uptime_pct=previous_avg,
            current_avg_uptime_pct=current_avg,
            has_data=True,
        )

    def xǁSlaReportServiceǁgenerate__mutmut_33(
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
            overall_breached_count=None,
            trend=classify_trend(current_avg, previous_avg),
            previous_avg_uptime_pct=previous_avg,
            current_avg_uptime_pct=current_avg,
            has_data=True,
        )

    def xǁSlaReportServiceǁgenerate__mutmut_34(
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
            trend=None,
            previous_avg_uptime_pct=previous_avg,
            current_avg_uptime_pct=current_avg,
            has_data=True,
        )

    def xǁSlaReportServiceǁgenerate__mutmut_35(
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
            previous_avg_uptime_pct=None,
            current_avg_uptime_pct=current_avg,
            has_data=True,
        )

    def xǁSlaReportServiceǁgenerate__mutmut_36(
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
            current_avg_uptime_pct=None,
            has_data=True,
        )

    def xǁSlaReportServiceǁgenerate__mutmut_37(
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
            has_data=None,
        )

    def xǁSlaReportServiceǁgenerate__mutmut_38(
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
            services=services,
            overall_met_count=sum(1 for service in services if service.met),
            overall_breached_count=sum(1 for service in services if not service.met),
            trend=classify_trend(current_avg, previous_avg),
            previous_avg_uptime_pct=previous_avg,
            current_avg_uptime_pct=current_avg,
            has_data=True,
        )

    def xǁSlaReportServiceǁgenerate__mutmut_39(
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
            overall_met_count=sum(1 for service in services if service.met),
            overall_breached_count=sum(1 for service in services if not service.met),
            trend=classify_trend(current_avg, previous_avg),
            previous_avg_uptime_pct=previous_avg,
            current_avg_uptime_pct=current_avg,
            has_data=True,
        )

    def xǁSlaReportServiceǁgenerate__mutmut_40(
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
            overall_breached_count=sum(1 for service in services if not service.met),
            trend=classify_trend(current_avg, previous_avg),
            previous_avg_uptime_pct=previous_avg,
            current_avg_uptime_pct=current_avg,
            has_data=True,
        )

    def xǁSlaReportServiceǁgenerate__mutmut_41(
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
            trend=classify_trend(current_avg, previous_avg),
            previous_avg_uptime_pct=previous_avg,
            current_avg_uptime_pct=current_avg,
            has_data=True,
        )

    def xǁSlaReportServiceǁgenerate__mutmut_42(
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
            previous_avg_uptime_pct=previous_avg,
            current_avg_uptime_pct=current_avg,
            has_data=True,
        )

    def xǁSlaReportServiceǁgenerate__mutmut_43(
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
            current_avg_uptime_pct=current_avg,
            has_data=True,
        )

    def xǁSlaReportServiceǁgenerate__mutmut_44(
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
            has_data=True,
        )

    def xǁSlaReportServiceǁgenerate__mutmut_45(
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
            )

    def xǁSlaReportServiceǁgenerate__mutmut_46(
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
            overall_met_count=sum(None),
            overall_breached_count=sum(1 for service in services if not service.met),
            trend=classify_trend(current_avg, previous_avg),
            previous_avg_uptime_pct=previous_avg,
            current_avg_uptime_pct=current_avg,
            has_data=True,
        )

    def xǁSlaReportServiceǁgenerate__mutmut_47(
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
            overall_met_count=sum(2 for service in services if service.met),
            overall_breached_count=sum(1 for service in services if not service.met),
            trend=classify_trend(current_avg, previous_avg),
            previous_avg_uptime_pct=previous_avg,
            current_avg_uptime_pct=current_avg,
            has_data=True,
        )

    def xǁSlaReportServiceǁgenerate__mutmut_48(
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
            overall_breached_count=sum(None),
            trend=classify_trend(current_avg, previous_avg),
            previous_avg_uptime_pct=previous_avg,
            current_avg_uptime_pct=current_avg,
            has_data=True,
        )

    def xǁSlaReportServiceǁgenerate__mutmut_49(
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
            overall_breached_count=sum(2 for service in services if not service.met),
            trend=classify_trend(current_avg, previous_avg),
            previous_avg_uptime_pct=previous_avg,
            current_avg_uptime_pct=current_avg,
            has_data=True,
        )

    def xǁSlaReportServiceǁgenerate__mutmut_50(
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
            overall_breached_count=sum(1 for service in services if service.met),
            trend=classify_trend(current_avg, previous_avg),
            previous_avg_uptime_pct=previous_avg,
            current_avg_uptime_pct=current_avg,
            has_data=True,
        )

    def xǁSlaReportServiceǁgenerate__mutmut_51(
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
            trend=classify_trend(None, previous_avg),
            previous_avg_uptime_pct=previous_avg,
            current_avg_uptime_pct=current_avg,
            has_data=True,
        )

    def xǁSlaReportServiceǁgenerate__mutmut_52(
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
            trend=classify_trend(current_avg, None),
            previous_avg_uptime_pct=previous_avg,
            current_avg_uptime_pct=current_avg,
            has_data=True,
        )

    def xǁSlaReportServiceǁgenerate__mutmut_53(
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
            trend=classify_trend(previous_avg),
            previous_avg_uptime_pct=previous_avg,
            current_avg_uptime_pct=current_avg,
            has_data=True,
        )

    def xǁSlaReportServiceǁgenerate__mutmut_54(
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
            trend=classify_trend(current_avg, ),
            previous_avg_uptime_pct=previous_avg,
            current_avg_uptime_pct=current_avg,
            has_data=True,
        )

    def xǁSlaReportServiceǁgenerate__mutmut_55(
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
            has_data=False,
        )

mutants_xǁSlaReportServiceǁgenerate__mutmut['_mutmut_orig'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_orig # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_1'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_1 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_2'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_2 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_3'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_3 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_4'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_4 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_5'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_5 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_6'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_6 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_7'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_7 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_8'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_8 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_9'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_9 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_10'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_10 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_11'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_11 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_12'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_12 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_13'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_13 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_14'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_14 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_15'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_15 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_16'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_16 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_17'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_17 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_18'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_18 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_19'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_19 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_20'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_20 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_21'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_21 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_22'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_22 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_23'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_23 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_24'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_24 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_25'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_25 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_26'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_26 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_27'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_27 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_28'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_28 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_29'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_29 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_30'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_30 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_31'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_31 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_32'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_32 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_33'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_33 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_34'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_34 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_35'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_35 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_36'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_36 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_37'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_37 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_38'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_38 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_39'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_39 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_40'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_40 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_41'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_41 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_42'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_42 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_43'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_43 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_44'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_44 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_45'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_45 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_46'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_46 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_47'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_47 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_48'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_48 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_49'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_49 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_50'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_50 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_51'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_51 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_52'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_52 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_53'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_53 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_54'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_54 # type: ignore # mutmut generated
mutants_xǁSlaReportServiceǁgenerate__mutmut['xǁSlaReportServiceǁgenerate__mutmut_55'] = SlaReportService.xǁSlaReportServiceǁgenerate__mutmut_55 # type: ignore # mutmut generated
mutants_x__group_breaches__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__group_breaches__mutmut)
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


def x__group_breaches__mutmut_orig(breaches: list[SlaBreachRaw]) -> dict[str, list[SlaBreach]]:
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


def x__group_breaches__mutmut_1(breaches: list[SlaBreachRaw]) -> dict[str, list[SlaBreach]]:
    grouped: dict[str, list[SlaBreach]] = None
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


def x__group_breaches__mutmut_2(breaches: list[SlaBreachRaw]) -> dict[str, list[SlaBreach]]:
    grouped: dict[str, list[SlaBreach]] = {}
    for raw in breaches:
        if raw["XXplanned_maintenanceXX"]:
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


def x__group_breaches__mutmut_3(breaches: list[SlaBreachRaw]) -> dict[str, list[SlaBreach]]:
    grouped: dict[str, list[SlaBreach]] = {}
    for raw in breaches:
        if raw["PLANNED_MAINTENANCE"]:
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


def x__group_breaches__mutmut_4(breaches: list[SlaBreachRaw]) -> dict[str, list[SlaBreach]]:
    grouped: dict[str, list[SlaBreach]] = {}
    for raw in breaches:
        if raw["planned_maintenance"]:
            break
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


def x__group_breaches__mutmut_5(breaches: list[SlaBreachRaw]) -> dict[str, list[SlaBreach]]:
    grouped: dict[str, list[SlaBreach]] = {}
    for raw in breaches:
        if raw["planned_maintenance"]:
            continue
        grouped.setdefault(raw["service_name"], []).append(
            None
        )
    return grouped


def x__group_breaches__mutmut_6(breaches: list[SlaBreachRaw]) -> dict[str, list[SlaBreach]]:
    grouped: dict[str, list[SlaBreach]] = {}
    for raw in breaches:
        if raw["planned_maintenance"]:
            continue
        grouped.setdefault(None, []).append(
            SlaBreach(
                service_name=raw["service_name"],
                date=raw["date"],
                duration_minutes=raw["duration_minutes"],
                impacted_users=raw["impacted_users"],
                root_cause_ref=raw["root_cause_ref"],
            )
        )
    return grouped


def x__group_breaches__mutmut_7(breaches: list[SlaBreachRaw]) -> dict[str, list[SlaBreach]]:
    grouped: dict[str, list[SlaBreach]] = {}
    for raw in breaches:
        if raw["planned_maintenance"]:
            continue
        grouped.setdefault(raw["service_name"], None).append(
            SlaBreach(
                service_name=raw["service_name"],
                date=raw["date"],
                duration_minutes=raw["duration_minutes"],
                impacted_users=raw["impacted_users"],
                root_cause_ref=raw["root_cause_ref"],
            )
        )
    return grouped


def x__group_breaches__mutmut_8(breaches: list[SlaBreachRaw]) -> dict[str, list[SlaBreach]]:
    grouped: dict[str, list[SlaBreach]] = {}
    for raw in breaches:
        if raw["planned_maintenance"]:
            continue
        grouped.setdefault([]).append(
            SlaBreach(
                service_name=raw["service_name"],
                date=raw["date"],
                duration_minutes=raw["duration_minutes"],
                impacted_users=raw["impacted_users"],
                root_cause_ref=raw["root_cause_ref"],
            )
        )
    return grouped


def x__group_breaches__mutmut_9(breaches: list[SlaBreachRaw]) -> dict[str, list[SlaBreach]]:
    grouped: dict[str, list[SlaBreach]] = {}
    for raw in breaches:
        if raw["planned_maintenance"]:
            continue
        grouped.setdefault(raw["service_name"], ).append(
            SlaBreach(
                service_name=raw["service_name"],
                date=raw["date"],
                duration_minutes=raw["duration_minutes"],
                impacted_users=raw["impacted_users"],
                root_cause_ref=raw["root_cause_ref"],
            )
        )
    return grouped


def x__group_breaches__mutmut_10(breaches: list[SlaBreachRaw]) -> dict[str, list[SlaBreach]]:
    grouped: dict[str, list[SlaBreach]] = {}
    for raw in breaches:
        if raw["planned_maintenance"]:
            continue
        grouped.setdefault(raw["XXservice_nameXX"], []).append(
            SlaBreach(
                service_name=raw["service_name"],
                date=raw["date"],
                duration_minutes=raw["duration_minutes"],
                impacted_users=raw["impacted_users"],
                root_cause_ref=raw["root_cause_ref"],
            )
        )
    return grouped


def x__group_breaches__mutmut_11(breaches: list[SlaBreachRaw]) -> dict[str, list[SlaBreach]]:
    grouped: dict[str, list[SlaBreach]] = {}
    for raw in breaches:
        if raw["planned_maintenance"]:
            continue
        grouped.setdefault(raw["SERVICE_NAME"], []).append(
            SlaBreach(
                service_name=raw["service_name"],
                date=raw["date"],
                duration_minutes=raw["duration_minutes"],
                impacted_users=raw["impacted_users"],
                root_cause_ref=raw["root_cause_ref"],
            )
        )
    return grouped


def x__group_breaches__mutmut_12(breaches: list[SlaBreachRaw]) -> dict[str, list[SlaBreach]]:
    grouped: dict[str, list[SlaBreach]] = {}
    for raw in breaches:
        if raw["planned_maintenance"]:
            continue
        grouped.setdefault(raw["service_name"], []).append(
            SlaBreach(
                service_name=None,
                date=raw["date"],
                duration_minutes=raw["duration_minutes"],
                impacted_users=raw["impacted_users"],
                root_cause_ref=raw["root_cause_ref"],
            )
        )
    return grouped


def x__group_breaches__mutmut_13(breaches: list[SlaBreachRaw]) -> dict[str, list[SlaBreach]]:
    grouped: dict[str, list[SlaBreach]] = {}
    for raw in breaches:
        if raw["planned_maintenance"]:
            continue
        grouped.setdefault(raw["service_name"], []).append(
            SlaBreach(
                service_name=raw["service_name"],
                date=None,
                duration_minutes=raw["duration_minutes"],
                impacted_users=raw["impacted_users"],
                root_cause_ref=raw["root_cause_ref"],
            )
        )
    return grouped


def x__group_breaches__mutmut_14(breaches: list[SlaBreachRaw]) -> dict[str, list[SlaBreach]]:
    grouped: dict[str, list[SlaBreach]] = {}
    for raw in breaches:
        if raw["planned_maintenance"]:
            continue
        grouped.setdefault(raw["service_name"], []).append(
            SlaBreach(
                service_name=raw["service_name"],
                date=raw["date"],
                duration_minutes=None,
                impacted_users=raw["impacted_users"],
                root_cause_ref=raw["root_cause_ref"],
            )
        )
    return grouped


def x__group_breaches__mutmut_15(breaches: list[SlaBreachRaw]) -> dict[str, list[SlaBreach]]:
    grouped: dict[str, list[SlaBreach]] = {}
    for raw in breaches:
        if raw["planned_maintenance"]:
            continue
        grouped.setdefault(raw["service_name"], []).append(
            SlaBreach(
                service_name=raw["service_name"],
                date=raw["date"],
                duration_minutes=raw["duration_minutes"],
                impacted_users=None,
                root_cause_ref=raw["root_cause_ref"],
            )
        )
    return grouped


def x__group_breaches__mutmut_16(breaches: list[SlaBreachRaw]) -> dict[str, list[SlaBreach]]:
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
                root_cause_ref=None,
            )
        )
    return grouped


def x__group_breaches__mutmut_17(breaches: list[SlaBreachRaw]) -> dict[str, list[SlaBreach]]:
    grouped: dict[str, list[SlaBreach]] = {}
    for raw in breaches:
        if raw["planned_maintenance"]:
            continue
        grouped.setdefault(raw["service_name"], []).append(
            SlaBreach(
                date=raw["date"],
                duration_minutes=raw["duration_minutes"],
                impacted_users=raw["impacted_users"],
                root_cause_ref=raw["root_cause_ref"],
            )
        )
    return grouped


def x__group_breaches__mutmut_18(breaches: list[SlaBreachRaw]) -> dict[str, list[SlaBreach]]:
    grouped: dict[str, list[SlaBreach]] = {}
    for raw in breaches:
        if raw["planned_maintenance"]:
            continue
        grouped.setdefault(raw["service_name"], []).append(
            SlaBreach(
                service_name=raw["service_name"],
                duration_minutes=raw["duration_minutes"],
                impacted_users=raw["impacted_users"],
                root_cause_ref=raw["root_cause_ref"],
            )
        )
    return grouped


def x__group_breaches__mutmut_19(breaches: list[SlaBreachRaw]) -> dict[str, list[SlaBreach]]:
    grouped: dict[str, list[SlaBreach]] = {}
    for raw in breaches:
        if raw["planned_maintenance"]:
            continue
        grouped.setdefault(raw["service_name"], []).append(
            SlaBreach(
                service_name=raw["service_name"],
                date=raw["date"],
                impacted_users=raw["impacted_users"],
                root_cause_ref=raw["root_cause_ref"],
            )
        )
    return grouped


def x__group_breaches__mutmut_20(breaches: list[SlaBreachRaw]) -> dict[str, list[SlaBreach]]:
    grouped: dict[str, list[SlaBreach]] = {}
    for raw in breaches:
        if raw["planned_maintenance"]:
            continue
        grouped.setdefault(raw["service_name"], []).append(
            SlaBreach(
                service_name=raw["service_name"],
                date=raw["date"],
                duration_minutes=raw["duration_minutes"],
                root_cause_ref=raw["root_cause_ref"],
            )
        )
    return grouped


def x__group_breaches__mutmut_21(breaches: list[SlaBreachRaw]) -> dict[str, list[SlaBreach]]:
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
                )
        )
    return grouped


def x__group_breaches__mutmut_22(breaches: list[SlaBreachRaw]) -> dict[str, list[SlaBreach]]:
    grouped: dict[str, list[SlaBreach]] = {}
    for raw in breaches:
        if raw["planned_maintenance"]:
            continue
        grouped.setdefault(raw["service_name"], []).append(
            SlaBreach(
                service_name=raw["XXservice_nameXX"],
                date=raw["date"],
                duration_minutes=raw["duration_minutes"],
                impacted_users=raw["impacted_users"],
                root_cause_ref=raw["root_cause_ref"],
            )
        )
    return grouped


def x__group_breaches__mutmut_23(breaches: list[SlaBreachRaw]) -> dict[str, list[SlaBreach]]:
    grouped: dict[str, list[SlaBreach]] = {}
    for raw in breaches:
        if raw["planned_maintenance"]:
            continue
        grouped.setdefault(raw["service_name"], []).append(
            SlaBreach(
                service_name=raw["SERVICE_NAME"],
                date=raw["date"],
                duration_minutes=raw["duration_minutes"],
                impacted_users=raw["impacted_users"],
                root_cause_ref=raw["root_cause_ref"],
            )
        )
    return grouped


def x__group_breaches__mutmut_24(breaches: list[SlaBreachRaw]) -> dict[str, list[SlaBreach]]:
    grouped: dict[str, list[SlaBreach]] = {}
    for raw in breaches:
        if raw["planned_maintenance"]:
            continue
        grouped.setdefault(raw["service_name"], []).append(
            SlaBreach(
                service_name=raw["service_name"],
                date=raw["XXdateXX"],
                duration_minutes=raw["duration_minutes"],
                impacted_users=raw["impacted_users"],
                root_cause_ref=raw["root_cause_ref"],
            )
        )
    return grouped


def x__group_breaches__mutmut_25(breaches: list[SlaBreachRaw]) -> dict[str, list[SlaBreach]]:
    grouped: dict[str, list[SlaBreach]] = {}
    for raw in breaches:
        if raw["planned_maintenance"]:
            continue
        grouped.setdefault(raw["service_name"], []).append(
            SlaBreach(
                service_name=raw["service_name"],
                date=raw["DATE"],
                duration_minutes=raw["duration_minutes"],
                impacted_users=raw["impacted_users"],
                root_cause_ref=raw["root_cause_ref"],
            )
        )
    return grouped


def x__group_breaches__mutmut_26(breaches: list[SlaBreachRaw]) -> dict[str, list[SlaBreach]]:
    grouped: dict[str, list[SlaBreach]] = {}
    for raw in breaches:
        if raw["planned_maintenance"]:
            continue
        grouped.setdefault(raw["service_name"], []).append(
            SlaBreach(
                service_name=raw["service_name"],
                date=raw["date"],
                duration_minutes=raw["XXduration_minutesXX"],
                impacted_users=raw["impacted_users"],
                root_cause_ref=raw["root_cause_ref"],
            )
        )
    return grouped


def x__group_breaches__mutmut_27(breaches: list[SlaBreachRaw]) -> dict[str, list[SlaBreach]]:
    grouped: dict[str, list[SlaBreach]] = {}
    for raw in breaches:
        if raw["planned_maintenance"]:
            continue
        grouped.setdefault(raw["service_name"], []).append(
            SlaBreach(
                service_name=raw["service_name"],
                date=raw["date"],
                duration_minutes=raw["DURATION_MINUTES"],
                impacted_users=raw["impacted_users"],
                root_cause_ref=raw["root_cause_ref"],
            )
        )
    return grouped


def x__group_breaches__mutmut_28(breaches: list[SlaBreachRaw]) -> dict[str, list[SlaBreach]]:
    grouped: dict[str, list[SlaBreach]] = {}
    for raw in breaches:
        if raw["planned_maintenance"]:
            continue
        grouped.setdefault(raw["service_name"], []).append(
            SlaBreach(
                service_name=raw["service_name"],
                date=raw["date"],
                duration_minutes=raw["duration_minutes"],
                impacted_users=raw["XXimpacted_usersXX"],
                root_cause_ref=raw["root_cause_ref"],
            )
        )
    return grouped


def x__group_breaches__mutmut_29(breaches: list[SlaBreachRaw]) -> dict[str, list[SlaBreach]]:
    grouped: dict[str, list[SlaBreach]] = {}
    for raw in breaches:
        if raw["planned_maintenance"]:
            continue
        grouped.setdefault(raw["service_name"], []).append(
            SlaBreach(
                service_name=raw["service_name"],
                date=raw["date"],
                duration_minutes=raw["duration_minutes"],
                impacted_users=raw["IMPACTED_USERS"],
                root_cause_ref=raw["root_cause_ref"],
            )
        )
    return grouped


def x__group_breaches__mutmut_30(breaches: list[SlaBreachRaw]) -> dict[str, list[SlaBreach]]:
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
                root_cause_ref=raw["XXroot_cause_refXX"],
            )
        )
    return grouped


def x__group_breaches__mutmut_31(breaches: list[SlaBreachRaw]) -> dict[str, list[SlaBreach]]:
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
                root_cause_ref=raw["ROOT_CAUSE_REF"],
            )
        )
    return grouped

mutants_x__group_breaches__mutmut['_mutmut_orig'] = x__group_breaches__mutmut_orig # type: ignore # mutmut generated
mutants_x__group_breaches__mutmut['x__group_breaches__mutmut_1'] = x__group_breaches__mutmut_1 # type: ignore # mutmut generated
mutants_x__group_breaches__mutmut['x__group_breaches__mutmut_2'] = x__group_breaches__mutmut_2 # type: ignore # mutmut generated
mutants_x__group_breaches__mutmut['x__group_breaches__mutmut_3'] = x__group_breaches__mutmut_3 # type: ignore # mutmut generated
mutants_x__group_breaches__mutmut['x__group_breaches__mutmut_4'] = x__group_breaches__mutmut_4 # type: ignore # mutmut generated
mutants_x__group_breaches__mutmut['x__group_breaches__mutmut_5'] = x__group_breaches__mutmut_5 # type: ignore # mutmut generated
mutants_x__group_breaches__mutmut['x__group_breaches__mutmut_6'] = x__group_breaches__mutmut_6 # type: ignore # mutmut generated
mutants_x__group_breaches__mutmut['x__group_breaches__mutmut_7'] = x__group_breaches__mutmut_7 # type: ignore # mutmut generated
mutants_x__group_breaches__mutmut['x__group_breaches__mutmut_8'] = x__group_breaches__mutmut_8 # type: ignore # mutmut generated
mutants_x__group_breaches__mutmut['x__group_breaches__mutmut_9'] = x__group_breaches__mutmut_9 # type: ignore # mutmut generated
mutants_x__group_breaches__mutmut['x__group_breaches__mutmut_10'] = x__group_breaches__mutmut_10 # type: ignore # mutmut generated
mutants_x__group_breaches__mutmut['x__group_breaches__mutmut_11'] = x__group_breaches__mutmut_11 # type: ignore # mutmut generated
mutants_x__group_breaches__mutmut['x__group_breaches__mutmut_12'] = x__group_breaches__mutmut_12 # type: ignore # mutmut generated
mutants_x__group_breaches__mutmut['x__group_breaches__mutmut_13'] = x__group_breaches__mutmut_13 # type: ignore # mutmut generated
mutants_x__group_breaches__mutmut['x__group_breaches__mutmut_14'] = x__group_breaches__mutmut_14 # type: ignore # mutmut generated
mutants_x__group_breaches__mutmut['x__group_breaches__mutmut_15'] = x__group_breaches__mutmut_15 # type: ignore # mutmut generated
mutants_x__group_breaches__mutmut['x__group_breaches__mutmut_16'] = x__group_breaches__mutmut_16 # type: ignore # mutmut generated
mutants_x__group_breaches__mutmut['x__group_breaches__mutmut_17'] = x__group_breaches__mutmut_17 # type: ignore # mutmut generated
mutants_x__group_breaches__mutmut['x__group_breaches__mutmut_18'] = x__group_breaches__mutmut_18 # type: ignore # mutmut generated
mutants_x__group_breaches__mutmut['x__group_breaches__mutmut_19'] = x__group_breaches__mutmut_19 # type: ignore # mutmut generated
mutants_x__group_breaches__mutmut['x__group_breaches__mutmut_20'] = x__group_breaches__mutmut_20 # type: ignore # mutmut generated
mutants_x__group_breaches__mutmut['x__group_breaches__mutmut_21'] = x__group_breaches__mutmut_21 # type: ignore # mutmut generated
mutants_x__group_breaches__mutmut['x__group_breaches__mutmut_22'] = x__group_breaches__mutmut_22 # type: ignore # mutmut generated
mutants_x__group_breaches__mutmut['x__group_breaches__mutmut_23'] = x__group_breaches__mutmut_23 # type: ignore # mutmut generated
mutants_x__group_breaches__mutmut['x__group_breaches__mutmut_24'] = x__group_breaches__mutmut_24 # type: ignore # mutmut generated
mutants_x__group_breaches__mutmut['x__group_breaches__mutmut_25'] = x__group_breaches__mutmut_25 # type: ignore # mutmut generated
mutants_x__group_breaches__mutmut['x__group_breaches__mutmut_26'] = x__group_breaches__mutmut_26 # type: ignore # mutmut generated
mutants_x__group_breaches__mutmut['x__group_breaches__mutmut_27'] = x__group_breaches__mutmut_27 # type: ignore # mutmut generated
mutants_x__group_breaches__mutmut['x__group_breaches__mutmut_28'] = x__group_breaches__mutmut_28 # type: ignore # mutmut generated
mutants_x__group_breaches__mutmut['x__group_breaches__mutmut_29'] = x__group_breaches__mutmut_29 # type: ignore # mutmut generated
mutants_x__group_breaches__mutmut['x__group_breaches__mutmut_30'] = x__group_breaches__mutmut_30 # type: ignore # mutmut generated
mutants_x__group_breaches__mutmut['x__group_breaches__mutmut_31'] = x__group_breaches__mutmut_31 # type: ignore # mutmut generated
mutants_x__build_service_sla__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__build_service_sla__mutmut)
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


def x__build_service_sla__mutmut_orig(raw: ServiceSlaRaw, breaches: list[SlaBreach]) -> ServiceSla:
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


def x__build_service_sla__mutmut_1(raw: ServiceSlaRaw, breaches: list[SlaBreach]) -> ServiceSla:
    evaluation = None
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


def x__build_service_sla__mutmut_2(raw: ServiceSlaRaw, breaches: list[SlaBreach]) -> ServiceSla:
    evaluation = evaluate_service(None)
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


def x__build_service_sla__mutmut_3(raw: ServiceSlaRaw, breaches: list[SlaBreach]) -> ServiceSla:
    evaluation = evaluate_service(raw)
    return ServiceSla(
        service_name=None,
        sla_target_pct=raw["sla_target_pct"],
        actual_uptime_pct=evaluation.actual_uptime_pct,
        met=evaluation.met,
        exceeded=evaluation.exceeded,
        breaches=breaches,
        breach_count=len(breaches),
        prorated=evaluation.prorated,
        coverage_days=evaluation.coverage_days,
    )


def x__build_service_sla__mutmut_4(raw: ServiceSlaRaw, breaches: list[SlaBreach]) -> ServiceSla:
    evaluation = evaluate_service(raw)
    return ServiceSla(
        service_name=raw["service_name"],
        sla_target_pct=None,
        actual_uptime_pct=evaluation.actual_uptime_pct,
        met=evaluation.met,
        exceeded=evaluation.exceeded,
        breaches=breaches,
        breach_count=len(breaches),
        prorated=evaluation.prorated,
        coverage_days=evaluation.coverage_days,
    )


def x__build_service_sla__mutmut_5(raw: ServiceSlaRaw, breaches: list[SlaBreach]) -> ServiceSla:
    evaluation = evaluate_service(raw)
    return ServiceSla(
        service_name=raw["service_name"],
        sla_target_pct=raw["sla_target_pct"],
        actual_uptime_pct=None,
        met=evaluation.met,
        exceeded=evaluation.exceeded,
        breaches=breaches,
        breach_count=len(breaches),
        prorated=evaluation.prorated,
        coverage_days=evaluation.coverage_days,
    )


def x__build_service_sla__mutmut_6(raw: ServiceSlaRaw, breaches: list[SlaBreach]) -> ServiceSla:
    evaluation = evaluate_service(raw)
    return ServiceSla(
        service_name=raw["service_name"],
        sla_target_pct=raw["sla_target_pct"],
        actual_uptime_pct=evaluation.actual_uptime_pct,
        met=None,
        exceeded=evaluation.exceeded,
        breaches=breaches,
        breach_count=len(breaches),
        prorated=evaluation.prorated,
        coverage_days=evaluation.coverage_days,
    )


def x__build_service_sla__mutmut_7(raw: ServiceSlaRaw, breaches: list[SlaBreach]) -> ServiceSla:
    evaluation = evaluate_service(raw)
    return ServiceSla(
        service_name=raw["service_name"],
        sla_target_pct=raw["sla_target_pct"],
        actual_uptime_pct=evaluation.actual_uptime_pct,
        met=evaluation.met,
        exceeded=None,
        breaches=breaches,
        breach_count=len(breaches),
        prorated=evaluation.prorated,
        coverage_days=evaluation.coverage_days,
    )


def x__build_service_sla__mutmut_8(raw: ServiceSlaRaw, breaches: list[SlaBreach]) -> ServiceSla:
    evaluation = evaluate_service(raw)
    return ServiceSla(
        service_name=raw["service_name"],
        sla_target_pct=raw["sla_target_pct"],
        actual_uptime_pct=evaluation.actual_uptime_pct,
        met=evaluation.met,
        exceeded=evaluation.exceeded,
        breaches=None,
        breach_count=len(breaches),
        prorated=evaluation.prorated,
        coverage_days=evaluation.coverage_days,
    )


def x__build_service_sla__mutmut_9(raw: ServiceSlaRaw, breaches: list[SlaBreach]) -> ServiceSla:
    evaluation = evaluate_service(raw)
    return ServiceSla(
        service_name=raw["service_name"],
        sla_target_pct=raw["sla_target_pct"],
        actual_uptime_pct=evaluation.actual_uptime_pct,
        met=evaluation.met,
        exceeded=evaluation.exceeded,
        breaches=breaches,
        breach_count=None,
        prorated=evaluation.prorated,
        coverage_days=evaluation.coverage_days,
    )


def x__build_service_sla__mutmut_10(raw: ServiceSlaRaw, breaches: list[SlaBreach]) -> ServiceSla:
    evaluation = evaluate_service(raw)
    return ServiceSla(
        service_name=raw["service_name"],
        sla_target_pct=raw["sla_target_pct"],
        actual_uptime_pct=evaluation.actual_uptime_pct,
        met=evaluation.met,
        exceeded=evaluation.exceeded,
        breaches=breaches,
        breach_count=len(breaches),
        prorated=None,
        coverage_days=evaluation.coverage_days,
    )


def x__build_service_sla__mutmut_11(raw: ServiceSlaRaw, breaches: list[SlaBreach]) -> ServiceSla:
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
        coverage_days=None,
    )


def x__build_service_sla__mutmut_12(raw: ServiceSlaRaw, breaches: list[SlaBreach]) -> ServiceSla:
    evaluation = evaluate_service(raw)
    return ServiceSla(
        sla_target_pct=raw["sla_target_pct"],
        actual_uptime_pct=evaluation.actual_uptime_pct,
        met=evaluation.met,
        exceeded=evaluation.exceeded,
        breaches=breaches,
        breach_count=len(breaches),
        prorated=evaluation.prorated,
        coverage_days=evaluation.coverage_days,
    )


def x__build_service_sla__mutmut_13(raw: ServiceSlaRaw, breaches: list[SlaBreach]) -> ServiceSla:
    evaluation = evaluate_service(raw)
    return ServiceSla(
        service_name=raw["service_name"],
        actual_uptime_pct=evaluation.actual_uptime_pct,
        met=evaluation.met,
        exceeded=evaluation.exceeded,
        breaches=breaches,
        breach_count=len(breaches),
        prorated=evaluation.prorated,
        coverage_days=evaluation.coverage_days,
    )


def x__build_service_sla__mutmut_14(raw: ServiceSlaRaw, breaches: list[SlaBreach]) -> ServiceSla:
    evaluation = evaluate_service(raw)
    return ServiceSla(
        service_name=raw["service_name"],
        sla_target_pct=raw["sla_target_pct"],
        met=evaluation.met,
        exceeded=evaluation.exceeded,
        breaches=breaches,
        breach_count=len(breaches),
        prorated=evaluation.prorated,
        coverage_days=evaluation.coverage_days,
    )


def x__build_service_sla__mutmut_15(raw: ServiceSlaRaw, breaches: list[SlaBreach]) -> ServiceSla:
    evaluation = evaluate_service(raw)
    return ServiceSla(
        service_name=raw["service_name"],
        sla_target_pct=raw["sla_target_pct"],
        actual_uptime_pct=evaluation.actual_uptime_pct,
        exceeded=evaluation.exceeded,
        breaches=breaches,
        breach_count=len(breaches),
        prorated=evaluation.prorated,
        coverage_days=evaluation.coverage_days,
    )


def x__build_service_sla__mutmut_16(raw: ServiceSlaRaw, breaches: list[SlaBreach]) -> ServiceSla:
    evaluation = evaluate_service(raw)
    return ServiceSla(
        service_name=raw["service_name"],
        sla_target_pct=raw["sla_target_pct"],
        actual_uptime_pct=evaluation.actual_uptime_pct,
        met=evaluation.met,
        breaches=breaches,
        breach_count=len(breaches),
        prorated=evaluation.prorated,
        coverage_days=evaluation.coverage_days,
    )


def x__build_service_sla__mutmut_17(raw: ServiceSlaRaw, breaches: list[SlaBreach]) -> ServiceSla:
    evaluation = evaluate_service(raw)
    return ServiceSla(
        service_name=raw["service_name"],
        sla_target_pct=raw["sla_target_pct"],
        actual_uptime_pct=evaluation.actual_uptime_pct,
        met=evaluation.met,
        exceeded=evaluation.exceeded,
        breach_count=len(breaches),
        prorated=evaluation.prorated,
        coverage_days=evaluation.coverage_days,
    )


def x__build_service_sla__mutmut_18(raw: ServiceSlaRaw, breaches: list[SlaBreach]) -> ServiceSla:
    evaluation = evaluate_service(raw)
    return ServiceSla(
        service_name=raw["service_name"],
        sla_target_pct=raw["sla_target_pct"],
        actual_uptime_pct=evaluation.actual_uptime_pct,
        met=evaluation.met,
        exceeded=evaluation.exceeded,
        breaches=breaches,
        prorated=evaluation.prorated,
        coverage_days=evaluation.coverage_days,
    )


def x__build_service_sla__mutmut_19(raw: ServiceSlaRaw, breaches: list[SlaBreach]) -> ServiceSla:
    evaluation = evaluate_service(raw)
    return ServiceSla(
        service_name=raw["service_name"],
        sla_target_pct=raw["sla_target_pct"],
        actual_uptime_pct=evaluation.actual_uptime_pct,
        met=evaluation.met,
        exceeded=evaluation.exceeded,
        breaches=breaches,
        breach_count=len(breaches),
        coverage_days=evaluation.coverage_days,
    )


def x__build_service_sla__mutmut_20(raw: ServiceSlaRaw, breaches: list[SlaBreach]) -> ServiceSla:
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
        )


def x__build_service_sla__mutmut_21(raw: ServiceSlaRaw, breaches: list[SlaBreach]) -> ServiceSla:
    evaluation = evaluate_service(raw)
    return ServiceSla(
        service_name=raw["XXservice_nameXX"],
        sla_target_pct=raw["sla_target_pct"],
        actual_uptime_pct=evaluation.actual_uptime_pct,
        met=evaluation.met,
        exceeded=evaluation.exceeded,
        breaches=breaches,
        breach_count=len(breaches),
        prorated=evaluation.prorated,
        coverage_days=evaluation.coverage_days,
    )


def x__build_service_sla__mutmut_22(raw: ServiceSlaRaw, breaches: list[SlaBreach]) -> ServiceSla:
    evaluation = evaluate_service(raw)
    return ServiceSla(
        service_name=raw["SERVICE_NAME"],
        sla_target_pct=raw["sla_target_pct"],
        actual_uptime_pct=evaluation.actual_uptime_pct,
        met=evaluation.met,
        exceeded=evaluation.exceeded,
        breaches=breaches,
        breach_count=len(breaches),
        prorated=evaluation.prorated,
        coverage_days=evaluation.coverage_days,
    )


def x__build_service_sla__mutmut_23(raw: ServiceSlaRaw, breaches: list[SlaBreach]) -> ServiceSla:
    evaluation = evaluate_service(raw)
    return ServiceSla(
        service_name=raw["service_name"],
        sla_target_pct=raw["XXsla_target_pctXX"],
        actual_uptime_pct=evaluation.actual_uptime_pct,
        met=evaluation.met,
        exceeded=evaluation.exceeded,
        breaches=breaches,
        breach_count=len(breaches),
        prorated=evaluation.prorated,
        coverage_days=evaluation.coverage_days,
    )


def x__build_service_sla__mutmut_24(raw: ServiceSlaRaw, breaches: list[SlaBreach]) -> ServiceSla:
    evaluation = evaluate_service(raw)
    return ServiceSla(
        service_name=raw["service_name"],
        sla_target_pct=raw["SLA_TARGET_PCT"],
        actual_uptime_pct=evaluation.actual_uptime_pct,
        met=evaluation.met,
        exceeded=evaluation.exceeded,
        breaches=breaches,
        breach_count=len(breaches),
        prorated=evaluation.prorated,
        coverage_days=evaluation.coverage_days,
    )

mutants_x__build_service_sla__mutmut['_mutmut_orig'] = x__build_service_sla__mutmut_orig # type: ignore # mutmut generated
mutants_x__build_service_sla__mutmut['x__build_service_sla__mutmut_1'] = x__build_service_sla__mutmut_1 # type: ignore # mutmut generated
mutants_x__build_service_sla__mutmut['x__build_service_sla__mutmut_2'] = x__build_service_sla__mutmut_2 # type: ignore # mutmut generated
mutants_x__build_service_sla__mutmut['x__build_service_sla__mutmut_3'] = x__build_service_sla__mutmut_3 # type: ignore # mutmut generated
mutants_x__build_service_sla__mutmut['x__build_service_sla__mutmut_4'] = x__build_service_sla__mutmut_4 # type: ignore # mutmut generated
mutants_x__build_service_sla__mutmut['x__build_service_sla__mutmut_5'] = x__build_service_sla__mutmut_5 # type: ignore # mutmut generated
mutants_x__build_service_sla__mutmut['x__build_service_sla__mutmut_6'] = x__build_service_sla__mutmut_6 # type: ignore # mutmut generated
mutants_x__build_service_sla__mutmut['x__build_service_sla__mutmut_7'] = x__build_service_sla__mutmut_7 # type: ignore # mutmut generated
mutants_x__build_service_sla__mutmut['x__build_service_sla__mutmut_8'] = x__build_service_sla__mutmut_8 # type: ignore # mutmut generated
mutants_x__build_service_sla__mutmut['x__build_service_sla__mutmut_9'] = x__build_service_sla__mutmut_9 # type: ignore # mutmut generated
mutants_x__build_service_sla__mutmut['x__build_service_sla__mutmut_10'] = x__build_service_sla__mutmut_10 # type: ignore # mutmut generated
mutants_x__build_service_sla__mutmut['x__build_service_sla__mutmut_11'] = x__build_service_sla__mutmut_11 # type: ignore # mutmut generated
mutants_x__build_service_sla__mutmut['x__build_service_sla__mutmut_12'] = x__build_service_sla__mutmut_12 # type: ignore # mutmut generated
mutants_x__build_service_sla__mutmut['x__build_service_sla__mutmut_13'] = x__build_service_sla__mutmut_13 # type: ignore # mutmut generated
mutants_x__build_service_sla__mutmut['x__build_service_sla__mutmut_14'] = x__build_service_sla__mutmut_14 # type: ignore # mutmut generated
mutants_x__build_service_sla__mutmut['x__build_service_sla__mutmut_15'] = x__build_service_sla__mutmut_15 # type: ignore # mutmut generated
mutants_x__build_service_sla__mutmut['x__build_service_sla__mutmut_16'] = x__build_service_sla__mutmut_16 # type: ignore # mutmut generated
mutants_x__build_service_sla__mutmut['x__build_service_sla__mutmut_17'] = x__build_service_sla__mutmut_17 # type: ignore # mutmut generated
mutants_x__build_service_sla__mutmut['x__build_service_sla__mutmut_18'] = x__build_service_sla__mutmut_18 # type: ignore # mutmut generated
mutants_x__build_service_sla__mutmut['x__build_service_sla__mutmut_19'] = x__build_service_sla__mutmut_19 # type: ignore # mutmut generated
mutants_x__build_service_sla__mutmut['x__build_service_sla__mutmut_20'] = x__build_service_sla__mutmut_20 # type: ignore # mutmut generated
mutants_x__build_service_sla__mutmut['x__build_service_sla__mutmut_21'] = x__build_service_sla__mutmut_21 # type: ignore # mutmut generated
mutants_x__build_service_sla__mutmut['x__build_service_sla__mutmut_22'] = x__build_service_sla__mutmut_22 # type: ignore # mutmut generated
mutants_x__build_service_sla__mutmut['x__build_service_sla__mutmut_23'] = x__build_service_sla__mutmut_23 # type: ignore # mutmut generated
mutants_x__build_service_sla__mutmut['x__build_service_sla__mutmut_24'] = x__build_service_sla__mutmut_24 # type: ignore # mutmut generated
mutants_x__average_uptime__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__average_uptime__mutmut)
def _average_uptime(services: list[ServiceSla]) -> float:
    if not services:
        return 0.0
    return round(sum(service.actual_uptime_pct for service in services) / len(services), 3)


def x__average_uptime__mutmut_orig(services: list[ServiceSla]) -> float:
    if not services:
        return 0.0
    return round(sum(service.actual_uptime_pct for service in services) / len(services), 3)


def x__average_uptime__mutmut_1(services: list[ServiceSla]) -> float:
    if services:
        return 0.0
    return round(sum(service.actual_uptime_pct for service in services) / len(services), 3)


def x__average_uptime__mutmut_2(services: list[ServiceSla]) -> float:
    if not services:
        return 1.0
    return round(sum(service.actual_uptime_pct for service in services) / len(services), 3)


def x__average_uptime__mutmut_3(services: list[ServiceSla]) -> float:
    if not services:
        return 0.0
    return round(None, 3)


def x__average_uptime__mutmut_4(services: list[ServiceSla]) -> float:
    if not services:
        return 0.0
    return round(sum(service.actual_uptime_pct for service in services) / len(services), None)


def x__average_uptime__mutmut_5(services: list[ServiceSla]) -> float:
    if not services:
        return 0.0
    return round(3)


def x__average_uptime__mutmut_6(services: list[ServiceSla]) -> float:
    if not services:
        return 0.0
    return round(sum(service.actual_uptime_pct for service in services) / len(services), )


def x__average_uptime__mutmut_7(services: list[ServiceSla]) -> float:
    if not services:
        return 0.0
    return round(sum(service.actual_uptime_pct for service in services) * len(services), 3)


def x__average_uptime__mutmut_8(services: list[ServiceSla]) -> float:
    if not services:
        return 0.0
    return round(sum(None) / len(services), 3)


def x__average_uptime__mutmut_9(services: list[ServiceSla]) -> float:
    if not services:
        return 0.0
    return round(sum(service.actual_uptime_pct for service in services) / len(services), 4)

mutants_x__average_uptime__mutmut['_mutmut_orig'] = x__average_uptime__mutmut_orig # type: ignore # mutmut generated
mutants_x__average_uptime__mutmut['x__average_uptime__mutmut_1'] = x__average_uptime__mutmut_1 # type: ignore # mutmut generated
mutants_x__average_uptime__mutmut['x__average_uptime__mutmut_2'] = x__average_uptime__mutmut_2 # type: ignore # mutmut generated
mutants_x__average_uptime__mutmut['x__average_uptime__mutmut_3'] = x__average_uptime__mutmut_3 # type: ignore # mutmut generated
mutants_x__average_uptime__mutmut['x__average_uptime__mutmut_4'] = x__average_uptime__mutmut_4 # type: ignore # mutmut generated
mutants_x__average_uptime__mutmut['x__average_uptime__mutmut_5'] = x__average_uptime__mutmut_5 # type: ignore # mutmut generated
mutants_x__average_uptime__mutmut['x__average_uptime__mutmut_6'] = x__average_uptime__mutmut_6 # type: ignore # mutmut generated
mutants_x__average_uptime__mutmut['x__average_uptime__mutmut_7'] = x__average_uptime__mutmut_7 # type: ignore # mutmut generated
mutants_x__average_uptime__mutmut['x__average_uptime__mutmut_8'] = x__average_uptime__mutmut_8 # type: ignore # mutmut generated
mutants_x__average_uptime__mutmut['x__average_uptime__mutmut_9'] = x__average_uptime__mutmut_9 # type: ignore # mutmut generated
