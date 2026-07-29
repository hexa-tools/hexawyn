from dataclasses import dataclass

from hexawyn.domain.models.unauthorized_access import UnauthorizedAccessReport


@dataclass
class ReportUnauthorizedAccessResponse:
    result: UnauthorizedAccessReport
