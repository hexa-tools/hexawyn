from abc import ABC, abstractmethod

from hexawyn.application.use_case.security.report_unauthorized_access.command import (  # noqa: E501
    ReportUnauthorizedAccessCommand,
)
from hexawyn.application.use_case.security.report_unauthorized_access.response import (  # noqa: E501
    ReportUnauthorizedAccessResponse,
)


class ReportUnauthorizedAccessServicePort(ABC):
    @abstractmethod
    def report(
        self, command: ReportUnauthorizedAccessCommand
    ) -> ReportUnauthorizedAccessResponse: ...
