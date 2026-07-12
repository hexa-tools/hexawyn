from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.report_unauthorized_access.report_unauthorized_access_command import (  # noqa: E501
    ReportUnauthorizedAccessCommand,
)
from hexawyn.application.ports.driving.report_unauthorized_access.report_unauthorized_access_response import (  # noqa: E501
    ReportUnauthorizedAccessResponse,
)


class ReportUnauthorizedAccessServicePort(ABC):
    @abstractmethod
    def report(
        self, command: ReportUnauthorizedAccessCommand
    ) -> ReportUnauthorizedAccessResponse: ...
