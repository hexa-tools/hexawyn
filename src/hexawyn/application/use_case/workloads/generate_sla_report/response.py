from dataclasses import dataclass

from hexawyn.domain.models.sla_report import SlaReport


@dataclass
class GenerateSLAReportResponse:
    result: SlaReport
