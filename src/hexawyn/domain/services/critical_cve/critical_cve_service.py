from __future__ import annotations

from hexawyn.application.ports.driven.critical_cve_port import CveRaw
from hexawyn.domain.models.critical_cve import CriticalCveReport, CveSummary


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
