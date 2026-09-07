from __future__ import annotations

from collections import defaultdict
from datetime import datetime
from typing import TypedDict

from hexawyn.domain.models.monthly_incident_report import (
    ImpactedService,
    MonthlyIncidentReport,
    SeverityBreakdown,
)


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


class IncidentAggregate(TypedDict):
    month: str
    total_count: int
    total_downtime_minutes: int
    per_severity: dict[str, dict[str, int]]
    most_impacted_services: list[ImpactedService]
mutants_xǁMonthlyIncidentReportEngineǁcompute__mutmut: MutantDict = {}  # type: ignore


class MonthlyIncidentReportEngine:
    @_mutmut_mutated(mutants_xǁMonthlyIncidentReportEngineǁcompute__mutmut)
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
    def xǁMonthlyIncidentReportEngineǁcompute__mutmut_orig(
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
    def xǁMonthlyIncidentReportEngineǁcompute__mutmut_1(
        self,
        incidents: list[dict[str, object]],
        previous_incidents: list[dict[str, object]] | None = None,
    ) -> MonthlyIncidentReport:
        prev_incidents = None
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
    def xǁMonthlyIncidentReportEngineǁcompute__mutmut_2(
        self,
        incidents: list[dict[str, object]],
        previous_incidents: list[dict[str, object]] | None = None,
    ) -> MonthlyIncidentReport:
        prev_incidents = previous_incidents and []
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
    def xǁMonthlyIncidentReportEngineǁcompute__mutmut_3(
        self,
        incidents: list[dict[str, object]],
        previous_incidents: list[dict[str, object]] | None = None,
    ) -> MonthlyIncidentReport:
        prev_incidents = previous_incidents or []
        curr_total, curr_downtime, curr_severity = None
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
    def xǁMonthlyIncidentReportEngineǁcompute__mutmut_4(
        self,
        incidents: list[dict[str, object]],
        previous_incidents: list[dict[str, object]] | None = None,
    ) -> MonthlyIncidentReport:
        prev_incidents = previous_incidents or []
        curr_total, curr_downtime, curr_severity = _process_incidents(None)
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
    def xǁMonthlyIncidentReportEngineǁcompute__mutmut_5(
        self,
        incidents: list[dict[str, object]],
        previous_incidents: list[dict[str, object]] | None = None,
    ) -> MonthlyIncidentReport:
        prev_incidents = previous_incidents or []
        curr_total, curr_downtime, curr_severity = _process_incidents(incidents)
        prev_total, prev_downtime, _ = None
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
    def xǁMonthlyIncidentReportEngineǁcompute__mutmut_6(
        self,
        incidents: list[dict[str, object]],
        previous_incidents: list[dict[str, object]] | None = None,
    ) -> MonthlyIncidentReport:
        prev_incidents = previous_incidents or []
        curr_total, curr_downtime, curr_severity = _process_incidents(incidents)
        prev_total, prev_downtime, _ = _process_incidents(None)
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
    def xǁMonthlyIncidentReportEngineǁcompute__mutmut_7(
        self,
        incidents: list[dict[str, object]],
        previous_incidents: list[dict[str, object]] | None = None,
    ) -> MonthlyIncidentReport:
        prev_incidents = previous_incidents or []
        curr_total, curr_downtime, curr_severity = _process_incidents(incidents)
        prev_total, prev_downtime, _ = _process_incidents(prev_incidents)
        decreasing = None

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
    def xǁMonthlyIncidentReportEngineǁcompute__mutmut_8(
        self,
        incidents: list[dict[str, object]],
        previous_incidents: list[dict[str, object]] | None = None,
    ) -> MonthlyIncidentReport:
        prev_incidents = previous_incidents or []
        curr_total, curr_downtime, curr_severity = _process_incidents(incidents)
        prev_total, prev_downtime, _ = _process_incidents(prev_incidents)
        decreasing = curr_total <= prev_total

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
    def xǁMonthlyIncidentReportEngineǁcompute__mutmut_9(
        self,
        incidents: list[dict[str, object]],
        previous_incidents: list[dict[str, object]] | None = None,
    ) -> MonthlyIncidentReport:
        prev_incidents = previous_incidents or []
        curr_total, curr_downtime, curr_severity = _process_incidents(incidents)
        prev_total, prev_downtime, _ = _process_incidents(prev_incidents)
        decreasing = curr_total < prev_total

        return MonthlyIncidentReport(
            total_count=None,
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
    def xǁMonthlyIncidentReportEngineǁcompute__mutmut_10(
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
            total_downtime_minutes=None,
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
    def xǁMonthlyIncidentReportEngineǁcompute__mutmut_11(
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
            per_severity=None,
            most_impacted_services=_rank_impacted_services(incidents),
            previous_month_total_count=prev_total,
            previous_month_downtime_minutes=prev_downtime,
            incidents_decreasing=decreasing,
        )
    def xǁMonthlyIncidentReportEngineǁcompute__mutmut_12(
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
            most_impacted_services=None,
            previous_month_total_count=prev_total,
            previous_month_downtime_minutes=prev_downtime,
            incidents_decreasing=decreasing,
        )
    def xǁMonthlyIncidentReportEngineǁcompute__mutmut_13(
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
            previous_month_total_count=None,
            previous_month_downtime_minutes=prev_downtime,
            incidents_decreasing=decreasing,
        )
    def xǁMonthlyIncidentReportEngineǁcompute__mutmut_14(
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
            previous_month_downtime_minutes=None,
            incidents_decreasing=decreasing,
        )
    def xǁMonthlyIncidentReportEngineǁcompute__mutmut_15(
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
            incidents_decreasing=None,
        )
    def xǁMonthlyIncidentReportEngineǁcompute__mutmut_16(
        self,
        incidents: list[dict[str, object]],
        previous_incidents: list[dict[str, object]] | None = None,
    ) -> MonthlyIncidentReport:
        prev_incidents = previous_incidents or []
        curr_total, curr_downtime, curr_severity = _process_incidents(incidents)
        prev_total, prev_downtime, _ = _process_incidents(prev_incidents)
        decreasing = curr_total < prev_total

        return MonthlyIncidentReport(
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
    def xǁMonthlyIncidentReportEngineǁcompute__mutmut_17(
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
    def xǁMonthlyIncidentReportEngineǁcompute__mutmut_18(
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
            most_impacted_services=_rank_impacted_services(incidents),
            previous_month_total_count=prev_total,
            previous_month_downtime_minutes=prev_downtime,
            incidents_decreasing=decreasing,
        )
    def xǁMonthlyIncidentReportEngineǁcompute__mutmut_19(
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
            previous_month_total_count=prev_total,
            previous_month_downtime_minutes=prev_downtime,
            incidents_decreasing=decreasing,
        )
    def xǁMonthlyIncidentReportEngineǁcompute__mutmut_20(
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
            previous_month_downtime_minutes=prev_downtime,
            incidents_decreasing=decreasing,
        )
    def xǁMonthlyIncidentReportEngineǁcompute__mutmut_21(
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
            incidents_decreasing=decreasing,
        )
    def xǁMonthlyIncidentReportEngineǁcompute__mutmut_22(
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
            )
    def xǁMonthlyIncidentReportEngineǁcompute__mutmut_23(
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
                    severity=None,
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
    def xǁMonthlyIncidentReportEngineǁcompute__mutmut_24(
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
                    count=None,
                    downtime_minutes=data["downtime"],
                )
                for sev, data in curr_severity.items()
            },
            most_impacted_services=_rank_impacted_services(incidents),
            previous_month_total_count=prev_total,
            previous_month_downtime_minutes=prev_downtime,
            incidents_decreasing=decreasing,
        )
    def xǁMonthlyIncidentReportEngineǁcompute__mutmut_25(
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
                    downtime_minutes=None,
                )
                for sev, data in curr_severity.items()
            },
            most_impacted_services=_rank_impacted_services(incidents),
            previous_month_total_count=prev_total,
            previous_month_downtime_minutes=prev_downtime,
            incidents_decreasing=decreasing,
        )
    def xǁMonthlyIncidentReportEngineǁcompute__mutmut_26(
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
    def xǁMonthlyIncidentReportEngineǁcompute__mutmut_27(
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
                    downtime_minutes=data["downtime"],
                )
                for sev, data in curr_severity.items()
            },
            most_impacted_services=_rank_impacted_services(incidents),
            previous_month_total_count=prev_total,
            previous_month_downtime_minutes=prev_downtime,
            incidents_decreasing=decreasing,
        )
    def xǁMonthlyIncidentReportEngineǁcompute__mutmut_28(
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
                    )
                for sev, data in curr_severity.items()
            },
            most_impacted_services=_rank_impacted_services(incidents),
            previous_month_total_count=prev_total,
            previous_month_downtime_minutes=prev_downtime,
            incidents_decreasing=decreasing,
        )
    def xǁMonthlyIncidentReportEngineǁcompute__mutmut_29(
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
                    count=data["XXcountXX"],
                    downtime_minutes=data["downtime"],
                )
                for sev, data in curr_severity.items()
            },
            most_impacted_services=_rank_impacted_services(incidents),
            previous_month_total_count=prev_total,
            previous_month_downtime_minutes=prev_downtime,
            incidents_decreasing=decreasing,
        )
    def xǁMonthlyIncidentReportEngineǁcompute__mutmut_30(
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
                    count=data["COUNT"],
                    downtime_minutes=data["downtime"],
                )
                for sev, data in curr_severity.items()
            },
            most_impacted_services=_rank_impacted_services(incidents),
            previous_month_total_count=prev_total,
            previous_month_downtime_minutes=prev_downtime,
            incidents_decreasing=decreasing,
        )
    def xǁMonthlyIncidentReportEngineǁcompute__mutmut_31(
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
                    downtime_minutes=data["XXdowntimeXX"],
                )
                for sev, data in curr_severity.items()
            },
            most_impacted_services=_rank_impacted_services(incidents),
            previous_month_total_count=prev_total,
            previous_month_downtime_minutes=prev_downtime,
            incidents_decreasing=decreasing,
        )
    def xǁMonthlyIncidentReportEngineǁcompute__mutmut_32(
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
                    downtime_minutes=data["DOWNTIME"],
                )
                for sev, data in curr_severity.items()
            },
            most_impacted_services=_rank_impacted_services(incidents),
            previous_month_total_count=prev_total,
            previous_month_downtime_minutes=prev_downtime,
            incidents_decreasing=decreasing,
        )
    def xǁMonthlyIncidentReportEngineǁcompute__mutmut_33(
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
            most_impacted_services=_rank_impacted_services(None),
            previous_month_total_count=prev_total,
            previous_month_downtime_minutes=prev_downtime,
            incidents_decreasing=decreasing,
        )

mutants_xǁMonthlyIncidentReportEngineǁcompute__mutmut['_mutmut_orig'] = MonthlyIncidentReportEngine.xǁMonthlyIncidentReportEngineǁcompute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁMonthlyIncidentReportEngineǁcompute__mutmut['xǁMonthlyIncidentReportEngineǁcompute__mutmut_1'] = MonthlyIncidentReportEngine.xǁMonthlyIncidentReportEngineǁcompute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁMonthlyIncidentReportEngineǁcompute__mutmut['xǁMonthlyIncidentReportEngineǁcompute__mutmut_2'] = MonthlyIncidentReportEngine.xǁMonthlyIncidentReportEngineǁcompute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁMonthlyIncidentReportEngineǁcompute__mutmut['xǁMonthlyIncidentReportEngineǁcompute__mutmut_3'] = MonthlyIncidentReportEngine.xǁMonthlyIncidentReportEngineǁcompute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁMonthlyIncidentReportEngineǁcompute__mutmut['xǁMonthlyIncidentReportEngineǁcompute__mutmut_4'] = MonthlyIncidentReportEngine.xǁMonthlyIncidentReportEngineǁcompute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁMonthlyIncidentReportEngineǁcompute__mutmut['xǁMonthlyIncidentReportEngineǁcompute__mutmut_5'] = MonthlyIncidentReportEngine.xǁMonthlyIncidentReportEngineǁcompute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁMonthlyIncidentReportEngineǁcompute__mutmut['xǁMonthlyIncidentReportEngineǁcompute__mutmut_6'] = MonthlyIncidentReportEngine.xǁMonthlyIncidentReportEngineǁcompute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁMonthlyIncidentReportEngineǁcompute__mutmut['xǁMonthlyIncidentReportEngineǁcompute__mutmut_7'] = MonthlyIncidentReportEngine.xǁMonthlyIncidentReportEngineǁcompute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁMonthlyIncidentReportEngineǁcompute__mutmut['xǁMonthlyIncidentReportEngineǁcompute__mutmut_8'] = MonthlyIncidentReportEngine.xǁMonthlyIncidentReportEngineǁcompute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁMonthlyIncidentReportEngineǁcompute__mutmut['xǁMonthlyIncidentReportEngineǁcompute__mutmut_9'] = MonthlyIncidentReportEngine.xǁMonthlyIncidentReportEngineǁcompute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁMonthlyIncidentReportEngineǁcompute__mutmut['xǁMonthlyIncidentReportEngineǁcompute__mutmut_10'] = MonthlyIncidentReportEngine.xǁMonthlyIncidentReportEngineǁcompute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁMonthlyIncidentReportEngineǁcompute__mutmut['xǁMonthlyIncidentReportEngineǁcompute__mutmut_11'] = MonthlyIncidentReportEngine.xǁMonthlyIncidentReportEngineǁcompute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁMonthlyIncidentReportEngineǁcompute__mutmut['xǁMonthlyIncidentReportEngineǁcompute__mutmut_12'] = MonthlyIncidentReportEngine.xǁMonthlyIncidentReportEngineǁcompute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁMonthlyIncidentReportEngineǁcompute__mutmut['xǁMonthlyIncidentReportEngineǁcompute__mutmut_13'] = MonthlyIncidentReportEngine.xǁMonthlyIncidentReportEngineǁcompute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁMonthlyIncidentReportEngineǁcompute__mutmut['xǁMonthlyIncidentReportEngineǁcompute__mutmut_14'] = MonthlyIncidentReportEngine.xǁMonthlyIncidentReportEngineǁcompute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁMonthlyIncidentReportEngineǁcompute__mutmut['xǁMonthlyIncidentReportEngineǁcompute__mutmut_15'] = MonthlyIncidentReportEngine.xǁMonthlyIncidentReportEngineǁcompute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁMonthlyIncidentReportEngineǁcompute__mutmut['xǁMonthlyIncidentReportEngineǁcompute__mutmut_16'] = MonthlyIncidentReportEngine.xǁMonthlyIncidentReportEngineǁcompute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁMonthlyIncidentReportEngineǁcompute__mutmut['xǁMonthlyIncidentReportEngineǁcompute__mutmut_17'] = MonthlyIncidentReportEngine.xǁMonthlyIncidentReportEngineǁcompute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁMonthlyIncidentReportEngineǁcompute__mutmut['xǁMonthlyIncidentReportEngineǁcompute__mutmut_18'] = MonthlyIncidentReportEngine.xǁMonthlyIncidentReportEngineǁcompute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁMonthlyIncidentReportEngineǁcompute__mutmut['xǁMonthlyIncidentReportEngineǁcompute__mutmut_19'] = MonthlyIncidentReportEngine.xǁMonthlyIncidentReportEngineǁcompute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁMonthlyIncidentReportEngineǁcompute__mutmut['xǁMonthlyIncidentReportEngineǁcompute__mutmut_20'] = MonthlyIncidentReportEngine.xǁMonthlyIncidentReportEngineǁcompute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁMonthlyIncidentReportEngineǁcompute__mutmut['xǁMonthlyIncidentReportEngineǁcompute__mutmut_21'] = MonthlyIncidentReportEngine.xǁMonthlyIncidentReportEngineǁcompute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁMonthlyIncidentReportEngineǁcompute__mutmut['xǁMonthlyIncidentReportEngineǁcompute__mutmut_22'] = MonthlyIncidentReportEngine.xǁMonthlyIncidentReportEngineǁcompute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁMonthlyIncidentReportEngineǁcompute__mutmut['xǁMonthlyIncidentReportEngineǁcompute__mutmut_23'] = MonthlyIncidentReportEngine.xǁMonthlyIncidentReportEngineǁcompute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁMonthlyIncidentReportEngineǁcompute__mutmut['xǁMonthlyIncidentReportEngineǁcompute__mutmut_24'] = MonthlyIncidentReportEngine.xǁMonthlyIncidentReportEngineǁcompute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁMonthlyIncidentReportEngineǁcompute__mutmut['xǁMonthlyIncidentReportEngineǁcompute__mutmut_25'] = MonthlyIncidentReportEngine.xǁMonthlyIncidentReportEngineǁcompute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁMonthlyIncidentReportEngineǁcompute__mutmut['xǁMonthlyIncidentReportEngineǁcompute__mutmut_26'] = MonthlyIncidentReportEngine.xǁMonthlyIncidentReportEngineǁcompute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁMonthlyIncidentReportEngineǁcompute__mutmut['xǁMonthlyIncidentReportEngineǁcompute__mutmut_27'] = MonthlyIncidentReportEngine.xǁMonthlyIncidentReportEngineǁcompute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁMonthlyIncidentReportEngineǁcompute__mutmut['xǁMonthlyIncidentReportEngineǁcompute__mutmut_28'] = MonthlyIncidentReportEngine.xǁMonthlyIncidentReportEngineǁcompute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁMonthlyIncidentReportEngineǁcompute__mutmut['xǁMonthlyIncidentReportEngineǁcompute__mutmut_29'] = MonthlyIncidentReportEngine.xǁMonthlyIncidentReportEngineǁcompute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁMonthlyIncidentReportEngineǁcompute__mutmut['xǁMonthlyIncidentReportEngineǁcompute__mutmut_30'] = MonthlyIncidentReportEngine.xǁMonthlyIncidentReportEngineǁcompute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁMonthlyIncidentReportEngineǁcompute__mutmut['xǁMonthlyIncidentReportEngineǁcompute__mutmut_31'] = MonthlyIncidentReportEngine.xǁMonthlyIncidentReportEngineǁcompute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁMonthlyIncidentReportEngineǁcompute__mutmut['xǁMonthlyIncidentReportEngineǁcompute__mutmut_32'] = MonthlyIncidentReportEngine.xǁMonthlyIncidentReportEngineǁcompute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁMonthlyIncidentReportEngineǁcompute__mutmut['xǁMonthlyIncidentReportEngineǁcompute__mutmut_33'] = MonthlyIncidentReportEngine.xǁMonthlyIncidentReportEngineǁcompute__mutmut_33 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__process_incidents__mutmut)
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

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_orig(
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

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_1(
    incidents: list[dict[str, object]],
) -> tuple[int, int, dict[str, dict[str, int]]]:
    total_count = None
    total_downtime = 0
    severity_map: dict[str, dict[str, int]] = {
        "P1": {"count": 0, "downtime": 0},
        "P2": {"count": 0, "downtime": 0},
        "P3": {"count": 0, "downtime": 0},
    }

    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_2(
    incidents: list[dict[str, object]],
) -> tuple[int, int, dict[str, dict[str, int]]]:
    total_count = 1
    total_downtime = 0
    severity_map: dict[str, dict[str, int]] = {
        "P1": {"count": 0, "downtime": 0},
        "P2": {"count": 0, "downtime": 0},
        "P3": {"count": 0, "downtime": 0},
    }

    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_3(
    incidents: list[dict[str, object]],
) -> tuple[int, int, dict[str, dict[str, int]]]:
    total_count = 0
    total_downtime = None
    severity_map: dict[str, dict[str, int]] = {
        "P1": {"count": 0, "downtime": 0},
        "P2": {"count": 0, "downtime": 0},
        "P3": {"count": 0, "downtime": 0},
    }

    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_4(
    incidents: list[dict[str, object]],
) -> tuple[int, int, dict[str, dict[str, int]]]:
    total_count = 0
    total_downtime = 1
    severity_map: dict[str, dict[str, int]] = {
        "P1": {"count": 0, "downtime": 0},
        "P2": {"count": 0, "downtime": 0},
        "P3": {"count": 0, "downtime": 0},
    }

    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_5(
    incidents: list[dict[str, object]],
) -> tuple[int, int, dict[str, dict[str, int]]]:
    total_count = 0
    total_downtime = 0
    severity_map: dict[str, dict[str, int]] = None

    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_6(
    incidents: list[dict[str, object]],
) -> tuple[int, int, dict[str, dict[str, int]]]:
    total_count = 0
    total_downtime = 0
    severity_map: dict[str, dict[str, int]] = {
        "XXP1XX": {"count": 0, "downtime": 0},
        "P2": {"count": 0, "downtime": 0},
        "P3": {"count": 0, "downtime": 0},
    }

    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_7(
    incidents: list[dict[str, object]],
) -> tuple[int, int, dict[str, dict[str, int]]]:
    total_count = 0
    total_downtime = 0
    severity_map: dict[str, dict[str, int]] = {
        "p1": {"count": 0, "downtime": 0},
        "P2": {"count": 0, "downtime": 0},
        "P3": {"count": 0, "downtime": 0},
    }

    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_8(
    incidents: list[dict[str, object]],
) -> tuple[int, int, dict[str, dict[str, int]]]:
    total_count = 0
    total_downtime = 0
    severity_map: dict[str, dict[str, int]] = {
        "P1": {"XXcountXX": 0, "downtime": 0},
        "P2": {"count": 0, "downtime": 0},
        "P3": {"count": 0, "downtime": 0},
    }

    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_9(
    incidents: list[dict[str, object]],
) -> tuple[int, int, dict[str, dict[str, int]]]:
    total_count = 0
    total_downtime = 0
    severity_map: dict[str, dict[str, int]] = {
        "P1": {"COUNT": 0, "downtime": 0},
        "P2": {"count": 0, "downtime": 0},
        "P3": {"count": 0, "downtime": 0},
    }

    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_10(
    incidents: list[dict[str, object]],
) -> tuple[int, int, dict[str, dict[str, int]]]:
    total_count = 0
    total_downtime = 0
    severity_map: dict[str, dict[str, int]] = {
        "P1": {"count": 1, "downtime": 0},
        "P2": {"count": 0, "downtime": 0},
        "P3": {"count": 0, "downtime": 0},
    }

    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_11(
    incidents: list[dict[str, object]],
) -> tuple[int, int, dict[str, dict[str, int]]]:
    total_count = 0
    total_downtime = 0
    severity_map: dict[str, dict[str, int]] = {
        "P1": {"count": 0, "XXdowntimeXX": 0},
        "P2": {"count": 0, "downtime": 0},
        "P3": {"count": 0, "downtime": 0},
    }

    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_12(
    incidents: list[dict[str, object]],
) -> tuple[int, int, dict[str, dict[str, int]]]:
    total_count = 0
    total_downtime = 0
    severity_map: dict[str, dict[str, int]] = {
        "P1": {"count": 0, "DOWNTIME": 0},
        "P2": {"count": 0, "downtime": 0},
        "P3": {"count": 0, "downtime": 0},
    }

    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_13(
    incidents: list[dict[str, object]],
) -> tuple[int, int, dict[str, dict[str, int]]]:
    total_count = 0
    total_downtime = 0
    severity_map: dict[str, dict[str, int]] = {
        "P1": {"count": 0, "downtime": 1},
        "P2": {"count": 0, "downtime": 0},
        "P3": {"count": 0, "downtime": 0},
    }

    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_14(
    incidents: list[dict[str, object]],
) -> tuple[int, int, dict[str, dict[str, int]]]:
    total_count = 0
    total_downtime = 0
    severity_map: dict[str, dict[str, int]] = {
        "P1": {"count": 0, "downtime": 0},
        "XXP2XX": {"count": 0, "downtime": 0},
        "P3": {"count": 0, "downtime": 0},
    }

    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_15(
    incidents: list[dict[str, object]],
) -> tuple[int, int, dict[str, dict[str, int]]]:
    total_count = 0
    total_downtime = 0
    severity_map: dict[str, dict[str, int]] = {
        "P1": {"count": 0, "downtime": 0},
        "p2": {"count": 0, "downtime": 0},
        "P3": {"count": 0, "downtime": 0},
    }

    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_16(
    incidents: list[dict[str, object]],
) -> tuple[int, int, dict[str, dict[str, int]]]:
    total_count = 0
    total_downtime = 0
    severity_map: dict[str, dict[str, int]] = {
        "P1": {"count": 0, "downtime": 0},
        "P2": {"XXcountXX": 0, "downtime": 0},
        "P3": {"count": 0, "downtime": 0},
    }

    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_17(
    incidents: list[dict[str, object]],
) -> tuple[int, int, dict[str, dict[str, int]]]:
    total_count = 0
    total_downtime = 0
    severity_map: dict[str, dict[str, int]] = {
        "P1": {"count": 0, "downtime": 0},
        "P2": {"COUNT": 0, "downtime": 0},
        "P3": {"count": 0, "downtime": 0},
    }

    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_18(
    incidents: list[dict[str, object]],
) -> tuple[int, int, dict[str, dict[str, int]]]:
    total_count = 0
    total_downtime = 0
    severity_map: dict[str, dict[str, int]] = {
        "P1": {"count": 0, "downtime": 0},
        "P2": {"count": 1, "downtime": 0},
        "P3": {"count": 0, "downtime": 0},
    }

    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_19(
    incidents: list[dict[str, object]],
) -> tuple[int, int, dict[str, dict[str, int]]]:
    total_count = 0
    total_downtime = 0
    severity_map: dict[str, dict[str, int]] = {
        "P1": {"count": 0, "downtime": 0},
        "P2": {"count": 0, "XXdowntimeXX": 0},
        "P3": {"count": 0, "downtime": 0},
    }

    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_20(
    incidents: list[dict[str, object]],
) -> tuple[int, int, dict[str, dict[str, int]]]:
    total_count = 0
    total_downtime = 0
    severity_map: dict[str, dict[str, int]] = {
        "P1": {"count": 0, "downtime": 0},
        "P2": {"count": 0, "DOWNTIME": 0},
        "P3": {"count": 0, "downtime": 0},
    }

    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_21(
    incidents: list[dict[str, object]],
) -> tuple[int, int, dict[str, dict[str, int]]]:
    total_count = 0
    total_downtime = 0
    severity_map: dict[str, dict[str, int]] = {
        "P1": {"count": 0, "downtime": 0},
        "P2": {"count": 0, "downtime": 1},
        "P3": {"count": 0, "downtime": 0},
    }

    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_22(
    incidents: list[dict[str, object]],
) -> tuple[int, int, dict[str, dict[str, int]]]:
    total_count = 0
    total_downtime = 0
    severity_map: dict[str, dict[str, int]] = {
        "P1": {"count": 0, "downtime": 0},
        "P2": {"count": 0, "downtime": 0},
        "XXP3XX": {"count": 0, "downtime": 0},
    }

    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_23(
    incidents: list[dict[str, object]],
) -> tuple[int, int, dict[str, dict[str, int]]]:
    total_count = 0
    total_downtime = 0
    severity_map: dict[str, dict[str, int]] = {
        "P1": {"count": 0, "downtime": 0},
        "P2": {"count": 0, "downtime": 0},
        "p3": {"count": 0, "downtime": 0},
    }

    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_24(
    incidents: list[dict[str, object]],
) -> tuple[int, int, dict[str, dict[str, int]]]:
    total_count = 0
    total_downtime = 0
    severity_map: dict[str, dict[str, int]] = {
        "P1": {"count": 0, "downtime": 0},
        "P2": {"count": 0, "downtime": 0},
        "P3": {"XXcountXX": 0, "downtime": 0},
    }

    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_25(
    incidents: list[dict[str, object]],
) -> tuple[int, int, dict[str, dict[str, int]]]:
    total_count = 0
    total_downtime = 0
    severity_map: dict[str, dict[str, int]] = {
        "P1": {"count": 0, "downtime": 0},
        "P2": {"count": 0, "downtime": 0},
        "P3": {"COUNT": 0, "downtime": 0},
    }

    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_26(
    incidents: list[dict[str, object]],
) -> tuple[int, int, dict[str, dict[str, int]]]:
    total_count = 0
    total_downtime = 0
    severity_map: dict[str, dict[str, int]] = {
        "P1": {"count": 0, "downtime": 0},
        "P2": {"count": 0, "downtime": 0},
        "P3": {"count": 1, "downtime": 0},
    }

    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_27(
    incidents: list[dict[str, object]],
) -> tuple[int, int, dict[str, dict[str, int]]]:
    total_count = 0
    total_downtime = 0
    severity_map: dict[str, dict[str, int]] = {
        "P1": {"count": 0, "downtime": 0},
        "P2": {"count": 0, "downtime": 0},
        "P3": {"count": 0, "XXdowntimeXX": 0},
    }

    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_28(
    incidents: list[dict[str, object]],
) -> tuple[int, int, dict[str, dict[str, int]]]:
    total_count = 0
    total_downtime = 0
    severity_map: dict[str, dict[str, int]] = {
        "P1": {"count": 0, "downtime": 0},
        "P2": {"count": 0, "downtime": 0},
        "P3": {"count": 0, "DOWNTIME": 0},
    }

    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_29(
    incidents: list[dict[str, object]],
) -> tuple[int, int, dict[str, dict[str, int]]]:
    total_count = 0
    total_downtime = 0
    severity_map: dict[str, dict[str, int]] = {
        "P1": {"count": 0, "downtime": 0},
        "P2": {"count": 0, "downtime": 0},
        "P3": {"count": 0, "downtime": 1},
    }

    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_30(
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
        if _as_bool(None):
            continue

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_31(
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
        if _as_bool(inc.get(None)):
            continue

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_32(
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
        if _as_bool(inc.get("XXis_planned_maintenanceXX")):
            continue

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_33(
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
        if _as_bool(inc.get("IS_PLANNED_MAINTENANCE")):
            continue

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_34(
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
            break

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_35(
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

        sev = None
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_36(
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

        sev = str(None)
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_37(
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

        sev = str(inc.get(None))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_38(
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

        sev = str(inc.get("XXseverityXX"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_39(
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

        sev = str(inc.get("SEVERITY"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_40(
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

        sev = str(inc.get("severity"))
        if sev in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_41(
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

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = None

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_42(
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

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "XXP3XX"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_43(
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

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "p3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_44(
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

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = None
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_45(
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

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(None)
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_46(
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

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get(None))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_47(
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

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("XXdowntime_minutesXX"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_48(
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

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("DOWNTIME_MINUTES"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_49(
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

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] = 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_50(
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

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] -= 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_51(
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

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["XXcountXX"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_52(
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

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["COUNT"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_53(
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

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 2
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_54(
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

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] = downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_55(
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

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] -= downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_56(
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

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["XXdowntimeXX"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_57(
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

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["DOWNTIME"] += downtime
        total_count += 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_58(
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

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count = 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_59(
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

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count -= 1
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_60(
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

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 2
        total_downtime += downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_61(
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

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime = downtime

    return total_count, total_downtime, severity_map


def x__process_incidents__mutmut_62(
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

        sev = str(inc.get("severity"))
        if sev not in severity_map:
            sev = "P3"

        downtime = _as_int(inc.get("downtime_minutes"))
        severity_map[sev]["count"] += 1
        severity_map[sev]["downtime"] += downtime
        total_count += 1
        total_downtime -= downtime

    return total_count, total_downtime, severity_map

mutants_x__process_incidents__mutmut['_mutmut_orig'] = x__process_incidents__mutmut_orig # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_1'] = x__process_incidents__mutmut_1 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_2'] = x__process_incidents__mutmut_2 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_3'] = x__process_incidents__mutmut_3 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_4'] = x__process_incidents__mutmut_4 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_5'] = x__process_incidents__mutmut_5 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_6'] = x__process_incidents__mutmut_6 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_7'] = x__process_incidents__mutmut_7 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_8'] = x__process_incidents__mutmut_8 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_9'] = x__process_incidents__mutmut_9 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_10'] = x__process_incidents__mutmut_10 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_11'] = x__process_incidents__mutmut_11 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_12'] = x__process_incidents__mutmut_12 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_13'] = x__process_incidents__mutmut_13 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_14'] = x__process_incidents__mutmut_14 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_15'] = x__process_incidents__mutmut_15 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_16'] = x__process_incidents__mutmut_16 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_17'] = x__process_incidents__mutmut_17 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_18'] = x__process_incidents__mutmut_18 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_19'] = x__process_incidents__mutmut_19 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_20'] = x__process_incidents__mutmut_20 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_21'] = x__process_incidents__mutmut_21 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_22'] = x__process_incidents__mutmut_22 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_23'] = x__process_incidents__mutmut_23 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_24'] = x__process_incidents__mutmut_24 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_25'] = x__process_incidents__mutmut_25 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_26'] = x__process_incidents__mutmut_26 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_27'] = x__process_incidents__mutmut_27 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_28'] = x__process_incidents__mutmut_28 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_29'] = x__process_incidents__mutmut_29 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_30'] = x__process_incidents__mutmut_30 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_31'] = x__process_incidents__mutmut_31 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_32'] = x__process_incidents__mutmut_32 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_33'] = x__process_incidents__mutmut_33 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_34'] = x__process_incidents__mutmut_34 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_35'] = x__process_incidents__mutmut_35 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_36'] = x__process_incidents__mutmut_36 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_37'] = x__process_incidents__mutmut_37 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_38'] = x__process_incidents__mutmut_38 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_39'] = x__process_incidents__mutmut_39 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_40'] = x__process_incidents__mutmut_40 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_41'] = x__process_incidents__mutmut_41 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_42'] = x__process_incidents__mutmut_42 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_43'] = x__process_incidents__mutmut_43 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_44'] = x__process_incidents__mutmut_44 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_45'] = x__process_incidents__mutmut_45 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_46'] = x__process_incidents__mutmut_46 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_47'] = x__process_incidents__mutmut_47 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_48'] = x__process_incidents__mutmut_48 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_49'] = x__process_incidents__mutmut_49 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_50'] = x__process_incidents__mutmut_50 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_51'] = x__process_incidents__mutmut_51 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_52'] = x__process_incidents__mutmut_52 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_53'] = x__process_incidents__mutmut_53 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_54'] = x__process_incidents__mutmut_54 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_55'] = x__process_incidents__mutmut_55 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_56'] = x__process_incidents__mutmut_56 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_57'] = x__process_incidents__mutmut_57 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_58'] = x__process_incidents__mutmut_58 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_59'] = x__process_incidents__mutmut_59 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_60'] = x__process_incidents__mutmut_60 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_61'] = x__process_incidents__mutmut_61 # type: ignore # mutmut generated
mutants_x__process_incidents__mutmut['x__process_incidents__mutmut_62'] = x__process_incidents__mutmut_62 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__rank_impacted_services__mutmut)
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


def x__rank_impacted_services__mutmut_orig(
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


def x__rank_impacted_services__mutmut_1(
    incidents: list[dict[str, object]],
) -> list[ImpactedService]:
    svc_map: dict[str, dict[str, int]] = None
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


def x__rank_impacted_services__mutmut_2(
    incidents: list[dict[str, object]],
) -> list[ImpactedService]:
    svc_map: dict[str, dict[str, int]] = {}
    for inc in incidents:
        if _as_bool(None):
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


def x__rank_impacted_services__mutmut_3(
    incidents: list[dict[str, object]],
) -> list[ImpactedService]:
    svc_map: dict[str, dict[str, int]] = {}
    for inc in incidents:
        if _as_bool(inc.get(None)):
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


def x__rank_impacted_services__mutmut_4(
    incidents: list[dict[str, object]],
) -> list[ImpactedService]:
    svc_map: dict[str, dict[str, int]] = {}
    for inc in incidents:
        if _as_bool(inc.get("XXis_planned_maintenanceXX")):
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


def x__rank_impacted_services__mutmut_5(
    incidents: list[dict[str, object]],
) -> list[ImpactedService]:
    svc_map: dict[str, dict[str, int]] = {}
    for inc in incidents:
        if _as_bool(inc.get("IS_PLANNED_MAINTENANCE")):
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


def x__rank_impacted_services__mutmut_6(
    incidents: list[dict[str, object]],
) -> list[ImpactedService]:
    svc_map: dict[str, dict[str, int]] = {}
    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            break
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


def x__rank_impacted_services__mutmut_7(
    incidents: list[dict[str, object]],
) -> list[ImpactedService]:
    svc_map: dict[str, dict[str, int]] = {}
    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue
        svc = None
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


def x__rank_impacted_services__mutmut_8(
    incidents: list[dict[str, object]],
) -> list[ImpactedService]:
    svc_map: dict[str, dict[str, int]] = {}
    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue
        svc = str(None)
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


def x__rank_impacted_services__mutmut_9(
    incidents: list[dict[str, object]],
) -> list[ImpactedService]:
    svc_map: dict[str, dict[str, int]] = {}
    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue
        svc = str(inc.get(None, ""))
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


def x__rank_impacted_services__mutmut_10(
    incidents: list[dict[str, object]],
) -> list[ImpactedService]:
    svc_map: dict[str, dict[str, int]] = {}
    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue
        svc = str(inc.get("service_name", None))
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


def x__rank_impacted_services__mutmut_11(
    incidents: list[dict[str, object]],
) -> list[ImpactedService]:
    svc_map: dict[str, dict[str, int]] = {}
    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue
        svc = str(inc.get(""))
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


def x__rank_impacted_services__mutmut_12(
    incidents: list[dict[str, object]],
) -> list[ImpactedService]:
    svc_map: dict[str, dict[str, int]] = {}
    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue
        svc = str(inc.get("service_name", ))
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


def x__rank_impacted_services__mutmut_13(
    incidents: list[dict[str, object]],
) -> list[ImpactedService]:
    svc_map: dict[str, dict[str, int]] = {}
    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue
        svc = str(inc.get("XXservice_nameXX", ""))
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


def x__rank_impacted_services__mutmut_14(
    incidents: list[dict[str, object]],
) -> list[ImpactedService]:
    svc_map: dict[str, dict[str, int]] = {}
    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue
        svc = str(inc.get("SERVICE_NAME", ""))
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


def x__rank_impacted_services__mutmut_15(
    incidents: list[dict[str, object]],
) -> list[ImpactedService]:
    svc_map: dict[str, dict[str, int]] = {}
    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue
        svc = str(inc.get("service_name", "XXXX"))
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


def x__rank_impacted_services__mutmut_16(
    incidents: list[dict[str, object]],
) -> list[ImpactedService]:
    svc_map: dict[str, dict[str, int]] = {}
    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue
        svc = str(inc.get("service_name", ""))
        downtime = None
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


def x__rank_impacted_services__mutmut_17(
    incidents: list[dict[str, object]],
) -> list[ImpactedService]:
    svc_map: dict[str, dict[str, int]] = {}
    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue
        svc = str(inc.get("service_name", ""))
        downtime = _as_int(None)
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


def x__rank_impacted_services__mutmut_18(
    incidents: list[dict[str, object]],
) -> list[ImpactedService]:
    svc_map: dict[str, dict[str, int]] = {}
    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue
        svc = str(inc.get("service_name", ""))
        downtime = _as_int(inc.get(None))
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


def x__rank_impacted_services__mutmut_19(
    incidents: list[dict[str, object]],
) -> list[ImpactedService]:
    svc_map: dict[str, dict[str, int]] = {}
    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue
        svc = str(inc.get("service_name", ""))
        downtime = _as_int(inc.get("XXdowntime_minutesXX"))
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


def x__rank_impacted_services__mutmut_20(
    incidents: list[dict[str, object]],
) -> list[ImpactedService]:
    svc_map: dict[str, dict[str, int]] = {}
    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue
        svc = str(inc.get("service_name", ""))
        downtime = _as_int(inc.get("DOWNTIME_MINUTES"))
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


def x__rank_impacted_services__mutmut_21(
    incidents: list[dict[str, object]],
) -> list[ImpactedService]:
    svc_map: dict[str, dict[str, int]] = {}
    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue
        svc = str(inc.get("service_name", ""))
        downtime = _as_int(inc.get("downtime_minutes"))
        if svc in svc_map:
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


def x__rank_impacted_services__mutmut_22(
    incidents: list[dict[str, object]],
) -> list[ImpactedService]:
    svc_map: dict[str, dict[str, int]] = {}
    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue
        svc = str(inc.get("service_name", ""))
        downtime = _as_int(inc.get("downtime_minutes"))
        if svc not in svc_map:
            svc_map[svc] = None
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


def x__rank_impacted_services__mutmut_23(
    incidents: list[dict[str, object]],
) -> list[ImpactedService]:
    svc_map: dict[str, dict[str, int]] = {}
    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue
        svc = str(inc.get("service_name", ""))
        downtime = _as_int(inc.get("downtime_minutes"))
        if svc not in svc_map:
            svc_map[svc] = {"XXtotal_downtimeXX": 0, "incident_count": 0}
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


def x__rank_impacted_services__mutmut_24(
    incidents: list[dict[str, object]],
) -> list[ImpactedService]:
    svc_map: dict[str, dict[str, int]] = {}
    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue
        svc = str(inc.get("service_name", ""))
        downtime = _as_int(inc.get("downtime_minutes"))
        if svc not in svc_map:
            svc_map[svc] = {"TOTAL_DOWNTIME": 0, "incident_count": 0}
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


def x__rank_impacted_services__mutmut_25(
    incidents: list[dict[str, object]],
) -> list[ImpactedService]:
    svc_map: dict[str, dict[str, int]] = {}
    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue
        svc = str(inc.get("service_name", ""))
        downtime = _as_int(inc.get("downtime_minutes"))
        if svc not in svc_map:
            svc_map[svc] = {"total_downtime": 1, "incident_count": 0}
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


def x__rank_impacted_services__mutmut_26(
    incidents: list[dict[str, object]],
) -> list[ImpactedService]:
    svc_map: dict[str, dict[str, int]] = {}
    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue
        svc = str(inc.get("service_name", ""))
        downtime = _as_int(inc.get("downtime_minutes"))
        if svc not in svc_map:
            svc_map[svc] = {"total_downtime": 0, "XXincident_countXX": 0}
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


def x__rank_impacted_services__mutmut_27(
    incidents: list[dict[str, object]],
) -> list[ImpactedService]:
    svc_map: dict[str, dict[str, int]] = {}
    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue
        svc = str(inc.get("service_name", ""))
        downtime = _as_int(inc.get("downtime_minutes"))
        if svc not in svc_map:
            svc_map[svc] = {"total_downtime": 0, "INCIDENT_COUNT": 0}
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


def x__rank_impacted_services__mutmut_28(
    incidents: list[dict[str, object]],
) -> list[ImpactedService]:
    svc_map: dict[str, dict[str, int]] = {}
    for inc in incidents:
        if _as_bool(inc.get("is_planned_maintenance")):
            continue
        svc = str(inc.get("service_name", ""))
        downtime = _as_int(inc.get("downtime_minutes"))
        if svc not in svc_map:
            svc_map[svc] = {"total_downtime": 0, "incident_count": 1}
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


def x__rank_impacted_services__mutmut_29(
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
        svc_map[svc]["total_downtime"] = downtime
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


def x__rank_impacted_services__mutmut_30(
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
        svc_map[svc]["total_downtime"] -= downtime
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


def x__rank_impacted_services__mutmut_31(
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
        svc_map[svc]["XXtotal_downtimeXX"] += downtime
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


def x__rank_impacted_services__mutmut_32(
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
        svc_map[svc]["TOTAL_DOWNTIME"] += downtime
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


def x__rank_impacted_services__mutmut_33(
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
        svc_map[svc]["incident_count"] = 1

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


def x__rank_impacted_services__mutmut_34(
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
        svc_map[svc]["incident_count"] -= 1

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


def x__rank_impacted_services__mutmut_35(
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
        svc_map[svc]["XXincident_countXX"] += 1

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


def x__rank_impacted_services__mutmut_36(
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
        svc_map[svc]["INCIDENT_COUNT"] += 1

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


def x__rank_impacted_services__mutmut_37(
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
        svc_map[svc]["incident_count"] += 2

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


def x__rank_impacted_services__mutmut_38(
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

    result = None
    result.sort(key=lambda s: s.total_downtime, reverse=True)
    return result


def x__rank_impacted_services__mutmut_39(
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
            service_name=None,
            total_downtime=data["total_downtime"],
            incident_count=data["incident_count"],
        )
        for svc, data in svc_map.items()
    ]
    result.sort(key=lambda s: s.total_downtime, reverse=True)
    return result


def x__rank_impacted_services__mutmut_40(
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
            total_downtime=None,
            incident_count=data["incident_count"],
        )
        for svc, data in svc_map.items()
    ]
    result.sort(key=lambda s: s.total_downtime, reverse=True)
    return result


def x__rank_impacted_services__mutmut_41(
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
            incident_count=None,
        )
        for svc, data in svc_map.items()
    ]
    result.sort(key=lambda s: s.total_downtime, reverse=True)
    return result


def x__rank_impacted_services__mutmut_42(
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
            total_downtime=data["total_downtime"],
            incident_count=data["incident_count"],
        )
        for svc, data in svc_map.items()
    ]
    result.sort(key=lambda s: s.total_downtime, reverse=True)
    return result


def x__rank_impacted_services__mutmut_43(
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
            incident_count=data["incident_count"],
        )
        for svc, data in svc_map.items()
    ]
    result.sort(key=lambda s: s.total_downtime, reverse=True)
    return result


def x__rank_impacted_services__mutmut_44(
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
            )
        for svc, data in svc_map.items()
    ]
    result.sort(key=lambda s: s.total_downtime, reverse=True)
    return result


def x__rank_impacted_services__mutmut_45(
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
            total_downtime=data["XXtotal_downtimeXX"],
            incident_count=data["incident_count"],
        )
        for svc, data in svc_map.items()
    ]
    result.sort(key=lambda s: s.total_downtime, reverse=True)
    return result


def x__rank_impacted_services__mutmut_46(
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
            total_downtime=data["TOTAL_DOWNTIME"],
            incident_count=data["incident_count"],
        )
        for svc, data in svc_map.items()
    ]
    result.sort(key=lambda s: s.total_downtime, reverse=True)
    return result


def x__rank_impacted_services__mutmut_47(
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
            incident_count=data["XXincident_countXX"],
        )
        for svc, data in svc_map.items()
    ]
    result.sort(key=lambda s: s.total_downtime, reverse=True)
    return result


def x__rank_impacted_services__mutmut_48(
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
            incident_count=data["INCIDENT_COUNT"],
        )
        for svc, data in svc_map.items()
    ]
    result.sort(key=lambda s: s.total_downtime, reverse=True)
    return result


def x__rank_impacted_services__mutmut_49(
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
    result.sort(key=None, reverse=True)
    return result


def x__rank_impacted_services__mutmut_50(
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
    result.sort(key=lambda s: s.total_downtime, reverse=None)
    return result


def x__rank_impacted_services__mutmut_51(
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
    result.sort(reverse=True)
    return result


def x__rank_impacted_services__mutmut_52(
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
    result.sort(key=lambda s: s.total_downtime, )
    return result


def x__rank_impacted_services__mutmut_53(
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
    result.sort(key=lambda s: None, reverse=True)
    return result


def x__rank_impacted_services__mutmut_54(
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
    result.sort(key=lambda s: s.total_downtime, reverse=False)
    return result

mutants_x__rank_impacted_services__mutmut['_mutmut_orig'] = x__rank_impacted_services__mutmut_orig # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_1'] = x__rank_impacted_services__mutmut_1 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_2'] = x__rank_impacted_services__mutmut_2 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_3'] = x__rank_impacted_services__mutmut_3 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_4'] = x__rank_impacted_services__mutmut_4 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_5'] = x__rank_impacted_services__mutmut_5 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_6'] = x__rank_impacted_services__mutmut_6 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_7'] = x__rank_impacted_services__mutmut_7 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_8'] = x__rank_impacted_services__mutmut_8 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_9'] = x__rank_impacted_services__mutmut_9 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_10'] = x__rank_impacted_services__mutmut_10 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_11'] = x__rank_impacted_services__mutmut_11 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_12'] = x__rank_impacted_services__mutmut_12 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_13'] = x__rank_impacted_services__mutmut_13 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_14'] = x__rank_impacted_services__mutmut_14 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_15'] = x__rank_impacted_services__mutmut_15 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_16'] = x__rank_impacted_services__mutmut_16 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_17'] = x__rank_impacted_services__mutmut_17 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_18'] = x__rank_impacted_services__mutmut_18 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_19'] = x__rank_impacted_services__mutmut_19 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_20'] = x__rank_impacted_services__mutmut_20 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_21'] = x__rank_impacted_services__mutmut_21 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_22'] = x__rank_impacted_services__mutmut_22 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_23'] = x__rank_impacted_services__mutmut_23 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_24'] = x__rank_impacted_services__mutmut_24 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_25'] = x__rank_impacted_services__mutmut_25 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_26'] = x__rank_impacted_services__mutmut_26 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_27'] = x__rank_impacted_services__mutmut_27 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_28'] = x__rank_impacted_services__mutmut_28 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_29'] = x__rank_impacted_services__mutmut_29 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_30'] = x__rank_impacted_services__mutmut_30 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_31'] = x__rank_impacted_services__mutmut_31 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_32'] = x__rank_impacted_services__mutmut_32 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_33'] = x__rank_impacted_services__mutmut_33 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_34'] = x__rank_impacted_services__mutmut_34 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_35'] = x__rank_impacted_services__mutmut_35 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_36'] = x__rank_impacted_services__mutmut_36 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_37'] = x__rank_impacted_services__mutmut_37 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_38'] = x__rank_impacted_services__mutmut_38 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_39'] = x__rank_impacted_services__mutmut_39 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_40'] = x__rank_impacted_services__mutmut_40 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_41'] = x__rank_impacted_services__mutmut_41 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_42'] = x__rank_impacted_services__mutmut_42 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_43'] = x__rank_impacted_services__mutmut_43 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_44'] = x__rank_impacted_services__mutmut_44 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_45'] = x__rank_impacted_services__mutmut_45 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_46'] = x__rank_impacted_services__mutmut_46 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_47'] = x__rank_impacted_services__mutmut_47 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_48'] = x__rank_impacted_services__mutmut_48 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_49'] = x__rank_impacted_services__mutmut_49 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_50'] = x__rank_impacted_services__mutmut_50 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_51'] = x__rank_impacted_services__mutmut_51 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_52'] = x__rank_impacted_services__mutmut_52 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_53'] = x__rank_impacted_services__mutmut_53 # type: ignore # mutmut generated
mutants_x__rank_impacted_services__mutmut['x__rank_impacted_services__mutmut_54'] = x__rank_impacted_services__mutmut_54 # type: ignore # mutmut generated
mutants_x__as_int__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__as_int__mutmut)
def _as_int(value: object) -> int:
    if value is None:
        return 0
    try:
        return int(float(value))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0


def x__as_int__mutmut_orig(value: object) -> int:
    if value is None:
        return 0
    try:
        return int(float(value))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0


def x__as_int__mutmut_1(value: object) -> int:
    if value is not None:
        return 0
    try:
        return int(float(value))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0


def x__as_int__mutmut_2(value: object) -> int:
    if value is None:
        return 1
    try:
        return int(float(value))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0


def x__as_int__mutmut_3(value: object) -> int:
    if value is None:
        return 0
    try:
        return int(None)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0


def x__as_int__mutmut_4(value: object) -> int:
    if value is None:
        return 0
    try:
        return int(float(None))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 0


def x__as_int__mutmut_5(value: object) -> int:
    if value is None:
        return 0
    try:
        return int(float(value))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return 1

mutants_x__as_int__mutmut['_mutmut_orig'] = x__as_int__mutmut_orig # type: ignore # mutmut generated
mutants_x__as_int__mutmut['x__as_int__mutmut_1'] = x__as_int__mutmut_1 # type: ignore # mutmut generated
mutants_x__as_int__mutmut['x__as_int__mutmut_2'] = x__as_int__mutmut_2 # type: ignore # mutmut generated
mutants_x__as_int__mutmut['x__as_int__mutmut_3'] = x__as_int__mutmut_3 # type: ignore # mutmut generated
mutants_x__as_int__mutmut['x__as_int__mutmut_4'] = x__as_int__mutmut_4 # type: ignore # mutmut generated
mutants_x__as_int__mutmut['x__as_int__mutmut_5'] = x__as_int__mutmut_5 # type: ignore # mutmut generated
mutants_x__as_bool__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__as_bool__mutmut)
def _as_bool(value: object) -> bool:
    if value is None:
        return False
    if isinstance(value, bool):
        return value
    return bool(value)


def x__as_bool__mutmut_orig(value: object) -> bool:
    if value is None:
        return False
    if isinstance(value, bool):
        return value
    return bool(value)


def x__as_bool__mutmut_1(value: object) -> bool:
    if value is not None:
        return False
    if isinstance(value, bool):
        return value
    return bool(value)


def x__as_bool__mutmut_2(value: object) -> bool:
    if value is None:
        return True
    if isinstance(value, bool):
        return value
    return bool(value)


def x__as_bool__mutmut_3(value: object) -> bool:
    if value is None:
        return False
    if isinstance(value, bool):
        return value
    return bool(None)

mutants_x__as_bool__mutmut['_mutmut_orig'] = x__as_bool__mutmut_orig # type: ignore # mutmut generated
mutants_x__as_bool__mutmut['x__as_bool__mutmut_1'] = x__as_bool__mutmut_1 # type: ignore # mutmut generated
mutants_x__as_bool__mutmut['x__as_bool__mutmut_2'] = x__as_bool__mutmut_2 # type: ignore # mutmut generated
mutants_x__as_bool__mutmut['x__as_bool__mutmut_3'] = x__as_bool__mutmut_3 # type: ignore # mutmut generated


SEVERITY_ORDER = ["P1", "P2", "P3"]
mutants_x_default_month_str__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_default_month_str__mutmut)
def default_month_str() -> str:
    now = datetime.now()
    return f"{now.year}-{now.month:02d}"


def x_default_month_str__mutmut_orig() -> str:
    now = datetime.now()
    return f"{now.year}-{now.month:02d}"


def x_default_month_str__mutmut_1() -> str:
    now = None
    return f"{now.year}-{now.month:02d}"

mutants_x_default_month_str__mutmut['_mutmut_orig'] = x_default_month_str__mutmut_orig # type: ignore # mutmut generated
mutants_x_default_month_str__mutmut['x_default_month_str__mutmut_1'] = x_default_month_str__mutmut_1 # type: ignore # mutmut generated
mutants_x_previous_month_name__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_previous_month_name__mutmut)
def previous_month_name(month: str) -> str:
    year, mo = month.split("-")
    y = int(year)
    m = int(mo)
    if m == 1:
        return f"{y - 1}-12"
    return f"{y}-{m - 1:02d}"


def x_previous_month_name__mutmut_orig(month: str) -> str:
    year, mo = month.split("-")
    y = int(year)
    m = int(mo)
    if m == 1:
        return f"{y - 1}-12"
    return f"{y}-{m - 1:02d}"


def x_previous_month_name__mutmut_1(month: str) -> str:
    year, mo = None
    y = int(year)
    m = int(mo)
    if m == 1:
        return f"{y - 1}-12"
    return f"{y}-{m - 1:02d}"


def x_previous_month_name__mutmut_2(month: str) -> str:
    year, mo = month.split(None)
    y = int(year)
    m = int(mo)
    if m == 1:
        return f"{y - 1}-12"
    return f"{y}-{m - 1:02d}"


def x_previous_month_name__mutmut_3(month: str) -> str:
    year, mo = month.split("XX-XX")
    y = int(year)
    m = int(mo)
    if m == 1:
        return f"{y - 1}-12"
    return f"{y}-{m - 1:02d}"


def x_previous_month_name__mutmut_4(month: str) -> str:
    year, mo = month.split("-")
    y = None
    m = int(mo)
    if m == 1:
        return f"{y - 1}-12"
    return f"{y}-{m - 1:02d}"


def x_previous_month_name__mutmut_5(month: str) -> str:
    year, mo = month.split("-")
    y = int(None)
    m = int(mo)
    if m == 1:
        return f"{y - 1}-12"
    return f"{y}-{m - 1:02d}"


def x_previous_month_name__mutmut_6(month: str) -> str:
    year, mo = month.split("-")
    y = int(year)
    m = None
    if m == 1:
        return f"{y - 1}-12"
    return f"{y}-{m - 1:02d}"


def x_previous_month_name__mutmut_7(month: str) -> str:
    year, mo = month.split("-")
    y = int(year)
    m = int(None)
    if m == 1:
        return f"{y - 1}-12"
    return f"{y}-{m - 1:02d}"


def x_previous_month_name__mutmut_8(month: str) -> str:
    year, mo = month.split("-")
    y = int(year)
    m = int(mo)
    if m != 1:
        return f"{y - 1}-12"
    return f"{y}-{m - 1:02d}"


def x_previous_month_name__mutmut_9(month: str) -> str:
    year, mo = month.split("-")
    y = int(year)
    m = int(mo)
    if m == 2:
        return f"{y - 1}-12"
    return f"{y}-{m - 1:02d}"


def x_previous_month_name__mutmut_10(month: str) -> str:
    year, mo = month.split("-")
    y = int(year)
    m = int(mo)
    if m == 1:
        return f"{y + 1}-12"
    return f"{y}-{m - 1:02d}"


def x_previous_month_name__mutmut_11(month: str) -> str:
    year, mo = month.split("-")
    y = int(year)
    m = int(mo)
    if m == 1:
        return f"{y - 2}-12"
    return f"{y}-{m - 1:02d}"


def x_previous_month_name__mutmut_12(month: str) -> str:
    year, mo = month.split("-")
    y = int(year)
    m = int(mo)
    if m == 1:
        return f"{y - 1}-12"
    return f"{y}-{m + 1:02d}"


def x_previous_month_name__mutmut_13(month: str) -> str:
    year, mo = month.split("-")
    y = int(year)
    m = int(mo)
    if m == 1:
        return f"{y - 1}-12"
    return f"{y}-{m - 2:02d}"

mutants_x_previous_month_name__mutmut['_mutmut_orig'] = x_previous_month_name__mutmut_orig # type: ignore # mutmut generated
mutants_x_previous_month_name__mutmut['x_previous_month_name__mutmut_1'] = x_previous_month_name__mutmut_1 # type: ignore # mutmut generated
mutants_x_previous_month_name__mutmut['x_previous_month_name__mutmut_2'] = x_previous_month_name__mutmut_2 # type: ignore # mutmut generated
mutants_x_previous_month_name__mutmut['x_previous_month_name__mutmut_3'] = x_previous_month_name__mutmut_3 # type: ignore # mutmut generated
mutants_x_previous_month_name__mutmut['x_previous_month_name__mutmut_4'] = x_previous_month_name__mutmut_4 # type: ignore # mutmut generated
mutants_x_previous_month_name__mutmut['x_previous_month_name__mutmut_5'] = x_previous_month_name__mutmut_5 # type: ignore # mutmut generated
mutants_x_previous_month_name__mutmut['x_previous_month_name__mutmut_6'] = x_previous_month_name__mutmut_6 # type: ignore # mutmut generated
mutants_x_previous_month_name__mutmut['x_previous_month_name__mutmut_7'] = x_previous_month_name__mutmut_7 # type: ignore # mutmut generated
mutants_x_previous_month_name__mutmut['x_previous_month_name__mutmut_8'] = x_previous_month_name__mutmut_8 # type: ignore # mutmut generated
mutants_x_previous_month_name__mutmut['x_previous_month_name__mutmut_9'] = x_previous_month_name__mutmut_9 # type: ignore # mutmut generated
mutants_x_previous_month_name__mutmut['x_previous_month_name__mutmut_10'] = x_previous_month_name__mutmut_10 # type: ignore # mutmut generated
mutants_x_previous_month_name__mutmut['x_previous_month_name__mutmut_11'] = x_previous_month_name__mutmut_11 # type: ignore # mutmut generated
mutants_x_previous_month_name__mutmut['x_previous_month_name__mutmut_12'] = x_previous_month_name__mutmut_12 # type: ignore # mutmut generated
mutants_x_previous_month_name__mutmut['x_previous_month_name__mutmut_13'] = x_previous_month_name__mutmut_13 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_aggregate_incidents__mutmut)
def aggregate_incidents(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_orig(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_1(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = None
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_2(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["XXP1XX", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_3(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["p1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_4(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "XXP2XX", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_5(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "p2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_6(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "XXP3XX"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_7(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "p3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_8(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = None
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_9(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"XXcountXX": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_10(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"COUNT": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_11(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 1, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_12(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "XXdowntime_minutesXX": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_13(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "DOWNTIME_MINUTES": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_14(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 1} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_15(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = None
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_16(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(None)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_17(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = None
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_18(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(None)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_19(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = None

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_20(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 1

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_21(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") and inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_22(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get(None) or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_23(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("XXis_planned_maintenanceXX") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_24(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("IS_PLANNED_MAINTENANCE") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_25(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get(None):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_26(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("XXreopenedXX"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_27(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("REOPENED"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_28(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            break
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_29(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = None
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_30(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(None)
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_31(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get(None))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_32(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("XXseverityXX"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_33(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("SEVERITY"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_34(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_35(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = None
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_36(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "XXP3XX"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_37(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "p3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_38(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = None
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_39(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(None)
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_40(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get(None))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_41(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("XXdowntime_minutesXX"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_42(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("DOWNTIME_MINUTES"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_43(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] = 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_44(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] -= 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_45(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["XXcountXX"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_46(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["COUNT"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_47(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 2
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_48(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] = dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_49(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] -= dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_50(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["XXdowntime_minutesXX"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_51(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["DOWNTIME_MINUTES"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_52(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime = dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_53(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime -= dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_54(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = None
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_55(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(None)
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_56(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get(None, "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_57(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", None))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_58(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_59(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", ))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_60(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("XXservice_nameXX", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_61(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("SERVICE_NAME", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_62(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "XXunknownXX"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_63(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "UNKNOWN"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_64(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] = dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_65(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] -= dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_66(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] = 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_67(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] -= 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_68(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 2

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_69(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = None

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_70(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        None,
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_71(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=None,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_72(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=None,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_73(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_74(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_75(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_76(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=None,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_77(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=None,
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_78(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=None,
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_79(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_80(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_81(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_82(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: None,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_83(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=False,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_84(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = None
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_85(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(None)[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_86(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get(None, ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_87(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", None))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_88(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get(""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_89(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_90(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[1].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_91(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("XXtimestampXX", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_92(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("TIMESTAMP", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_93(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", "XXXX"))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_94(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:8] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_95(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else "XXXX"
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_96(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "XXmonthXX": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_97(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "MONTH": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_98(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "XXtotal_countXX": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_99(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "TOTAL_COUNT": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_100(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "XXtotal_downtime_minutesXX": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_101(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "TOTAL_DOWNTIME_MINUTES": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_102(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "XXper_severityXX": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_103(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "PER_SEVERITY": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_104(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"XXcountXX": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_105(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"COUNT": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_106(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["XXcountXX"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_107(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["COUNT"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_108(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "XXdowntime_minutesXX": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_109(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "DOWNTIME_MINUTES": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_110(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["XXdowntime_minutesXX"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_111(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["DOWNTIME_MINUTES"]}
            for sev, d in per_sev.items()
        },
        "most_impacted_services": impacted,
    }


def x_aggregate_incidents__mutmut_112(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "XXmost_impacted_servicesXX": impacted,
    }


def x_aggregate_incidents__mutmut_113(
    incidents: list[dict[str, object]],
) -> IncidentAggregate:
    sev_keys = ["P1", "P2", "P3"]
    per_sev: dict[str, dict[str, int]] = {k: {"count": 0, "downtime_minutes": 0} for k in sev_keys}
    svc_downtime: dict[str, int] = defaultdict(int)
    svc_count: dict[str, int] = defaultdict(int)
    total_downtime = 0

    for inc in incidents:
        if inc.get("is_planned_maintenance") or inc.get("reopened"):
            continue
        sev = str(inc.get("severity"))
        if sev not in per_sev:
            sev = "P3"
        dt = _as_int(inc.get("downtime_minutes"))
        per_sev[sev]["count"] += 1
        per_sev[sev]["downtime_minutes"] += dt
        total_downtime += dt
        svc = str(inc.get("service_name", "unknown"))
        svc_downtime[svc] += dt
        svc_count[svc] += 1

    impacted = sorted(
        [
            ImpactedService(
                service_name=svc,
                total_downtime=svc_downtime[svc],
                incident_count=svc_count[svc],
            )
            for svc in svc_downtime
        ],
        key=lambda s: s.total_downtime,
        reverse=True,
    )

    month = str(incidents[0].get("timestamp", ""))[:7] if incidents else ""
    return {
        "month": month,
        "total_count": len(incidents),
        "total_downtime_minutes": total_downtime,
        "per_severity": {
            sev: {"count": d["count"], "downtime_minutes": d["downtime_minutes"]}
            for sev, d in per_sev.items()
        },
        "MOST_IMPACTED_SERVICES": impacted,
    }

mutants_x_aggregate_incidents__mutmut['_mutmut_orig'] = x_aggregate_incidents__mutmut_orig # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_1'] = x_aggregate_incidents__mutmut_1 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_2'] = x_aggregate_incidents__mutmut_2 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_3'] = x_aggregate_incidents__mutmut_3 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_4'] = x_aggregate_incidents__mutmut_4 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_5'] = x_aggregate_incidents__mutmut_5 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_6'] = x_aggregate_incidents__mutmut_6 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_7'] = x_aggregate_incidents__mutmut_7 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_8'] = x_aggregate_incidents__mutmut_8 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_9'] = x_aggregate_incidents__mutmut_9 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_10'] = x_aggregate_incidents__mutmut_10 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_11'] = x_aggregate_incidents__mutmut_11 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_12'] = x_aggregate_incidents__mutmut_12 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_13'] = x_aggregate_incidents__mutmut_13 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_14'] = x_aggregate_incidents__mutmut_14 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_15'] = x_aggregate_incidents__mutmut_15 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_16'] = x_aggregate_incidents__mutmut_16 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_17'] = x_aggregate_incidents__mutmut_17 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_18'] = x_aggregate_incidents__mutmut_18 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_19'] = x_aggregate_incidents__mutmut_19 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_20'] = x_aggregate_incidents__mutmut_20 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_21'] = x_aggregate_incidents__mutmut_21 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_22'] = x_aggregate_incidents__mutmut_22 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_23'] = x_aggregate_incidents__mutmut_23 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_24'] = x_aggregate_incidents__mutmut_24 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_25'] = x_aggregate_incidents__mutmut_25 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_26'] = x_aggregate_incidents__mutmut_26 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_27'] = x_aggregate_incidents__mutmut_27 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_28'] = x_aggregate_incidents__mutmut_28 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_29'] = x_aggregate_incidents__mutmut_29 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_30'] = x_aggregate_incidents__mutmut_30 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_31'] = x_aggregate_incidents__mutmut_31 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_32'] = x_aggregate_incidents__mutmut_32 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_33'] = x_aggregate_incidents__mutmut_33 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_34'] = x_aggregate_incidents__mutmut_34 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_35'] = x_aggregate_incidents__mutmut_35 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_36'] = x_aggregate_incidents__mutmut_36 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_37'] = x_aggregate_incidents__mutmut_37 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_38'] = x_aggregate_incidents__mutmut_38 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_39'] = x_aggregate_incidents__mutmut_39 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_40'] = x_aggregate_incidents__mutmut_40 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_41'] = x_aggregate_incidents__mutmut_41 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_42'] = x_aggregate_incidents__mutmut_42 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_43'] = x_aggregate_incidents__mutmut_43 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_44'] = x_aggregate_incidents__mutmut_44 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_45'] = x_aggregate_incidents__mutmut_45 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_46'] = x_aggregate_incidents__mutmut_46 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_47'] = x_aggregate_incidents__mutmut_47 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_48'] = x_aggregate_incidents__mutmut_48 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_49'] = x_aggregate_incidents__mutmut_49 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_50'] = x_aggregate_incidents__mutmut_50 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_51'] = x_aggregate_incidents__mutmut_51 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_52'] = x_aggregate_incidents__mutmut_52 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_53'] = x_aggregate_incidents__mutmut_53 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_54'] = x_aggregate_incidents__mutmut_54 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_55'] = x_aggregate_incidents__mutmut_55 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_56'] = x_aggregate_incidents__mutmut_56 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_57'] = x_aggregate_incidents__mutmut_57 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_58'] = x_aggregate_incidents__mutmut_58 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_59'] = x_aggregate_incidents__mutmut_59 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_60'] = x_aggregate_incidents__mutmut_60 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_61'] = x_aggregate_incidents__mutmut_61 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_62'] = x_aggregate_incidents__mutmut_62 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_63'] = x_aggregate_incidents__mutmut_63 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_64'] = x_aggregate_incidents__mutmut_64 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_65'] = x_aggregate_incidents__mutmut_65 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_66'] = x_aggregate_incidents__mutmut_66 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_67'] = x_aggregate_incidents__mutmut_67 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_68'] = x_aggregate_incidents__mutmut_68 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_69'] = x_aggregate_incidents__mutmut_69 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_70'] = x_aggregate_incidents__mutmut_70 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_71'] = x_aggregate_incidents__mutmut_71 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_72'] = x_aggregate_incidents__mutmut_72 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_73'] = x_aggregate_incidents__mutmut_73 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_74'] = x_aggregate_incidents__mutmut_74 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_75'] = x_aggregate_incidents__mutmut_75 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_76'] = x_aggregate_incidents__mutmut_76 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_77'] = x_aggregate_incidents__mutmut_77 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_78'] = x_aggregate_incidents__mutmut_78 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_79'] = x_aggregate_incidents__mutmut_79 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_80'] = x_aggregate_incidents__mutmut_80 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_81'] = x_aggregate_incidents__mutmut_81 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_82'] = x_aggregate_incidents__mutmut_82 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_83'] = x_aggregate_incidents__mutmut_83 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_84'] = x_aggregate_incidents__mutmut_84 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_85'] = x_aggregate_incidents__mutmut_85 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_86'] = x_aggregate_incidents__mutmut_86 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_87'] = x_aggregate_incidents__mutmut_87 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_88'] = x_aggregate_incidents__mutmut_88 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_89'] = x_aggregate_incidents__mutmut_89 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_90'] = x_aggregate_incidents__mutmut_90 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_91'] = x_aggregate_incidents__mutmut_91 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_92'] = x_aggregate_incidents__mutmut_92 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_93'] = x_aggregate_incidents__mutmut_93 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_94'] = x_aggregate_incidents__mutmut_94 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_95'] = x_aggregate_incidents__mutmut_95 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_96'] = x_aggregate_incidents__mutmut_96 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_97'] = x_aggregate_incidents__mutmut_97 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_98'] = x_aggregate_incidents__mutmut_98 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_99'] = x_aggregate_incidents__mutmut_99 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_100'] = x_aggregate_incidents__mutmut_100 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_101'] = x_aggregate_incidents__mutmut_101 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_102'] = x_aggregate_incidents__mutmut_102 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_103'] = x_aggregate_incidents__mutmut_103 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_104'] = x_aggregate_incidents__mutmut_104 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_105'] = x_aggregate_incidents__mutmut_105 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_106'] = x_aggregate_incidents__mutmut_106 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_107'] = x_aggregate_incidents__mutmut_107 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_108'] = x_aggregate_incidents__mutmut_108 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_109'] = x_aggregate_incidents__mutmut_109 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_110'] = x_aggregate_incidents__mutmut_110 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_111'] = x_aggregate_incidents__mutmut_111 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_112'] = x_aggregate_incidents__mutmut_112 # type: ignore # mutmut generated
mutants_x_aggregate_incidents__mutmut['x_aggregate_incidents__mutmut_113'] = x_aggregate_incidents__mutmut_113 # type: ignore # mutmut generated
