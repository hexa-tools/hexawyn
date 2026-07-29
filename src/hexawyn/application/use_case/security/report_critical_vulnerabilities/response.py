from dataclasses import dataclass

from hexawyn.domain.models.critical_cve import CriticalCveReport


@dataclass
class ReportCriticalVulnerabilitiesResponse:
    result: CriticalCveReport
