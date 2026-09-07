from __future__ import annotations

from hexawyn.application.ports.driven.critical_cve_port import CveRaw
from hexawyn.domain.models.critical_cve import CriticalCveReport, CveSummary


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_compute_critical_cve_report__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_compute_critical_cve_report__mutmut)
def compute_critical_cve_report(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, warning="Aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["severity"] == "critical" and cve["count"] > 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["count"] for cve in critical),
        affected_service_count=len(critical),
        oldest_unresolved_days=max((cve["oldest_unresolved_days"] for cve in critical), default=0),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_orig(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, warning="Aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["severity"] == "critical" and cve["count"] > 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["count"] for cve in critical),
        affected_service_count=len(critical),
        oldest_unresolved_days=max((cve["oldest_unresolved_days"] for cve in critical), default=0),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_1(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, warning="Aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["severity"] == "critical" and cve["count"] > 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["count"] for cve in critical),
        affected_service_count=len(critical),
        oldest_unresolved_days=max((cve["oldest_unresolved_days"] for cve in critical), default=0),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_2(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=None, has_data=False, warning="Aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["severity"] == "critical" and cve["count"] > 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["count"] for cve in critical),
        affected_service_count=len(critical),
        oldest_unresolved_days=max((cve["oldest_unresolved_days"] for cve in critical), default=0),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_3(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=None, warning="Aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["severity"] == "critical" and cve["count"] > 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["count"] for cve in critical),
        affected_service_count=len(critical),
        oldest_unresolved_days=max((cve["oldest_unresolved_days"] for cve in critical), default=0),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_4(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, warning=None
        )

    critical = [cve for cve in cves if cve["severity"] == "critical" and cve["count"] > 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["count"] for cve in critical),
        affected_service_count=len(critical),
        oldest_unresolved_days=max((cve["oldest_unresolved_days"] for cve in critical), default=0),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_5(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            has_data=False, warning="Aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["severity"] == "critical" and cve["count"] > 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["count"] for cve in critical),
        affected_service_count=len(critical),
        oldest_unresolved_days=max((cve["oldest_unresolved_days"] for cve in critical), default=0),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_6(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, warning="Aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["severity"] == "critical" and cve["count"] > 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["count"] for cve in critical),
        affected_service_count=len(critical),
        oldest_unresolved_days=max((cve["oldest_unresolved_days"] for cve in critical), default=0),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_7(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, )

    critical = [cve for cve in cves if cve["severity"] == "critical" and cve["count"] > 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["count"] for cve in critical),
        affected_service_count=len(critical),
        oldest_unresolved_days=max((cve["oldest_unresolved_days"] for cve in critical), default=0),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_8(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=True, warning="Aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["severity"] == "critical" and cve["count"] > 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["count"] for cve in critical),
        affected_service_count=len(critical),
        oldest_unresolved_days=max((cve["oldest_unresolved_days"] for cve in critical), default=0),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_9(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, warning="XXAucune donnee de scan disponible.XX"
        )

    critical = [cve for cve in cves if cve["severity"] == "critical" and cve["count"] > 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["count"] for cve in critical),
        affected_service_count=len(critical),
        oldest_unresolved_days=max((cve["oldest_unresolved_days"] for cve in critical), default=0),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_10(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, warning="aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["severity"] == "critical" and cve["count"] > 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["count"] for cve in critical),
        affected_service_count=len(critical),
        oldest_unresolved_days=max((cve["oldest_unresolved_days"] for cve in critical), default=0),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_11(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, warning="AUCUNE DONNEE DE SCAN DISPONIBLE."
        )

    critical = [cve for cve in cves if cve["severity"] == "critical" and cve["count"] > 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["count"] for cve in critical),
        affected_service_count=len(critical),
        oldest_unresolved_days=max((cve["oldest_unresolved_days"] for cve in critical), default=0),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_12(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, warning="Aucune donnee de scan disponible."
        )

    critical = None
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["count"] for cve in critical),
        affected_service_count=len(critical),
        oldest_unresolved_days=max((cve["oldest_unresolved_days"] for cve in critical), default=0),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_13(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, warning="Aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["severity"] == "critical" or cve["count"] > 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["count"] for cve in critical),
        affected_service_count=len(critical),
        oldest_unresolved_days=max((cve["oldest_unresolved_days"] for cve in critical), default=0),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_14(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, warning="Aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["XXseverityXX"] == "critical" and cve["count"] > 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["count"] for cve in critical),
        affected_service_count=len(critical),
        oldest_unresolved_days=max((cve["oldest_unresolved_days"] for cve in critical), default=0),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_15(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, warning="Aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["SEVERITY"] == "critical" and cve["count"] > 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["count"] for cve in critical),
        affected_service_count=len(critical),
        oldest_unresolved_days=max((cve["oldest_unresolved_days"] for cve in critical), default=0),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_16(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, warning="Aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["severity"] != "critical" and cve["count"] > 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["count"] for cve in critical),
        affected_service_count=len(critical),
        oldest_unresolved_days=max((cve["oldest_unresolved_days"] for cve in critical), default=0),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_17(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, warning="Aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["severity"] == "XXcriticalXX" and cve["count"] > 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["count"] for cve in critical),
        affected_service_count=len(critical),
        oldest_unresolved_days=max((cve["oldest_unresolved_days"] for cve in critical), default=0),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_18(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, warning="Aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["severity"] == "CRITICAL" and cve["count"] > 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["count"] for cve in critical),
        affected_service_count=len(critical),
        oldest_unresolved_days=max((cve["oldest_unresolved_days"] for cve in critical), default=0),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_19(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, warning="Aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["severity"] == "critical" and cve["XXcountXX"] > 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["count"] for cve in critical),
        affected_service_count=len(critical),
        oldest_unresolved_days=max((cve["oldest_unresolved_days"] for cve in critical), default=0),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_20(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, warning="Aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["severity"] == "critical" and cve["COUNT"] > 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["count"] for cve in critical),
        affected_service_count=len(critical),
        oldest_unresolved_days=max((cve["oldest_unresolved_days"] for cve in critical), default=0),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_21(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, warning="Aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["severity"] == "critical" and cve["count"] >= 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["count"] for cve in critical),
        affected_service_count=len(critical),
        oldest_unresolved_days=max((cve["oldest_unresolved_days"] for cve in critical), default=0),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_22(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, warning="Aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["severity"] == "critical" and cve["count"] > 1]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["count"] for cve in critical),
        affected_service_count=len(critical),
        oldest_unresolved_days=max((cve["oldest_unresolved_days"] for cve in critical), default=0),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_23(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, warning="Aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["severity"] == "critical" and cve["count"] > 0]
    return CriticalCveReport(
        period_label=None,
        total_critical_cves=sum(cve["count"] for cve in critical),
        affected_service_count=len(critical),
        oldest_unresolved_days=max((cve["oldest_unresolved_days"] for cve in critical), default=0),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_24(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, warning="Aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["severity"] == "critical" and cve["count"] > 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=None,
        affected_service_count=len(critical),
        oldest_unresolved_days=max((cve["oldest_unresolved_days"] for cve in critical), default=0),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_25(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, warning="Aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["severity"] == "critical" and cve["count"] > 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["count"] for cve in critical),
        affected_service_count=None,
        oldest_unresolved_days=max((cve["oldest_unresolved_days"] for cve in critical), default=0),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_26(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, warning="Aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["severity"] == "critical" and cve["count"] > 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["count"] for cve in critical),
        affected_service_count=len(critical),
        oldest_unresolved_days=None,
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_27(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, warning="Aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["severity"] == "critical" and cve["count"] > 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["count"] for cve in critical),
        affected_service_count=len(critical),
        oldest_unresolved_days=max((cve["oldest_unresolved_days"] for cve in critical), default=0),
        cves=None,
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_28(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, warning="Aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["severity"] == "critical" and cve["count"] > 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["count"] for cve in critical),
        affected_service_count=len(critical),
        oldest_unresolved_days=max((cve["oldest_unresolved_days"] for cve in critical), default=0),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=None,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_29(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, warning="Aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["severity"] == "critical" and cve["count"] > 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["count"] for cve in critical),
        affected_service_count=len(critical),
        oldest_unresolved_days=max((cve["oldest_unresolved_days"] for cve in critical), default=0),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=None,
    )


def x_compute_critical_cve_report__mutmut_30(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, warning="Aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["severity"] == "critical" and cve["count"] > 0]
    return CriticalCveReport(
        total_critical_cves=sum(cve["count"] for cve in critical),
        affected_service_count=len(critical),
        oldest_unresolved_days=max((cve["oldest_unresolved_days"] for cve in critical), default=0),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_31(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, warning="Aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["severity"] == "critical" and cve["count"] > 0]
    return CriticalCveReport(
        period_label=period,
        affected_service_count=len(critical),
        oldest_unresolved_days=max((cve["oldest_unresolved_days"] for cve in critical), default=0),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_32(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, warning="Aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["severity"] == "critical" and cve["count"] > 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["count"] for cve in critical),
        oldest_unresolved_days=max((cve["oldest_unresolved_days"] for cve in critical), default=0),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_33(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, warning="Aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["severity"] == "critical" and cve["count"] > 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["count"] for cve in critical),
        affected_service_count=len(critical),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_34(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, warning="Aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["severity"] == "critical" and cve["count"] > 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["count"] for cve in critical),
        affected_service_count=len(critical),
        oldest_unresolved_days=max((cve["oldest_unresolved_days"] for cve in critical), default=0),
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_35(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, warning="Aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["severity"] == "critical" and cve["count"] > 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["count"] for cve in critical),
        affected_service_count=len(critical),
        oldest_unresolved_days=max((cve["oldest_unresolved_days"] for cve in critical), default=0),
        cves=[CveSummary(**cve) for cve in critical],
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_36(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, warning="Aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["severity"] == "critical" and cve["count"] > 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["count"] for cve in critical),
        affected_service_count=len(critical),
        oldest_unresolved_days=max((cve["oldest_unresolved_days"] for cve in critical), default=0),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        )


def x_compute_critical_cve_report__mutmut_37(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, warning="Aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["severity"] == "critical" and cve["count"] > 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(None),
        affected_service_count=len(critical),
        oldest_unresolved_days=max((cve["oldest_unresolved_days"] for cve in critical), default=0),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_38(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, warning="Aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["severity"] == "critical" and cve["count"] > 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["XXcountXX"] for cve in critical),
        affected_service_count=len(critical),
        oldest_unresolved_days=max((cve["oldest_unresolved_days"] for cve in critical), default=0),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_39(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, warning="Aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["severity"] == "critical" and cve["count"] > 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["COUNT"] for cve in critical),
        affected_service_count=len(critical),
        oldest_unresolved_days=max((cve["oldest_unresolved_days"] for cve in critical), default=0),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_40(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, warning="Aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["severity"] == "critical" and cve["count"] > 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["count"] for cve in critical),
        affected_service_count=len(critical),
        oldest_unresolved_days=max(None, default=0),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_41(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, warning="Aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["severity"] == "critical" and cve["count"] > 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["count"] for cve in critical),
        affected_service_count=len(critical),
        oldest_unresolved_days=max((cve["oldest_unresolved_days"] for cve in critical), default=None),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_42(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, warning="Aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["severity"] == "critical" and cve["count"] > 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["count"] for cve in critical),
        affected_service_count=len(critical),
        oldest_unresolved_days=max(default=0),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_43(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, warning="Aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["severity"] == "critical" and cve["count"] > 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["count"] for cve in critical),
        affected_service_count=len(critical),
        oldest_unresolved_days=max((cve["oldest_unresolved_days"] for cve in critical), ),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_44(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, warning="Aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["severity"] == "critical" and cve["count"] > 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["count"] for cve in critical),
        affected_service_count=len(critical),
        oldest_unresolved_days=max((cve["XXoldest_unresolved_daysXX"] for cve in critical), default=0),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_45(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, warning="Aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["severity"] == "critical" and cve["count"] > 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["count"] for cve in critical),
        affected_service_count=len(critical),
        oldest_unresolved_days=max((cve["OLDEST_UNRESOLVED_DAYS"] for cve in critical), default=0),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_46(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, warning="Aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["severity"] == "critical" and cve["count"] > 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["count"] for cve in critical),
        affected_service_count=len(critical),
        oldest_unresolved_days=max((cve["oldest_unresolved_days"] for cve in critical), default=1),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=True,
    )


def x_compute_critical_cve_report__mutmut_47(
    cves: list[CveRaw], total_scanned: int, has_data: bool, period: str
) -> CriticalCveReport:
    if not has_data:
        return CriticalCveReport(
            period_label=period, has_data=False, warning="Aucune donnee de scan disponible."
        )

    critical = [cve for cve in cves if cve["severity"] == "critical" and cve["count"] > 0]
    return CriticalCveReport(
        period_label=period,
        total_critical_cves=sum(cve["count"] for cve in critical),
        affected_service_count=len(critical),
        oldest_unresolved_days=max((cve["oldest_unresolved_days"] for cve in critical), default=0),
        cves=[CveSummary(**cve) for cve in critical],
        total_images_scanned=total_scanned,
        has_data=False,
    )

mutants_x_compute_critical_cve_report__mutmut['_mutmut_orig'] = x_compute_critical_cve_report__mutmut_orig # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_1'] = x_compute_critical_cve_report__mutmut_1 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_2'] = x_compute_critical_cve_report__mutmut_2 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_3'] = x_compute_critical_cve_report__mutmut_3 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_4'] = x_compute_critical_cve_report__mutmut_4 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_5'] = x_compute_critical_cve_report__mutmut_5 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_6'] = x_compute_critical_cve_report__mutmut_6 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_7'] = x_compute_critical_cve_report__mutmut_7 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_8'] = x_compute_critical_cve_report__mutmut_8 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_9'] = x_compute_critical_cve_report__mutmut_9 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_10'] = x_compute_critical_cve_report__mutmut_10 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_11'] = x_compute_critical_cve_report__mutmut_11 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_12'] = x_compute_critical_cve_report__mutmut_12 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_13'] = x_compute_critical_cve_report__mutmut_13 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_14'] = x_compute_critical_cve_report__mutmut_14 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_15'] = x_compute_critical_cve_report__mutmut_15 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_16'] = x_compute_critical_cve_report__mutmut_16 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_17'] = x_compute_critical_cve_report__mutmut_17 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_18'] = x_compute_critical_cve_report__mutmut_18 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_19'] = x_compute_critical_cve_report__mutmut_19 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_20'] = x_compute_critical_cve_report__mutmut_20 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_21'] = x_compute_critical_cve_report__mutmut_21 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_22'] = x_compute_critical_cve_report__mutmut_22 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_23'] = x_compute_critical_cve_report__mutmut_23 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_24'] = x_compute_critical_cve_report__mutmut_24 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_25'] = x_compute_critical_cve_report__mutmut_25 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_26'] = x_compute_critical_cve_report__mutmut_26 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_27'] = x_compute_critical_cve_report__mutmut_27 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_28'] = x_compute_critical_cve_report__mutmut_28 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_29'] = x_compute_critical_cve_report__mutmut_29 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_30'] = x_compute_critical_cve_report__mutmut_30 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_31'] = x_compute_critical_cve_report__mutmut_31 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_32'] = x_compute_critical_cve_report__mutmut_32 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_33'] = x_compute_critical_cve_report__mutmut_33 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_34'] = x_compute_critical_cve_report__mutmut_34 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_35'] = x_compute_critical_cve_report__mutmut_35 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_36'] = x_compute_critical_cve_report__mutmut_36 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_37'] = x_compute_critical_cve_report__mutmut_37 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_38'] = x_compute_critical_cve_report__mutmut_38 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_39'] = x_compute_critical_cve_report__mutmut_39 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_40'] = x_compute_critical_cve_report__mutmut_40 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_41'] = x_compute_critical_cve_report__mutmut_41 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_42'] = x_compute_critical_cve_report__mutmut_42 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_43'] = x_compute_critical_cve_report__mutmut_43 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_44'] = x_compute_critical_cve_report__mutmut_44 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_45'] = x_compute_critical_cve_report__mutmut_45 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_46'] = x_compute_critical_cve_report__mutmut_46 # type: ignore # mutmut generated
mutants_x_compute_critical_cve_report__mutmut['x_compute_critical_cve_report__mutmut_47'] = x_compute_critical_cve_report__mutmut_47 # type: ignore # mutmut generated
