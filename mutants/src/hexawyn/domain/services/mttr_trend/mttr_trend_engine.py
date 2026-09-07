from __future__ import annotations

from hexawyn.domain.models.mttr_trend import (
    MTTRPerSeverity,
    MTTRTrendReport,
    SlowestIncident,
)

_BENCHMARKS = {"P1": 30, "P2": 120}
_SIGNIFICANT_TREND_PCT = 10


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁMTTRTrendEngineǁcompute__mutmut: MutantDict = {}  # type: ignore


class MTTRTrendEngine:
    @_mutmut_mutated(mutants_xǁMTTRTrendEngineǁcompute__mutmut)
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_orig(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_1(
        self,
        months: dict[str, list[dict[str, object]]],
    ) -> MTTRTrendReport:
        per_month: dict[str, dict[str, MTTRPerSeverity]] = None
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_2(
        self,
        months: dict[str, list[dict[str, object]]],
    ) -> MTTRTrendReport:
        per_month: dict[str, dict[str, MTTRPerSeverity]] = {}
        all_slowest: list[dict[str, object]] = None

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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_3(
        self,
        months: dict[str, list[dict[str, object]]],
    ) -> MTTRTrendReport:
        per_month: dict[str, dict[str, MTTRPerSeverity]] = {}
        all_slowest: list[dict[str, object]] = []

        for month, incidents in months.items():
            per_month[month] = None
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_4(
        self,
        months: dict[str, list[dict[str, object]]],
    ) -> MTTRTrendReport:
        per_month: dict[str, dict[str, MTTRPerSeverity]] = {}
        all_slowest: list[dict[str, object]] = []

        for month, incidents in months.items():
            per_month[month] = {}
            sev_data: dict[str, dict[str, float | int]] = None

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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_5(
        self,
        months: dict[str, list[dict[str, object]]],
    ) -> MTTRTrendReport:
        per_month: dict[str, dict[str, MTTRPerSeverity]] = {}
        all_slowest: list[dict[str, object]] = []

        for month, incidents in months.items():
            per_month[month] = {}
            sev_data: dict[str, dict[str, float | int]] = {}

            for inc in incidents:
                all_slowest.append(None)
                if not _as_bool(inc.get("resolved")):
                    continue

                sev = str(inc.get("severity", "P1"))
                mins = _as_int(inc.get("resolution_minutes"))

                if sev not in sev_data:
                    sev_data[sev] = {"total": 0.0, "count": 0}
                sev_data[sev]["total"] += mins
                sev_data[sev]["count"] += 1

            for sev in _BENCHMARKS:
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_6(
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
                if _as_bool(inc.get("resolved")):
                    continue

                sev = str(inc.get("severity", "P1"))
                mins = _as_int(inc.get("resolution_minutes"))

                if sev not in sev_data:
                    sev_data[sev] = {"total": 0.0, "count": 0}
                sev_data[sev]["total"] += mins
                sev_data[sev]["count"] += 1

            for sev in _BENCHMARKS:
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_7(
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
                if not _as_bool(None):
                    continue

                sev = str(inc.get("severity", "P1"))
                mins = _as_int(inc.get("resolution_minutes"))

                if sev not in sev_data:
                    sev_data[sev] = {"total": 0.0, "count": 0}
                sev_data[sev]["total"] += mins
                sev_data[sev]["count"] += 1

            for sev in _BENCHMARKS:
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_8(
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
                if not _as_bool(inc.get(None)):
                    continue

                sev = str(inc.get("severity", "P1"))
                mins = _as_int(inc.get("resolution_minutes"))

                if sev not in sev_data:
                    sev_data[sev] = {"total": 0.0, "count": 0}
                sev_data[sev]["total"] += mins
                sev_data[sev]["count"] += 1

            for sev in _BENCHMARKS:
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_9(
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
                if not _as_bool(inc.get("XXresolvedXX")):
                    continue

                sev = str(inc.get("severity", "P1"))
                mins = _as_int(inc.get("resolution_minutes"))

                if sev not in sev_data:
                    sev_data[sev] = {"total": 0.0, "count": 0}
                sev_data[sev]["total"] += mins
                sev_data[sev]["count"] += 1

            for sev in _BENCHMARKS:
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_10(
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
                if not _as_bool(inc.get("RESOLVED")):
                    continue

                sev = str(inc.get("severity", "P1"))
                mins = _as_int(inc.get("resolution_minutes"))

                if sev not in sev_data:
                    sev_data[sev] = {"total": 0.0, "count": 0}
                sev_data[sev]["total"] += mins
                sev_data[sev]["count"] += 1

            for sev in _BENCHMARKS:
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_11(
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
                    break

                sev = str(inc.get("severity", "P1"))
                mins = _as_int(inc.get("resolution_minutes"))

                if sev not in sev_data:
                    sev_data[sev] = {"total": 0.0, "count": 0}
                sev_data[sev]["total"] += mins
                sev_data[sev]["count"] += 1

            for sev in _BENCHMARKS:
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_12(
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

                sev = None
                mins = _as_int(inc.get("resolution_minutes"))

                if sev not in sev_data:
                    sev_data[sev] = {"total": 0.0, "count": 0}
                sev_data[sev]["total"] += mins
                sev_data[sev]["count"] += 1

            for sev in _BENCHMARKS:
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_13(
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

                sev = str(None)
                mins = _as_int(inc.get("resolution_minutes"))

                if sev not in sev_data:
                    sev_data[sev] = {"total": 0.0, "count": 0}
                sev_data[sev]["total"] += mins
                sev_data[sev]["count"] += 1

            for sev in _BENCHMARKS:
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_14(
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

                sev = str(inc.get(None, "P1"))
                mins = _as_int(inc.get("resolution_minutes"))

                if sev not in sev_data:
                    sev_data[sev] = {"total": 0.0, "count": 0}
                sev_data[sev]["total"] += mins
                sev_data[sev]["count"] += 1

            for sev in _BENCHMARKS:
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_15(
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

                sev = str(inc.get("severity", None))
                mins = _as_int(inc.get("resolution_minutes"))

                if sev not in sev_data:
                    sev_data[sev] = {"total": 0.0, "count": 0}
                sev_data[sev]["total"] += mins
                sev_data[sev]["count"] += 1

            for sev in _BENCHMARKS:
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_16(
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

                sev = str(inc.get("P1"))
                mins = _as_int(inc.get("resolution_minutes"))

                if sev not in sev_data:
                    sev_data[sev] = {"total": 0.0, "count": 0}
                sev_data[sev]["total"] += mins
                sev_data[sev]["count"] += 1

            for sev in _BENCHMARKS:
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_17(
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

                sev = str(inc.get("severity", ))
                mins = _as_int(inc.get("resolution_minutes"))

                if sev not in sev_data:
                    sev_data[sev] = {"total": 0.0, "count": 0}
                sev_data[sev]["total"] += mins
                sev_data[sev]["count"] += 1

            for sev in _BENCHMARKS:
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_18(
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

                sev = str(inc.get("XXseverityXX", "P1"))
                mins = _as_int(inc.get("resolution_minutes"))

                if sev not in sev_data:
                    sev_data[sev] = {"total": 0.0, "count": 0}
                sev_data[sev]["total"] += mins
                sev_data[sev]["count"] += 1

            for sev in _BENCHMARKS:
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_19(
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

                sev = str(inc.get("SEVERITY", "P1"))
                mins = _as_int(inc.get("resolution_minutes"))

                if sev not in sev_data:
                    sev_data[sev] = {"total": 0.0, "count": 0}
                sev_data[sev]["total"] += mins
                sev_data[sev]["count"] += 1

            for sev in _BENCHMARKS:
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_20(
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

                sev = str(inc.get("severity", "XXP1XX"))
                mins = _as_int(inc.get("resolution_minutes"))

                if sev not in sev_data:
                    sev_data[sev] = {"total": 0.0, "count": 0}
                sev_data[sev]["total"] += mins
                sev_data[sev]["count"] += 1

            for sev in _BENCHMARKS:
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_21(
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

                sev = str(inc.get("severity", "p1"))
                mins = _as_int(inc.get("resolution_minutes"))

                if sev not in sev_data:
                    sev_data[sev] = {"total": 0.0, "count": 0}
                sev_data[sev]["total"] += mins
                sev_data[sev]["count"] += 1

            for sev in _BENCHMARKS:
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_22(
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
                mins = None

                if sev not in sev_data:
                    sev_data[sev] = {"total": 0.0, "count": 0}
                sev_data[sev]["total"] += mins
                sev_data[sev]["count"] += 1

            for sev in _BENCHMARKS:
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_23(
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
                mins = _as_int(None)

                if sev not in sev_data:
                    sev_data[sev] = {"total": 0.0, "count": 0}
                sev_data[sev]["total"] += mins
                sev_data[sev]["count"] += 1

            for sev in _BENCHMARKS:
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_24(
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
                mins = _as_int(inc.get(None))

                if sev not in sev_data:
                    sev_data[sev] = {"total": 0.0, "count": 0}
                sev_data[sev]["total"] += mins
                sev_data[sev]["count"] += 1

            for sev in _BENCHMARKS:
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_25(
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
                mins = _as_int(inc.get("XXresolution_minutesXX"))

                if sev not in sev_data:
                    sev_data[sev] = {"total": 0.0, "count": 0}
                sev_data[sev]["total"] += mins
                sev_data[sev]["count"] += 1

            for sev in _BENCHMARKS:
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_26(
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
                mins = _as_int(inc.get("RESOLUTION_MINUTES"))

                if sev not in sev_data:
                    sev_data[sev] = {"total": 0.0, "count": 0}
                sev_data[sev]["total"] += mins
                sev_data[sev]["count"] += 1

            for sev in _BENCHMARKS:
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_27(
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

                if sev in sev_data:
                    sev_data[sev] = {"total": 0.0, "count": 0}
                sev_data[sev]["total"] += mins
                sev_data[sev]["count"] += 1

            for sev in _BENCHMARKS:
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_28(
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
                    sev_data[sev] = None
                sev_data[sev]["total"] += mins
                sev_data[sev]["count"] += 1

            for sev in _BENCHMARKS:
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_29(
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
                    sev_data[sev] = {"XXtotalXX": 0.0, "count": 0}
                sev_data[sev]["total"] += mins
                sev_data[sev]["count"] += 1

            for sev in _BENCHMARKS:
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_30(
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
                    sev_data[sev] = {"TOTAL": 0.0, "count": 0}
                sev_data[sev]["total"] += mins
                sev_data[sev]["count"] += 1

            for sev in _BENCHMARKS:
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_31(
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
                    sev_data[sev] = {"total": 1.0, "count": 0}
                sev_data[sev]["total"] += mins
                sev_data[sev]["count"] += 1

            for sev in _BENCHMARKS:
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_32(
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
                    sev_data[sev] = {"total": 0.0, "XXcountXX": 0}
                sev_data[sev]["total"] += mins
                sev_data[sev]["count"] += 1

            for sev in _BENCHMARKS:
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_33(
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
                    sev_data[sev] = {"total": 0.0, "COUNT": 0}
                sev_data[sev]["total"] += mins
                sev_data[sev]["count"] += 1

            for sev in _BENCHMARKS:
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_34(
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
                    sev_data[sev] = {"total": 0.0, "count": 1}
                sev_data[sev]["total"] += mins
                sev_data[sev]["count"] += 1

            for sev in _BENCHMARKS:
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_35(
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
                sev_data[sev]["total"] = mins
                sev_data[sev]["count"] += 1

            for sev in _BENCHMARKS:
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_36(
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
                sev_data[sev]["total"] -= mins
                sev_data[sev]["count"] += 1

            for sev in _BENCHMARKS:
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_37(
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
                sev_data[sev]["XXtotalXX"] += mins
                sev_data[sev]["count"] += 1

            for sev in _BENCHMARKS:
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_38(
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
                sev_data[sev]["TOTAL"] += mins
                sev_data[sev]["count"] += 1

            for sev in _BENCHMARKS:
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_39(
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
                sev_data[sev]["count"] = 1

            for sev in _BENCHMARKS:
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_40(
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
                sev_data[sev]["count"] -= 1

            for sev in _BENCHMARKS:
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_41(
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
                sev_data[sev]["XXcountXX"] += 1

            for sev in _BENCHMARKS:
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_42(
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
                sev_data[sev]["COUNT"] += 1

            for sev in _BENCHMARKS:
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_43(
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
                sev_data[sev]["count"] += 2

            for sev in _BENCHMARKS:
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_44(
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
                if sev not in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_45(
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
                if sev in sev_data:
                    mttr = None
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_46(
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
                if sev in sev_data:
                    mttr = round(None, 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_47(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], None)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_48(
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
                if sev in sev_data:
                    mttr = round(1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_49(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], )
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_50(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] * sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_51(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["XXtotalXX"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_52(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["TOTAL"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_53(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["XXcountXX"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_54(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["COUNT"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_55(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 2)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_56(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = None
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
    def xǁMTTRTrendEngineǁcompute__mutmut_57(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr < _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_58(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
                    per_month[month][sev] = None
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
    def xǁMTTRTrendEngineǁcompute__mutmut_59(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
                    per_month[month][sev] = MTTRPerSeverity(
                        severity=None,
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
    def xǁMTTRTrendEngineǁcompute__mutmut_60(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
                    per_month[month][sev] = MTTRPerSeverity(
                        severity=sev,
                        mttr_minutes=None,
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
    def xǁMTTRTrendEngineǁcompute__mutmut_61(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
                    per_month[month][sev] = MTTRPerSeverity(
                        severity=sev,
                        mttr_minutes=mttr,
                        incident_count=None,
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
    def xǁMTTRTrendEngineǁcompute__mutmut_62(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
                    per_month[month][sev] = MTTRPerSeverity(
                        severity=sev,
                        mttr_minutes=mttr,
                        incident_count=int(sev_data[sev]["count"]),
                        meets_benchmark=None,
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
    def xǁMTTRTrendEngineǁcompute__mutmut_63(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
                    per_month[month][sev] = MTTRPerSeverity(
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
    def xǁMTTRTrendEngineǁcompute__mutmut_64(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
                    per_month[month][sev] = MTTRPerSeverity(
                        severity=sev,
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
    def xǁMTTRTrendEngineǁcompute__mutmut_65(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
                    per_month[month][sev] = MTTRPerSeverity(
                        severity=sev,
                        mttr_minutes=mttr,
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
    def xǁMTTRTrendEngineǁcompute__mutmut_66(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
                    per_month[month][sev] = MTTRPerSeverity(
                        severity=sev,
                        mttr_minutes=mttr,
                        incident_count=int(sev_data[sev]["count"]),
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
    def xǁMTTRTrendEngineǁcompute__mutmut_67(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
                    per_month[month][sev] = MTTRPerSeverity(
                        severity=sev,
                        mttr_minutes=mttr,
                        incident_count=int(None),
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
    def xǁMTTRTrendEngineǁcompute__mutmut_68(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
                    per_month[month][sev] = MTTRPerSeverity(
                        severity=sev,
                        mttr_minutes=mttr,
                        incident_count=int(sev_data[sev]["XXcountXX"]),
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
    def xǁMTTRTrendEngineǁcompute__mutmut_69(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
                    per_month[month][sev] = MTTRPerSeverity(
                        severity=sev,
                        mttr_minutes=mttr,
                        incident_count=int(sev_data[sev]["COUNT"]),
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
    def xǁMTTRTrendEngineǁcompute__mutmut_70(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
                    per_month[month][sev] = MTTRPerSeverity(
                        severity=sev,
                        mttr_minutes=mttr,
                        incident_count=int(sev_data[sev]["count"]),
                        meets_benchmark=meets,
                    )
                else:
                    per_month[month][sev] = None

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
    def xǁMTTRTrendEngineǁcompute__mutmut_71(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
                    per_month[month][sev] = MTTRPerSeverity(
                        severity=sev,
                        mttr_minutes=mttr,
                        incident_count=int(sev_data[sev]["count"]),
                        meets_benchmark=meets,
                    )
                else:
                    per_month[month][sev] = MTTRPerSeverity(
                        severity=None,
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
    def xǁMTTRTrendEngineǁcompute__mutmut_72(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
                        incident_count=None,
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
    def xǁMTTRTrendEngineǁcompute__mutmut_73(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
                        meets_benchmark=None,
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
    def xǁMTTRTrendEngineǁcompute__mutmut_74(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
                    per_month[month][sev] = MTTRPerSeverity(
                        severity=sev,
                        mttr_minutes=mttr,
                        incident_count=int(sev_data[sev]["count"]),
                        meets_benchmark=meets,
                    )
                else:
                    per_month[month][sev] = MTTRPerSeverity(
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
    def xǁMTTRTrendEngineǁcompute__mutmut_75(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
                    per_month[month][sev] = MTTRPerSeverity(
                        severity=sev,
                        mttr_minutes=mttr,
                        incident_count=int(sev_data[sev]["count"]),
                        meets_benchmark=meets,
                    )
                else:
                    per_month[month][sev] = MTTRPerSeverity(
                        severity=sev,
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
    def xǁMTTRTrendEngineǁcompute__mutmut_76(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_77(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
    def xǁMTTRTrendEngineǁcompute__mutmut_78(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
                        incident_count=1,
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
    def xǁMTTRTrendEngineǁcompute__mutmut_79(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
                        meets_benchmark=True,
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
    def xǁMTTRTrendEngineǁcompute__mutmut_80(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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

        sorted_months = None
        trend, recommendation = _compute_trend(per_month, sorted_months)

        slowest = _rank_slowest(all_slowest)

        report = MTTRTrendReport(
            per_month=per_month,
            slowest_incidents=slowest,
            trend=trend,
            recommendation=recommendation,
        )
        return report
    def xǁMTTRTrendEngineǁcompute__mutmut_81(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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

        sorted_months = sorted(None)
        trend, recommendation = _compute_trend(per_month, sorted_months)

        slowest = _rank_slowest(all_slowest)

        report = MTTRTrendReport(
            per_month=per_month,
            slowest_incidents=slowest,
            trend=trend,
            recommendation=recommendation,
        )
        return report
    def xǁMTTRTrendEngineǁcompute__mutmut_82(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
        trend, recommendation = None

        slowest = _rank_slowest(all_slowest)

        report = MTTRTrendReport(
            per_month=per_month,
            slowest_incidents=slowest,
            trend=trend,
            recommendation=recommendation,
        )
        return report
    def xǁMTTRTrendEngineǁcompute__mutmut_83(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
        trend, recommendation = _compute_trend(None, sorted_months)

        slowest = _rank_slowest(all_slowest)

        report = MTTRTrendReport(
            per_month=per_month,
            slowest_incidents=slowest,
            trend=trend,
            recommendation=recommendation,
        )
        return report
    def xǁMTTRTrendEngineǁcompute__mutmut_84(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
        trend, recommendation = _compute_trend(per_month, None)

        slowest = _rank_slowest(all_slowest)

        report = MTTRTrendReport(
            per_month=per_month,
            slowest_incidents=slowest,
            trend=trend,
            recommendation=recommendation,
        )
        return report
    def xǁMTTRTrendEngineǁcompute__mutmut_85(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
        trend, recommendation = _compute_trend(sorted_months)

        slowest = _rank_slowest(all_slowest)

        report = MTTRTrendReport(
            per_month=per_month,
            slowest_incidents=slowest,
            trend=trend,
            recommendation=recommendation,
        )
        return report
    def xǁMTTRTrendEngineǁcompute__mutmut_86(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
        trend, recommendation = _compute_trend(per_month, )

        slowest = _rank_slowest(all_slowest)

        report = MTTRTrendReport(
            per_month=per_month,
            slowest_incidents=slowest,
            trend=trend,
            recommendation=recommendation,
        )
        return report
    def xǁMTTRTrendEngineǁcompute__mutmut_87(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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

        slowest = None

        report = MTTRTrendReport(
            per_month=per_month,
            slowest_incidents=slowest,
            trend=trend,
            recommendation=recommendation,
        )
        return report
    def xǁMTTRTrendEngineǁcompute__mutmut_88(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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

        slowest = _rank_slowest(None)

        report = MTTRTrendReport(
            per_month=per_month,
            slowest_incidents=slowest,
            trend=trend,
            recommendation=recommendation,
        )
        return report
    def xǁMTTRTrendEngineǁcompute__mutmut_89(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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

        report = None
        return report
    def xǁMTTRTrendEngineǁcompute__mutmut_90(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
            per_month=None,
            slowest_incidents=slowest,
            trend=trend,
            recommendation=recommendation,
        )
        return report
    def xǁMTTRTrendEngineǁcompute__mutmut_91(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
            slowest_incidents=None,
            trend=trend,
            recommendation=recommendation,
        )
        return report
    def xǁMTTRTrendEngineǁcompute__mutmut_92(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
            trend=None,
            recommendation=recommendation,
        )
        return report
    def xǁMTTRTrendEngineǁcompute__mutmut_93(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
            recommendation=None,
        )
        return report
    def xǁMTTRTrendEngineǁcompute__mutmut_94(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
            slowest_incidents=slowest,
            trend=trend,
            recommendation=recommendation,
        )
        return report
    def xǁMTTRTrendEngineǁcompute__mutmut_95(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
            trend=trend,
            recommendation=recommendation,
        )
        return report
    def xǁMTTRTrendEngineǁcompute__mutmut_96(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
            recommendation=recommendation,
        )
        return report
    def xǁMTTRTrendEngineǁcompute__mutmut_97(
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
                if sev in sev_data:
                    mttr = round(sev_data[sev]["total"] / sev_data[sev]["count"], 1)
                    meets = mttr <= _BENCHMARKS[sev]
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
            )
        return report

mutants_xǁMTTRTrendEngineǁcompute__mutmut['_mutmut_orig'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_orig # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_1'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_1 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_2'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_2 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_3'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_3 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_4'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_4 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_5'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_5 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_6'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_6 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_7'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_7 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_8'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_8 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_9'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_9 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_10'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_10 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_11'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_11 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_12'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_12 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_13'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_13 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_14'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_14 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_15'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_15 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_16'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_16 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_17'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_17 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_18'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_18 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_19'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_19 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_20'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_20 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_21'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_21 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_22'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_22 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_23'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_23 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_24'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_24 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_25'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_25 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_26'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_26 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_27'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_27 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_28'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_28 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_29'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_29 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_30'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_30 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_31'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_31 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_32'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_32 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_33'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_33 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_34'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_34 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_35'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_35 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_36'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_36 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_37'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_37 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_38'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_38 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_39'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_39 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_40'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_40 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_41'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_41 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_42'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_42 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_43'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_43 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_44'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_44 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_45'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_45 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_46'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_46 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_47'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_47 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_48'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_48 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_49'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_49 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_50'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_50 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_51'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_51 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_52'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_52 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_53'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_53 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_54'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_54 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_55'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_55 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_56'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_56 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_57'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_57 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_58'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_58 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_59'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_59 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_60'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_60 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_61'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_61 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_62'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_62 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_63'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_63 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_64'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_64 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_65'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_65 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_66'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_66 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_67'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_67 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_68'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_68 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_69'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_69 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_70'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_70 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_71'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_71 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_72'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_72 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_73'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_73 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_74'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_74 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_75'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_75 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_76'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_76 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_77'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_77 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_78'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_78 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_79'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_79 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_80'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_80 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_81'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_81 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_82'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_82 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_83'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_83 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_84'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_84 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_85'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_85 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_86'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_86 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_87'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_87 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_88'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_88 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_89'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_89 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_90'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_90 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_91'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_91 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_92'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_92 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_93'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_93 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_94'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_94 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_95'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_95 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_96'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_96 # type: ignore # mutmut generated
mutants_xǁMTTRTrendEngineǁcompute__mutmut['xǁMTTRTrendEngineǁcompute__mutmut_97'] = MTTRTrendEngine.xǁMTTRTrendEngineǁcompute__mutmut_97 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__compute_trend__mutmut)
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


def x__compute_trend__mutmut_orig(
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


def x__compute_trend__mutmut_1(
    per_month: dict[str, dict[str, MTTRPerSeverity]],
    sorted_months: list[str],
) -> tuple[str, str]:
    p1_values: list[float] = None
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


def x__compute_trend__mutmut_2(
    per_month: dict[str, dict[str, MTTRPerSeverity]],
    sorted_months: list[str],
) -> tuple[str, str]:
    p1_values: list[float] = []
    for m in sorted_months:
        p1 = None
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


def x__compute_trend__mutmut_3(
    per_month: dict[str, dict[str, MTTRPerSeverity]],
    sorted_months: list[str],
) -> tuple[str, str]:
    p1_values: list[float] = []
    for m in sorted_months:
        p1 = per_month.get(m, {}).get(None)
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


def x__compute_trend__mutmut_4(
    per_month: dict[str, dict[str, MTTRPerSeverity]],
    sorted_months: list[str],
) -> tuple[str, str]:
    p1_values: list[float] = []
    for m in sorted_months:
        p1 = per_month.get(None, {}).get("P1")
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


def x__compute_trend__mutmut_5(
    per_month: dict[str, dict[str, MTTRPerSeverity]],
    sorted_months: list[str],
) -> tuple[str, str]:
    p1_values: list[float] = []
    for m in sorted_months:
        p1 = per_month.get(m, None).get("P1")
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


def x__compute_trend__mutmut_6(
    per_month: dict[str, dict[str, MTTRPerSeverity]],
    sorted_months: list[str],
) -> tuple[str, str]:
    p1_values: list[float] = []
    for m in sorted_months:
        p1 = per_month.get({}).get("P1")
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


def x__compute_trend__mutmut_7(
    per_month: dict[str, dict[str, MTTRPerSeverity]],
    sorted_months: list[str],
) -> tuple[str, str]:
    p1_values: list[float] = []
    for m in sorted_months:
        p1 = per_month.get(m, ).get("P1")
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


def x__compute_trend__mutmut_8(
    per_month: dict[str, dict[str, MTTRPerSeverity]],
    sorted_months: list[str],
) -> tuple[str, str]:
    p1_values: list[float] = []
    for m in sorted_months:
        p1 = per_month.get(m, {}).get("XXP1XX")
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


def x__compute_trend__mutmut_9(
    per_month: dict[str, dict[str, MTTRPerSeverity]],
    sorted_months: list[str],
) -> tuple[str, str]:
    p1_values: list[float] = []
    for m in sorted_months:
        p1 = per_month.get(m, {}).get("p1")
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


def x__compute_trend__mutmut_10(
    per_month: dict[str, dict[str, MTTRPerSeverity]],
    sorted_months: list[str],
) -> tuple[str, str]:
    p1_values: list[float] = []
    for m in sorted_months:
        p1 = per_month.get(m, {}).get("P1")
        if p1 or p1.mttr_minutes is not None:
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


def x__compute_trend__mutmut_11(
    per_month: dict[str, dict[str, MTTRPerSeverity]],
    sorted_months: list[str],
) -> tuple[str, str]:
    p1_values: list[float] = []
    for m in sorted_months:
        p1 = per_month.get(m, {}).get("P1")
        if p1 and p1.mttr_minutes is None:
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


def x__compute_trend__mutmut_12(
    per_month: dict[str, dict[str, MTTRPerSeverity]],
    sorted_months: list[str],
) -> tuple[str, str]:
    p1_values: list[float] = []
    for m in sorted_months:
        p1 = per_month.get(m, {}).get("P1")
        if p1 and p1.mttr_minutes is not None:
            p1_values.append(None)

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


def x__compute_trend__mutmut_13(
    per_month: dict[str, dict[str, MTTRPerSeverity]],
    sorted_months: list[str],
) -> tuple[str, str]:
    p1_values: list[float] = []
    for m in sorted_months:
        p1 = per_month.get(m, {}).get("P1")
        if p1 and p1.mttr_minutes is not None:
            p1_values.append(p1.mttr_minutes)

    if len(p1_values) <= 2:  # noqa: PLR2004
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


def x__compute_trend__mutmut_14(
    per_month: dict[str, dict[str, MTTRPerSeverity]],
    sorted_months: list[str],
) -> tuple[str, str]:
    p1_values: list[float] = []
    for m in sorted_months:
        p1 = per_month.get(m, {}).get("P1")
        if p1 and p1.mttr_minutes is not None:
            p1_values.append(p1.mttr_minutes)

    if len(p1_values) < 3:  # noqa: PLR2004
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


def x__compute_trend__mutmut_15(
    per_month: dict[str, dict[str, MTTRPerSeverity]],
    sorted_months: list[str],
) -> tuple[str, str]:
    p1_values: list[float] = []
    for m in sorted_months:
        p1 = per_month.get(m, {}).get("P1")
        if p1 and p1.mttr_minutes is not None:
            p1_values.append(p1.mttr_minutes)

    if len(p1_values) < 2:  # noqa: PLR2004
        return "XXinsufficient_dataXX", "Need at least 2 months of P1 data for trend analysis"

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


def x__compute_trend__mutmut_16(
    per_month: dict[str, dict[str, MTTRPerSeverity]],
    sorted_months: list[str],
) -> tuple[str, str]:
    p1_values: list[float] = []
    for m in sorted_months:
        p1 = per_month.get(m, {}).get("P1")
        if p1 and p1.mttr_minutes is not None:
            p1_values.append(p1.mttr_minutes)

    if len(p1_values) < 2:  # noqa: PLR2004
        return "INSUFFICIENT_DATA", "Need at least 2 months of P1 data for trend analysis"

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


def x__compute_trend__mutmut_17(
    per_month: dict[str, dict[str, MTTRPerSeverity]],
    sorted_months: list[str],
) -> tuple[str, str]:
    p1_values: list[float] = []
    for m in sorted_months:
        p1 = per_month.get(m, {}).get("P1")
        if p1 and p1.mttr_minutes is not None:
            p1_values.append(p1.mttr_minutes)

    if len(p1_values) < 2:  # noqa: PLR2004
        return "insufficient_data", "XXNeed at least 2 months of P1 data for trend analysisXX"

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


def x__compute_trend__mutmut_18(
    per_month: dict[str, dict[str, MTTRPerSeverity]],
    sorted_months: list[str],
) -> tuple[str, str]:
    p1_values: list[float] = []
    for m in sorted_months:
        p1 = per_month.get(m, {}).get("P1")
        if p1 and p1.mttr_minutes is not None:
            p1_values.append(p1.mttr_minutes)

    if len(p1_values) < 2:  # noqa: PLR2004
        return "insufficient_data", "need at least 2 months of p1 data for trend analysis"

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


def x__compute_trend__mutmut_19(
    per_month: dict[str, dict[str, MTTRPerSeverity]],
    sorted_months: list[str],
) -> tuple[str, str]:
    p1_values: list[float] = []
    for m in sorted_months:
        p1 = per_month.get(m, {}).get("P1")
        if p1 and p1.mttr_minutes is not None:
            p1_values.append(p1.mttr_minutes)

    if len(p1_values) < 2:  # noqa: PLR2004
        return "insufficient_data", "NEED AT LEAST 2 MONTHS OF P1 DATA FOR TREND ANALYSIS"

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


def x__compute_trend__mutmut_20(
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

    first = None
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


def x__compute_trend__mutmut_21(
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

    first = p1_values[1]
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


def x__compute_trend__mutmut_22(
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
    last = None
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


def x__compute_trend__mutmut_23(
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
    last = p1_values[+1]
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


def x__compute_trend__mutmut_24(
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
    last = p1_values[-2]
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


def x__compute_trend__mutmut_25(
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
    if first != 0:
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


def x__compute_trend__mutmut_26(
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
    if first == 1:
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


def x__compute_trend__mutmut_27(
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
        return "XXstableXX", "No change in MTTR"

    delta = round(((last - first) / first) * 100.0, 1)

    if abs(delta) < _SIGNIFICANT_TREND_PCT:
        return "stable", "MTTR is stable across the period"
    if delta < 0:
        return "improving", f"MTTR improved by {abs(delta):.0f}% — response processes are effective"
    return (
        "degrading",
        f"MTTR degraded by {delta:.0f}% — review on-call runbooks and escalation paths",
    )


def x__compute_trend__mutmut_28(
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
        return "STABLE", "No change in MTTR"

    delta = round(((last - first) / first) * 100.0, 1)

    if abs(delta) < _SIGNIFICANT_TREND_PCT:
        return "stable", "MTTR is stable across the period"
    if delta < 0:
        return "improving", f"MTTR improved by {abs(delta):.0f}% — response processes are effective"
    return (
        "degrading",
        f"MTTR degraded by {delta:.0f}% — review on-call runbooks and escalation paths",
    )


def x__compute_trend__mutmut_29(
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
        return "stable", "XXNo change in MTTRXX"

    delta = round(((last - first) / first) * 100.0, 1)

    if abs(delta) < _SIGNIFICANT_TREND_PCT:
        return "stable", "MTTR is stable across the period"
    if delta < 0:
        return "improving", f"MTTR improved by {abs(delta):.0f}% — response processes are effective"
    return (
        "degrading",
        f"MTTR degraded by {delta:.0f}% — review on-call runbooks and escalation paths",
    )


def x__compute_trend__mutmut_30(
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
        return "stable", "no change in mttr"

    delta = round(((last - first) / first) * 100.0, 1)

    if abs(delta) < _SIGNIFICANT_TREND_PCT:
        return "stable", "MTTR is stable across the period"
    if delta < 0:
        return "improving", f"MTTR improved by {abs(delta):.0f}% — response processes are effective"
    return (
        "degrading",
        f"MTTR degraded by {delta:.0f}% — review on-call runbooks and escalation paths",
    )


def x__compute_trend__mutmut_31(
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
        return "stable", "NO CHANGE IN MTTR"

    delta = round(((last - first) / first) * 100.0, 1)

    if abs(delta) < _SIGNIFICANT_TREND_PCT:
        return "stable", "MTTR is stable across the period"
    if delta < 0:
        return "improving", f"MTTR improved by {abs(delta):.0f}% — response processes are effective"
    return (
        "degrading",
        f"MTTR degraded by {delta:.0f}% — review on-call runbooks and escalation paths",
    )


def x__compute_trend__mutmut_32(
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

    delta = None

    if abs(delta) < _SIGNIFICANT_TREND_PCT:
        return "stable", "MTTR is stable across the period"
    if delta < 0:
        return "improving", f"MTTR improved by {abs(delta):.0f}% — response processes are effective"
    return (
        "degrading",
        f"MTTR degraded by {delta:.0f}% — review on-call runbooks and escalation paths",
    )


def x__compute_trend__mutmut_33(
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

    delta = round(None, 1)

    if abs(delta) < _SIGNIFICANT_TREND_PCT:
        return "stable", "MTTR is stable across the period"
    if delta < 0:
        return "improving", f"MTTR improved by {abs(delta):.0f}% — response processes are effective"
    return (
        "degrading",
        f"MTTR degraded by {delta:.0f}% — review on-call runbooks and escalation paths",
    )


def x__compute_trend__mutmut_34(
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

    delta = round(((last - first) / first) * 100.0, None)

    if abs(delta) < _SIGNIFICANT_TREND_PCT:
        return "stable", "MTTR is stable across the period"
    if delta < 0:
        return "improving", f"MTTR improved by {abs(delta):.0f}% — response processes are effective"
    return (
        "degrading",
        f"MTTR degraded by {delta:.0f}% — review on-call runbooks and escalation paths",
    )


def x__compute_trend__mutmut_35(
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

    delta = round(1)

    if abs(delta) < _SIGNIFICANT_TREND_PCT:
        return "stable", "MTTR is stable across the period"
    if delta < 0:
        return "improving", f"MTTR improved by {abs(delta):.0f}% — response processes are effective"
    return (
        "degrading",
        f"MTTR degraded by {delta:.0f}% — review on-call runbooks and escalation paths",
    )


def x__compute_trend__mutmut_36(
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

    delta = round(((last - first) / first) * 100.0, )

    if abs(delta) < _SIGNIFICANT_TREND_PCT:
        return "stable", "MTTR is stable across the period"
    if delta < 0:
        return "improving", f"MTTR improved by {abs(delta):.0f}% — response processes are effective"
    return (
        "degrading",
        f"MTTR degraded by {delta:.0f}% — review on-call runbooks and escalation paths",
    )


def x__compute_trend__mutmut_37(
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

    delta = round(((last - first) / first) / 100.0, 1)

    if abs(delta) < _SIGNIFICANT_TREND_PCT:
        return "stable", "MTTR is stable across the period"
    if delta < 0:
        return "improving", f"MTTR improved by {abs(delta):.0f}% — response processes are effective"
    return (
        "degrading",
        f"MTTR degraded by {delta:.0f}% — review on-call runbooks and escalation paths",
    )


def x__compute_trend__mutmut_38(
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

    delta = round(((last - first) * first) * 100.0, 1)

    if abs(delta) < _SIGNIFICANT_TREND_PCT:
        return "stable", "MTTR is stable across the period"
    if delta < 0:
        return "improving", f"MTTR improved by {abs(delta):.0f}% — response processes are effective"
    return (
        "degrading",
        f"MTTR degraded by {delta:.0f}% — review on-call runbooks and escalation paths",
    )


def x__compute_trend__mutmut_39(
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

    delta = round(((last + first) / first) * 100.0, 1)

    if abs(delta) < _SIGNIFICANT_TREND_PCT:
        return "stable", "MTTR is stable across the period"
    if delta < 0:
        return "improving", f"MTTR improved by {abs(delta):.0f}% — response processes are effective"
    return (
        "degrading",
        f"MTTR degraded by {delta:.0f}% — review on-call runbooks and escalation paths",
    )


def x__compute_trend__mutmut_40(
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

    delta = round(((last - first) / first) * 101.0, 1)

    if abs(delta) < _SIGNIFICANT_TREND_PCT:
        return "stable", "MTTR is stable across the period"
    if delta < 0:
        return "improving", f"MTTR improved by {abs(delta):.0f}% — response processes are effective"
    return (
        "degrading",
        f"MTTR degraded by {delta:.0f}% — review on-call runbooks and escalation paths",
    )


def x__compute_trend__mutmut_41(
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

    delta = round(((last - first) / first) * 100.0, 2)

    if abs(delta) < _SIGNIFICANT_TREND_PCT:
        return "stable", "MTTR is stable across the period"
    if delta < 0:
        return "improving", f"MTTR improved by {abs(delta):.0f}% — response processes are effective"
    return (
        "degrading",
        f"MTTR degraded by {delta:.0f}% — review on-call runbooks and escalation paths",
    )


def x__compute_trend__mutmut_42(
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

    if abs(None) < _SIGNIFICANT_TREND_PCT:
        return "stable", "MTTR is stable across the period"
    if delta < 0:
        return "improving", f"MTTR improved by {abs(delta):.0f}% — response processes are effective"
    return (
        "degrading",
        f"MTTR degraded by {delta:.0f}% — review on-call runbooks and escalation paths",
    )


def x__compute_trend__mutmut_43(
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

    if abs(delta) <= _SIGNIFICANT_TREND_PCT:
        return "stable", "MTTR is stable across the period"
    if delta < 0:
        return "improving", f"MTTR improved by {abs(delta):.0f}% — response processes are effective"
    return (
        "degrading",
        f"MTTR degraded by {delta:.0f}% — review on-call runbooks and escalation paths",
    )


def x__compute_trend__mutmut_44(
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
        return "XXstableXX", "MTTR is stable across the period"
    if delta < 0:
        return "improving", f"MTTR improved by {abs(delta):.0f}% — response processes are effective"
    return (
        "degrading",
        f"MTTR degraded by {delta:.0f}% — review on-call runbooks and escalation paths",
    )


def x__compute_trend__mutmut_45(
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
        return "STABLE", "MTTR is stable across the period"
    if delta < 0:
        return "improving", f"MTTR improved by {abs(delta):.0f}% — response processes are effective"
    return (
        "degrading",
        f"MTTR degraded by {delta:.0f}% — review on-call runbooks and escalation paths",
    )


def x__compute_trend__mutmut_46(
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
        return "stable", "XXMTTR is stable across the periodXX"
    if delta < 0:
        return "improving", f"MTTR improved by {abs(delta):.0f}% — response processes are effective"
    return (
        "degrading",
        f"MTTR degraded by {delta:.0f}% — review on-call runbooks and escalation paths",
    )


def x__compute_trend__mutmut_47(
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
        return "stable", "mttr is stable across the period"
    if delta < 0:
        return "improving", f"MTTR improved by {abs(delta):.0f}% — response processes are effective"
    return (
        "degrading",
        f"MTTR degraded by {delta:.0f}% — review on-call runbooks and escalation paths",
    )


def x__compute_trend__mutmut_48(
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
        return "stable", "MTTR IS STABLE ACROSS THE PERIOD"
    if delta < 0:
        return "improving", f"MTTR improved by {abs(delta):.0f}% — response processes are effective"
    return (
        "degrading",
        f"MTTR degraded by {delta:.0f}% — review on-call runbooks and escalation paths",
    )


def x__compute_trend__mutmut_49(
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
    if delta <= 0:
        return "improving", f"MTTR improved by {abs(delta):.0f}% — response processes are effective"
    return (
        "degrading",
        f"MTTR degraded by {delta:.0f}% — review on-call runbooks and escalation paths",
    )


def x__compute_trend__mutmut_50(
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
    if delta < 1:
        return "improving", f"MTTR improved by {abs(delta):.0f}% — response processes are effective"
    return (
        "degrading",
        f"MTTR degraded by {delta:.0f}% — review on-call runbooks and escalation paths",
    )


def x__compute_trend__mutmut_51(
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
        return "XXimprovingXX", f"MTTR improved by {abs(delta):.0f}% — response processes are effective"
    return (
        "degrading",
        f"MTTR degraded by {delta:.0f}% — review on-call runbooks and escalation paths",
    )


def x__compute_trend__mutmut_52(
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
        return "IMPROVING", f"MTTR improved by {abs(delta):.0f}% — response processes are effective"
    return (
        "degrading",
        f"MTTR degraded by {delta:.0f}% — review on-call runbooks and escalation paths",
    )


def x__compute_trend__mutmut_53(
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
        return "improving", f"MTTR improved by {abs(None):.0f}% — response processes are effective"
    return (
        "degrading",
        f"MTTR degraded by {delta:.0f}% — review on-call runbooks and escalation paths",
    )


def x__compute_trend__mutmut_54(
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
        "XXdegradingXX",
        f"MTTR degraded by {delta:.0f}% — review on-call runbooks and escalation paths",
    )


def x__compute_trend__mutmut_55(
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
        "DEGRADING",
        f"MTTR degraded by {delta:.0f}% — review on-call runbooks and escalation paths",
    )

mutants_x__compute_trend__mutmut['_mutmut_orig'] = x__compute_trend__mutmut_orig # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_1'] = x__compute_trend__mutmut_1 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_2'] = x__compute_trend__mutmut_2 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_3'] = x__compute_trend__mutmut_3 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_4'] = x__compute_trend__mutmut_4 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_5'] = x__compute_trend__mutmut_5 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_6'] = x__compute_trend__mutmut_6 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_7'] = x__compute_trend__mutmut_7 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_8'] = x__compute_trend__mutmut_8 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_9'] = x__compute_trend__mutmut_9 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_10'] = x__compute_trend__mutmut_10 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_11'] = x__compute_trend__mutmut_11 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_12'] = x__compute_trend__mutmut_12 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_13'] = x__compute_trend__mutmut_13 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_14'] = x__compute_trend__mutmut_14 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_15'] = x__compute_trend__mutmut_15 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_16'] = x__compute_trend__mutmut_16 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_17'] = x__compute_trend__mutmut_17 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_18'] = x__compute_trend__mutmut_18 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_19'] = x__compute_trend__mutmut_19 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_20'] = x__compute_trend__mutmut_20 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_21'] = x__compute_trend__mutmut_21 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_22'] = x__compute_trend__mutmut_22 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_23'] = x__compute_trend__mutmut_23 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_24'] = x__compute_trend__mutmut_24 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_25'] = x__compute_trend__mutmut_25 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_26'] = x__compute_trend__mutmut_26 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_27'] = x__compute_trend__mutmut_27 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_28'] = x__compute_trend__mutmut_28 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_29'] = x__compute_trend__mutmut_29 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_30'] = x__compute_trend__mutmut_30 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_31'] = x__compute_trend__mutmut_31 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_32'] = x__compute_trend__mutmut_32 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_33'] = x__compute_trend__mutmut_33 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_34'] = x__compute_trend__mutmut_34 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_35'] = x__compute_trend__mutmut_35 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_36'] = x__compute_trend__mutmut_36 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_37'] = x__compute_trend__mutmut_37 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_38'] = x__compute_trend__mutmut_38 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_39'] = x__compute_trend__mutmut_39 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_40'] = x__compute_trend__mutmut_40 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_41'] = x__compute_trend__mutmut_41 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_42'] = x__compute_trend__mutmut_42 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_43'] = x__compute_trend__mutmut_43 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_44'] = x__compute_trend__mutmut_44 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_45'] = x__compute_trend__mutmut_45 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_46'] = x__compute_trend__mutmut_46 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_47'] = x__compute_trend__mutmut_47 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_48'] = x__compute_trend__mutmut_48 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_49'] = x__compute_trend__mutmut_49 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_50'] = x__compute_trend__mutmut_50 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_51'] = x__compute_trend__mutmut_51 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_52'] = x__compute_trend__mutmut_52 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_53'] = x__compute_trend__mutmut_53 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_54'] = x__compute_trend__mutmut_54 # type: ignore # mutmut generated
mutants_x__compute_trend__mutmut['x__compute_trend__mutmut_55'] = x__compute_trend__mutmut_55 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__rank_slowest__mutmut)
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


def x__rank_slowest__mutmut_orig(
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


def x__rank_slowest__mutmut_1(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = None
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


def x__rank_slowest__mutmut_2(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(None, key=lambda i: _as_int(i.get("resolution_minutes")), reverse=True)
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


def x__rank_slowest__mutmut_3(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=None, reverse=True)
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


def x__rank_slowest__mutmut_4(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("resolution_minutes")), reverse=None)
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


def x__rank_slowest__mutmut_5(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(key=lambda i: _as_int(i.get("resolution_minutes")), reverse=True)
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


def x__rank_slowest__mutmut_6(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, reverse=True)
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


def x__rank_slowest__mutmut_7(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("resolution_minutes")), )
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


def x__rank_slowest__mutmut_8(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: None, reverse=True)
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


def x__rank_slowest__mutmut_9(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(None), reverse=True)
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


def x__rank_slowest__mutmut_10(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get(None)), reverse=True)
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


def x__rank_slowest__mutmut_11(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("XXresolution_minutesXX")), reverse=True)
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


def x__rank_slowest__mutmut_12(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("RESOLUTION_MINUTES")), reverse=True)
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


def x__rank_slowest__mutmut_13(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("resolution_minutes")), reverse=False)
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


def x__rank_slowest__mutmut_14(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("resolution_minutes")), reverse=True)
    top = None
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


def x__rank_slowest__mutmut_15(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("resolution_minutes")), reverse=True)
    top = ranked[:4]
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


def x__rank_slowest__mutmut_16(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("resolution_minutes")), reverse=True)
    top = ranked[:3]
    return [
        SlowestIncident(
            incident_id=None,
            service_name=str(inc.get("service_name", "")),
            severity=str(inc.get("severity", "P1")),
            resolution_minutes=_as_int(inc.get("resolution_minutes")),
            root_cause=str(inc.get("root_cause", "")),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_17(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("resolution_minutes")), reverse=True)
    top = ranked[:3]
    return [
        SlowestIncident(
            incident_id=str(inc.get("incident_id", "")),
            service_name=None,
            severity=str(inc.get("severity", "P1")),
            resolution_minutes=_as_int(inc.get("resolution_minutes")),
            root_cause=str(inc.get("root_cause", "")),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_18(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("resolution_minutes")), reverse=True)
    top = ranked[:3]
    return [
        SlowestIncident(
            incident_id=str(inc.get("incident_id", "")),
            service_name=str(inc.get("service_name", "")),
            severity=None,
            resolution_minutes=_as_int(inc.get("resolution_minutes")),
            root_cause=str(inc.get("root_cause", "")),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_19(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("resolution_minutes")), reverse=True)
    top = ranked[:3]
    return [
        SlowestIncident(
            incident_id=str(inc.get("incident_id", "")),
            service_name=str(inc.get("service_name", "")),
            severity=str(inc.get("severity", "P1")),
            resolution_minutes=None,
            root_cause=str(inc.get("root_cause", "")),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_20(
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
            root_cause=None,
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_21(
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
            month=None,
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_22(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("resolution_minutes")), reverse=True)
    top = ranked[:3]
    return [
        SlowestIncident(
            service_name=str(inc.get("service_name", "")),
            severity=str(inc.get("severity", "P1")),
            resolution_minutes=_as_int(inc.get("resolution_minutes")),
            root_cause=str(inc.get("root_cause", "")),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_23(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("resolution_minutes")), reverse=True)
    top = ranked[:3]
    return [
        SlowestIncident(
            incident_id=str(inc.get("incident_id", "")),
            severity=str(inc.get("severity", "P1")),
            resolution_minutes=_as_int(inc.get("resolution_minutes")),
            root_cause=str(inc.get("root_cause", "")),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_24(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("resolution_minutes")), reverse=True)
    top = ranked[:3]
    return [
        SlowestIncident(
            incident_id=str(inc.get("incident_id", "")),
            service_name=str(inc.get("service_name", "")),
            resolution_minutes=_as_int(inc.get("resolution_minutes")),
            root_cause=str(inc.get("root_cause", "")),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_25(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("resolution_minutes")), reverse=True)
    top = ranked[:3]
    return [
        SlowestIncident(
            incident_id=str(inc.get("incident_id", "")),
            service_name=str(inc.get("service_name", "")),
            severity=str(inc.get("severity", "P1")),
            root_cause=str(inc.get("root_cause", "")),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_26(
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
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_27(
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
            )
        for inc in top
    ]


def x__rank_slowest__mutmut_28(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("resolution_minutes")), reverse=True)
    top = ranked[:3]
    return [
        SlowestIncident(
            incident_id=str(None),
            service_name=str(inc.get("service_name", "")),
            severity=str(inc.get("severity", "P1")),
            resolution_minutes=_as_int(inc.get("resolution_minutes")),
            root_cause=str(inc.get("root_cause", "")),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_29(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("resolution_minutes")), reverse=True)
    top = ranked[:3]
    return [
        SlowestIncident(
            incident_id=str(inc.get(None, "")),
            service_name=str(inc.get("service_name", "")),
            severity=str(inc.get("severity", "P1")),
            resolution_minutes=_as_int(inc.get("resolution_minutes")),
            root_cause=str(inc.get("root_cause", "")),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_30(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("resolution_minutes")), reverse=True)
    top = ranked[:3]
    return [
        SlowestIncident(
            incident_id=str(inc.get("incident_id", None)),
            service_name=str(inc.get("service_name", "")),
            severity=str(inc.get("severity", "P1")),
            resolution_minutes=_as_int(inc.get("resolution_minutes")),
            root_cause=str(inc.get("root_cause", "")),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_31(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("resolution_minutes")), reverse=True)
    top = ranked[:3]
    return [
        SlowestIncident(
            incident_id=str(inc.get("")),
            service_name=str(inc.get("service_name", "")),
            severity=str(inc.get("severity", "P1")),
            resolution_minutes=_as_int(inc.get("resolution_minutes")),
            root_cause=str(inc.get("root_cause", "")),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_32(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("resolution_minutes")), reverse=True)
    top = ranked[:3]
    return [
        SlowestIncident(
            incident_id=str(inc.get("incident_id", )),
            service_name=str(inc.get("service_name", "")),
            severity=str(inc.get("severity", "P1")),
            resolution_minutes=_as_int(inc.get("resolution_minutes")),
            root_cause=str(inc.get("root_cause", "")),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_33(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("resolution_minutes")), reverse=True)
    top = ranked[:3]
    return [
        SlowestIncident(
            incident_id=str(inc.get("XXincident_idXX", "")),
            service_name=str(inc.get("service_name", "")),
            severity=str(inc.get("severity", "P1")),
            resolution_minutes=_as_int(inc.get("resolution_minutes")),
            root_cause=str(inc.get("root_cause", "")),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_34(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("resolution_minutes")), reverse=True)
    top = ranked[:3]
    return [
        SlowestIncident(
            incident_id=str(inc.get("INCIDENT_ID", "")),
            service_name=str(inc.get("service_name", "")),
            severity=str(inc.get("severity", "P1")),
            resolution_minutes=_as_int(inc.get("resolution_minutes")),
            root_cause=str(inc.get("root_cause", "")),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_35(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("resolution_minutes")), reverse=True)
    top = ranked[:3]
    return [
        SlowestIncident(
            incident_id=str(inc.get("incident_id", "XXXX")),
            service_name=str(inc.get("service_name", "")),
            severity=str(inc.get("severity", "P1")),
            resolution_minutes=_as_int(inc.get("resolution_minutes")),
            root_cause=str(inc.get("root_cause", "")),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_36(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("resolution_minutes")), reverse=True)
    top = ranked[:3]
    return [
        SlowestIncident(
            incident_id=str(inc.get("incident_id", "")),
            service_name=str(None),
            severity=str(inc.get("severity", "P1")),
            resolution_minutes=_as_int(inc.get("resolution_minutes")),
            root_cause=str(inc.get("root_cause", "")),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_37(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("resolution_minutes")), reverse=True)
    top = ranked[:3]
    return [
        SlowestIncident(
            incident_id=str(inc.get("incident_id", "")),
            service_name=str(inc.get(None, "")),
            severity=str(inc.get("severity", "P1")),
            resolution_minutes=_as_int(inc.get("resolution_minutes")),
            root_cause=str(inc.get("root_cause", "")),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_38(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("resolution_minutes")), reverse=True)
    top = ranked[:3]
    return [
        SlowestIncident(
            incident_id=str(inc.get("incident_id", "")),
            service_name=str(inc.get("service_name", None)),
            severity=str(inc.get("severity", "P1")),
            resolution_minutes=_as_int(inc.get("resolution_minutes")),
            root_cause=str(inc.get("root_cause", "")),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_39(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("resolution_minutes")), reverse=True)
    top = ranked[:3]
    return [
        SlowestIncident(
            incident_id=str(inc.get("incident_id", "")),
            service_name=str(inc.get("")),
            severity=str(inc.get("severity", "P1")),
            resolution_minutes=_as_int(inc.get("resolution_minutes")),
            root_cause=str(inc.get("root_cause", "")),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_40(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("resolution_minutes")), reverse=True)
    top = ranked[:3]
    return [
        SlowestIncident(
            incident_id=str(inc.get("incident_id", "")),
            service_name=str(inc.get("service_name", )),
            severity=str(inc.get("severity", "P1")),
            resolution_minutes=_as_int(inc.get("resolution_minutes")),
            root_cause=str(inc.get("root_cause", "")),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_41(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("resolution_minutes")), reverse=True)
    top = ranked[:3]
    return [
        SlowestIncident(
            incident_id=str(inc.get("incident_id", "")),
            service_name=str(inc.get("XXservice_nameXX", "")),
            severity=str(inc.get("severity", "P1")),
            resolution_minutes=_as_int(inc.get("resolution_minutes")),
            root_cause=str(inc.get("root_cause", "")),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_42(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("resolution_minutes")), reverse=True)
    top = ranked[:3]
    return [
        SlowestIncident(
            incident_id=str(inc.get("incident_id", "")),
            service_name=str(inc.get("SERVICE_NAME", "")),
            severity=str(inc.get("severity", "P1")),
            resolution_minutes=_as_int(inc.get("resolution_minutes")),
            root_cause=str(inc.get("root_cause", "")),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_43(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("resolution_minutes")), reverse=True)
    top = ranked[:3]
    return [
        SlowestIncident(
            incident_id=str(inc.get("incident_id", "")),
            service_name=str(inc.get("service_name", "XXXX")),
            severity=str(inc.get("severity", "P1")),
            resolution_minutes=_as_int(inc.get("resolution_minutes")),
            root_cause=str(inc.get("root_cause", "")),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_44(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("resolution_minutes")), reverse=True)
    top = ranked[:3]
    return [
        SlowestIncident(
            incident_id=str(inc.get("incident_id", "")),
            service_name=str(inc.get("service_name", "")),
            severity=str(None),
            resolution_minutes=_as_int(inc.get("resolution_minutes")),
            root_cause=str(inc.get("root_cause", "")),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_45(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("resolution_minutes")), reverse=True)
    top = ranked[:3]
    return [
        SlowestIncident(
            incident_id=str(inc.get("incident_id", "")),
            service_name=str(inc.get("service_name", "")),
            severity=str(inc.get(None, "P1")),
            resolution_minutes=_as_int(inc.get("resolution_minutes")),
            root_cause=str(inc.get("root_cause", "")),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_46(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("resolution_minutes")), reverse=True)
    top = ranked[:3]
    return [
        SlowestIncident(
            incident_id=str(inc.get("incident_id", "")),
            service_name=str(inc.get("service_name", "")),
            severity=str(inc.get("severity", None)),
            resolution_minutes=_as_int(inc.get("resolution_minutes")),
            root_cause=str(inc.get("root_cause", "")),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_47(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("resolution_minutes")), reverse=True)
    top = ranked[:3]
    return [
        SlowestIncident(
            incident_id=str(inc.get("incident_id", "")),
            service_name=str(inc.get("service_name", "")),
            severity=str(inc.get("P1")),
            resolution_minutes=_as_int(inc.get("resolution_minutes")),
            root_cause=str(inc.get("root_cause", "")),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_48(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("resolution_minutes")), reverse=True)
    top = ranked[:3]
    return [
        SlowestIncident(
            incident_id=str(inc.get("incident_id", "")),
            service_name=str(inc.get("service_name", "")),
            severity=str(inc.get("severity", )),
            resolution_minutes=_as_int(inc.get("resolution_minutes")),
            root_cause=str(inc.get("root_cause", "")),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_49(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("resolution_minutes")), reverse=True)
    top = ranked[:3]
    return [
        SlowestIncident(
            incident_id=str(inc.get("incident_id", "")),
            service_name=str(inc.get("service_name", "")),
            severity=str(inc.get("XXseverityXX", "P1")),
            resolution_minutes=_as_int(inc.get("resolution_minutes")),
            root_cause=str(inc.get("root_cause", "")),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_50(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("resolution_minutes")), reverse=True)
    top = ranked[:3]
    return [
        SlowestIncident(
            incident_id=str(inc.get("incident_id", "")),
            service_name=str(inc.get("service_name", "")),
            severity=str(inc.get("SEVERITY", "P1")),
            resolution_minutes=_as_int(inc.get("resolution_minutes")),
            root_cause=str(inc.get("root_cause", "")),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_51(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("resolution_minutes")), reverse=True)
    top = ranked[:3]
    return [
        SlowestIncident(
            incident_id=str(inc.get("incident_id", "")),
            service_name=str(inc.get("service_name", "")),
            severity=str(inc.get("severity", "XXP1XX")),
            resolution_minutes=_as_int(inc.get("resolution_minutes")),
            root_cause=str(inc.get("root_cause", "")),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_52(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("resolution_minutes")), reverse=True)
    top = ranked[:3]
    return [
        SlowestIncident(
            incident_id=str(inc.get("incident_id", "")),
            service_name=str(inc.get("service_name", "")),
            severity=str(inc.get("severity", "p1")),
            resolution_minutes=_as_int(inc.get("resolution_minutes")),
            root_cause=str(inc.get("root_cause", "")),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_53(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("resolution_minutes")), reverse=True)
    top = ranked[:3]
    return [
        SlowestIncident(
            incident_id=str(inc.get("incident_id", "")),
            service_name=str(inc.get("service_name", "")),
            severity=str(inc.get("severity", "P1")),
            resolution_minutes=_as_int(None),
            root_cause=str(inc.get("root_cause", "")),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_54(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("resolution_minutes")), reverse=True)
    top = ranked[:3]
    return [
        SlowestIncident(
            incident_id=str(inc.get("incident_id", "")),
            service_name=str(inc.get("service_name", "")),
            severity=str(inc.get("severity", "P1")),
            resolution_minutes=_as_int(inc.get(None)),
            root_cause=str(inc.get("root_cause", "")),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_55(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("resolution_minutes")), reverse=True)
    top = ranked[:3]
    return [
        SlowestIncident(
            incident_id=str(inc.get("incident_id", "")),
            service_name=str(inc.get("service_name", "")),
            severity=str(inc.get("severity", "P1")),
            resolution_minutes=_as_int(inc.get("XXresolution_minutesXX")),
            root_cause=str(inc.get("root_cause", "")),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_56(
    incidents: list[dict[str, object]],
) -> list[SlowestIncident]:
    ranked = sorted(incidents, key=lambda i: _as_int(i.get("resolution_minutes")), reverse=True)
    top = ranked[:3]
    return [
        SlowestIncident(
            incident_id=str(inc.get("incident_id", "")),
            service_name=str(inc.get("service_name", "")),
            severity=str(inc.get("severity", "P1")),
            resolution_minutes=_as_int(inc.get("RESOLUTION_MINUTES")),
            root_cause=str(inc.get("root_cause", "")),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_57(
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
            root_cause=str(None),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_58(
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
            root_cause=str(inc.get(None, "")),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_59(
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
            root_cause=str(inc.get("root_cause", None)),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_60(
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
            root_cause=str(inc.get("")),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_61(
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
            root_cause=str(inc.get("root_cause", )),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_62(
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
            root_cause=str(inc.get("XXroot_causeXX", "")),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_63(
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
            root_cause=str(inc.get("ROOT_CAUSE", "")),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_64(
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
            root_cause=str(inc.get("root_cause", "XXXX")),
            month="",
        )
        for inc in top
    ]


def x__rank_slowest__mutmut_65(
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
            month="XXXX",
        )
        for inc in top
    ]

mutants_x__rank_slowest__mutmut['_mutmut_orig'] = x__rank_slowest__mutmut_orig # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_1'] = x__rank_slowest__mutmut_1 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_2'] = x__rank_slowest__mutmut_2 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_3'] = x__rank_slowest__mutmut_3 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_4'] = x__rank_slowest__mutmut_4 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_5'] = x__rank_slowest__mutmut_5 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_6'] = x__rank_slowest__mutmut_6 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_7'] = x__rank_slowest__mutmut_7 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_8'] = x__rank_slowest__mutmut_8 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_9'] = x__rank_slowest__mutmut_9 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_10'] = x__rank_slowest__mutmut_10 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_11'] = x__rank_slowest__mutmut_11 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_12'] = x__rank_slowest__mutmut_12 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_13'] = x__rank_slowest__mutmut_13 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_14'] = x__rank_slowest__mutmut_14 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_15'] = x__rank_slowest__mutmut_15 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_16'] = x__rank_slowest__mutmut_16 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_17'] = x__rank_slowest__mutmut_17 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_18'] = x__rank_slowest__mutmut_18 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_19'] = x__rank_slowest__mutmut_19 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_20'] = x__rank_slowest__mutmut_20 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_21'] = x__rank_slowest__mutmut_21 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_22'] = x__rank_slowest__mutmut_22 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_23'] = x__rank_slowest__mutmut_23 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_24'] = x__rank_slowest__mutmut_24 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_25'] = x__rank_slowest__mutmut_25 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_26'] = x__rank_slowest__mutmut_26 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_27'] = x__rank_slowest__mutmut_27 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_28'] = x__rank_slowest__mutmut_28 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_29'] = x__rank_slowest__mutmut_29 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_30'] = x__rank_slowest__mutmut_30 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_31'] = x__rank_slowest__mutmut_31 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_32'] = x__rank_slowest__mutmut_32 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_33'] = x__rank_slowest__mutmut_33 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_34'] = x__rank_slowest__mutmut_34 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_35'] = x__rank_slowest__mutmut_35 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_36'] = x__rank_slowest__mutmut_36 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_37'] = x__rank_slowest__mutmut_37 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_38'] = x__rank_slowest__mutmut_38 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_39'] = x__rank_slowest__mutmut_39 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_40'] = x__rank_slowest__mutmut_40 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_41'] = x__rank_slowest__mutmut_41 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_42'] = x__rank_slowest__mutmut_42 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_43'] = x__rank_slowest__mutmut_43 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_44'] = x__rank_slowest__mutmut_44 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_45'] = x__rank_slowest__mutmut_45 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_46'] = x__rank_slowest__mutmut_46 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_47'] = x__rank_slowest__mutmut_47 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_48'] = x__rank_slowest__mutmut_48 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_49'] = x__rank_slowest__mutmut_49 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_50'] = x__rank_slowest__mutmut_50 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_51'] = x__rank_slowest__mutmut_51 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_52'] = x__rank_slowest__mutmut_52 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_53'] = x__rank_slowest__mutmut_53 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_54'] = x__rank_slowest__mutmut_54 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_55'] = x__rank_slowest__mutmut_55 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_56'] = x__rank_slowest__mutmut_56 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_57'] = x__rank_slowest__mutmut_57 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_58'] = x__rank_slowest__mutmut_58 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_59'] = x__rank_slowest__mutmut_59 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_60'] = x__rank_slowest__mutmut_60 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_61'] = x__rank_slowest__mutmut_61 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_62'] = x__rank_slowest__mutmut_62 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_63'] = x__rank_slowest__mutmut_63 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_64'] = x__rank_slowest__mutmut_64 # type: ignore # mutmut generated
mutants_x__rank_slowest__mutmut['x__rank_slowest__mutmut_65'] = x__rank_slowest__mutmut_65 # type: ignore # mutmut generated
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
