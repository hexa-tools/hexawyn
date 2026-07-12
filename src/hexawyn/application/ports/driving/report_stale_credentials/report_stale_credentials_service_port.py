from abc import ABC, abstractmethod

from hexawyn.application.ports.driving.report_stale_credentials.report_stale_credentials_command import (  # noqa: E501
    ReportStaleCredentialsCommand,
)
from hexawyn.application.ports.driving.report_stale_credentials.report_stale_credentials_response import (  # noqa: E501
    ReportStaleCredentialsResponse,
)


class ReportStaleCredentialsServicePort(ABC):
    @abstractmethod
    def report(self, command: ReportStaleCredentialsCommand) -> ReportStaleCredentialsResponse: ...
